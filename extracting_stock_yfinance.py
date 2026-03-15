import yfinance as yf
import pandas as pd


apple = yf.Ticker("AAPL")
#Using the `Ticker` module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is `AAPL`.


import json
with open("dataFileMap/apple.json") as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info


apple_info['country']


apple_share_price_data = apple.history(period="max")
# Using the history() method we can get the share price of the stock over a certain period of time.

apple_share_price_data.head()
#The format that the data is returned in is a Pandas DataFrame. With the `Date` as the index the share `Open`, `High`, `Low`, `Close`, `Volume`, and `Stock Splits` are given for each day.


apple_share_price_data.reset_index(inplace=True)


print(apple_share_price_data.plot(x="Date", y="Open"))


print(apple.dividends)

print(apple.dividends.plot())
