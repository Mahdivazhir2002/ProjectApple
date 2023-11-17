#import needs library for project
import yfinance as yf
import pandas as pd
import datetime
import csv 
#get data about Apple
symbol = "AAPL"
start_date = datetime.datetime.now() - datetime.timedelta(days=365)
end_date = datetime.datetime.now()

data = yf.download(symbol, start=start_date, end=end_date, interval="1d")
datafream=pd.DataFrame(data)

#save recive datafream in csv file 
CreateFile = open('all.csv','w')
datafream.to_csv('all.csv')
df1 = pd.read_csv('all.csv')

#create new row name=candle and value default is down
df1['Candle']='Down'
df1.loc[df1['Open']<df1['Close'],'Candle']='Up'   
#finish work and create  new csv file write this 
file = open('finall.csv','w')
df1.to_csv('finall.csv')
