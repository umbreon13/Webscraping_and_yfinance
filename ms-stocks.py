# we're going to check the Microsoft financial information using yfinance library

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# plt.style.use('seaborn')

import yfinance as yf

msft = yf.Ticker('msft')  # create the msft object
msft_info = msft.info  # store the info

# for key, value in msft_info.items():
#     print(key, ':', value)

# n_shares = msft.info['sharesOutstanding']
# print(n_shares)

# # check dividends, splits & holders
# print(msft.dividends)  # this is a pandas dataframe!!
# print(msft.splits)
# print(msft.major_holders)
# print(msft.institutional_holders)

# visualize numbers
df = msft.dividends
data = df.resample('Y').sum()  #resample the data by year ('y') into another df called data, getting the cummulative per year
data = data.reset_index()  #reset index to create a new column in the df 'data' with just the year
data['Year'] = data['Date'].dt.year

# plot with matplotlib
plt.figure()
plt.bar(data['Year'], data['Dividends'])
plt.ylabel('Dividend yield($)')
plt.xlabel('Year')
plt.title('Microsoft Dividend History')
plt.xlim(2002,2020)
plt.show()

# check the history and plot
today = datetime.now().date().strftime("%Y-%m-%d")  # establish today's date

# df_hist = msft.history(period='max')  #it's a dataframe, we can set the periodto '1mo', '3mo', '5y', '1d'...,
# df_hist = msft.history(start='2007-01-01', end='2015-01-01')
df_hist = msft.history(start='2007-01-01', end=today)

plt.figure()
plt.plot(df_hist['Close'])  # Closing price
# plt.plot(df_hist['High'])  # highest price
plt.show()
