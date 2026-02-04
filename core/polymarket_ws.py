import asyncio
import websockets
import json

class PolymarketWS:
    def __init__(self, market_id):
        self.market_id = market_id
        self.ws_url = "wss://ws.clob.polymarket.com"
        self.up_price = None
        self.down_price = None
        self.orderbook = {}

    async def connect(self):
        async with websockets.connect(self.ws_url) as ws:
            # Subscribe orderbook
            sub_msg = {
                "type": "subscribe",
                "channels": [
                    {
                        "name": "orderbook",
                        "market_ids": [self.market_id]
                    },
                    {
                        "name": "trades",
                        "market_ids": [self.market_id]
                    }
                ]
            }

            await ws.send(json.dumps(sub_msg))
            print("✅ Connected to Polymarket WS")

            while True:
                msg = await ws.recv()
                data = json.loads(msg)
                self.handle_message(data)

    def handle_message(self, data):
        if "channel" not in data:
            return

        if data["channel"] == "orderbook":
            self.parse_orderbook(data["data"])

        if data["channel"] == "trades":
            self.parse_trades(data["data"])

    def parse_orderbook(self, data):
        # data contains bids & asks for outcomes
        self.orderbook = data

        # Example structure parsing (simplified)
        for outcome in data.get("outcomes", []):
            if outcome["name"].lower() == "up":
                self.up_price = float(outcome["mid"])
            elif outcome["name"].lower() == "down":
                self.down_price = float(outcome["mid"])

    def parse_trades(self, data):
        pass  # optional for later analytics
