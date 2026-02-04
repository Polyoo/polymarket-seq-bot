class Strategy:
    def __init__(self, trade_amount=5, threshold=0.40):
        self.trade_amount = trade_amount
        self.threshold = threshold
        self.total_profit = 0
        self.history = []

    def check_price(self, market_id, up_price, down_price):
        buy_msg = ""
        profit_change = 0

        if up_price < self.threshold:
            buy_msg = f"💹 BUY UP! Price: {up_price:.2f}"
            profit_change = self.trade_amount * (1 - up_price)
            self.total_profit += profit_change
            self.history.append(("Up", up_price, profit_change))

        elif down_price < self.threshold:
            buy_msg = f"💹 BUY DOWN! Price: {down_price:.2f}"
            profit_change = self.trade_amount * (1 - down_price)
            self.total_profit += profit_change
            self.history.append(("Down", down_price, profit_change))

        self.display_panel(market_id, up_price, down_price, buy_msg)

    def display_panel(self, market_id, up_price, down_price, buy_msg):
        print("\033c", end="")  # clear terminal
        print(f"🚀 Polymarket Live Dashboard")
        print(f"🕒 Market ID: {market_id}")
        print(f"💹 Current Prices -> Up: {up_price:.2f} | Down: {down_price:.2f}")
        if buy_msg:
            print(buy_msg)
        print(f"💰 Total Profit: {self.total_profit:.2f} USD")
        print("-" * 40)
        if self.history:
            print("History (last 5):")
            for h in self.history[-5:]:
                print(f"{h[0]} @ {h[1]:.2f} => Profit: {h[2]:.2f}")
