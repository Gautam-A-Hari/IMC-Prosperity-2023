# import backtrader as bt
import pandas as pd
#class MA(bt.Strategy):
#    def __init__(self):
#        self.ma_100 = bt.indicators.MovingAverageSimple(self.data,period=20,
#         plotname="20 SMA")
nameOfFile = "prices_round_1_day_-1.csv"
dataFrame = pd.read_csv("TradingFiles\\"+nameOfFile, sep=";")
print(dataFrame.head(20))

<<<<<<< HEAD
df = pd.read_csv("TradingFiles/prices_round_1_day_-1.csv", sep=";")
print(df.head(20))

#print(df.loc[df.product == "BANANAS"])
pd.set_option("display.max_columns", None)

df_bananas = df.loc[df['product']=="BANANAS"]
df_pearls = df.loc[df['product']=="PEARLS"]

=======
print(dataFrame.product)
>>>>>>> e3d0003d225bd3254ad6d2ea672508fc8a42a499


        