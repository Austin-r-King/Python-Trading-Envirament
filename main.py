import yfinance as yf
import datetime
from datetime import date
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def MakingLists():
    with open("KO prices and dates.txt", "r") as koPrices:
        lines = koPrices.readlines()

        Day = []
        Price = []

        ko_file = open("KO prices and dates.txt", "r")
        data = ko_file.read()
        data_into_list = data.split("|")
        print(data_into_list)
        amount = len(data_into_list)

        while len(data_into_list)>=0:
            del data_into_list[1]

            print(Day)
            print(Price)
        print(data_into_list)
def CreatingGraph():
    Day = []
    Price = []

    data_plot = pd.DataFrame({"Day":Day, "Price":Price})
    sns.lineplot(x = "Day", y = "Price", data=data_plot)
    plt.show()



def KO_Info():
    ticker = yf.Ticker('KO').info
    market_price = ticker['regularMarketPrice']

    print('Ticker: KO')
    print('Market Price:', market_price)


def getting_data_today():
    OpenTime = datetime.datetime.today().replace(hour=9, minute=3, second=0, microsecond=0)
    today = date.today()
    ticker = yf.Ticker('KO').info

    if datetime.datetime.today() >= OpenTime:

        for amount_saved in range (0,78):

            market_price = ticker['regularMarketPrice']

            f = open("KO prices and dates.txt", "a")
            time = datetime.datetime.today().replace(second=0, microsecond=0)

            f.write(str(market_price)+"="+str(time)+"|")
            f.close()



#KO_Info()
getting_data_today()
MakingLists()
#lol()
