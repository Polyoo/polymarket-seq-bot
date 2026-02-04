from config import DRY_RUN, ORDER_SIZE

def execute_trade(side, price, size=ORDER_SIZE):
    if DRY_RUN:
        print(f"[SIM] Buy {size} {side} at ${price:.4f}")
    else:
        # nanti sambungkan ke Polymarket API / CLOB
        print(f"[LIVE] Buy {size} {side} at ${price:.4f}")
