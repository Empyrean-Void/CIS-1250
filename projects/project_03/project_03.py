# Functions #
def display_header():
    print('''#########################
              \n Welcome to Point Wiki!
              \n#########################\n''')


def display_exit():
    print('''\n#################################
        \nThank you for using Point Wiki!
        \n#################################''')


def display_menu():
    print('''(O)pen a point file
          \nDisplay a point's (I)nformation
          \n(A)dd a point
          \n(R)emove a point
          \n(E)dit a point
          \n(F)ind closest point
          \n(S)ave point file
          \n(Q)uit Point Wiki
          \n###############################''')


def get_user_choice():
    choice = input('\nPlease make a selection: ').upper()

    return choice


def open_file(points_of_interest):
    pass


def display_point_info(points_of_interest):
    pass


def add_point(points_of_interest):
    pass


def remove_point(points_of_interest):
    pass


def find_closet_point(points_of_interest):
    pass


def edit_point(points_of_interest):
    pass


def save_file(points_of_interest):
    pass


# Main #
if __name__ == "__main__":
    display_header()

    while True:
        display_menu()

        points_of_interest = None

        choice = get_user_choice()

        if choice == 'O':
            open_file(points_of_interest)

        elif choice == 'I':
            display_point_info(points_of_interest)

        elif choice == 'A':
            add_point(points_of_interest)

        elif choice == 'R':
            confirm = input('Are you sure? (y/N): ').lower() or 'n'

            if choice == 'n':
                remove_point(points_of_interest)

        elif choice == 'F':
            find_closet_point(points_of_interest)

        elif choice == 'S':
            save_file(points_of_interest)

        elif choice == 'Q':
            break

        else:
            print(f'\n{choice} is an invalid selection!\n')

    display_exit()
