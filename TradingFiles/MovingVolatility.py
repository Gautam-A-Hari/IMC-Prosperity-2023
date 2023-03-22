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
dataFrame = pd.read_csv("Round_1_data//"+nameOfFile, sep=";")
print(dataFrame.head(20))

print(dataFrame.product)