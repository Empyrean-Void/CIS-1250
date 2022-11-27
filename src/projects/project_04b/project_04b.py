# Name: project_04b.py
# Programmer: Jonah Shortz
# Email: jshortz@cnm.edu
# Purpose: Translate terms in one language to english

# Functions #
def display_keys(key_terms):
    for term in key_terms:
        print(term)


def get_search():
    search = input('Select a term to translate: ')

    return search


def show_translation(search, key_terms):
    if search in key_terms:
        print(f'{search} means {key_terms[search]}.')

    else:
        print(f'{search} was not found!')


def run_again():
    do_another = input('Run again? (Y/n): ').lower() or 'y'

    return do_another


# Main #
if __name__ == "__main__":
    key_terms = {'Kon\'nichiwa': 'Hello', 'Sayonara': 'Goodbye',
                 'Konpyutasaiensu': 'Computer Science'}

    while True:
        display_keys(key_terms)

        # Get search term from user
        search = get_search()

        # Display translatation for matching key term
        show_translation(search, key_terms)

        # Ask user to run program again
        do_another = run_again()

        if do_another != 'y':
            break
