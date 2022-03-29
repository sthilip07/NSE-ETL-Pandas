from time import time, sleep
from datetime import datetime
import nsepy
import datetime
import pandas as pd

    #sleep(60 - time() % 60)

while True:
    sleep(60 - time() % 60)
    def get_data(symbol):
        live_data = {}

        live_data = {"open": float(nsepy.get_quote(symbol)["data"][0]["open"].replace(',', '')),
                     "close": float(nsepy.get_quote(symbol)["data"][0]["closePrice"].replace(',', '')),
                     "lastPrice": float(nsepy.get_quote(symbol)["data"][0]["lastPrice"].replace(',', '')),
                     "dayLow": float(nsepy.get_quote(symbol)["data"][0]["dayLow"].replace(',', '')),
                     "dayHigh": float(nsepy.get_quote(symbol)["data"][0]["dayHigh"].replace(',', '')),
                     "basePrice": float(nsepy.get_quote(symbol)["data"][0]["basePrice"].replace(',', '')),
                     "Time": str(datetime.datetime.now()).split('.')[0],
                     "Company": str(nsepy.get_quote(symbol)["data"][0]["symbol"]),
                     "previousClose": float(nsepy.get_quote(symbol)["data"][0]["previousClose"].replace(',', ''))
                     }
        return (live_data)


    symbol = "TCS"
    data = []
    data = [get_data(symbol)]

    df = pd.DataFrame(data)

    df['Date'] = df['Time'].str[0:10]

    today_date = datetime.date.today()

    df.to_csv('nse_live_data_pd.csv', mode='a', index=False, header=False)

    columns = ['open','close','lastPrice','dayLow','dayHigh','basePrice','Time','Company','previousClose','Date']
    df = pd.read_csv('nse_live_data_pd.csv',names=columns , header=None)

    df['Time1'] = df['Time'].str[11:16]
    today_date = datetime.datetime.now()
    today_date = today_date.strftime("%Y-%m-%d")

    # daily_df contains only today's data
    daily_df = df[df['Date'] == today_date]
    daily_df.to_csv('nse_live_graph.csv', mode='w', index=False, header=True)
    print("written to csv")


