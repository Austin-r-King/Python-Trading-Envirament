import yfinance as yf
import datetime
from datetime import date

def KO_Info():
    ticker = yf.Ticker('KO').inmfo
    market_price = ticker['regularMarketPrice']
    print('Ticker: KO')
    print('Market Price:', market_price)



def getting_data_today():
    today = date.today()
    OpenTime = datetime.datetime.today().replace(hour=9, minute=3, second=0, microsecond=0)
    ticker = yf.Ticker('KO').info
    if datetime.datetime.today() >= OpenTime:
        for amount_saved in range (0,78):
            market_price = ticker['regularMarketPrice']
            f = open("KO prices and dates.txt", "a")
            time = datetime.datetime.today().replace(second=0, microsecond=0)
            f.write(str(market_price)+":"+str(time)+" - ")
            f.close()
getting_data_today()
