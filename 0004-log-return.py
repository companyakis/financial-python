garanti["log return"] = np.log(garanti['Adj Close'] / garanti['Adj Close'].shift(1))

print(garanti["log return"])

"""
Date
2000-05-10         NaN
2000-05-11   -0.057820
2000-05-12    0.023531
2000-05-15   -0.023531
2000-05-16    0.000000
                ...   
2024-01-02    0.008532
2024-01-03   -0.040751
2024-01-04    0.019282
2024-01-05   -0.003478
2024-01-08    0.078702
Name: log return, Length: 6067, dtype: float64
"""
