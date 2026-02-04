import httpx

POLYMARKET_BASE = "https://clob.polymarket.com"

def get_btc_15m_market_slug():
    """Return latest 15-min BTC market slug"""
    resp = httpx.get(f"{POLYMARKET_BASE}/api/markets/crypto")
    data = resp.json()
    for m in data:
        if "btc-updown-15m" in m["slug"]:
            return m["slug"]
    return None

def get_market_prices(slug):
    """Return UP/DOWN prices"""
    resp = httpx.get(f"{POLYMARKET_BASE}/api/markets/{slug}")
    data = resp.json()
    up = float(data["up"]["price"])
    down = float(data["down"]["price"])
    return up, down
