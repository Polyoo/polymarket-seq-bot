import asyncio
import requests

from config import SERIES_SLUG
from core.polymarket_ws import PolymarketWS
from core.strategy import Strategy
from core.timer import Timer
from core.state_machine import StateMachine
from core.execution import Execution

# Step 1: Fetch latest market from Gamma API
def fetch_latest_market():
    resp = requests.get(f"https://gamma-api.polymarket.com/markets?seriesSlug={SERIES_SLUG}&active=true")
    data = resp.json()
    market = data[0]  # ambil first active market
    market_id = market["id"]
    clob_ids = market["clobTokenIds"]
    up_id = clob_ids[0]
    down_id = clob_ids[1]
    return market_id, up_id, down_id

async def main():
    market_id, up_id, down_id = fetch_latest_market()
    print(f"🌐 Market ID: {market_id}, UP: {up_id}, DOWN: {down_id}")

    ws = PolymarketWS(market_id, up_id, down_id)
    strategy = Strategy(ws)
    timer = Timer()
    state = StateMachine(strategy, timer)
    execution = Execution()

    async def run_ws():
        await ws.connect()

    async def run_logic():
        while True:
            strategy.check_and_trade()
            state.run()
            await asyncio.sleep(1)

    await asyncio.gather(run_ws(), run_logic())

if __name__ == "__main__":
    asyncio.run(main())
