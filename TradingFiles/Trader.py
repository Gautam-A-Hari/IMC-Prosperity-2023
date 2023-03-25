from typing import Dict, List

from datamodel import OrderDepth, TradingState, Order
# from DataCollector import *
import pandas as pd
import numpy as np
import math

class Trader:
    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        # Initialize the method output dict as an empty dict
        result = {}

        # Iterate over all the keys (the available products) contained in the order depths
        for product in state.order_depths.keys():
            total_coconut = 0
            total_pina = 0

            if total_coconut + total_pina <= -20000:
                print("Hit the panic button ! out of business")
                break
            # Check if the current product is the 'COCONUTS' product, only then run the order logic
            if product == "COCONUTS":
                # Retrieve the Order Depth containing all the market BUY and SELL orders for COCONUT
                order_depth: OrderDepth = state.order_depths[product]

                # Initialize the list of Orders to be sent as an empty list
                orders: list[Order] = []
                """
                if (state.position["PRODUCT1"]) > 600:
                
                    best_bid_sell = max(order_depth.buy_orders.keys())
                    best_bid_sell_volume = order_depth.buy_orders[best_bid_sell]
                    orders.append(Order(product, best_bid_sell, -best_bid_sell_volume))
                    result[product] = orders
                # Define a fair value for the PEARLS.
                # Note that this value of 1 is just a dummy value, you should likely change it!
                """
                # If statement checks if there are any SELL orders in the PEARLS market
                if len(order_depth.sell_orders) > 0:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_bid = max(order_depth.buy_orders.keys())
                    acceptable_price = best_ask * 1.01 
                    # Sort all the available sell orders by their price,
                    # and select only the sell order with the lowest price
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
                        total_coconut -= (best_ask * best_ask_volume)
                # The below code block is similar to the one above,
                # the difference is that it finds the highest bid (buy order)
                # If the price of the order is higher than the fair value
                # This is an opportunity to sell at a premium
                if len(order_depth.buy_orders) != 0:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    acceptable_price = 1
                    if best_bid > acceptable_price:
                        print("SELL", str(best_bid_volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, -best_bid_volume))
                        total_coconut += (best_bid * best_bid_volume)
                # Add all the above orders to the result dict
                result[product] = orders

                # Return the dict of orders
                # These possibly contain buy or sell orders for PEARLS
                # Depending on the logic above
            elif product == 'PINA_COLADAS':
                # Retrieve the Order Depth containing all the market BUY and SELL orders for COCONUT
                order_depth_pina: OrderDepth = state.order_depths[product]

                # Initialize the list of Orders to be sent as an empty list
                orders_pina: list[Order] = []
                """
                if state.position["PRODUCT2"] > 300:
                
                    best_bid_sell = max(order_depth_pina.buy_orders.keys())
                    best_bid_sell_volume = order_depth_pina.buy_orders[best_bid_sell]
                    orders_pina.append(Order(product, best_bid_sell, -best_bid_sell_volume))
                    result[product] = orders_pina
                """
                # Define a fair value for the PEARLS.
                # Note that this value of 1 is just a dummy value, you should likely change it!

                # If statement checks if there are any SELL orders in the PEARLS(Pina) market
                if len(order_depth_pina.sell_orders) > 0:
                    best_ask_pina = min(order_depth_pina.sell_orders.keys())
                    best_bid_pina = max(order_depth_pina.buy_orders.keys())
                    acceptable_price_pina = 1 #(best_ask + best_bid) * 0.5
                    # Sort all the available sell orders by their price,
                    # and select only the sell order with the lowest price
                # best_ask_pina = min(order_depth_pina.sell_orders.keys())
                    best_ask_volume_pina = order_depth_pina.sell_orders[best_ask_pina]
                    # Check if the lowest ask (sell order) is lower than the above defined fair value
                    if best_ask_pina < acceptable_price_pina:
                        # In case the lowest ask is lower than our fair value,
                        # This presents an opportunity for us to buy cheaply
                        # The code below therefore sends a BUY order at the price level of the ask,
                        # with the same quantity
                        # We expect this order to trade with the sell order
                        print("BUY", str(-best_ask_volume_pina) + "x", best_ask_pina)
                        orders_pina.append(Order(product, best_ask_pina, -best_ask_volume_pina))
                        total_pina -= (best_ask_pina * best_ask_volume_pina)
                # The below code block is similar to the one above,
                # the difference is that it finds the highest bid (buy order)
                # If the price of the order is higher than the fair value
                # This is an opportunity to sell at a premium
                elif len(order_depth_pina.buy_orders)  != 0:
                    best_bid_pina = max(order_depth_pina.buy_orders.keys())
                    best_bid_volume_pina = order_depth_pina.buy_orders[best_bid_pina]
                    acceptable_price_pina = 1
                    if best_bid_pina > acceptable_price_pina:
                        print("SELL", str(best_bid_volume_pina) + "x", best_bid_pina)
                        orders_pina.append(Order(product, best_bid_pina, -best_bid_volume_pina))
                        total_pina += (best_ask_pina * best_ask_volume_pina)
                # Add all the above orders to the result dict
                result[product] = orders_pina

                # Return the dict of orders
                # These possibly contain buy or sell orders for PEARLS
                # Depending on the logic above
        return result