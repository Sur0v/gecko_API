import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_excel('/Users/suregeeralp/Desktop/gecko_API-main/gecko_auto.xlsx')  
#print(df.head())

def calculate_and_visualize_ema(df, coin_id, period, weighting_factor=None):
    """
    Calculate and visualize the Exponential Moving Average (EMA) for a given coin over a specified time interval.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the historical data.
    coin_id (str): ID of the coin for which to calculate the EMA.
    period (int): Number of days over which to calculate the EMA.
    weighting_factor (float, optional): Weighting factor for the EMA calculation. Defaults to 2/(1+N).
    """
    # Filter the DataFrame for the specified coin
    coin_data = df[df['coin_id'] == coin_id]
    
    # Ensure the period is valid
    if period < 1 or period > len(coin_data):
        raise ValueError("Period must be between 1 and the length of the coin data.")
    
    # Calculate the EMA of price
    if weighting_factor is None:
        weighting_factor = 2 / (1 + period)
    prices = coin_data['price'].values
    ema = np.zeros(len(prices))
    sma = np.mean(prices[:period])
    ema[period - 1] = sma
    for i in range(period, len(prices)):
        ema[i] = (prices[i] * weighting_factor) + (ema[i - 1] * (1 - weighting_factor))
    
    # Create a DataFrame with the EMA values and corresponding dates
    ema_df = pd.DataFrame({'date': coin_data['date'].iloc[:len(ema)], 'price_ema': ema})
    
    # Filter the DataFrame to exclude initial zero values
    ema_df = ema_df[ema_df['price_ema'] > 0]
    
    # Create the line plot using Plotly Express
    fig = px.line(ema_df, x='date', y='price_ema', title=f'Exponential Moving Average({period}) for {coin_id}'.title())
    
    # Show the plot
    fig.show()

# Usage example:
# df must contain 'coin_id', 'date', and 'price' columns
# Call the function with the DataFrame, the coin ID, and the time interval
calculate_and_visualize_ema(df, 'bitcoin', 20)
