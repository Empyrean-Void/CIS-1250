# Functions #
def header():
    print('\nWelcome to Pyramid Calculator\nVersion 1.0\n')


def get_base():
    base = float(input('Enter pyramid base (in meters): '))

    return base


def get_height():
    height = float(input('Enter pyramid height(in meters): '))

    return height


def get_pyramid_volume(base, height):
    volume = (base ** 2 * height)/3

    return volume


def display_volume(volume):
    print(f'The pyramid volume is {volume:.2f} meters cubed.')


if __name__ == "__main__":
    header()

    # Get user input
    base = get_base()
    height = get_height()

    # Calculate pyramid volume
    volume = get_pyramid_volume(base, height)

    # Display volume to user
    display_volume(volume)
