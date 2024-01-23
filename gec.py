from pycoingecko import CoinGeckoAPI

def fetch_historical_prices(coin_id, days):
    """
    Fetches historical market data for a given cryptocurrency.

    Parameters:
    - coin_id (str): Coin ID (e.g., 'bitcoin').
    - days (int): Number of days of historical data to retrieve.

    Returns:
    - list: List of historical prices.
    """
    cg = CoinGeckoAPI()
    historical_data = cg.get_coin_market_chart_by_id(coin_id, vs_currency='usd', days=days)
    prices = historical_data['prices']
    return [price[1] for price in prices]  # Extracting the closing prices


def calculate_sma(prices, window_size):
    """
    Calculates the Simple Moving Average (SMA) for a given list of prices.

    Parameters:
    - prices (list): List of numeric values representing the prices.
    - window_size (int): Number of days or periods for calculating the average.

    Returns:
    - list: List of SMA values.
    """
    sma_values = []

    for i in range(len(prices) - window_size + 1):
        window = prices[i : i + window_size]
        sma = sum(window) / window_size
        sma_values.append(sma)

    return sma_values

# Example usage:
coin_id = 'bitcoin'
days = 50  # You can adjust the number of days as needed
window_size = 10  # Adjust the window size for SMA calculation

# Fetch historical prices for Bitcoin
bitcoin_prices = fetch_historical_prices(coin_id, days)

# Calculate SMA
sma_result = calculate_sma(bitcoin_prices, window_size)

print(f"SMA({window_size}) Values for Bitcoin:", sma_result)
