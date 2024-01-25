from pycoingecko import CoinGeckoAPI
from datetime import datetime

cg = CoinGeckoAPI()

genel_market = cg.get_coins_markets(vs_currency="usd", order="market_cap_desc")[0:5]
top_100_ids1 = [coin["id"] for coin in genel_market]

crypto_data_dict = {}

for coin_id in top_100_ids1:
    for date in ['22-01-2024', '23-01-2024', '24-01-2024']:  # Add more dates as needed
        coin_data = cg.get_coin_history_by_id(id=coin_id, date=date, localization='false')

        # Extract relevant information
        if "market_data" in coin_data:
            current_price = coin_data["market_data"]["current_price"]["usd"]
            market_cap = coin_data["market_data"]["market_cap"]["usd"]

            # Build dictionary
            if coin_id not in crypto_data_dict:
                crypto_data_dict[coin_id] = {}

            crypto_data_dict[coin_id][date] = {
                'market_cap': market_cap,
                'price': current_price
            }
        else:
            print(f"Skipping {coin_id} on {date}. 'market_data' not found in response.")

# Print or use crypto_data_dict as needed
print(crypto_data_dict)
