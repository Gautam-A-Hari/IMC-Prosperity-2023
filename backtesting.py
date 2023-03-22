# import backtrader as bt
import pandas as pd
#class MA(bt.Strategy):
#    def __init__(self):
#        self.ma_100 = bt.indicators.MovingAverageSimple(self.data,period=20,
#         plotname="20 SMA")
nameOfFile = "prices_round_1_day_-1.csv"
#dataFrame = pd.read_csv("TradingFiles\\"+nameOfFile, sep=";")
#print(dataFrame.head(20))

df = pd.read_csv("TradingFiles/prices_round_1_day_-1.csv", sep=";")
#print(df.head(20))

#print(df.loc[df.product == "BANANAS"])
pd.set_option("display.max_columns", None)
df = df.fillna(0)


df_bananas = df.loc[df['product']=="BANANAS"]
df_pearls = df.loc[df['product']=="PEARLS"]

df_bananas = df_bananas[["timestamp", 
"product","bid_price_1", "bid_volume_1",
                        "ask_price_1", "ask_volume_1",
                         "mid_price", "profit_and_loss"]]
bid_list = []
for bid in df_bananas["bid_price_1"]:
    bid_list.append(bid)

bid_vol_list = []
for bid_vol in df_bananas["bid_volume_1"]:
    bid_vol_list.append(bid_vol)

ask_list = []
for ask in df_bananas["ask_price_1"]:
    ask_list.append(ask)

ask_vol_list = []
for ask_vol in df_bananas["ask_volume_1"]:
    ask_vol_list.append(ask_vol)


print(bid_list[0])
df_bananas["pct_change"] = df["mid_price"].pct_change()
print(df_bananas.head(50))

for 


        