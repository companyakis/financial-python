from binance import Client

import pandas as pd

client = Client(None, None)

coin = "ETHUSDT"

coin_raw_data = client.get_historical_klines(coin,
                                             Client.KLINE_INTERVAL_1WEEK,
                                             "1 January 2024",
                                             "15 June 2024")

data = pd.DataFrame(coin_raw_data)

print(data.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 24 entries, 0 to 23
Data columns (total 12 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       24 non-null     int64 
 1   1       24 non-null     object
 2   2       24 non-null     object
 3   3       24 non-null     object
 4   4       24 non-null     object
 5   5       24 non-null     object
 6   6       24 non-null     int64 
 7   7       24 non-null     object
 8   8       24 non-null     int64 
 9   9       24 non-null     object
 10  10      24 non-null     object
 11  11      24 non-null     object

"""

# What are the column names?

# https://stackoverflow.com/questions/50374993/what-are-the-column-header-names-in-from-historical-klines-websocket-in-binance

# I am not sure yet!
