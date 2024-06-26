import pandas as pd
import yfinance as yf

start_date = "2024-01-01"

end_date = "2024-05-15"
 
symbol = "GARAN.IS" 

df = yf.download(symbol, start_date, end_date)

print(df.head(10))

print("*************************************************************************")

print(df.info())

print("*************************************************************************")

print(df.describe())

"""
[*********************100%%**********************]  1 of 1 completed
                 Open       High        Low      Close  Adj Close    Volume
Date                                                                       
2024-01-02  59.299999  60.150002  58.250000  58.849998  56.282829  16881291
2024-01-03  58.599998  59.150002  56.299999  56.500000  54.035343  20141213
2024-01-04  56.400002  57.750000  55.000000  57.599998  55.087357  31275024
2024-01-05  57.700001  58.000000  56.549999  57.400002  54.896084  22935879
2024-01-08  58.299999  62.750000  58.299999  62.099998  59.391056  62599601
2024-01-09  62.400002  63.700001  61.250000  62.599998  59.869244  60396241
2024-01-10  62.500000  64.449997  62.349998  63.799999  61.016899  41187587
2024-01-11  64.250000  68.699997  64.000000  65.599998  62.738380  48524495
2024-01-12  65.400002  69.199997  64.650002  67.800003  64.842415  66351606
2024-01-15  67.050003  67.650002  66.150002  66.500000  63.599121  30258890
*************************************************************************
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 90 entries, 2024-01-02 to 2024-05-14
Data columns (total 6 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   Open       90 non-null     float64
 1   High       90 non-null     float64
 2   Low        90 non-null     float64
 3   Close      90 non-null     float64
 4   Adj Close  90 non-null     float64
 5   Volume     90 non-null     int64  
dtypes: float64(5), int64(1)
memory usage: 4.9 KB
None
*************************************************************************
            Open       High        Low      Close  Adj Close        Volume
count  90.000000  90.000000  90.000000  90.000000  90.000000  9.000000e+01
mean   68.280556  69.777777  67.170556  68.357777  66.407596  3.188529e+07
std     7.984584   8.225994   7.950616   8.165778   9.247931  1.223030e+07
min    56.400002  57.750000  55.000000  56.500000  54.035343  1.320246e+07
25%    63.212501  64.124998  62.012501  63.175001  60.419165  2.408278e+07
50%    65.199997  66.449997  64.250000  65.025002  62.188465  2.896853e+07
75%    69.962500  73.275002  69.487499  71.275000  70.474998  3.866550e+07
max    89.400002  91.150002  87.750000  90.000000  90.000000  7.353749e+07

"""
