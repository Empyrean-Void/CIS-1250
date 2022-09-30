# Functions #
def open_file():
    file = open('output/test.txt', 'r')

    return file


def read_file(file):
    text = file.read()

    return text


def display_file(text):
    print(text)


# Main #
if __name__ == "__main__":
    file = open_file()

    text = read_file(file)

    display_file(text)
