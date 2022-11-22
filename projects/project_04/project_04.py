from math import radians, sqrt, cos, sin, atan2


RADIUS = 6371


class PointWiki:
    Id = 0
    city = ""
    lat = ""
    lon = ""
    desc = ""


def get_point_from_user():
    point = PointWiki()
    point.city = input('Enter city name: ')
    point.lat = float(input('Enter city latitude: '))
    point.lon = float(input('Enter city longitude: '))
    point.desc = input('Enter a short description: ')

    return point


def get_points_from_user(points):
    do_another = 'y'

    while do_another == 'y':
        point = get_point_from_user()
        point.Id = len(points) + 1
        points.append(point)

        do_another = input(
            'Do you want to add another point? (Y/n): ').lower() or 'y'


def display_point(point):
    print(f"City: {point.city}\n")
    print(f"Lat: {point.lat}\n")
    print(f"Lon: {point.lon}\n")
    print(f"Desc: {point.desc}\n")


def display_point_as_row(point):
    print(f"{point.Id:5} {point.city:20} {point.lat:20} {point.lon:20} {point.lon:20}")


def display_points(points):
    print(f"{'Id':5} {'City':20} {'Lat':20} {'Lon':20} {'Desc':20}")
    for point in points:
        display_point_as_row(point)


def save_points_to_file(points):
    file_name = input("PLease enter a file name: ")
    f = open(file_name, 'w')
    for point in points:
        f.write(f"{point.Id}\t")
        f.write(f"{point.city}\t")
        f.write(f"{point.lat}\t")
        f.write(f"{point.lon}\t")
        f.write(f"{point.desc}\t")
    f.close()


def read_points_from_file():
    file_name = input("PLease enter a file name: ")
    f = open(file_name, 'r')
    points = []
    while True:
        line = f.readline()
        if not line:
            break

        elements = line.split('\t')
        point = PointWiki()
        point.Id = int(elements[0])
        point.city = elements[1]
        point.lat = float(elements[2])
        point.lon = float(elements[3])
        point.desc = elements[4]
        points.append(point)
    f.close()
    return points


def edit_point(points):
    display_points(points)

    get_point = int(input('Select a city to edit (ex. 1): ')) - 1

    point = points[get_point]

    city = point.city
    lat = point.lat
    lon = point.lon
    desc = point.desc

    point.insert(0, city)
    point.insert(1, lat)
    point.insert(2, lon)
    point.insert(3, desc)

    points.insert(get_point, point)
    points.pop(get_point - 1)

    return points


def get_distance(points):
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


if __name__ == "__main__":
    points = []
    while True:
        display_points(points)
        choice = input("(A)dd, (D)isplay, (S)ave, (O)pen, (F)ind point, (Q)uit: ")[
            0].upper()
        if choice == 'A':
            get_points_from_user(points)
        if choice == 'D':
            point_id = int(input("please enter Id: "))
            for point in points:
                if point.Id == point_id:
                    display_point(point)
        elif choice == 'S':
            save_points_to_file(points)
        elif choice == 'O':
            points = read_points_from_file()
        elif choice == 'F':
            get_distance(points)
        elif choice == 'Q':
            break
        else:
            print("I did not understand that.")
