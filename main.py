import yfinance as yf
import numpy as np
from matplotlib import animation as animation, pyplot as plt, cm
import datetime
from datetime import date
import seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

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
    open = datetime.datetime.today().replace(hour=9, minute=3, second=0, microsecond=0)
    ticker = yf.Ticker('KO').info
    market_price = ticker['regularMarketPrice']
    if datetime.datetime.today() >= open:
        for amount_saved in range (0,78):
            print(market_price)
            print(datetime.datetime.today().replace( microsecond=0 ) )
            time.sleep(300)
getting_data_today()