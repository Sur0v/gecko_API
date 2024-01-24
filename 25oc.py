from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()
detailed_prices = cg.get_price(ids='bitcoin',
                vs_currencies='usd',
                include_market_cap=True,
                include_24hr_vol=True,
                include_24hr_change=True,
                include_last_updated_at=False)
market = cg.get_coins_markets(vs_currency = "usd", order = "market_cap_desc")[0:2][0]["id"]  #bunun çıktısı direkt idye eşit. bitcoin veriyor.
genel_market = cg.get_coins_markets(vs_currency = "usd", order = "market_cap_desc")[0:99]
i = 0
top_100_ids1 = list()

while i<len(genel_market):
    top_100_ids1.append(genel_market[i]["id"])
    i += 1
#print(top_100_ids1)
data = cg.get_coin_history_by_id(id='bitcoin',date='10-11-2020', localization='false') #gün özelinde data çekmek: data["usd"]

datam2 = cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days='3') #tarih değil timestamp veriyor bu da belli bir aralıkta.

print(datam2)
"""
hist = cg.get_coin_market_chart_range_by_id(id = "bitcoin",
                                            vs_currency = "usd",
                                            from_timestamp = "1705834453",
                                            to_timestamp = "1706134453")
print(hist)
"""
