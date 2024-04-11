import yfinance as yf

fb = yf.Ticker("META")
df = fb.history(start="2020-01-03")
df.to_parquet("META.parquet")
