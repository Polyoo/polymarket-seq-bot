import asyncio
from core.polymarket_ws import PolymarketWS
from core.strategy import Strategy
from core.timer import Timer
from core.execution import Execution
from core.state_machine import StateMachine
from core.polymarket_api import PolymarketAPI
from config import SESSION_SECONDS

async def bot_loop(ws, strategy, timer, api):
    """
    Loop utama bot:
    - Auto fetch latest market tiap session
    - Run strategy setiap saat
    """
    while True:
        # Step 1: Fetch new market jika session tamat atau market belum ada
        if timer.is_over() or not ws.market_id:
            market_id, up_id, down_id = api.fetch_latest_market()
            if market_id:
                ws.update_market(market_id, up_id, down_id)
                strategy.reset()
                timer.reset()
                print(f"🕒 New session started for Market {market_id}")
            else:
                print("❌ Tiada market aktif. Retry dalam 5s")
                await asyncio.sleep(5)
                continue

        # Step 2: Check & trigger strategy
        strategy.check_and_trade()

        # Step 3: Sleep 1s sebelum loop next
        await asyncio.sleep(1)

async def main():
    # Initialize modules
    api = PolymarketAPI()
    ws = PolymarketWS()
    execution = Execution()
    strategy = Strategy(ws, execution)
    timer = Timer(SESSION_SECONDS)
    state = StateMachine(strategy, timer)

    # Run WS + bot loop concurrently
    task_ws = asyncio.create_task(ws.connect())
    task_loop = asyncio.create_task(bot_loop(ws, strategy, timer, api))

    await asyncio.gather(task_ws, task_loop)

if __name__ == "__main__":
    asyncio.run(main())
