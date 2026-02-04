# Polymarket Sequential BTC 15-Minute Arbitrage Bot

## Overview
This bot uses a sequential arbitrage strategy: buy whichever side (UP/DOWN) reaches <$0.40 first, then wait for the other side to reach <$0.40. The expected combined cost is around $0.80, excluding spread.

## How to Use
1. Fund your Polymarket wallet with USDC.
2. Configure `.env` with API keys and private key.
3. Start the bot:
bash python -m src/btc_15m_arb_bot
4. Monitor logs for arbitrage opportunities.

## Notes 
• Always test with DRY_RUN=true first.
• Adjust TARGET_PAIR_COST and ORDER_SIZE based on risk preference.
4. Scroll down → **Commit new file**  
   - Write commit message: `Add USER_GUIDE.md`  
   - Commit directly to **main** branch → Click **Commit new file**

---

### **Step 3: Tambah file strategy**

1. Klik **Add file** → **Create new file**  
2. Nama file: `STRATEGY.md`  
3. Isi content strategy kau:

markdown
# Sequential Arbitrage Strategy (v1)

- Watch BTC 15-min market on Polymarket.
- Monitor UP and DOWN prices:
  - Buy the side that first drops below $0.40
  - Wait for the other side to drop below $0.40
- Expected total cost ≈ $0.80 per pair
- Execute both orders as a pair (all-or-nothing)
- Repeat every 15 minutes market cycle
