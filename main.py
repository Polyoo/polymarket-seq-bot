import asyncio
from core.polymarket_poll import PolymarketPoll
from core.strategy import Strategy  # pastikan ada method check_price(up_price, down_price)
from config import TRADE_AMOUNT_USD, THRESHOLD_CENT, SESSION_SECONDS

async def bot_loop():
    # Init polling bot & strategy
    poll = PolymarketPoll()
    strategy = Strategy(trade_amount=TRADE_AMOUNT_USD, threshold=THRESHOLD_CENT)

    def update_callback(up_price, down_price):
        """
        Trigger setiap kali price update
        """
        # Check logic kau: harga < threshold
        strategy.check_price(up_price, down_price)

    # Start polling loop
    await poll.start_polling(update_callback)

if __name__ == "__main__":
    print("🚀 Polymarket live polling bot started!")
    asyncio.run(bot_loop())
