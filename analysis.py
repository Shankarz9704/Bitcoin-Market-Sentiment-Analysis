import pandas as pd
import matplotlib.pyplot as plt

print("🔹 STEP 2: DATA LOADING")
df = pd.read_csv("bitcoin_data.csv")
print("Initial Data:")
print(df.head())
print("-" * 50, "\n")

print("🔹 STEP 3: DATA CLEANING")
# Remove missing values
df.dropna(inplace=True)
# Remove duplicates
df.drop_duplicates(inplace=True)
# Fix date format
df['Date'] = pd.to_datetime(df['Date'])
print(f"Cleaned Data Profile:\nTotal Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
print("-" * 50, "\n")

print("🔹 STEP 4: DATA PREPROCESSING")
# Convert sentiment -> numeric
df['Sentiment_Numeric'] = df['Sentiment'].map({
    'Fear': 0,
    'Neutral': 1,
    'Greed': 2
})
print("Mapped Sentiments Sample:")
print(df[['Sentiment', 'Sentiment_Numeric']].head())
print("-" * 50, "\n")

print("🔹 STEP 5: EXPLORATORY DATA ANALYSIS (EDA)")
print("Statistical Summary:")
print(df.describe())
print("\nAverage Price by Sentiment:")
avg_price_sentiment = df.groupby('Sentiment')['Price'].mean()
print(avg_price_sentiment)
print("-" * 50, "\n")

print("🔹 STEP 6: VISUALIZATION")
# Plot 1: Average Price by Sentiment Bar Chart
plt.figure(figsize=(8, 5))
avg_price_sentiment.reindex(['Fear', 'Neutral', 'Greed']).plot(
    kind='bar', color=['red', 'gray', 'green']
)
plt.title("Average Bitcoin Price vs Market Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Average Price (USD)")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("price_by_sentiment.png")
print("Saved visualization: 'price_by_sentiment.png'")

# Plot 2: Bitcoin Price Trend Over Time
plt.figure(figsize=(12, 5))
df_sorted = df.sort_values(by="Date")
plt.plot(df_sorted['Date'], df_sorted['Price'], color='blue', alpha=0.7)
plt.title("Bitcoin Price Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("price_trend.png")
print("Saved visualization: 'price_trend.png'")

print("\n🔥 Analysis complete! Please check the output logs and generated plots.")
