import yfinance as yf
import talib as ta
import pandas as pd
import matplotlib.pyplot as plt

fb = yf.Ticker("META")
df = fb.history(start="2020-01-03")

plt.style.use("fivethirtyeight")
df['MACD'], df['MACD_SIGNAL'], df['MACD_HIST'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
fig, ax = plt.subplots(nrows=2,ncols=1, sharex=True)
df['Close'].plot(ax=ax[0])
df[['MACD', 'MACD_SIGNAL']].plot(ax=ax[1])
plt.show()
