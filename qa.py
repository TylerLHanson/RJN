import ccxt
# import local_config
import pandas as pd
import requests
import ta
from ta.volatility import BollingerBands, AverageTrueRange


# -------------------------------------------------------------------------------------------------------
# c = requests.get("https://api.opensea.io/api/v1/collections")
# print(c.json())

# b = requests.get("https://api.opensea.io/api/v1/collections")
# print(b.json())


# -------------------------------------------------------------------------------------------------------
# https://github.com/bukosabino/ta/blob/7ffda486d574fcb5e8f6426a4d92cd115d17b7cf/ta/volatility.py#L67
# bb_indicator = BollingerBands()


# -------------------------------------------------------------------------------------------------------
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

exchange = ccxt.coinbasepro()

bars = exchange.fetch_ohlcv('BTC/USDT', limit=40)

# for bar in bars:
#     print(bar)

df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

atr_indicator = AverageTrueRange(df['high'], df['low'], df['close'])
df['atr'] = atr_indicator.average_true_range()
print(df)
