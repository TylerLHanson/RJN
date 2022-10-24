import ccxt
import local_config
import requests


# Sch PTL - TA Lib PT











# for x in ccxt.exchanges:
#     print(x)

# exchange = ccxt.kucoin({
#     'apiKey': local_config.KUCOIN_API_KEY,
#     'secret': local_config.KUCOIN_SECRET_KEY,
#     'password': local_config.KUCOIN_PASSPHRASE,
# })

exchange = ccxt.coinbasepro()

markets = exchange.load_markets()
# print(markets)

assets = []
for x in markets:
    pairs = x.split('/')
    assets.append(pairs[0])
    # print(pairs[0])
    # print(pairs[1])

for x in set(assets):
    print(x)










# Horizen
# ticker = exchange.fetch_ticker('ZEN/USDT')
# print(ticker)

# ohlc = exchange.fetch_ohlcv('ETH/USDT', timeframe='1d', limit=5)
# print(ohlc)

# for candle in ohlc:
#     print(candle)

# order_book = exchange.fetch_order_book('ETH/USDT')
# print(order_book)

# balance = exchange.fetch_balance()
# print(balance)
# # 19:00


# c = requests.get("https://api.opensea.io/api/v1/collections")
# print(c.json())

# b = requests.get("https://api.opensea.io/api/v1/collections")
# print(b.json())

