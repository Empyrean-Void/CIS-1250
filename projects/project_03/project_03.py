# Imports #
from os.path import exists as file_exists
from math import radians, sqrt, cos, sin, atan2

# Constants #
RADIUS = 6371


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
    points = []

    file_name = input('Enter path to file: ')

    file_check = file_exists(file_name)

    if file_check is False:
        print('Error file does not exist!')

        return points

    file = open(file_name, 'r')

    for x in file:
        txt = x.strip().split(", ")
        info = {"City": txt[0], "Latitude": float(
            txt[1]), "Longitude": float(txt[2]), "Discription": txt[3]}
        points.append(info)

    return points


def display_point_info(points):
    poi = int(input('\nSelect a point to view: ')) - 1

    print(points[poi])


def list_points(points):
    print("Current point list is: ")
    count = 0
    for x in points:
        print("[", count, "] : ", x)
        count = count + 1


def add_point(points):
    city = input("\nCity name: ")
    lat = float(input("Latitude: "))
    lon = float(input("Longitude: "))
    dsc = input("Short discrption: ")
    info = {"City": city, "Latitude": lat,
            "Longitude": lon, "Discription": dsc}

    confirm = input('\nAre you sure? (Y/n): ').lower() or 'y'

    if confirm != "y":
        print("\nNo points added to the list.")

        return points

    points.append(info)

    return points


def remove_point(points):
    list_points(points)
    num = int(input("Which point do you want to remove: ")) - 1

    confirm = input('Are you sure? (y/N): ').lower() or 'n'
    if confirm != 'y':
        print("No points removed form the list.")

    del points[num]
    return points


def get_distance(points, origin):
    pass


def find_closet_point(points, origin, destination):
    # Break input into individual latitude and longitude
    origin_lat = origin[0]
    destination_lat = destination[0]
    lat = origin[0] - destination[0]
    long = origin[1] - destination[1]

    # Calculate distance
    a = sin(radians(lat) / 2) ** 2 + cos(radians(origin_lat)) * \
        cos(radians(destination_lat)) * sin(radians(long) / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = RADIUS * c

    return distance


def edit_point(points):
    # Select a point
    point_of_interest = int(input('Select a point to edit: '))

    # Edit each value for the respective dictionary keys


def save_file(points):
    pass


# Main #
if __name__ == "__main__":
    points = []

    display_header()

    while True:
        display_menu()

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
            origin = int(input('Select a point: ')) - 1
            destination = []
            for point in points:
                find_closet_point(points, origin, destination)

        elif choice == 'S':
            save_file(points)

        elif choice == 'Q' or 'exit':
            break

        else:
            print(f'\n{choice} is an invalid selection!\n')

    display_exit()
