import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
file_path = 'data/NIFTY_data.csv'
data = pd.read_csv(file_path)

# Strip any whitespace from column names
data.columns = data.columns.str.strip()

# Check if 'Date' column exists
print(data.columns)  # To verify column names

# Preprocess the data
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%b-%Y')
    data.set_index('Date', inplace=True)
else:
    print("Error: 'Date' column not found in the CSV file.")
    exit()

# Calculate daily percentage movement
data['Daily Move %'] = ((data['High'] - data['Low']) / data['Open']) * 100

# Strategy: Sell ATM+1% Call & Put Options when movement < 1%
data['Sell Call P/L'] = np.where(data['Daily Move %'] < 1, 100, -100)
data['Sell Put P/L'] = np.where(data['Daily Move %'] < 1, 100, -100)
data['Total P/L'] = data['Sell Call P/L'] + data['Sell Put P/L']

# Cumulative performance
data['Cumulative P/L'] = data['Total P/L'].cumsum()

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Cumulative P/L'], label='Cumulative P/L', color='blue')
plt.xlabel('Date')
plt.ylabel('Profit/Loss (₹)')
plt.title('Nifty Options Trading Strategy Backtest')
plt.legend()
plt.grid()
plt.savefig('data/cumulative_pnl.png')
plt.show()

# Performance Metrics
total_trades = len(data)
winning_trades = len(data[data['Total P/L'] > 0])
win_rate = (winning_trades / total_trades) * 100
final_pnl = data['Cumulative P/L'].iloc[-1]

with open('data/performance_metrics.txt', 'w', encoding='utf-8') as f:
    f.write(f'Total Trades: {total_trades}\n')
    f.write(f'Winning Trades: {winning_trades}\n')
    f.write(f'Win Rate: {win_rate:.2f}%\n')
    f.write(f'Final P/L: ₹{final_pnl:.2f}\n')

print(f'Total Trades: {total_trades}')
print(f'Winning Trades: {winning_trades}')
print(f'Win Rate: {win_rate:.2f}%')
print(f'Final P/L: ₹{final_pnl:.2f}')