import json
from datamodel import Order, ProsperityEncoder, Symbol, Trade, TradingState
from typing import Any

class Logger:
    def __init__(self) -> None:
        self.logs = ""

    def print(self, *objects: Any, sep: str = " ", end: str = "\n") -> None:
        self.logs += sep.join(map(str, objects)) + end

    def flush(self, state: TradingState, orders: dict[Symbol, list[Order]]) -> None:
        print(json.dumps({
            "state": self.compress_state(state),
            "orders": self.compress_orders(orders),
            "logs": self.logs,
        }, cls=ProsperityEncoder, separators=(",", ":"), sort_keys=True))

        self.logs = ""

    def compress_state(self, state: TradingState) -> dict[str, Any]:
        listings = []
        for listing in state.listings.values():
            listings.append([listing["symbol"], listing["product"], listing["denomination"]])

        order_depths = {}
        for symbol, order_depth in state.order_depths.items():
            order_depths[symbol] = [order_depth.buy_orders, order_depth.sell_orders]

        return {
            "t": state.timestamp,
            "l": listings,
            "od": order_depths,
            "ot": self.compress_trades(state.own_trades),
            "mt": self.compress_trades(state.market_trades),
            "p": state.position,
            "o": state.observations,
        }

    def compress_trades(self, trades: dict[Symbol, list[Trade]]) -> list[list[Any]]:
        compressed = []
        for arr in trades.values():
            for trade in arr:
                compressed.append([
                    trade.symbol,
                    trade.buyer,
                    trade.seller,
                    trade.price,
                    trade.quantity,
                    trade.timestamp,
                ])

        return compressed

    def compress_orders(self, orders: dict[Symbol, list[Order]]) -> list[list[Any]]:
        compressed = []
        for arr in orders.values():
            for order in arr:
                compressed.append([order.symbol, order.price, order.quantity])

        return compressed

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
            order_depth: OrderDepth = state.order_depths[product]
            # Initialize the list of Orders to be sent as an empty list
            orders: list[Order] = []
            # If statement checks if there are any SELL orders in the PEARLS market
            if len(order_depth.sell_orders) > 0:
                best_ask = min(order_depth.sell_orders.keys())
                acceptable_price = round(best_ask * 1.01)
                # Check if the lowest ask (sell order) is lower than the above defined fair value
                if (len(self.past_data[product])) == 10:
                    self.past_data[product].pop(0)
                    self.past_data[product].append(acceptable_price)
                    change = (self.past_data[product][0] / self.past_data[product][9])
                    if change > 0.9:
                            # In case the lowest ask is lower than our fair value,
                            # This presents an opportunity for us to buy cheaply
                            # The code below therefore sends a BUY order at the price level of the ask,
                            # with the same quantity
                            # We expect this order to trade with the sell order
                        logger.print("BUY", str(30) + "x", best_ask)
                        orders.append(Order(product, best_ask, 30))
                    else:
                        logger.print("SELL", str(5) + "x", best_ask)
                        orders.append(Order(product, best_ask, 5))
                else:
                    self.past_data[product].append(acceptable_price)
                    logger.print("BUY", str(1) + "x", best_ask)
                    orders.append(Order(product, best_ask, 1))
            # The below code block is similar to the one above,
            # the difference is that it finds the highest bid (buy order)
            # If the price of the order is higher than the fair value
            # This is an opportunity to sell at a premium
            if len(order_depth.buy_orders) > 0:
                best_bid = max(order_depth.buy_orders.keys())
                acceptable_price = round(best_bid * 0.99)
                if (len(self.past_data[product])) == 10:
                    self.past_data[product].pop(0)
                    self.past_data[product].append(acceptable_price)
                    change = (self.past_data[product][0] / self.past_data[product][9])
                    if change > 0.9:
                        logger.print("SELL", str(30) + "x", best_bid)
                        orders.append(Order(product, best_bid, 30))
                    else:
                        logger.print("BUY", str(5) + "x", best_bid)
                        orders.append(Order(product, best_bid, 5))
                else:
                    self.past_data[product].append(acceptable_price)
                    logger.print("SELL", str(1) + "x", best_bid)
                    orders.append(Order(product, best_bid, 1))
            # Add all the above orders to the result dict
            orders1[product] = orders

            # Return the dict of orders
            # These possibly contain buy or sell orders for PEARLS
            # Depending on the logic above
            # Print last/most recent acc_price
        logger.flush(state, orders1)
        return orders1