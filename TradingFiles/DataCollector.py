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
        
        
    def log(self, txt, dt=None)->None:
        print(f"{dt} {txt}")

    def readData(self):
        dataArr = []
        File_object = open(self.nameOfFile)
        for line in File_object:
                dataArr.append(line)
        File_object.close()
        return dataArr

if __name__ == "__main__":
    data = DataCollector(50, "/Users/tringuyen/Documents/GitHub/IMC-Prosperity-2023/Round_1_data/prices_round_1_day_0.csv")
    
    print(data.readData())

        