# import backtrader as bt
import pandas as pd
#class MA(bt.Strategy):
#    def __init__(self):
#        self.ma_100 = bt.indicators.MovingAverageSimple(self.data,period=20,
#         plotname="20 SMA")
nameOfFile = "prices_round_1_day_-1.csv"
dataFrame = pd.read_csv("TradingFiles\\"+nameOfFile, sep=";")
print(dataFrame.head(20))

print(dataFrame.product)


        