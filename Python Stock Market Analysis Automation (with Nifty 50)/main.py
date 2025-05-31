import os
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Confirm Working Directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# 2. Create Project Folders
folders = ["data", "graphs", "summary"]
for folder in folders:
    folder_path = os.path.join(current_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder created: {folder_path}")

# 3. Download Nifty 50 Data
print("Downloading Nifty 50 data...")
nifty = yf.download("^NSEI", start="2020-01-01", end="2024-12-31", interval="1d", auto_adjust=True)

# 4. Calculate Moving Averages and Returns
nifty['MA_20'] = nifty['Close'].rolling(window=20).mean()
nifty['MA_50'] = nifty['Close'].rolling(window=50).mean()
nifty['MA_200'] = nifty['Close'].rolling(window=200).mean()
nifty['Daily Return'] = nifty['Close'].pct_change()
nifty['Cumulative Return'] = (1 + nifty['Daily Return']).cumprod()

# 5. Save Raw Data to Excel
data_file = os.path.abspath(os.path.join("data", "nifty_data_with_ma.xlsx"))
nifty.to_excel(data_file)
print(f"Data saved to: {data_file}")

# 6. Plot Price with Moving Averages
plt.figure(figsize=(14, 7))
plt.plot(nifty['Close'], label='Nifty Close', linewidth=2)
plt.plot(nifty['MA_20'], label='MA 20', linestyle='--')
plt.plot(nifty['MA_50'], label='MA 50', linestyle='--')
plt.title('Nifty 50 Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
ma_plot_file = os.path.abspath(os.path.join("graphs", "ma_plot.png"))
plt.savefig(ma_plot_file)
plt.close()
print(f"Moving averages plot saved to: {ma_plot_file}")

# 7. Plot Daily Return Histogram
plt.figure(figsize=(12,6))
nifty['Daily Return'].hist(bins=50, color='skyblue')
plt.title('Distribution of Daily Returns')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.grid(True)
daily_return_file = os.path.abspath(os.path.join("graphs", "daily_return_hist.png"))
plt.savefig(daily_return_file)
plt.close()
print(f"Daily returns histogram saved to: {daily_return_file}")

# 8. Plot Cumulative Return
plt.figure(figsize=(12,6))
plt.plot(nifty['Cumulative Return'], color='green')
plt.title('Cumulative Return Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid(True)
cum_return_file = os.path.abspath(os.path.join("graphs", "cumulative_return.png"))
plt.savefig(cum_return_file)
plt.close()
print(f"Cumulative return plot saved to: {cum_return_file}")

# 9. Summary Statistics
summary = nifty[['Close', 'Daily Return']].describe()
summary_file = os.path.abspath(os.path.join("summary", "summary_stats.xlsx"))
summary.to_excel(summary_file)
print(f"Summary statistics saved to: {summary_file}")

print("\n Script completed successfully!")
