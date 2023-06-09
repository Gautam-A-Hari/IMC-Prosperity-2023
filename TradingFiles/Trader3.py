import json
from datamodel import Order, ProsperityEncoder, Symbol, TradingState
from typing import Any

class Logger:
    def __init__(self) -> None:
        self.logs = ""

    def print(self, *objects: Any, sep: str = " ", end: str = "\n") -> None:
        self.logs += sep.join(map(str, objects)) + end

    def flush(self, state: TradingState, orders: dict[Symbol, list[Order]]) -> None:
        print(json.dumps({
            "state": state,
            "orders": orders,
            "logs": self.logs,
        }, cls=ProsperityEncoder, separators=(",", ":"), sort_keys=True))

        self.logs = ""

logger = Logger()

class Trader:
    # Initialize past data collector
    past_data = {'BANANAS': [],
                 'COCONUTS': [],
                 'PINA_COLADAS': [],
                 'PEARLS': [],
                 'BERRIES': [],
                 'DIVING_GEAR': [],
                 'UKULELE': [],
                 'DIP': [],
                 'PICNIC_BASKET': [],
                 'BAGUETTE': []}
    def run(self, state: TradingState) -> dict[str, list[Order]]:
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        
        # Initialize the method output dict as an empty dict
        orders1 = {}
        # Iterate over all the keys (the available products) contained in the order depths
        for product in state.order_depths.keys():
            # Retrieve the Order Depth containing all the market BUY and SELL orders for COCONUT
            order_depth = state.order_depths[product]
            # Initialize the list of Orders to be sent as an empty list
            orders: list[Order] = []
            # If statement checks if there are any SELL orders in the PEARLS market
            if len(order_depth.sell_orders) > 0:
                best_ask = min(order_depth.sell_orders.keys())
                
                best_ask_volume = order_depth.sell_orders[best_ask]
                # Check if the lowest ask (sell order) is lower than the above defined fair value
                if (len(self.past_data[product])) == 10:
                    self.past_data[product].pop(0)
                    self.past_data[product].append(best_ask)
                    change = ((self.past_data[product][0] / self.past_data[product][9]) * 100)
                    if change > 0.9:
                      
                            logger.print("BUY", str(-best_ask_volume) + "x", best_ask)
                            orders.append(Order(product, best_ask, -best_ask_volume))
                    else:
                        logger.print("SELL", str(30) + "x", best_ask)
                        orders.append(Order(product, best_ask, 30))  
                else:
                    self.past_data[product].append(best_ask)
                    logger.print("BUY", str(1) + "x", best_ask)
                    orders.append(Order(product, best_ask, 1))
            # The below code block is similar to the one above,
            # the difference is that it finds the highest bid (buy order)
            # If the price of the order is higher than the fair value
            # This is an opportunity to sell at a premium
            if len(order_depth.buy_orders) > 0:
                best_bid = max(order_depth.buy_orders.keys())
                best_bid_volume = order_depth.buy_orders[best_bid]
                if (len(self.past_data[product])) == 50:
                    self.past_data[product].pop(0)
                    self.past_data[product].append(best_bid)
                    change = (self.past_data[product][1] / self.past_data[product][49])
                    if change > 0.9:
                        logger.print("SELL", str(best_bid_volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, -best_bid_volume))
                    else:
                        logger.print("BUY", str(30) + "x", best_bid)
                        orders.append(Order(product, best_bid, 30)) 
                else:
                    self.past_data[product].append(best_bid)
                    logger.print("SELL", str(1) + "x", best_bid)
                    orders.append(Order(product, best_bid, 1))
            # Add all the above orders to the result dict
            orders1[product] = orders

            # Return the dict of orders
            # These possibly contain buy or sell orders for PEARLS
            # Depending on the logic above
            # Print last/most recent acc_price
        logger.flush(state, orders)
        return orders1