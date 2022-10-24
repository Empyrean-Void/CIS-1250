if __name__ == "__main__":
    names = ['Alice', 'Beth', 'Cecil', 'Dee-dee', 'Earl']

    numbers = ['1234', '9102', '3158', '0142', '5551']

    print(', '.join(names))

    name = input('\nEnter a name: ')

    name_index = names.index(name)
    print(f'\nIndex of {name}: {name_index}')

    phone_number = numbers[name_index]
    print(f'Number of {name}: {phone_number}')
