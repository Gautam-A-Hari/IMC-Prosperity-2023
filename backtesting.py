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


# def takePriceData(state: T	radingState, product): # fix the inputs, product is incorrect
    #     df = pd.read_csv("TradingFiles\\prices_round_2_day_-1.csv", sep=";")
    #     df = df.fillna(0)
    #     if (product == "COCONUTS"):
	# 		      df_output = df.loc[df['product']=="COCONUTS"]
    #     # elif (product =="PINA_COLADAS"):
    #     #       df_output = df.loc[df['product']=="PINA_COLADAS"]
    #     df_output = df_output[["timestamp", 
    #     "product","bid_price_1", "bid_volume_1",
    #                             "ask_price_1", "ask_volume_1",
    #                             "mid_price", "profit_and_loss"]]
    #     bid_list = []
    #     for bid in df_output["bid_price_1"]:
    #         bid_list.append(bid)

    #     bid_vol_list = []
    #     for bid_vol in df_output["bid_volume_1"]:
    #         bid_vol_list.append(bid_vol)

    #     ask_list = []
    #     for ask in df_output["ask_price_1"]:
    #         ask_list.append(ask)

    #     ask_vol_list = []
    #     for ask_vol in df_output["ask_volume_1"]:
    #         ask_vol_list.append(ask_vol)

    #     df_output["pct_change"] = df["mid_price"].pct_change()
    #     output = df_output.head(50)["mid_price"]
    #     print(output)
    #     return output
    
	# logs the score and spread value over time.
    # def zScoreAndSpread(self, state: TradingState) -> Dict[int]:
    #     arrCoconutsPrices = np.array()
    #     arrPinaColadasPrices = np.array()
    #     for product in state.order_depths.keys():
    #         # Check if the current product is the 'COCONUTS' product, only then run the order logic
    #         if product == 'COCONUTS':
    #               # fix spread calculations to retrieve prices from other product
    #               OrderDepth = state.order_depths[product]
    #               best_ask = min(state.order_depth.sell_orders.keys())
    #               best_bid = max(state.order_depth.buy_orders.keys())
    #               coconutsPrice = (best_bid + best_ask) / 2
    #               arrCoconutsPrices.append(coconutsPrice)
    #               spread = math.log(coconutsPrice) - (0.8 * math.log(self.arrPinaColadasPrices(-1)))
    #             #   meanVal = self.takePriceData('COCONUTS').mean()
    #             #   stdDev = self.takePriceData('COCONUTS').std()
    #             #   z = (product - meanVal) / stdDev
    #               # spread = log(COCONUTS prices) - nlog(PINA_COLADAS prices)
    #               return spread, arrCoconutsPrices
    #         elif product == 'PINA_COLADAS':
    #               # fix spread calculations to retrieve prices from other product
    #               best_ask = min(state.order_depth.sell_orders.keys())
    #               best_bid = max(state.order_depth.buy_orders.keys())
    #               # spread = best_ask - best_bid
    #               pinaColadasPrice = (best_bid + best_ask) / 2
    #               arrPinaColadasPrices.append(pinaColadasPrice)
    #               spread = math.log(pinaColadasPrice) - (0.8 * math.log(self.arrCoconutsPrices(-1)))
    #             #   meanVal = self.takePriceData('PINA_COLADAS').mean()
    #             #   stdDev = self.takePriceData('PINA_COLADAS').std()
    #             #   z = (product - meanVal) / stdDev 
    #               # spread = log(PINA_COLADAS price) - log(COCONUTS price)
    #               return spread, arrPinaColadasPrices
        