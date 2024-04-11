import talib as ta
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet("META.parquet")
plt.style.use("fivethirtyeight")
df['SMA_50'] = ta.SMA(df['Close'], timeperiod=50)
df['SMA_200'] = ta.SMA(df['Close'], timeperiod=200)
df[['Close', 'SMA_50', 'SMA_200']].plot()
plt.show()
