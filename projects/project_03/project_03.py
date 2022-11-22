# Imports #
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


# Add point
def get_city():
    city = input('Enter city name: ')

    return city


def get_lon():
    lon = float(input('Enter city longitude: '))

    return lon


def get_lat():
    lat = float(input('Enter city latitude: '))

    return lat


def get_desc():
    desc = input('Enter city description: ')

    return desc


def add_point(points):
    city = get_city()
    lat = get_lat()
    lon = get_lon()
    desc = get_desc()

    point = [city, lat, lon, desc]

    points.append(point)

    return points


# Display point
def display_points(points):
    for point in points:
        print(point)


def display_point_info(points):
    point = int(input('Select a point (ex. 1): ')) - 1

    if point in points:
        pass

    print(f'City: {point[0]}')
    print(f'Lat: {point[1]}')
    print(f'Lon: {point[2]}')
    print(f'Desc: {point[3]}')


# Remove point
def remove_point(points):
    display_points(points)

    get_point = int(input('Select a city to remove (ex. 1): ')) - 1

    confirm = input('Are you sure? (y/N): ').lower() or 'n'

    if confirm == 'n':
        points.pop(get_point)

    return points


# Find point
def find_closest_point(points):
    get_point = int(input('Select a city: (ex. 1): ')) - 1

    point = points[get_point]

    if get_point < len(point):
        get_next_point = get_point + 1

    else:
        get_next_point = get_point - 1

    next_point = points[get_next_point]

    origin_lat = point[1]
    destination_lat = next_point[1]

    lat = point[1] - next_point[1]
    lon = point[2] - next_point[2]

    a = sin(radians(lat) / 2) ** 2 + cos(radians(origin_lat)) * \
        cos(radians(destination_lat)) * sin(radians(lon) / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = RADIUS * c

    return distance


# Edit point
def edit_point(points):
    display_points(points)

    get_point = int(input('Select a city to edit (ex. 1): ')) - 1

    point = points[get_point]

    city = get_city()
    lat = get_lat()
    lon = get_lon()
    desc = get_desc()

    point.insert(0, city)
    point.insert(1, lat)
    point.insert(2, lon)
    point.insert(3, desc)

    points.insert(get_point, point)
    points.pop(get_point - 1)

    return points


# Open file
def open_file(points):
    file_name = input('Enter file name: ')
    f = open(file_name, 'r')
    points = []

    while True:
        line = f.readline()
        if not line:
            break

        elements = line.split(',')

        city = elements[0]
        lat = elements[1]
        lon = elements[2]
        desc = elements[3]

        point = [city, lat, lon, desc]
        points.append(point)

    f.close()
    return points


# Save file
def save_file(points):
    file_name = input("PLease enter a file name: ")
    f = open(file_name, 'w')
    for point in points:
        f.write(f"{point}\t")
    f.close()


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

        elif choice == 'E':
            edit_point(points)

        elif choice == 'R':
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
