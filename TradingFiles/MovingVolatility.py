# testing moving volatility

from typing import Dict, List
# from TradingFiles import OrderDepth, TradingState, Order

import numpy as np
import pandas as pd

"""def getMovingAverage(OrderDepth): 
	df = pd.read_csv("IMC-Prosperity-2023\Round_1_data\prices_round_1_day_-1.csv")
	print(df.head)"""

#pd.set_option("display.max_row")

nameOfFile = "prices_round_1_day_-1.csv"
dataFrame = pd.read_csv("TradingFiles//"+nameOfFile, sep=";")
print(dataFrame.head(20))
volatilityArr = []

class getMovingVolatility():
    def getStdDev(self, priceWindow):
        stdDev = np.std(priceWindow)
        # volatility = self.getStdDev * np.sqrt(50)
        return stdDev # , volatility
    def getVolatility(self) -> None:
        volatility = self.getStdDev * np.sqrt(50)
        return volatility
    def volatilityDataCollector(self):
           self.volatilityArr = self.volatilityArr.append(self.getVolatility())
           return volatilityArr
    def makeDecision(self, priceWindow):
        # returns true if a order needs to be bought, and false if no order needed
		# if self.volatility > self.volatilityArray()
		   return priceWindow