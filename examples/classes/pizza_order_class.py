class Pizza:
    size = 'm'
    crust = 1
    toppings = ['Cheese']


def get_pizza():
    new_pizza = Pizza()

    new_pizza.size = input('Enter a size (s, m, l): ').lower()
    new_pizza.crust = int(
        input('Select a crust [(1) Thin, (2) Hand tossed, (3) Deep dish]: '))
    new_pizza.toppings = []

    while True:
        topping = input('Enter a topping to add (or press Enter to quit): ')

        if not topping:
            break

        new_pizza.toppings.append(topping)

    return new_pizza


if __name__ == "__main__":
    pizza = get_pizza()

    print(pizza)
