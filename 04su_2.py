import numpy as np
import pandas as pd
from pycoingecko import CoinGeckoAPI
from generate_days import generate_dates
df = pd.read_excel('/Users/suregeeralp/Desktop/gecko_API-main/gecko_auto.xlsx')  
print(df.head())
import pandas as pd

def calculate_price_sma(df, coin_id, time_interval):
    """
    Function to calculate the Simple Moving Average (SMA) of price for a given coin over a specified time interval.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the historical data.
    coin_id (str): ID of the coin for which to calculate the SMA.
    time_interval (int): Number of days over which to calculate the SMA.
    
    Returns:
    pd.Series: Series object containing the SMA of price for the specified coin and time interval.
    """
    # Filter the DataFrame for the specified coin
    coin_data = df[df['coin_id'] == coin_id]
    
    # Calculate the SMA of price
    price_sma = coin_data['price'].rolling(window=time_interval).mean()
    price_sma = price_sma.dropna()
    
    return price_sma

def calculate_volume_sma(df, coin_id, time_interval):
    """
    Function to calculate the Simple Moving Average (SMA) of volume for a given coin over a specified time interval.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the historical data.
    coin_id (str): ID of the coin for which to calculate the SMA.
    time_interval (int): Number of days over which to calculate the SMA.
    
    Returns:
    pd.Series: Series object containing the SMA of volume for the specified coin and time interval.
    """
    # Filter the DataFrame for the specified coin
    coin_data = df[df['coin_id'] == coin_id]
    
    # Calculate the SMA of volume
    volume_sma = coin_data['total_volume'].rolling(window=time_interval).mean()
    volume_sma = volume_sma.dropna()

    return volume_sma

print(calculate_price_sma(df,"bitcoin",5))