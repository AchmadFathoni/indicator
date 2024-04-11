import yfinance as yf
import talib as ta
import pandas as pd
import matplotlib.pyplot as plt

fb = yf.Ticker("META")
df = fb.history(start="2021-01-03")

plt.style.use("fivethirtyeight")
df['EMA_50'] = ta.EMA(df['Close'], timeperiod=50)
df['EMA_200'] = ta.EMA(df['Close'], timeperiod=200)
df[['Close', 'EMA_50', 'EMA_200']].plot()
plt.show()
