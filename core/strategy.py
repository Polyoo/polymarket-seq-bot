class Strategy:
    def __init__(self, trade_amount=5, threshold=0.40):
        self.trade_amount = trade_amount
        self.threshold = threshold
        self.session_active = False

    def check_price(self, up_price, down_price):
        """Trigger buy logic tiap price update"""
        if not self.session_active:
            print(f"🕒 New session detected!")
            self.session_active = True

        if up_price < self.threshold:
            print(f"💹 BUY UP! Current price: {up_price}")

        elif down_price < self.threshold:
            print(f"💹 BUY DOWN! Current price: {down_price}")
