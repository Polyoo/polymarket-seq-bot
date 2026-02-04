
from config import Config

def main():
    print("🔧 Checking config...")
    print(f"Private Key: {'✓' if Config.PRIVATE_KEY else '✗'}")
    print(f"Signature Type: {Config.SIGNATURE_TYPE}")
    print(f"Funder: {Config.FUNDER or 'None'}")
    print(f"API Key: {'✓' if Config.API_KEY else '✗'}")
    print(f"API Secret: {'✓' if Config.API_SECRET else '✗'}")
    print(f"API Passphrase: {'✓' if Config.API_PASSPHRASE else '✗'}")
    print(f"DRY_RUN: {Config.DRY_RUN}")

if __name__ == "__main__":
    main()
