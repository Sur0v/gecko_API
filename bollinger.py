import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_excel('/Users/suregeeralp/Desktop/gecko_API-main/gecko_auto.xlsx')  
#print(df.head())

def calculate_bollinger_bands_for_coin(df, coin_id, period=20, std_dev=2):
    """
    Calculate Bollinger Bands for a specific coin in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the historical data.
    coin_id (str): ID of the coin for which to calculate the Bollinger Bands.
    period (int, optional): Number of days over which to calculate the SMA. Defaults to 20.
    std_dev (int, optional): Number of standard deviations for the upper and lower bands. Defaults to 2.
    
    Returns:
    pd.DataFrame: DataFrame with the SMA, upper band, and lower band for the specified coin.
    """
    # Filter the DataFrame for the specified coin
    coin_data = df[df['coin_id'] == coin_id]
    
    # Calculate the SMA
    coin_data['SMA'] = coin_data['price'].rolling(window=period).mean()
    
    # Calculate the standard deviation
    coin_data['SD'] = coin_data['price'].rolling(window=period).std()
    
    # Calculate the upper and lower bands
    coin_data['Upper_Band'] = coin_data['SMA'] + (coin_data['SD'] * std_dev)
    coin_data['Lower_Band'] = coin_data['SMA'] - (coin_data['SD'] * std_dev)
    
    return coin_data

def plot_bollinger_bands_for_coin(coin_data):
    """
    Plot the Bollinger Bands along with the price data for a specific coin.
    
    Parameters:
    coin_data (pd.DataFrame): DataFrame containing the historical data with SMA, upper band, and lower band for the specified coin.
    """
    fig = go.Figure()
    
    # Add the price data
    fig.add_trace(go.Scatter(x=coin_data['date'], y=coin_data['price'], mode='lines', name='Price'))
    
    # Add the SMA
    fig.add_trace(go.Scatter(x=coin_data['date'], y=coin_data['SMA'], mode='lines', name='SMA'))
    
    # Add the upper band
    fig.add_trace(go.Scatter(x=coin_data['date'], y=coin_data['Upper_Band'], mode='lines', name='Upper Band'))
    
    # Add the lower band
    fig.add_trace(go.Scatter(x=coin_data['date'], y=coin_data['Lower_Band'], mode='lines', name='Lower Band'))
    
    # Set the title and labels
    fig.update_layout(title=f'Bollinger Bands for {coin_data["coin_id"].iloc[0]}', xaxis_title='Date', yaxis_title='Price')
    
    # Show the plot
    fig.show()

btc_bol = calculate_bollinger_bands_for_coin(df, "bitcoin", period=20, std_dev=2)
plot_bollinger_bands_for_coin(btc_bol)
