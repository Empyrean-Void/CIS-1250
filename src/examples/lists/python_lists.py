# Create a list
def create_list():
    my_list = ['apple', 'banana', 'cherry']

    return my_list


# Print a list
def print_list(my_list):
    print(f'Example List: {my_list}')


# Get length of a list
def list_len(my_list):
    print(f'Length: {len(my_list)}')


# Type of list
def list_type(my_list):
    print(f'Type: {type(my_list)}')


if __name__ == "__main__":
    my_list = create_list()

    print_list(my_list)

    list_len(my_list)

    list_type(my_list)
