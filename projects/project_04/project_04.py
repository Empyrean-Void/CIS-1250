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


if __name__ == "__main__":
    points = []
    while True:
        display_points(points)
        choice = input("(A)dd, (D)isplay, (S)ave, (O)pen, (Q)uit: ")[0].upper()
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
        elif choice == 'Q':
            break
        else:
            print("I did not understand that.")
