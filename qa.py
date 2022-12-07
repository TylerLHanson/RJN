import ccxt
# import local_config
import pandas as pd
import numpy as np
import requests
import ta
from ta.volatility import BollingerBands, AverageTrueRange


# -------------------------------------------------------------------------------------------------------
# c = requests.get("https://api.opensea.io/api/v1/collections")
# print(c.json())

# b = requests.get("https://api.opensea.io/api/v1/collections")
# print(b.json())


# -------------------------------------------------------------------------------------------------------
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
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')


# https://github.com/bukosabino/ta/blob/7ffda486d574fcb5e8f6426a4d92cd115d17b7cf/ta/volatility.py#L14
atr_indicator = AverageTrueRange(df['high'], df['low'], df['close'], fillna=False)
df['atr'] = atr_indicator.average_true_range()
df['atr'].replace(0, np.nan, inplace=True)

# df['previous_close'] = df['close'].shift(1)

def supertrend(df, period=7, multiplier=3):
    df['basic_upperband'] = ((df['high'] + df['low']) / 2) + (multiplier * df['atr'])
    df['basic_lowerband'] = ((df['high'] + df['low']) / 2) - (multiplier * df['atr'])

supertrend(df)
print(df)
