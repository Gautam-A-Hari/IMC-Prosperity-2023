import json
from datamodel import Order, Symbol, TradingState, ProsperityEncoder
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
    def run(self, state: TradingState) -> dict[str, list[Order]]:
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        # Initialize the method output dict as an empty dict
        orders1 = {}
        balance = 0
        # Iterate over all the keys (the available products) contained in the order depths
        for product in state.order_depths.keys():
            logger.print(balance)
            # Retrieve the Order Depth containing all the market BUY and SELL orders for COCONUT
            if balance < -10000:
                break
            order_depth: OrderDepth = state.order_depths[product]
            # Initialize the list of Orders to be sent as an empty list
            orders: list[Order] = []
            # If statement checks if there are any SELL orders in the PEARLS market
            if len(order_depth.sell_orders) > 0:
                best_ask = min(order_depth.sell_orders.keys())
                best_bid = max(order_depth.buy_orders.keys())
                mid_price = (best_ask + best_bid) / 2
                
                if product == 'COCONUTS':
                    coconuts_price = self.coconuts_price.append(best_ask)
                # Check if the lowest ask (sell order) is lower than the above defined fair value
                if best_ask - mid_price < 2:
                    # In case the lowest ask is lower than our fair value,
                    # This presents an opportunity for us to buy cheaply
                    # The code below therefore sends a BUY order at the price level of the ask,
                    # with the same quantity
                    # We expect this order to trade with the sell order
                    logger.print("BUY", str(20) + "x", best_ask)
                    orders.append(Order(product, best_ask, -20))
                    balance -= 20 * best_ask
            # The below code block is similar to the one above,
            # the difference is that it finds the highest bid (buy order)
            # If the price of the order is higher than the fair value
            # This is an opportunity to sell at a premium
            if len(order_depth.buy_orders) > 0:
                best_bid = max(order_depth.buy_orders.keys())
                acceptable_price = best_bid * 0.99
                if best_bid > acceptable_price:
                    logger.print("SELL", str(20) + "x", best_bid)
                    orders.append(Order(product, best_bid, -20))
                    balance += 20 * best_bid
            # Add all the above orders to the result dict
            orders1[product] = orders
        

            # Return the dict of orders
            # These possibly contain buy or sell orders for PEARLS
            # Depending on the logic above
        logger.flush(state, orders1)
        return orders1, balance