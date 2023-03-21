import pandas as pd

class DataCollector:
    dataFrameSize = 0
    nameOfFile = ""

    def __init__(self, frameSize, file) -> None:
        self.dataFrameSize = frameSize
        self.nameOfFile = file
        
        
    def readData(self):
        dataArr = []
        File_object = open("Round_1_data\\"+self.nameOfFile, r)
        for line in File_object:
                dataArr.append(line)
        File_object.close()
        