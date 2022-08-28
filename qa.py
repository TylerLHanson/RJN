import ccxt
print(ccxt.exchanges)

kucoin = ccxt.kucoin({
    'apikey': 'xxxx'
})

print(kucoin)

symbol = 'BTC-USDT'
timeframe = '15m'
limit = 500

bars = kucoin.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
print(bars)
