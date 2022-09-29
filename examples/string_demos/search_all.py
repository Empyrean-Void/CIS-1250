# Functions #
def find_all(text, text_to_find):
    location = text.find(text_to_find)

    while location != -1:
        print(location)
        location = text.find(text_to_find, location + 1)


# Main #
if __name__ == "__main__":
    find_all('aa bb aa cc aa dd', 'aa')
