import pandas as pd
import backtrader as bt
class DataCollector():
    dataFrameSize = 0
    nameOfFile = ""
    param_fast = 50
    param_slow = 100
    def __init__(self, frameSize, file) -> None:
        self.dataFrameSize = frameSize
        self.nameOfFile = file
            
    def log(self, txt, dateTime=None)->None:
        print(f"{dateTime} {txt}")

    def readData(self):
        dataArr = []
        df = pd.read_csv(self.nameOfFile, sep=";")
        df.loc(["mid_price"])
        for line in df:
                dataArr.append(line)
        # df.close()
        return dataArr
    
    
    def filterDataByProduct(self,productName):
        
        
    
    
    #def dataInFrameSize(self):
# https://jmerle.github.io/imc-prosperity-visualizer/        
        

if __name__ == "__main__":
    data = DataCollector(50, r"C:\Users\gauta\OneDrive - Indiana University\2022-2023\Spring term\Intro to software systems\Homework\IMC-Prosperity-2023\Round_1_data\prices_round_1_day_-2.csv")
    print(data.readData())
    
        