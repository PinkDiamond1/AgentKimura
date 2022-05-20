import ccxt

exchange = ccxt.liquid()

book = exchange.fetch_order_book("BTC/JPY")
print(book)