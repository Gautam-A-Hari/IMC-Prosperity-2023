from datamodel import Order, Symbol, TradingState
from typing import Any
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
                self.past_data[product].append(acceptable_price)
                # Check if the lowest ask (sell order) is lower than the above defined fair value
                if best_ask < acceptable_price:
                    # In case the lowest ask is lower than our fair value,
                    # This presents an opportunity for us to buy cheaply
                    # The code below therefore sends a BUY order at the price level of the ask,
                    # with the same quantity
                    # We expect this order to trade with the sell order
                    print("BUY", str(20) + "x", best_ask)
                    orders.append(Order(product, best_ask, 20))
            # The below code block is similar to the one above,
            # the difference is that it finds the highest bid (buy order)
            # If the price of the order is higher than the fair value
            # This is an opportunity to sell at a premium
            if len(order_depth.buy_orders) > 0:
                best_bid = max(order_depth.buy_orders.keys())
                acceptable_price = round(best_bid * 0.99)
                self.past_data[product].append(acceptable_price)
                if best_bid > acceptable_price:
                    print("SELL", str(20) + "x", best_bid)
                    orders.append(Order(product, best_bid, 20))
            # Add all the above orders to the result dict
            orders1[product] = orders

            # Return the dict of orders
            # These possibly contain buy or sell orders for PEARLS
            # Depending on the logic above
            # Print last/most recent acc_price
            if (len(self.past_data[product])) > 51:
                print("apple" + self.past_data[product][-50])
        return orders1