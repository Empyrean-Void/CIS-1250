# Functions #
def while_demo():
    x = 1
    while x <= 5:  # <- Conditional statement
        print(x)
        x += 1  # <- Counter to prevent infinite loop


def name_loop():
    name = ''
    while not name:
        name = input('Please enter name: ')
    print(f'\nHello {name}!')


def do_another_while():
    do_another = 'y'
    while do_another == 'y':
        print('\nDo some stuff\n')
        do_another = input('Do another (Y/n): ').lower() or 'y'
    print('\nThank you for using my program.')


# Main #
while_demo()
name_loop()
do_another_while()
