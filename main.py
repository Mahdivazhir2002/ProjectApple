import yfinance as yf
import pandas as pd
import datetime
import csv 
symbol = "AAPL"
start_date = datetime.datetime.now() - datetime.timedelta(days=365)
end_date = datetime.datetime.now()

data = yf.download(symbol, start=start_date, end=end_date, interval="1d")

# افزودن ستون جدید به DataFrame
datafream=pd.DataFrame(data)



df1 = pd.read_csv('all.csv')




#create new row
df1['Candle']='Down'
df1.loc[df1['Open']<df1['Close'],'Candle']='Up'   
#finish work and create  new csv file write this 
file = open('finall.csv','w')
df1.to_csv('finall.csv')
