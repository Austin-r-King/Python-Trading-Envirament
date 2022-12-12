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
#    print('Ticker: KO')
    print('Market Price:', market_price)
#    print('Previous Close Price:', previous_close_price)

print(datetime.datetime.today())
def getting_data_today():
    today = date.today()
    ticker = yf.Ticker('KO').info
    print (market_price = ticker['regularMarketPrice'])
    while (datetime.time.today < today+"10:23:28"):

#KO_Info()
