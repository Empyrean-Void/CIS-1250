if __name__ == "__main__":
    phone_book = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3158'}

    print(', '.join(phone_book.keys()))

    name = input('\nEnter a name: ')
    number = phone_book[name]

    print(f'\n{name}\'s phone number is {number}')
