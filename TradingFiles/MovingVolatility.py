# testing moving volatility

from typing import Dict, List
from DataCollector import *

import numpy as np
import pandas as pd

# volatilityArr = []
DataCollector.takePriceData("BANANA")

# class getMovingVolatility():
#     def getStdDev(self, priceWindow):
#         stdDev = np.std(priceWindow)
#         print(stdDev)
#         # volatility = self.getStdDev * np.sqrt(50)
#         return stdDev # , volatility
#     def getVolatility(self):
#         volatility = self.getStdDev * np.sqrt(50)
#         return volatility
#     def volatilityDataCollector(self):
#            self.volatilityArr = self.volatilityArr.append(self.getVolatility())
#            return volatilityArr
#     def makeDecision(self, priceWindow, takePriceData):
#         # returns true if a order needs to be bought, and false if no order needed
# 		   if self.volatility not in range (self.volatilityArray(-1) - 0.2, self.volatilityArr(-2) + 0.2):
#                     return True