import pandas as pd
import talib as ta
import matplotlib.pyplot as plt

df = pd.read_parquet("META.parquet")
df["TEMA"] = ta.TEMA(df["Close"], timeperiod=10)
ax = df[["Close", "TEMA"]].plot(grid=True)
plt.show()
