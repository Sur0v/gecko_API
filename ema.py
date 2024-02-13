import pandas as pd
import numpy as np

# Create a dataset with closing prices for a stock
prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
df = pd.DataFrame({'close': prices})

# Calculate the EMA with a period of 5 days and a weighting factor of 0.2
df['ema'] = df['close'].ewm(span=5, adjust=False, min_periods=5).mean()

print(df)

def exponential_moving_average(prices, period, weighting_factor=0.2):
    ema = np.zeros(len(prices))
    sma = np.mean(prices[:period])
    ema[period - 1] = sma
    for i in range(period, len(prices)):
        ema[i] = (prices[i] * weighting_factor) + (ema[i - 1] * (1 - weighting_factor))
    return ema

prices = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
period = 5
weighting_factor = 0.2

ema = exponential_moving_average(prices, period, weighting_factor)
print(ema)