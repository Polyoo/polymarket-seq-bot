import asyncio
import requests
from config import SERIES_SLUG, SESSION_SECONDS
from core.polymarket_ws import PolymarketWS
from core.strategy import Strategy
from core.timer import Timer
from core.execution import Execution

GAMMA_API_URL = "https://gamma-api.polymarket.com/markets"

# Step 1: fetch latest BTC 15-min market
def fetch_latest_market():
    resp = requests.get(f"{GAMMA_API_URL}?seriesSlug={SERIES_SLUG}&active=true")
    data = resp.json()
    market = data[0]
    market_id = market["id"]
    up_id = market["clobTokenIds"][0]
    down_id = market["clobTokenIds"][1]
    return market_id, up_id, down_id

async def bot_loop():
    ws = PolymarketWS()
    execution = Execution()
    strategy = Strategy(ws, execution)
    timer = Timer(SESSION_SECONDS)

    while True:
        # Fetch new market if session over or first start
        if timer.is_over() or not ws.market_id:
            market_id, up_id, down_id = fetch_latest_market()
            ws.update_market(market_id, up_id, down_id)
            strategy.reset()
            timer.reset()
            print(f"🕒 New session started for Market {market_id}")

        # Strategy check
        strategy.check_and_trade()
        await asyncio.sleep(1)  # loop 1s

async def main():
    ws = PolymarketWS()
    task_ws = asyncio.create_task(ws.connect())
    task_logic = asyncio.create_task(bot_loop())
    await asyncio.gather(task_ws, task_logic)

if __name__ == "__main__":
    asyncio.run(main())
