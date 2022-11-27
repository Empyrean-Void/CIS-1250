# Functions #
def open_file():
    file = open('output/test.txt', 'w')

    return file


def get_text():
    text = input('Enter some text: ')

    return text


def write_file(text):
    file.write(text)


# Main #
if __name__ == "__main__":
    file = open_file()

    text = get_text()

    write_file(text)

    file.close()
