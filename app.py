from iexfinance.stocks import Stock

a = Stock("TSLA", token="sk_f5ff8d3e0e234960a182e0017fb0a220")
print(a.get_price())