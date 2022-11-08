import ccxt
import local_config
import pandas as pd
import requests
import ta
from ta.volatility import BollingerBands, AverageTrueRange


exchange = ccxt.coinbasepro()

bars = exchange.fetch_ohlcv('ETH/USDT', limit=20)

# for bar in bars:
#     print(bar)


# timestamp
# https://www.unixtimestamp.com/

df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
print(df)

# https://github.com/bukosabino/ta/blob/7ffda486d574fcb5e8f6426a4d92cd115d17b7cf/ta/volatility.py#L67
# bb_indicator = BollingerBands()








# ----------------------------------------------------------------------------

# for x in ccxt.exchanges:
#     print(x)

# exchange = ccxt.kucoin({
#     'apiKey': local_config.KUCOIN_API_KEY,
#     'secret': local_config.KUCOIN_SECRET_KEY,
#     'password': local_config.KUCOIN_PASSPHRASE,
# })


# markets = exchange.load_markets()
# print(markets)

# assets = []
# for x in markets:
#     pairs = x.split('/')
#     assets.append(pairs[0])
#     # print(pairs[0])
#     # print(pairs[1])

# for x in sorted(set(assets)):
#     print(x)

# for x in sorted(markets):
#     print(x)

# ohlc = exchange.fetch_ohlcv('ETH/USDT', timeframe='1d', limit=5)
# print(ohlc)

# p00ls = exchange.fetch_ohlcv('00/USD', timeframe='1d', limit=5)
# print(p00ls)

# for candle in p00ls:
#     print(candle)








# Horizen
# ticker = exchange.fetch_ticker('ZEN/USDT')
# print(ticker)

# order_book = exchange.fetch_order_book('ETH/USDT')
# print(order_book)

# balance = exchange.fetch_balance()
# print(balance)
# # 19:00


# c = requests.get("https://api.opensea.io/api/v1/collections")
# print(c.json())

# b = requests.get("https://api.opensea.io/api/v1/collections")
# print(b.json())

