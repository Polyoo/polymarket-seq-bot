import asyncio
import websockets
import json

class PolymarketWS:
    def __init__(self):
        self.ws_url = "wss://ws.clob.polymarket.com"
        self.market_id = None
        self.up_id = None
        self.down_id = None
        self.up_price = None
        self.down_price = None
        self.connected = False

    async def connect(self):
        while True:
            try:
                async with websockets.connect(self.ws_url) as ws:
                    self.connected = True
                    print("✅ WS Connected")
                    await self.subscribe(ws)
                    async for msg in ws:
                        data = json.loads(msg)
                        self.handle_message(data)
            except Exception as e:
                print(f"❌ WS disconnected: {e}, reconnect in 5s")
                self.connected = False
                await asyncio.sleep(5)

    async def subscribe(self, ws):
        if not self.market_id:
            return
        sub_msg = {
            "type": "subscribe",
            "channels": [
                {"name": "orderbook", "market_ids": [self.market_id]},
                {"name": "trades", "market_ids": [self.market_id]}
            ]
        }
        await ws.send(json.dumps(sub_msg))
        print(f"Subscribed to market {self.market_id}")

    def update_market(self, market_id, up_id, down_id):
        self.market_id = market_id
        self.up_id = up_id
        self.down_id = down_id
        self.up_price = None
        self.down_price = None
        print(f"🔄 Updated Market: {market_id}")

    def handle_message(self, data):
        if "channel" not in data:
            return
        if data["channel"] == "orderbook":
            for outcome in data["data"].get("outcomes", []):
                if outcome["id"] == self.up_id:
                    self.up_price = float(outcome["mid"])
                elif outcome["id"] == self.down_id:
                    self.down_price = float(outcome["mid"])
