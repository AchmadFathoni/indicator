import pandas as pd
import talib as ta
import matplotlib.pyplot as plt

df = pd.read_parquet("META.parquet")
df["RSI"] = ta.RSI(df["Close"])
fig, ax = plt.subplots(nrows=2,ncols=1, sharex=True)
df["Close"].plot(ax=ax[0])
df['RSI'].plot(ax=ax[1], color='yellow')
ax[1].hlines(y=[30, 100],xmin=df.index[0], xmax=df.index[-1], color=['red', 'green'])
ax[0].grid(True)
ax[1].grid(True)
plt.show()
