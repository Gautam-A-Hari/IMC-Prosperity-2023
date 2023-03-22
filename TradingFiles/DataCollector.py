import pandas as pd

class DataCollector():
    dataFrameSize = 0
    nameOfFile = ""
    def __init__(self, frameSize, file) -> None:
        self.dataFrameSize = frameSize
        self.nameOfFile = file
            
    def log(self, txt, dateTime=None)->None:
        print(f"{dateTime} {txt}")

    def readData(self):
        dataArr = []
        return pd.read_csv(self.nameOfFile, sep=";")
        # for line in df:
        #         dataArr.append(line)
        # return dataArr
    
    def filterDataByProduct(self, productName):
        
        df = self.readData()
        ProductNameFiltered = df[(df['Shipping Type'] == productName)]

    def takePriceData(productName):
        df = pd.read_csv("TradingFiles\prices_round_2_day_-1.csv", sep=";")

        pd.set_option("display.max_columns", None)
        df = df.fillna(0)
        df_bananas = df.loc[df['product']=="BANANAS"]
        df_pearls = df.loc[df['product']=="PEARLS"]
        df_coconuts = df.loc[df['product']=="COCONUTS"]
        df_pina_coladas = df.loc[df['product']=="PINA_COLADAS"]

        df_output = df.loc[df['product']==productName]
        df_output = df_output[["timestamp", 
        "product","bid_price_1", "bid_volume_1",
                                "ask_price_1", "ask_volume_1",
                                "mid_price", "profit_and_loss"]]
        bid_list = []
        for bid in df_output["bid_price_1"]:
            bid_list.append(bid)

        bid_vol_list = []
        for bid_vol in df_output["bid_volume_1"]:
            bid_vol_list.append(bid_vol)

        ask_list = []
        for ask in df_output["ask_price_1"]:
            ask_list.append(ask)

        ask_vol_list = []
        for ask_vol in df_output["ask_volume_1"]:
            ask_vol_list.append(ask_vol)

        # print(bid_list[0])
        df_output["pct_change"] = df["mid_price"].pct_change()
        # print(df_bananas.head(50))
        output = df_output.head(50)["mid_price"]
        print(output)
        return output
        
    #def dataInFrameSize(self):
# https://jmerle.github.io/imc-prosperity-visualizer/        
    
        