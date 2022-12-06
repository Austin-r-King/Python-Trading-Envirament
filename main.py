import yfinance as yf
import datetime


today = datetime.datetime.now()
d = datetime.timedelta(days = 50)# amount of days subtracted from today
a = today - d



#WEFGQEUIBVQEUB3B#

def KO_Info():
    ticker = yf.Ticker('KO').info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
    print('Ticker: KO')
    print('Market Price:', market_price)
    print('Previous Close Price:', previous_close_price)



