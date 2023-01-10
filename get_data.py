import ccxt
# import local_config
import pandas as pd
import numpy as np
import requests
import ta
from ta.volatility import BollingerBands, AverageTrueRange


# this script uses ccxt to pull daily asset data from 4:00pm to 4:30pm UTC

# for x in ccxt.exchanges:
#     print(x)


# https://github.com/ccxt/ccxt/blob/master/python/ccxt/kucoin.py
# def fetch_ohlcv

exchange = ccxt.kucoin()
candlestick_data = exchange.fetch_ohlcv('BTC/USDT', limit=1500,
  # needs milli (below ex. tho)
  # since=1673305339262
    )
# exchange = ccxt.kucoin({
#     'apiKey': local_config.KUCOIN_API_KEY,
#     'secret': local_config.KUCOIN_SECRET_KEY,
#     'password': local_config.KUCOIN_PASSPHRASE,
# })



df = pd.DataFrame(candlestick_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
# https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
# just shave off 3 0's for s
print(df)
# CREATE THE MOST BASIC VISUAL WITHIN VS CODE

# min 






# ------------------------------------------------------------------------------------------
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




# averagetruerange
# https://github.com/bukosabino/ta/blob/master/ta/volatility.py

# bars = exchange.fetch_ohlcv('BTC/USDT', limit=40)

# # for bar in bars:
# #     print(bar)


# atr_indicator = AverageTrueRange(df['high'], df['low'], df['close'], fillna=False)
# df['atr'] = atr_indicator.average_true_range()
# df['atr'].replace(0, np.nan, inplace=True)

# # df['previous_close'] = df['close'].shift(1)

# def supertrend(df, period=7, multiplier=3):
#     df['basic_upperband'] = ((df['high'] + df['low']) / 2) + (multiplier * df['atr'])
#     df['basic_lowerband'] = ((df['high'] + df['low']) / 2) - (multiplier * df['atr'])

# supertrend(df)
# print(df)
