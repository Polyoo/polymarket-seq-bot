import requests

class PolymarketAPI:
    def __init__(self):
        # Base API URL Polymarket Gamma
        self.base_url = "https://gamma-api.polymarket.com/markets"
        self.series_slug = "btc-up-or-down-15m"

    def fetch_latest_market(self):
        """
        Fetch latest active BTC 15-min market
        Returns: (market_id, up_id, down_id)
        """
        try:
            # Fetch all active markets in series
            resp = requests.get(f"{self.base_url}?seriesSlug={self.series_slug}&active=true")
            resp.raise_for_status()
            data = resp.json()

            if "markets" in data and len(data["markets"]) > 0:
                latest = data["markets"][0]  # ambil yang paling latest
                market_id = latest["id"]
                outcomes = latest["outcomes"]
                up_id = None
                down_id = None
                for idx, outcome in enumerate(outcomes):
                    if outcome == "Up":
                        up_id = idx
                    elif outcome == "Down":
                        down_id = idx
                return market_id, up_id, down_id
            return None, None, None

        except Exception as e:
            print(f"❌ Error fetching latest market: {e}")
            return None, None, None

    def fetch_market_prices(self, market_id):
        """
        Fetch current outcome prices for a given market_id
        Returns: {"Up": 0.66, "Down": 0.34}
        """
        try:
            resp = requests.get(f"{self.base_url}/{market_id}")
            resp.raise_for_status()
            data = resp.json()
            if "markets" in data and len(data["markets"]) > 0:
                market = data["markets"][0]
                # outcomePrices dan outcomes dalam bentuk string
                prices = market.get("outcomePrices", [])
                outcomes = market.get("outcomes", [])
                # convert string prices to float, zip dengan outcomes
                result = dict(zip(outcomes, map(float, prices)))
                return result
            return {}
        except Exception as e:
            print(f"❌ Error fetching market prices: {e}")
            return {}
