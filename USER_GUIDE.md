# Polymarket Sequential BTC 15-Minute Arbitrage Bot

## Overview
This bot uses a sequential arbitrage strategy: buy whichever side (UP/DOWN) reaches <$0.40 first, then wait for the other side to reach <$0.40. The expected combined cost is around $0.80, excluding spread.

## How to Use
1. Fund your Polymarket wallet with USDC.
2. Configure `.env` with API keys and private key.
3. Start the bot:
```bash
python -m src/btc_15m_arb_bot
