import time
import random
from config import Config
from market_lookup import get_current_btc_market
from trading import execute_trade

def main():
    print("🚀 BTC 15M ARBITRAGE BOT STARTED")
    print("="*70)
    print(f"Mode: {'SIMULATION' if Config.DRY_RUN else 'LIVE'}")
    print(f"Target pair cost: {Config.TARGET_PAIR_COST}")
    print(f"Order size: {Config.ORDER_SIZE}")
    print("="*70)

    market_slug = get_current_btc_market()
    print(f"Market: {market_slug}")
    print("="*70)

    scan_count = 1
    try:
        while True:
            # Simulate market prices for demo
            up_price = round(random.uniform(0.35, 0.55), 2)
            down_price = round(random.uniform(0.35, 0.55), 2)

            print(f"[Scan #{scan_count}] UP=${up_price} DOWN=${down_price}")
            execute_trade(up_price, down_price, Config.ORDER_SIZE, Config.TARGET_PAIR_COST, Config.DRY_RUN)

            scan_count += 1
            time.sleep(5)  # wait 5 seconds before next scan

    except KeyboardInterrupt:
        print("🛑 BOT STOPPED")

if __name__ == "__main__":
    main()
