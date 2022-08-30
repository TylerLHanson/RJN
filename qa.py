import ccxt
import local_config

# for x in ccxt.exchanges:
#     print(x)

exchange = ccxt.kucoin({
    'apiKey': local_config.KUCOIN_API_KEY,
    'secret': local_config.KUCOIN_SECRET_KEY,
    'password': local_config.KUCOIN_PASSPHRASE,
})

# markets = exchange.load_markets()

# for x in markets:
#     print(x)

# Horizen
# ticker = exchange.fetch_ticker('ZEN/USDT')
# print(ticker)

# ohlc = exchange.fetch_ohlcv('ETH/USDT', timeframe='1d', limit=5)
# print(ohlc)

# for candle in ohlc:
#     print(candle)

# order_book = exchange.fetch_order_book('ETH/USDT')
# print(order_book)

balance = exchange.fetch_balance()
print(balance)
# 19:00