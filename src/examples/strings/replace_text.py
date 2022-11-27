# Functions #
def get_text():
    original_text = input('Enter some text: ')

    return original_text


def search_text():
    search_pattern = input('Enter search pattern: ')

    return search_pattern


def replace_text():
    text_to_repalce = input('Text to replace with: ')

    return text_to_repalce


def create_text(original_text, search_pattern, text_to_repalce):
    new_text = original_text.replace(search_pattern, text_to_repalce)

    return new_text


def display_text(new_text):
    print(new_text)


# Main #
if __name__ == "__main__":
    while True:
        original_text = get_text()
        search_pattern = search_text()
        text_to_repalce = replace_text()
        new_text = create_text(original_text, search_pattern, text_to_repalce)

        display_text(new_text)

        do_another = input('Run again (Y/n)? ').lower() or 'y'

        if do_another != 'y':
            break
