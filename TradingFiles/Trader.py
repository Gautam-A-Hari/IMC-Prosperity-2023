from typing import Dict, List

from datamodel import OrderDepth, TradingState, Order
# from DataCollector import *
import pandas as pd
import numpy as np
import math

class Trader:
    # def takePriceData(state: T	radingState, product): # fix the inputs, product is incorrect
    #     df = pd.read_csv("TradingFiles\\prices_round_2_day_-1.csv", sep=";")
    #     df = df.fillna(0)
    #     if (product == "COCONUTS"):
	# 		      df_output = df.loc[df['product']=="COCONUTS"]
    #     # elif (product =="PINA_COLADAS"):
    #     #       df_output = df.loc[df['product']=="PINA_COLADAS"]
    #     df_output = df_output[["timestamp", 
    #     "product","bid_price_1", "bid_volume_1",
    #                             "ask_price_1", "ask_volume_1",
    #                             "mid_price", "profit_and_loss"]]
    #     bid_list = []
    #     for bid in df_output["bid_price_1"]:
    #         bid_list.append(bid)

    #     bid_vol_list = []
    #     for bid_vol in df_output["bid_volume_1"]:
    #         bid_vol_list.append(bid_vol)

    #     ask_list = []
    #     for ask in df_output["ask_price_1"]:
    #         ask_list.append(ask)

    #     ask_vol_list = []
    #     for ask_vol in df_output["ask_volume_1"]:
    #         ask_vol_list.append(ask_vol)

    #     df_output["pct_change"] = df["mid_price"].pct_change()
    #     output = df_output.head(50)["mid_price"]
    #     print(output)
    #     return output
    
	# logs the score and spread value over time.
    def zScoreAndSpread(self, state: TradingState) -> Dict[int]:
        arrCoconutsPrices = np.array()
        arrPinaColadasPrices = np.array()
        for product in state.order_depths.keys():
            # Check if the current product is the 'COCONUTS' product, only then run the order logic
            if product == 'COCONUTS':
                  # fix spread calculations to retrieve prices from other product
                  OrderDepth = state.order_depths[product]
                  best_ask = min(state.order_depth.sell_orders.keys())
                  best_bid = max(state.order_depth.buy_orders.keys())
                  coconutsPrice = (best_bid + best_ask) / 2
                  arrCoconutsPrices.append(coconutsPrice)
                  spread = math.log(coconutsPrice) - (0.8 * math.log(self.arrPinaColadasPrices(-1)))
                #   meanVal = self.takePriceData('COCONUTS').mean()
                #   stdDev = self.takePriceData('COCONUTS').std()
                #   z = (product - meanVal) / stdDev
                  # spread = log(COCONUTS prices) - nlog(PINA_COLADAS prices)
                  return spread, arrCoconutsPrices
            elif product == 'PINA_COLADAS':
                  # fix spread calculations to retrieve prices from other product
                  best_ask = min(state.order_depth.sell_orders.keys())
                  best_bid = max(state.order_depth.buy_orders.keys())
                  # spread = best_ask - best_bid
                  pinaColadasPrice = (best_bid + best_ask) / 2
                  arrPinaColadasPrices.append(pinaColadasPrice)
                  spread = math.log(pinaColadasPrice) - (0.8 * math.log(self.arrCoconutsPrices(-1)))
                #   meanVal = self.takePriceData('PINA_COLADAS').mean()
                #   stdDev = self.takePriceData('PINA_COLADAS').std()
                #   z = (product - meanVal) / stdDev 
                  # spread = log(PINA_COLADAS price) - log(COCONUTS price)
                  return spread, arrPinaColadasPrices
    
def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        # Initialize the method output dict as an empty dict
        result = {}

        # Iterate over all the keys (the available products) contained in the order depths
        for product in state.order_depths.keys():

            # Check if the current product is the 'COCONUTS' product, only then run the order logic
            if product == 'COCONUTS':
                # Retrieve the Order Depth containing all the market BUY and SELL orders for COCONUT
                order_depth: OrderDepth = state.order_depths[product]

                # Initialize the list of Orders to be sent as an empty list
                orders: list[Order] = []

                # Define a fair value for the PEARLS.
                # Note that this value of 1 is just a dummy value, you should likely change it!

                # If statement checks if there are any SELL orders in the PEARLS market
                if len(order_depth.sell_orders) > 0:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_bid = max(order_depth.buy_orders.keys())
                    acceptable_price = (best_ask + best_bid) / 2 
                    # Sort all the available sell orders by their price,
                    # and select only the sell order with the lowest price
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]

                    # Check if the lowest ask (sell order) is lower than the above defined fair value
                    if best_ask < acceptable_price:

                        # In case the lowest ask is lower than our fair value,
                        # This presents an opportunity for us to buy cheaply
                        # The code below therefore sends a BUY order at the price level of the ask,
                        # with the same quantity
                        # We expect this order to trade with the sell order
                        print("BUY", str(-best_ask_volume) + "x", best_ask)
                        orders.append(Order(product, best_ask, -best_ask_volume))

                # The below code block is similar to the one above,
                # the difference is that it finds the highest bid (buy order)
                # If the price of the order is higher than the fair value
                # This is an opportunity to sell at a premium
                if len(order_depth.buy_orders) != 0:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    if best_bid > acceptable_price:
                        print("SELL", str(best_bid_volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, -best_bid_volume))

                # Add all the above orders to the result dict
                result[product] = orders

                # Return the dict of orders
                # These possibly contain buy or sell orders for PEARLS
                # Depending on the logic above
            elif product == 'PINA_COLADAS':
                # Retrieve the Order Depth containing all the market BUY and SELL orders for COCONUT
                order_depth: OrderDepth = state.order_depths[product]

                # Initialize the list of Orders to be sent as an empty list
                orders: list[Order] = []

                # Define a fair value for the PEARLS.
                # Note that this value of 1 is just a dummy value, you should likely change it!

                # If statement checks if there are any SELL orders in the PEARLS market
                if len(order_depth.sell_orders) > 0:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_bid = max(order_depth.buy_orders.keys())
                    acceptable_price = (best_ask + best_bid) / 2
                    # Sort all the available sell orders by their price,
                    # and select only the sell order with the lowest price
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]

                    # Check if the lowest ask (sell order) is lower than the above defined fair value
                    if best_ask < acceptable_price:

                        # In case the lowest ask is lower than our fair value,
                        # This presents an opportunity for us to buy cheaply
                        # The code below therefore sends a BUY order at the price level of the ask,
                        # with the same quantity
                        # We expect this order to trade with the sell order
                        print("BUY", str(-best_ask_volume) + "x", best_ask)
                        orders.append(Order(product, best_ask, -best_ask_volume))

                # The below code block is similar to the one above,
                # the difference is that it finds the highest bid (buy order)
                # If the price of the order is higher than the fair value
                # This is an opportunity to sell at a premium
                if len(order_depth.buy_orders) != 0:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    if best_bid > acceptable_price:
                        print("SELL", str(best_bid_volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, -best_bid_volume))

                # Add all the above orders to the result dict
                result[product] = orders

                # Return the dict of orders
                # These possibly contain buy or sell orders for PEARLS
                # Depending on the logic above
        return result