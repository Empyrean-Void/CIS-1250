class Pizza:
    def __init__(self):
        self.size = 'm'
        self.crust = 1
        self.toppings_available = ['cheese', 'pepperonie', 'sausage',
                                   'mushrooms', 'green pepper', 'green chile',
                                   'olives']
    toppings = ['Cheese']
    price = 9.5

    def set_size(self, size):
        if size == 's' or size == 'm' or size == 'l':
            self.size = size
        else:
            raise Exception('Invalid size')

    def get_size(self):
        return self.size

    def set_crust(self, crust):
        if crust in (1, 2, 3):
            self.crust = crust
        else:
            raise Exception('Invalid crust')

    def get_crust(self):
        return self.crust

    def set_toppings(self, toppings):
        if len(set(toppings).difference(set(self.toppings_available))) == 0:
            self.toppings = toppings
        else:
            raise Exception('Invalid toppings')

    def get_toppings(self):
        return self.toppings

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def get_pizza_order(self):
        return f"Size: {self.size} Crust: {self.crust} Toppings: {', '.join(self.toppings)} Price: ${self.price:.2f}"


if __name__ == "__main__":
    pizza = Pizza()
    pizza.set_size('l')
    pizza.set_crust(1)
    pizza.set_toppings(['cheese', 'pepperonie'])

    print(pizza.get_pizza_order())
