# Functions #
def display_url():
    tag = '<a href "http://www.python.org">Python web site</a>'

    print(tag[9:30])  # Slicing is inclusive:exclusive
    print(f'\n{tag[32:-4]}')


# Main #
if __name__ == "__main__":
    display_url()
