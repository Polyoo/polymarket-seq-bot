import time
from market import get_btc_15m_market_slug, get_market_prices
from trading import execute_trade
from config import TARGET_PAIR_COST, COOLDOWN_SECONDS, ORDER_SIZE

def main():
    print("🚀 POLYMARKET SEQUENTIAL BTC 15MIN ARB BOT STARTED")
    market_slug = get_btc_15m_market_slug()
    if not market_slug:
        print("❌ No BTC 15-min market found")
        return
    print(f"Market: {market_slug}")

    while True:
        up, down = get_market_prices(market_slug)
        print(f"[Scan] UP=${up:.4f}, DOWN=${down:.4f}")

        # Sequential arbitrage logic
        if up < 0.40:
            print("🎯 UP below $0.40, buy UP")
            execute_trade("UP", up, ORDER_SIZE)
        if down < 0.40:
            print("🎯 DOWN below $0.40, buy DOWN")
            execute_trade("DOWN", down, ORDER_SIZE)

        total_cost = up + down
        print(f"Total cost UP+DOWN = ${total_cost:.4f}")
        if total_cost <= TARGET_PAIR_COST:
            print("✅ Sequential arbitrage opportunity!")
        time.sleep(COOLDOWN_SECONDS)

if __name__ == "__main__":
    main()
