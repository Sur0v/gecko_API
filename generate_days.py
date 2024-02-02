import numpy as np
from datetime import datetime, timedelta
from pycoingecko import CoinGeckoAPI


def generate_dates(starting_date, last_date):
    start_date = datetime.strptime(starting_date, "%d-%m-%Y")
    end_date = datetime.strptime(last_date, "%d-%m-%Y")

    current_date = end_date
    dates = []

    while current_date <= start_date:
        dates.append(current_date.strftime("%d-%m-%Y"))
        current_date += timedelta(days=1)

    return np.array(dates, dtype=str)

global_dates = generate_dates("31-01-2024","21-01-2024")

# Print each date on a separate line
for date in global_dates:
    print(date)
print(global_dates)
print(type(global_dates))
print(global_dates[0])
print(type(global_dates[0]))

cg = CoinGeckoAPI()

genel_market = cg.get_coins_markets(vs_currency="usd", order="market_cap_desc")[0:3]
top_100_ids1 = [coin["id"] for coin in genel_market]
top100ids_np = np.array(top_100_ids1)

crypto_data_dict = {}

for coin_id in top_100_ids1:
    for date in global_dates: # Add more dates as needed
        coin_data = cg.get_coin_history_by_id(id=coin_id, date=date, localization='false')

        # Extract relevant information
        if "market_data" in coin_data:
            current_price = coin_data["market_data"]["current_price"]["usd"]
            market_cap = coin_data["market_data"]["market_cap"]["usd"]
            total_volume = coin_data["market_data"]["total_volume"]["usd"]

            # Build dictionary
            if coin_id not in crypto_data_dict:
                crypto_data_dict[coin_id] = {}

            crypto_data_dict[coin_id][date] = {
                'market_cap': market_cap,
                'price': current_price,
                'total_volume': total_volume
            }
        else:
            print(f"Skipping {coin_id} on {date}. 'market_data' not found in response.")
            print(crypto_data_dict)