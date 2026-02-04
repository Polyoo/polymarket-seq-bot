import asyncio
import websockets
import json

class PolymarketWS:
    def __init__(self, market_id, up_id, down_id):
        self.market_id = market_id
        self.up_id = up_id
        self.down_id = down_id
        self.ws_url = "wss://ws.clob.polymarket.com"
        self.up_price = None
        self.down_price = None

    async def connect(self):
        async with websockets.connect(self.ws_url) as ws:
            sub_msg = {
                "type": "subscribe",
                "channels": [
                    {"name": "orderbook", "market_ids": [self.market_id]},
                    {"name": "trades", "market_ids": [self.market_id]}
                ]
            }
            await ws.send(json.dumps(sub_msg))
            print(f"✅ Connected WS Market {self.market_id}")

            while True:
                msg = await ws.recv()
                data = json.loads(msg)
                self.handle_message(data)

    def handle_message(self, data):
        if "channel" not in data:
            return

        if data["channel"] == "orderbook":
            self.parse_orderbook(data["data"])

    def parse_orderbook(self, data):
        for outcome in data.get("outcomes", []):
            if outcome["id"] == self.up_id:
                self.up_price = float(outcome["mid"])
            elif outcome["id"] == self.down_id:
                self.down_price = float(outcome["mid"])
