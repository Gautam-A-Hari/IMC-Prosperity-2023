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

    def takePriceData():
        df = pd.read_csv("TradingFiles/prices_round_1_day_-1.csv", sep=";")

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


        # print(bid_list[0])
        df_bananas["pct_change"] = df["mid_price"].pct_change()
        # print(df_bananas.head(50))
        output = df_bananas.head(50)["mid_price"]
        print(output)
        return output
        
        
    
    
    #def dataInFrameSize(self):
# https://jmerle.github.io/imc-prosperity-visualizer/        
        

if __name__ == "__main__":
    data = DataCollector(50, r"C:\Users\gauta\OneDrive - Indiana University\2022-2023\Spring term\Intro to software systems\Homework\IMC-Prosperity-2023\Round_1_data\prices_round_1_day_-2.csv")
    print(data.readData())
    
        