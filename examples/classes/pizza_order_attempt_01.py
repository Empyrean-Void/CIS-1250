size = input('Please enter size of pizza (s, m, l): ').lower()

toppings = []

while True:
    topping = input('Please enter a topping to add (or enter to quit): ')

    if not topping:
        break

    toppings.append(topping)

print(f'Your pizza is size {size}')
print('Your toppings are: ')
print('\n'.join(toppings))
