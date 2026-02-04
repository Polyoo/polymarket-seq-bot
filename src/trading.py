def execute_trade(up_price, down_price, order_size, target_cost, dry_run=True):
    total_cost = up_price + down_price
    if total_cost <= target_cost:
        if dry_run:
            print(f"🎯 SIMULATION: Buy {order_size} UP + {order_size} DOWN @ total {total_cost:.2f}")
        else:
            print(f"✅ LIVE: Executing {order_size} UP + {order_size} DOWN orders")
            # TODO: integrate Polymarket CLOB API buy function here
        profit = order_size * (1 - total_cost)  # simplified profit estimate
        print(f"Expected profit: {profit:.2f}")
        return True
    else:
        print(f"No arbitrage: UP={up_price} + DOWN={down_price} = {total_cost:.2f} (needs <= {target_cost})")
        return False
