from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
#Price çekme id ile. liste oluşturup tek tek priceları böyle isime özel tutabiliriz.
prices = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies='usd')
#print(prices)
prices_list = list()
for i in prices:
    prices_list.append(prices[i]["usd"])
#print(prices_list)
#print(prices.keys()) #keyler coin listesi görevi görüyor.

detailed_prices = cg.get_price(ids='bitcoin',
                vs_currencies='usd',
                include_market_cap=True,
                include_24hr_vol=True,
                include_24hr_change=True,
                include_last_updated_at=True)
#print(detailed_prices)
ping = cg.ping()
#print(ping)
coins_list = cg.get_coins_list()
#print(coins_list[0:4])
market = cg.get_coins_markets(vs_currency = "usd", order = "market_cap_desc")[0:5]
print(market)

hist = cg.get_coin_market_chart_range_by_id(id = "bitcoin",
                                            vs_currency = "usd",
                                            from_timestamp = "0",
                                            to_timestamp = "1")
print(hist)
"""
hist2 = cg.(id = "bitcoin",
                                            vs_currency = "usd",
                                            from_timestamp = "1609459200",
                                            to_timestamp = "1612137600")
print(hist2)
data = cg.get_coin_history_by_id(id='bitcoin',date='10-11-2020', localization='false')

cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days='3')
