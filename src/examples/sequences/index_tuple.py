# Functions #
def get_name():
    names = ('Rob', 'Ada', 'Bjarney', 'Grace')

    print('Pick a name by it\'s index number.')

    for i in range(len(names)):
        print(i + 1, names[i])

    choice = int(input('> ')) - 1

    print(f'You chose {names[choice]}.')


# Main #
if __name__ == "__main__":
    while True:
        get_name()

        do_another = input('Run again (Y/n): ').lower() or 'y'

        if do_another != 'y':
            break
