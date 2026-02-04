from config import THRESHOLD_CENT, TRADE_AMOUNT_USD

class Strategy:
    def __init__(self, ws):
        self.ws = ws
        self.has_traded = False

    def check_and_trade(self):
        if self.has_traded:
            return

        # Check UP price
        if self.ws.up_price and self.ws.up_price < THRESHOLD_CENT:
            print(f"⚡ Trigger BUY UP @ {self.ws.up_price}")
            # call execution.buy_up(TRADE_AMOUNT_USD)
            self.has_traded = True

        # Check DOWN price
        if self.ws.down_price and self.ws.down_price < THRESHOLD_CENT:
            print(f"⚡ Trigger BUY DOWN @ {self.ws.down_price}")
            # call execution.buy_down(TRADE_AMOUNT_USD)
            self.has_traded = True
