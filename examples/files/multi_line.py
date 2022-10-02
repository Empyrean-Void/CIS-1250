# Functions #
def open_file():
    file = open('output/multi_line.txt', 'w')

    return file


def get_line():
    line = input('Enter a line of text')

    return line


def num_of_lines():
    line_count = int(input('How many lines do you want? '))

    return line_count

# Main #
if __name__ == "__main__":
    file = open_file()
    line = get_line()
    line_count = num_of_lines()
