class DataCollector:
    import pandas as pd
    dataFrameSize = 0
    nameOfFile = ""
    dataArr = []
    
    
    def __init__(self, frameSize, file) -> None:
        self.dataFrameSize = frameSize
        self.nameOfFile = file
        
        
    def readData(self):
        File_object = open("Round_1_data\\"+self.nameOfFile, r)
        while():
            File_object.readline([n])
        File_object.close()
        