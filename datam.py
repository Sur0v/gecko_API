import numpy as np
import pandas as pd
from pycoingecko import CoinGeckoAPI
from generate_days import generate_dates

cg = CoinGeckoAPI()

# Collect top 100 coin ids and store them as a numpy array
genel_market = cg.get_coins_markets(vs_currency="usd", order="market_cap_desc")[0:99]
top_100_ids1 = [coin["id"] for coin in genel_market]
top_100_ids_np = np.array(top_100_ids1)

# Build a numpy array for dates
global_dates = generate_dates("01-01-2020", "31-01-2024")
#dates_np = np.array(global_dates)

# Store the data locally as a pandas DataFrame
df = pd.DataFrame(columns=['coin_id', 'date', 'market_cap', 'price', 'total_volume'])

for coin_id in top_100_ids1:
    for date in global_dates:
        coin_data = cg.get_coin_history_by_id(id=coin_id, date=date, localization='false')

        if "market_data" in coin_data:
            current_price = coin_data["market_data"]["current_price"]["usd"]
            market_cap = coin_data["market_data"]["market_cap"]["usd"]
            total_volume = coin_data["market_data"]["total_volume"]["usd"]

            df = df.append({'coin_id': coin_id, 'date': date, 'market_cap': market_cap, 'price': current_price, 'total_volume': total_volume}, ignore_index=True)

# Save the DataFrame
df.to_excel('./gecko_autogenel.xlsx', index=False)
df = pd.read_excel('/Users/suregeeralp/Desktop/gecko_API-main/gecko_autogenel.xlsx')  
print(df.head(5))