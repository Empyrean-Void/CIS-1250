def create_list():
    my_list = ['apple', 'banana', 'cherry']

    return my_list


def print_list(my_list):
    print(f'Example List: {my_list}')


def access_item(my_list):
    print(f'Print First Item: {my_list[0]}')


def reverse_access(my_list):
    print(f'Print Last Item: {my_list[1]}')


if __name__ == "__main__":
    my_list = create_list()

    print_list(my_list)

    access_item(my_list)

    reverse_access(my_list)
