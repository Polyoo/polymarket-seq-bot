import requests

class PolymarketAPI:
    def __init__(self):
        self.base_url = "https://gamma-api.polymarket.com/markets"
        self.series_slug = "btc-up-or-down-15m"

    def fetch_latest_market(self):
        """Fetch latest active BTC 15-min market"""
        try:
            resp = requests.get(f"{self.base_url}?seriesSlug={self.series_slug}&active=true")
            resp.raise_for_status()
            data = resp.json()
            markets = data.get("markets", [])
            if len(markets) == 0:
                print("⚠️ Tiada market aktif sekarang")
                return None, None, None

            latest = markets[0]
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
            market = data.get("markets", [{}])[0]
            outcomes = market.get("outcomes", [])
            prices = list(map(float, market.get("outcomePrices", [])))
            return dict(zip(outcomes, prices))
        except Exception as e:
            print(f"❌ Error fetch_market_prices: {e}")
            return {}
