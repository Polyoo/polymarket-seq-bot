import asyncio
from core.polymarket_ws import PolymarketWS

MARKET_ID = "ISI_MARKET_ID_POLYMARKET"

ws = PolymarketWS(MARKET_ID)

async def run():
    await ws.connect()

asyncio.run(run())
