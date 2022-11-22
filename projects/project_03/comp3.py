# IanP5
# Programmer: Ian Voth
# EMail: ivoth@cnm.edu
# Purpose: provides user capability to view contact info

from secrets import choice
from os.path import exists
from math import radians, sin, cos, atan2, sqrt, pow

# Function ----------------------------------------------
# no parameters


def display_header():  # <-- funtion defintion
    print("weclome to a cordine distance cal")


def open_file_and_return_list():
    my_place_list = []
    file_name = input("What file do you want to use: ")
    file_exists = exists(file_name)
    if (file_exists is False):
        print("File does not exist. Returning empty list.")
        return my_place_list
    file = open(file_name, "r")
    for x in file:
        txt = x.strip().split(", ")
        my_dict = {"City": txt[0], "Latitude": float(
            txt[1]), "Longitude": float(txt[2]), "Discription": txt[3]}
        my_place_list.append(my_dict)

    return my_place_list


def display_info():
    print(my_place_list)
    return my_place_list


def add_a_point(place_list):
    city = input("City name:  ")
    lat = float(input("lat: "))
    lon = float(input("lon: "))
    dsc = input("short discrption: ")
    my_dict = {"City": city, "Latitude": lat,
               "Longitude": lon, "Discription": dsc}
    confirm = input('Are you sure? (y/N): ').lower()
    if confirm != "y":
        print("No points added to the list.")
        return place_list
    place_list.append(my_dict)
    return place_list


def remove_point(place_list):
    list_points(place_list)
    num = int(input("Which point do you want to remove: "))
    confirm = input('Are you sure? (y/N): ').lower() or 'n'
    if confirm == 'n':
        print("No points removed form the list.")
    del place_list[num]
    return place_list


def list_points(point_list):
    print("Current point list is: ")
    count = 0
    for x in point_list:
        print("[", count, "] : ", x)
        count = count + 1


def find_nearest(point_list):
    point_list = input("What is your Lon and Lan?: ")
    loc1, loc2 = point_list
    while True:
        lat1 = radians(loc1[0])
        lon1 = radians(loc1[1])
        lat2 = radians(loc2[0])
        lon2 = radians(loc2[1])
        print(lat1, lon1, lat2, lon2)
        R = 6371.0
        A = pow((sin((lat1-lat2)/2)), 2) + cos(lat1) * \
            cos(lon1) * pow(sin((lon1-lon2)/2), 2)
        C = 2 * atan2(sqrt(A), sqrt(1-A))
        D = R * C
        return point_list, D


def save_file(file):

    file_name = input("What file do you want to use")
    file = open(file_name, "w")
    file_name.close()
    return file


def edit_points(my_place_list):
    print(my_place_list)
    file = my_place_list
    x = input("What point do you want to edit? ")
    if x != file:
        x = file.replace()
        return my_place_list


my_place_list = []
while True:
    get_user_choice = input("""(O)pen a point file, Display a single points (I)nformation, 
                            (A)dd a point, (R)emove a point, (E)dit a point, (F)ind closest, 
                            (S)ave points file, (L)ist points, (Q)uit: """)[0]
    get_user_choice = get_user_choice.upper()
    if get_user_choice == "O":
        my_place_list = open_file_and_return_list()
    elif get_user_choice == "I":
        my_place_list = display_info()
    elif get_user_choice == "A":
        my_place_list = add_a_point(my_place_list)
    elif get_user_choice == "R":
        my_place_list = remove_point(my_place_list)
    elif get_user_choice == "L":
        list_points(my_place_list)
    elif get_user_choice == "E":
        my_place_list = edit_points(my_place_list)
    elif get_user_choice == "F":
        my_place_list = find_nearest(my_place_list)
    elif get_user_choice == "S":
        my_place_list = save_file(my_place_list)
    elif get_user_choice == " Q":
        break
