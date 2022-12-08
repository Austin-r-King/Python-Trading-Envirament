import yfinance as yf
import numpy as np
from matplotlib import animation as animation, pyplot as plt, cm
import datetime
from datetime import date



#WEFGQEUIBVQEUB3B#

def KO_Info():
    ticker = yf.Ticker('KO').info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
    print('Ticker: KO')
    print('Market Price:', market_price)
    print('Previous Close Price:', previous_close_price)


def getting_data_week():
    today = date.today()
    PastWeek = today - date.today(days=7)
    start_date = PastWeek
    end_date = today
    ko= yf.Ticker("KO")
    ko_historical = ko.history(start= PastWeek, end="today", interval="1m")
    print(ko_historical)
#getting_data_week()

today = datetime.datetime.today()
Time = str(today - datetime.timedelta(days=7))
i=0
PastWeek = ""
while (i <11):
    PastWeek = PastWeek + Time[i]
    i += 1


print(PastWeek)



