import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Polymarket credentials
    PRIVATE_KEY = os.getenv("POLYMARKET_PRIVATE_KEY")
    SIGNATURE_TYPE = int(os.getenv("POLYMARKET_SIGNATURE_TYPE", "1"))
    FUNDER = os.getenv("POLYMARKET_FUNDER", None)

    API_KEY = os.getenv("POLYMARKET_API_KEY")
    API_SECRET = os.getenv("POLYMARKET_API_SECRET")
    API_PASSPHRASE = os.getenv("POLYMARKET_API_PASSPHRASE")

    # Bot settings
    TARGET_PAIR_COST = float(os.getenv("TARGET_PAIR_COST", "0.80"))
    ORDER_SIZE = int(os.getenv("ORDER_SIZE", "5"))
    DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"
    VERBOSE = os.getenv("VERBOSE", "false").lower() == "true"
