import pandas as pd
import talib as ta
import matplotlib.pyplot as plt

df = pd.read_parquet("META.parquet")
df["ATR"] = ta.ATR(df["High"], df["Low"], df["Close"], timeperiod=14)
fig, ax = plt.subplots(nrows=2,ncols=1, sharex=True)
df["Close"].plot(ax=ax[0])
df["ATR"].plot(ax=ax[1])
ax[0].grid(True)
ax[1].grid(True)
plt.show()
