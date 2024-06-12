from binance import Client

client = Client(None, None)

coin = "ETHUSDT"

coin_raw_data = client.get_historical_klines(coin,
                                             Client.KLINE_INTERVAL_1WEEK,
                                             "1 January 2024",
                                             "15 June 2024")

#print(coin_raw_data)

print(type(coin_raw_data)) # <class 'list'>

#print(coin_raw_data[0])

print(len(coin_raw_data)) # 24

"""
[1704067200000, '2281.87000000', '2431.30000000', '2100.00000000', '2221.42000000', '2729092.45640000', 1704671999999, '6206804228.44682200', 5422816, '1385089.59850000', '3149644206.21471300', '0']

"""
