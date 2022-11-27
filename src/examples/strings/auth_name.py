# Functions #
def get_name():
    name = input('Enter you name: ').title()

    return name


def check_name(name):
    auth_names = ['Rob', 'Bill', 'John', 'Linus']

    if name in auth_names:
        print('Access granted')
    else:
        print('Access denied')


# Main #
if __name__ == "__main__":
    while True:
        name = get_name()

        check_name(name)

        do_another = input('Run again (Y/n)? ') or 'y'

        if do_another != 'y':
            break
