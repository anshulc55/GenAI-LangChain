import pandas as pd
import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/Users/anshul/Training/GenAI-LangChain/9-Create_WebApps_for_Machine_Learning/Nifty500 - Sheet1.csv')

# Extract the 'Symbol' column and add '.NS' suffix for NSE stocks
tickers = df['SYMBOL'].apply(lambda x: x + '.NS').tolist()

# Step 2: Parameters
start_date = "2024-10-23"
end_date = "2024-12-01"

# Step 3: Process Each Stock
for ticker in tickers:
    print(f"Processing {ticker}...")

    # Download Historical Data
    data = yf.download(ticker, start=start_date, end=end_date)

    # Calculate RSI
    data['RSI'] = ta.rsi(data['Close'], length=14)

    # Identify Oversold RSI (<30)
    data['Oversold'] = data['RSI'] < 30

    # Detect Bullish Divergence
    data['Price_Low'] = data['Close'].rolling(window=3).min()  # Find local lows
    data['RSI_Low'] = data['RSI'].rolling(window=3).min()     # RSI lows
    data['Lower_Low'] = data['Price_Low'] < data['Price_Low'].shift(1)  # Lower low in price
    data['Higher_RSI'] = data['RSI_Low'] > data['RSI_Low'].shift(1)     # Higher low in RSI

    # Mark Bullish Divergence
    data['Bullish_Divergence'] = data['Lower_Low'] & data['Higher_RSI'] & data['Oversold']

    # Filter Divergence Points
    divergence_points = data[data['Bullish_Divergence']]

    # Check if there are any divergence points
    if divergence_points.empty:
        print(f"No bullish divergence found for {ticker}. Skipping graph...")
        continue

    print(f"Bullish divergence detected for {ticker}. Plotting results...")

    # Plotting
    plt.figure(figsize=(12, 8))

    # Price Plot
    plt.subplot(2, 1, 1)
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.scatter(divergence_points.index, divergence_points['Close'], color='green', label='Bullish Divergence', marker='^')
    plt.title(f'{ticker} Price Chart with Bullish Divergence')
    plt.legend()

    # RSI Plot
    plt.subplot(2, 1, 2)
    plt.plot(data['RSI'], label='RSI', color='purple')
    plt.axhline(30, linestyle='--', color='red', label='Oversold Line')
    plt.scatter(divergence_points.index, divergence_points['RSI'], color='green', label='Bullish Divergence', marker='^')
    plt.title('RSI Chart')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Optional: Save Results to a File
    divergence_points.to_csv(f"{ticker}_bullish_divergence.csv")
    print(f"Divergence points for {ticker} saved to {ticker}_bullish_divergence.csv")