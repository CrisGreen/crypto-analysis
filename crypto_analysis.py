# Import the necessary libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Get Bitcoin data from Yahoo Finance
bitcoin = yf.Ticker("BTC-USD")

# Fetch historical price data (5 years of daily data)
btc_data = bitcoin.history(period="5y")

# Display the first few rows of the data to understand its structure
print(btc_data.head())

# Plot the closing price over time
plt.figure(figsize=(10, 6))
plt.plot(btc_data.index, btc_data['Close'], label='BTC-USD')
plt.title('Bitcoin Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()
# Calculate the 30-day moving average
btc_data['30-day MA'] = btc_data['Close'].rolling(window=30).mean()

# Plot the closing price along with the 30-day moving average
plt.figure(figsize=(10, 6))
plt.plot(btc_data.index, btc_data['Close'], label='BTC-USD')
plt.plot(btc_data.index, btc_data['30-day MA'], label='30-Day Moving Average', color='orange')
plt.title('Bitcoin Price and 30-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()
# Calculate daily returns
btc_data['Daily Return'] = btc_data['Close'].pct_change()

# Plot the daily returns
plt.figure(figsize=(10, 6))
plt.plot(btc_data.index, btc_data['Daily Return'], label='Daily Return', color='red')
plt.title('Bitcoin Daily Return Over Time')
plt.xlabel('Date')
plt.ylabel('Daily')
