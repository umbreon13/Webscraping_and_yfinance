# Comparing the stocks value of different companies

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# plt.style.use('seaborn')                       

import yfinance as yf

#list woth different codes
securities = ['voo', 'msft', 'aapl', 'tsla', 'nvda', 'jnj', 'axp', 'dis']

df = pd.DataFrame()  # declare empty df where the data will be stored dfor each company

today = datetime.now().date().strftime("%Y-%m-%d")  # establish today's date

for security in securities:
    df[security] = yf.Ticker(security).history(start='2007-01-01', end=today).Close

# plot comparision
plt.figure()
plt.plot(df)  # Closing price
plt.ylabel('Price ($)')
plt.xlabel('Year')
plt.legend(securities)
plt.show()