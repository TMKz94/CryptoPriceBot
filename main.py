from config import create_api
import tweepy
import logging
import time
import os
from price import bitcoin, ethereum, link, solana, litecoin


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

btc = f"Bitcoin  -  ${bitcoin[0]}  (€{bitcoin[1]})"
eth = f"Ethereum  -  ${ethereum[0]}  (€{ethereum[1]})"
link = f"Chainlink  -  ${link[0]}  (€{link[1]})"
sol = f"Solana  -  ${solana[0]} (€{solana[1]})"
ltc = f"Litecoin  -  ${litecoin[0]} (€{litecoin[1]})"

tweet = f"{btc}\n{eth}\n{link}\n{sol}\n{ltc}"

def main():
	api = create_api()
	api.update_status(tweet)
	logger.info("Tweet Sent")

if __name__ == "__main__":
	main()
