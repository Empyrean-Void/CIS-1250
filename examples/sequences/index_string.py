# Function #
def get_string():
    greeting = input('Enter a string: ')

    return greeting


def string_index(greeting):
    result = greeting[0]
    print(result)


def index_input(greeting):
    i = int(input('Enter an index number (first index is 1): '))

    if i > 0 and i <= len(greeting):
        result = greeting[i - 1]

        print(result)
    else:
        print('Index out of range...')


# Main #
if __name__ == "__main__":
    while True:
        greeting = get_string()

        string_index(greeting)
        index_input(greeting)

        do_another = input('Run again (Y/n): ').lower() or 'y'

        if do_another != 'y':
            break
