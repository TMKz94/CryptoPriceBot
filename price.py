from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

prices = cg.get_price(ids=['bitcoin', 'chainlink', 'ethereum', 'solana', 'litecoin'], vs_currencies=['usd', 'eur'])

btc_usd = float(prices['bitcoin']['usd'])
btc_eur = float(prices['bitcoin']['eur'])

eth_usd = float(prices['ethereum']['usd'])
eth_eur = float(prices['ethereum']['eur'])

link_usd = float(prices['chainlink']['usd'])
link_eur = float(prices['chainlink']['eur'])

sol_usd = float(prices['solana']['usd'])
sol_eur = float(prices['solana']['eur'])

ltc_usd = float(prices['litecoin']['usd'])
ltc_eur = float(prices['litecoin']['eur'])

bitcoin = (btc_usd, btc_eur)
ethereum = (eth_usd, eth_eur)
link = (link_usd, link_eur)
solana = (sol_usd, sol_eur)
litecoin = (ltc_usd, ltc_eur)
