import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_excel('/Users/suregeeralp/Desktop/gecko_API-main/gecko_auto.xlsx')  
def calculate_and_visualize_ema(df, coin_id, period, weighting_factor=None):
    coin_data = df[df['coin_id'] == coin_id]
    if period < 1 or period > len(coin_data):
        raise ValueError("Period must be between 1 and the length of the coin data.")
    if weighting_factor is None:
        weighting_factor = 2 / (1 + period)
    prices = coin_data['price'].values
    ema = np.zeros(len(prices))
    sma = np.mean(prices[:period])
    ema[period - 1] = sma
    for i in range(period, len(prices)):
        ema[i] = (prices[i] * weighting_factor) + (ema[i - 1] * (1 - weighting_factor))
    ema_df = pd.DataFrame({'date': coin_data['date'].iloc[:len(ema)], 'price_ema': ema})
    ema_df = ema_df[ema_df['price_ema'] > 0]
    fig = px.line(ema_df, x='date', y='price_ema', title=f'Exponential Moving Average({period}) for {coin_id}'.title())
    fig.show()

calculate_and_visualize_ema(df, 'bitcoin', 20)
