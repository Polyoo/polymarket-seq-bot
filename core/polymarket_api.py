import requests

class PolymarketAPI:
    def __init__(self):
        self.base_url = "https://gamma-api.polymarket.com/markets"

    def fetch_latest_market(self):
        """Fetch latest active BTC 15-min market automatically"""
        try:
            resp = requests.get(f"{self.base_url}?active=true")
            resp.raise_for_status()
            markets = resp.json()  # list

            # ambil market btc-updown-15m paling terbaru
            btc_markets = [m for m in markets if "btc-updown-15m" in m.get("slug","")]
            if not btc_markets:
                print("⚠️ Tiada market BTC aktif sekarang")
                return None, None, None

            latest = btc_markets[-1]  # ambil paling terbaru
            outcomes = latest.get("outcomes", [])
            up_id = outcomes.index("Up") if "Up" in outcomes else None
            down_id = outcomes.index("Down") if "Down" in outcomes else None
            return latest["id"], up_id, down_id

        except Exception as e:
            print(f"❌ Error fetch_latest_market: {e}")
            return None, None, None

    def fetch_market_prices(self, market_id):
        """Fetch current prices for given market"""
        try:
            resp = requests.get(f"{self.base_url}/{market_id}")
            resp.raise_for_status()
            data = resp.json()
            market = data[0] if isinstance(data, list) else data
            outcomes = market.get("outcomes", [])
            prices = list(map(float, market.get("outcomePrices", [])))
            return dict(zip(outcomes, prices))
        except Exception as e:
            print(f"❌ Error fetch_market_prices: {e}")
            return {}
