import ccxt
import local_config
import requests

# for x in ccxt.exchanges:
#     print(x)

# exchange = ccxt.kucoin({
#     'apiKey': local_config.KUCOIN_API_KEY,
#     'secret': local_config.KUCOIN_SECRET_KEY,
#     'password': local_config.KUCOIN_PASSPHRASE,
# })

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

# balance = exchange.fetch_balance()
# print(balance)
# 19:00


c = requests.get("https://api.opensea.io/api/v1/collections")
print(c.json())

b = requests.get("https://api.opensea.io/api/v1/collections")
print(b.json())


# Add parent hash
class Block:
    id = None
    history = None
    parent_id = None

block_A = Block()
block_A.id = 1
block_A.history = 'Nelson likes cat'

block_B = Block()
block_B.id = 2
block_B.history = 'Marie likes dog'
block_B.parent_id = block_A.id

block_C = Block()
block_C.id = 3
block_C.history = 'Sky hates dog'
block_C.parent_id = block_B.id










