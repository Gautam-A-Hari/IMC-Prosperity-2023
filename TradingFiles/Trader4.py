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
    past_data = {'BANANAS': {'bid_price': [], 'ask_price':[]},
                 'COCONUTS': {"bid_price": [], 'ask_price':[]},
                 'PINA_COLADAS':{'bid_price': [], 'ask_price':[]},
                 'PEARLS': {'bid_price': [], 'ask_price':[]},
                 'BERRIES': {'bid_price': [], 'ask_price':[]},
                 'DIVING_GEAR': {'bid_price': [], 'ask_price':[]},
                 'UKULELE': {'bid_price': [], 'ask_price':[]},
                 'DIP': {'bid_price': [], 'ask_price':[]},
                 'PICNIC_BASKET': {'bid_price': [], 'ask_price':[]},
                 'BAGUETTE': {'bid_price': [], 'ask_price':[]}}
    orderLimit = {'BANANAS': 9,
                  'COCONUTS': 299,
                  'PINA_COLADAS': 149,
                  'PEARLS': 9,
                  'BERRIES': 124,
                  'DIVING_GEAR': 24,
                  'UKULELE': 34,
                  'DIP': 149,
                  'PICNIC_BASKET': 34,
                  'BAGUETTE': 74}
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
            volume = self.orderLimit[product]
            if len(order_depth.sell_orders) > 0:
                best_ask = min(order_depth.sell_orders.keys())
                # Check if the lowest ask (sell order) is lower than the above defined fair value
                if (len(self.past_data[product]['ask_price'])) == 10:
                    self.past_data[product]['ask_price'].pop(0)
                    self.past_data[product]['ask_price'].append(best_ask)
                    change = (self.past_data[product]['ask_price'][0] / self.past_data[product]['ask_price'][9])
                    if change > 0.995:
                            # In case the lowest ask is lower than our fair value,
                            # This presents an opportunity for us to buy cheaply
                            # The code below therefore sends a BUY order at the price level of the ask,
                            # with the same quantity
                            # We expect this order to trade with the sell order
                        logger.print("BUY", str(-volume) + "x", best_ask)
                        orders.append(Order(product, best_ask, -volume))
                    else:
                        logger.print("SELL", str(volume) + "x", best_ask)
                        orders.append(Order(product, best_ask, volume))
                else:
                    self.past_data[product]['ask_price'].append(best_ask)
                    logger.print("BUY", str(1) + "x", best_ask)
                    orders.append(Order(product, best_ask, 1))
            # The below code block is similar to the one above,
            # the difference is that it finds the highest bid (buy order)
            # If the price of the order is higher than the fair value
            # This is an opportunity to sell at a premium
            if len(order_depth.buy_orders) > 0:
                best_bid = max(order_depth.buy_orders.keys())
                if (len(self.past_data[product]['bid_price'])) == 10:
                    self.past_data[product]['bid_price'].pop(0)
                    self.past_data[product]['bid_price'].append(best_bid)
                    change = (self.past_data[product][0] / self.past_data[product][9])
                    if change > 0.995:
                        logger.print("SELL", str(volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, volume))
                    else:
                        logger.print("BUY", str(volume) + "x", best_bid)
                        orders.append(Order(product, best_bid, -volume))
                else:
                    self.past_data[product]['bid_price'].append(best_bid)
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