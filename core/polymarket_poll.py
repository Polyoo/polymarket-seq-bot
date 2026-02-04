import asyncio
from core.polymarket_api import PolymarketAPI

class PolymarketPoll:
    def __init__(self):
        self.api = PolymarketAPI()
        self.market_id = None
        self.up_id = None
        self.down_id = None
        self.last_up_price = 0
        self.last_down_price = 0

    async def start_polling(self, update_callback):
        while True:
            market_id, up_id, down_id = self.api.fetch_latest_market()
            if market_id:
                if market_id != self.market_id:
                    print(f"🕒 New session started for Market {market_id}")
                    self.market_id = market_id
                    self.up_id = up_id
                    self.down_id = down_id

                prices = self.api.fetch_market_prices(market_id)
                print(f"🔄 Updated Market: {market_id}, prices: {prices}")
                if prices:
                    self.last_up_price = prices.get("Up", 0)
                    self.last_down_price = prices.get("Down", 0)
                    update_callback(self.last_up_price, self.last_down_price)

            await asyncio.sleep(1)
