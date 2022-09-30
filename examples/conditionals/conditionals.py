# Functions #
def get_number():
    x = float(input('Enter a number: '))

    return x


def if_demo(x):
    if x < 0:
        print('\nNumber is negative.\n')
    elif x > 0:
        print('\nNumber is positive.\n')
    else:
        print('\nZero\n')


# Main #
if __name__ == "__main__":
    while True:
        x = get_number()

        if_demo(x)

        do_another = input('Run again (Y/n)? ').lower() or 'y'

        if do_another == 'n':
            break
