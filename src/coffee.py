class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self.orders = []

    @property
    def name(self):
        return self._name

    def num_orders(self):
        """Returns the total number of orders for the coffee."""
        return len(self.orders)

    def average_price(self):
        """Returns the average price of all orders for this coffee."""
        if self.orders:
            return sum(order.price for order in self.orders) / len(self.orders)
        return 0

    def customers(self):
        """Returns a unique list of customers who have ordered this coffee."""
        return list({order.customer for order in self.orders})
