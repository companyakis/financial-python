#use historical data

garanti['simple return'] = (garanti['Adj Close'] / garanti['Adj Close'].shift(1)) - 1

garanti['simple return']

"""
Date
2000-05-10         NaN
2000-05-11   -0.056180
2000-05-12    0.023810
2000-05-15   -0.023256
2000-05-16    0.000000
                ...   
2024-01-02    0.008569
2024-01-03   -0.039932
2024-01-04    0.019469
2024-01-05   -0.003472
2024-01-08    0.081881
Name: simple return, Length: 6067, dtype: float64

"""
