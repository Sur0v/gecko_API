from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
btc_price = cg.get_price(ids='bitcoin', vs_currencies='usd')
print(btc_price.keys())
print(btc_price["bitcoin"])
print(btc_price["bitcoin"]["usd"])
s = cg.get_coin_history_by_id('bitcoin',"30-12-2022",localization = False)
print(s["market_data"]['current_price']['usd'])
"""
current_price
market_cap (market capitalization)
total_volume (time period?)
total_supply /gerekirse max supply
circulating_supply
price_change (term? short/long)

functions
Simple Moving Average (SMA)
avg price or volume of a token over specific number of days
Simple_Moving_Average (token_id,days)
asasdfaasdfasdfsasdf
Exponential Moving Average (EMA) (token_id,days)
more weight to recent prices/voulumes
3. Weighted Moving Average (WMA)
different weights for different time periods
