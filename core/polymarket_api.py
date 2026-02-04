import requests
from config import SERIES_SLUG, GAMMA_API_URL

class PolymarketAPI:
    def __init__(self):
        self.base_url = GAMMA_API_URL
        self.series_slug = SERIES_SLUG

    def fetch_latest_market(self):
        """
        Fetch the latest active BTC 15-min market
        Returns: market_id, up_id, down_id
        """
        try:
            resp = requests.get(f"{self.base_url}?seriesSlug={self.series_slug}&active=true")
            resp.raise_for_status()
            data = resp.json()
            if not data:
                print("❌ No active markets found!")
                return None, None, None

            # Ambil first active market
            market = data[0]
            market_id = market["id"]
            clob_ids = market["clobTokenIds"]
            up_id = clob_ids[0]
            down_id = clob_ids[1]

            return market_id, up_id, down_id

        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching market: {e}")
            return None, None, None

    def fetch_all_active_markets(self):
        """
        Fetch all active markets (optional, for advanced filtering)
        Returns: list of market dicts
        """
        try:
            resp = requests.get(f"{self.base_url}?active=true")
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching all markets: {e}")
            return []
