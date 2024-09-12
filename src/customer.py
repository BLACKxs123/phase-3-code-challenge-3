class Customer:
    all_customers = []  # To track all customer instances

    def __init__(self, name):
        self.name = name
        self.orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def create_order(self, coffee, price):
        """Creates a new Order for the customer."""
        order = Order(self, coffee, price)
        self.orders.append(order)
        coffee.orders.append(order)
        return order

    def coffees(self):
        """Returns a unique list of all coffees the customer has ordered."""
        return list({order.coffee for order in self.orders})

    @classmethod
    def most_aficionado(cls, coffee):
        """Finds the customer who has spent the most money on the provided coffee."""
        highest_spender = None
        highest_spent = 0
        for customer in cls.all_customers:
            total_spent = sum(order.price for order in customer.orders if order.coffee == coffee)
            if total_spent > highest_spent:
                highest_spender = customer
                highest_spent = total_spent
        return highest_spender
