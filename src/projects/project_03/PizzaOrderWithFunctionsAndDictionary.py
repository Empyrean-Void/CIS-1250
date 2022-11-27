from operator import is_, truediv


def get_pizza_size_from_user():
    size = input('Please enter size (s,m,l): ')
    return size


def get_pizza_toppings_from_user():
    toppings = []
    while True:
        topping = input('Please enter a topping to add (or enter to quit): ')
        if not topping:
            break
        toppings.append(topping)
    return toppings


def get_pizza_type_of_crust_from_user():
    type_of_crust = int(
        input('Please enter type of crust (1=thin, 2=hand tosed, 3=deep dish): '))
    return type_of_crust


def validate_pizza(pizza):
    size = pizza['size']
    type_of_crust = pizza['crust']
    result = ""
    size_ok = size == 's' or size == 'm' or size == 'l'
    crust_ok = type_of_crust in (1, 2, 3)
    if not size_ok:
        result += "Invalid Size "
    if not crust_ok:
        result += "Invalid crust "
    if result == "":
        result = "Valid"
    return result


def calculate_price(pizza):
    # calculate price
    if pizza['size'] == 's':
        price = 5.0
    elif pizza['size'] == 'm':
        price = 7.0
    elif pizza['size'] == 'l':
        price = 9.0
    else:
        print('invalid size')
    price += len(pizza['toppings'])*1.5
    if pizza['crust'] == 1:
        price += 1
    elif pizza['crust'] == 2:
        price += 3
    elif pizza['crust'] == 3:
        price += 2
    else:
        print('invalid crust')
    pizza['price'] = price  # <--how we add things to a dictionary


def display_pizza_info(pizza):
    size = pizza['size']
    type_of_crust = pizza['crust']
    toppings = pizza['toppings']
    price = pizza['price']
    # displays the information
    print(f"Pizza is size {size}")
    print(f"Crust is type: {type_of_crust}")
    print("Toppings are: ")
    print("\n".join(toppings))
    print(f"Price is {price}.")


def get_pizza():
    size = get_pizza_size_from_user()
    crust = get_pizza_type_of_crust_from_user()
    toppings = get_pizza_toppings_from_user()
    pizza = {"size": size, "crust": crust, "toppings": toppings}  # <--- tupple
    return pizza


if __name__ == "__main__":
    # get a pizza from user
    pizza = get_pizza()

    # validate pizza
    validation = validate_pizza(pizza)

    # if valid
    if validation == "Valid":
        # calculate price
        calculate_price(pizza)

        # display pizza info
        display_pizza_info(pizza)
    # else display error
    else:
        print(f"Invalid pizza: {validation}")
