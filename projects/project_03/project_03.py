# Functions #

# Print welcome message
def display_header():
    print('Welcome to Point Wiki!')


# Print exit message
def display_exit():
    print('\nThank you for using Point Wiki!')


# Print user selections
def display_menu():
    print('''\n(O)pen a point file
          \nDisplay a point's (I)nformation
          \n(A)dd a point
          \n(R)emove a point
          \n(E)dit a point
          \n(F)ind closest point
          \n(S)ave point file
          \n(Q)uit Point Wiki''')


def get_user_choice():
    choice = input('\nPlease make a selection: ').upper()

    return choice


def open_file(points):
    file = open('output/points.txt', 'w')

    return file


def display_point_info(points):
    key_term = input('\nEnter a point name: ').title()

    print(f'\n{key_term} is located at: {points[key_term]}\n')


def add_point(points):
    pass


def remove_point(points):
    pass


def find_closet_point(points):
    pass


def edit_point(points):
    pass


def save_file(points, file):
    file.write(points)


# Main #
if __name__ == "__main__":
    display_header()

    while True:
        display_menu()

        points = {'Albuqurque': (35.0844, 106.6504),
                  'Santa Fe': (35.6870, 105.9378)
                  }

        choice = get_user_choice()

        if choice == 'O':
            open_file(points)

        elif choice == 'I':
            display_point_info(points)

        elif choice == 'A':
            add_point(points)

        elif choice == 'R':
            confirm = input('Are you sure? (y/N): ').lower() or 'n'

            if choice == 'n':
                remove_point(points)

        elif choice == 'F':
            find_closet_point(points)

        elif choice == 'S':
            save_file(points)

        elif choice == 'Q' or 'exit':
            break

        else:
            print(f'\n{choice} is an invalid selection!\n')

    display_exit()
