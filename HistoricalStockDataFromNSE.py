# In this example we will be exploring the power of Python by using one of the many publicly available libraries: NSEpy
# NSEpy is a library to extract historical and realtime data from NSE’s website. This Library aims to keep the API very simple.
# This code was initially shared by Kumar Saurabh, I have modified it to:
# 1) complete the code so that it runs smoothly - have imported the right libraries and removed some unused variables
# 2) made it more readable with the comments
# 3) modified it to use my list of stocks
# You can find NSEpy documentation at: https://nsepy.xyz/
# This has been tested on Anaconda distribution with Python 3.7

# a. import the required modules
import pandas as pd
import nsepy as nse
import datetime as dt

# b. Build the list of stocks for which you need the data
symbol =  ['NESTLEIND','HINDUNILVR','APLAPOLLO']

data1=[]
data1 = pd.DataFrame(data1)

# c. Run loop to extract price volume data (one iteration per stock). Mention start date and end date as per your need.
for x in symbol:
    data = nse.get_history(symbol=x, start=dt.date(2020,4,1), end=dt.date(2020,4,23))
    data = pd.DataFrame(data)
    data1 = pd.concat([data1,data])
    print(x)

# d. Write data to your local drive in a csv format
data1.to_csv('firstprice.csv', index=True)