import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_bitcoin_data(num_days=365):
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(num_days)]
    
    # 0 = Fear, 1 = Neutral, 2 = Greed
    sentiments = np.random.choice(["Fear", "Neutral", "Greed"], size=num_days, p=[0.3, 0.4, 0.3])
    
    prices = []
    base_price = 45000
    for sentiment in sentiments:
        if sentiment == "Greed":
            # Higher prices during greed
            prices.append(base_price + np.random.normal(8000, 3000))
        elif sentiment == "Fear":
            # Lower prices during fear
            prices.append(base_price - np.random.normal(10000, 3000))
        else:
            # Neutral
            prices.append(base_price + np.random.normal(0, 2000))
            
    df = pd.DataFrame({
        "Date": dates,
        "Sentiment": sentiments,
        "Price": prices
    })
    
    # Inject missing values to simulate dirty data
    df.loc[10:15, 'Price'] = np.nan
    df.loc[20:25, 'Sentiment'] = np.nan
    
    # Inject duplicates
    df = pd.concat([df, df.iloc[50:55]], ignore_index=True)
    
    # Write to CSV
    df.to_csv("bitcoin_data.csv", index=False)
    print("Dataset 'bitcoin_data.csv' generated successfully!")

if __name__ == "__main__":
    generate_bitcoin_data()
