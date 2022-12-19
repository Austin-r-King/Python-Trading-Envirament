import yfinance as yf
import datetime
from datetime import date
import time

def KO_Info():
    ticker = yf.Ticker('KO').info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
#    print('Ticker: KO')
    print('Market Price:', market_price)
#    print('Previous Close Price:', previous_close_price)



def getting_data_today():
    f = ('KO prices and dates.txt', 'w')
    today = date.today()
    open = datetime.datetime.today().replace(hour=9, minute=3, second=0, microsecond=0)
    ticker = yf.Ticker('KO').info
    market_price = ticker['regularMarketPrice']
    if datetime.datetime.today() >= open:
        for amount_saved in range (0,78):
            f = open("KO prices and dates.txt", "a")
            time = "lol"
            f.write(time + market_price)
            f.close()
getting_data_today()