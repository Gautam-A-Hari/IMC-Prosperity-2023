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
        File_object = open(self.nameOfFile)
        for line in File_object:
                dataArr.append(line)
        File_object.close()
        return dataArr

if __name__ == "__main__":
    data = DataCollector(50, "Round_1_data\prices_round_1_day_-2.csv")
    
    print(data.readData())

        