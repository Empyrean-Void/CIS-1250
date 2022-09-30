# Functions #
def get_numbers():
    number = float(input('Enter a number: '))

    return number


def add_numbers(num_1, num_2):
    result = num_1 + num_2

    return result


def display_answer(num_1, num_2, result):
    print(f'{num_1} + {num_2} = {result}')


# Main #
do_another = 'y'

while True:
    if __name__ == "__main__":
        # Get numbers from user
        num_1 = get_numbers()
        num_2 = get_numbers()

        # Calculate sum
        result = add_numbers(num_1, num_2)

        # Display answer
        display_answer(num_1, num_2, result)

        # Loop program
        do_another = input('Run again (Y/n): ') or 'y'

        if do_another == 'n':
            break
