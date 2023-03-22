import backtrader as bt

class MA(bt.Strategy):
    def __init__(self):
        self.ma_100 = bt.indicators.MovingAverageSimple(self.data,period=20,
         plotname="20 SMA")


        