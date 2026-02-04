import asyncio
from core.polymarket_poll import PolymarketPoll
from core.strategy import Strategy

TRADE_AMOUNT_USD = 5
THRESHOLD_CENT = 0.40

async def bot_loop():
    poll = PolymarketPoll()
    strategy = Strategy(trade_amount=TRADE_AMOUNT_USD, threshold=THRESHOLD_CENT)

    def update_callback(up_price, down_price):
        strategy.check_price(poll.market_id, up_price, down_price)

    await poll.start_polling(update_callback)

if __name__ == "__main__":
    print("🚀 Polymarket live polling bot started!")
    asyncio.run(bot_loop())
