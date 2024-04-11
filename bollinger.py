import pandas as pd
import talib as ta
import matplotlib.pyplot as plt

df = pd.read_parquet("META.parquet")
df["upper"], df["middle"], df["lower"] = ta.BBANDS(df["Close"])
df[["Close", "middle", "upper", "lower"]].plot(grid=True)
plt.fill_between(df.index, df["upper"], df["lower"], alpha=0.5)
plt.show()
