from binance import Client

import pandas as pd

client = Client(None, None)

coins = ["BTCUSDT", "ETHUSDT"]

for coin in coins:
    
    coin_raw_data = client.get_historical_klines(coin,
                                                 Client.KLINE_INTERVAL_1WEEK,
                                                 "1 January 2024",
                                                 "15 June 2024")
    
    data = pd.DataFrame(coin_raw_data)
    
    data.to_csv(f"{coin.lower()}.csv")
