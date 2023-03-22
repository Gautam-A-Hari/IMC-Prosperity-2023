import pandas as pd
import backtrader as bt
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
    
    
    def filterDataByProduct(self,productName):
        
        df = self.readData()
        ProductNameFiltered = df[(df['Shipping Type'] == productName)]
        
        
    
    
    #def dataInFrameSize(self):
# https://jmerle.github.io/imc-prosperity-visualizer/        
        

if __name__ == "__main__":
    data = DataCollector(50, r"C:\Users\gauta\OneDrive - Indiana University\2022-2023\Spring term\Intro to software systems\Homework\IMC-Prosperity-2023\Round_1_data\prices_round_1_day_-2.csv")
    print(data.readData())
    
        