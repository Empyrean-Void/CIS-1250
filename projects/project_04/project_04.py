# Functions #
def create_dict():
    phrases = {'Privet': 'Hello', 'Kak dela': 'How are you?',
               'Do svidaniya': 'Goodbye'}

    return phrases

# Display phrases for user


def display_keys(phrases):
    key_list = list(phrases.keys())

    print(key_list)


def get_key_term():
    key_term = input('\nEnter a phrase to translate: ')

    return key_term


# Add simple input validation
def display_trans(key_term, phrases):
    if key_term in phrases:
        return f'\nTranslation from russian to english is: {phrases[key_term]}'
    else:
        return f'\n{key_term} is not in dictionary!'


# Main #
if __name__ == "__main__":
    phrases = create_dict()
    do_another = 'y'

# Loop program
    while True:
        display_keys(phrases)

        key_term = get_key_term()
        translation = display_trans(key_term, phrases)

        print(translation)

        # Check if user wants to run again
        # Set default choice to yes
        do_another = input(
            '\nTranslate another phrase? (Y/n): ').lower() or 'y'

        if do_another != 'y':
            break
