import yfinance as yf
import numpy as np
from matplotlib import animation as animation, pyplot as plt, cm
import datetime
from datetime import date
import seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def KO_Info():
    ticker = yf.Ticker('KO').info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
    print('Ticker: KO')
    print('Market Price:', market_price)
    print('Previous Close Price:', previous_close_price)


def getting_data_week():
    today = datetime.datetime.today()
    Time = str(today - datetime.timedelta(days=7))
    i = 0
    pastWeek = ""
    while (i < 11):
        pastWeek = pastWeek + Time[i]
        i += 1
    today = date.today()
    start_date = pastWeek
    end_date = today
    ko= yf.Ticker("KO")
    ko_historical = ko.history(start= pastWeek, end=today, interval="1m")
    print(ko_historical)
#getting_data_week()

aapl= yf.Ticker("aapl")
print(aapl)
aapl_historical = aapl.history(start="2020-06-02", end="2020-06-07", interval="1m")
aapl_historical




