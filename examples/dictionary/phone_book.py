# Functions #
def display_header():
    print('Welcome to Py Phone!')


def display_exit():
    print('Exiting...')


def display_names():
    phone_book = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3158'}

    print(', '.join(phone_book.keys()))


def display_menu():
    print('\n(O)pen \n(A)dd number \n(R)emove number \n(L)ook up number \n(S)ave \n(Q)uit')


def get_menu_choice():
    choice = input('\nSelect a menu option: ')

    return choice


def eval_user_choice(choice):
    if choice == 'O':
        open_phone_book()

    elif choice == 'A':
        add_number(phone_book)

    elif choice == 'R':
        remove_number(phone_book)

    elif choice == 'L':
        look_up(phone_book)

    elif choice == 'S':
        save_phone_book(phone_book)


def open_phone_book():
    file_name = input('Enter a file name: ')
    f = open(file_name, 'r')
    phone_book.clear()

    while True:
        line = f.readline()

        if not line:
            break

        elements = line.strip().split('\t')
        phone_book[elements[0]] = elements[1]

    f.close()


def add_number(phone_book):
    name = input('Enter a name: ')
    phone_number = input('Enter a phone number: ')

    phone_book[name] = phone_number


def remove_number(phone_book):
    name = input('Enter a name: ')
    confirm = input('Are you sure? (y/N): ').lower() or 'n'

    if confirm == 'y':
        del phone_book[name]


def look_up(phone_book):
    name = input('Enter a name: ')
    print(f'{name}\'s phone number is {phone_book[name]}')


def save_phone_book(phone_book):
    file_name = input('Enter a file name: ')
    f = open(file_name, 'w')

    for item in phone_book:
        f.write(f'{item}\t{phone_book[item]}\n')

    f.close()


# Main #
if __name__ == '__main__':
    phone_book = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3158'}

    # Display welcome message
    display_header()

    while True:
        display_names()

        display_menu()

        choice = get_menu_choice()

        # Evaluate user choice
        eval_user_choice(choice)

        if choice == 'Q':
            break

        else:
            print(f'{choice} is not a valid option!')

        # Display an exit message
        display_exit()
