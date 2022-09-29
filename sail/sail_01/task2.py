from math import pi


def circle_area(radius):
    PI = 3.14
    area = PI * (radius ** 2)

    return area


def sphere_volume(radius):
    PI = 3.14
    volume = (4/3) * PI * (radius ** 3)

    return volume


def add_word(text, word):
    phrase = text + ' ' + word

    return phrase


def max_minus_min(first_num, second_num):
    result = max(first_num, second_num) - min(first_num, second_num)

    return result


def max_minus_min_abs(first_num, second_num):
    result = max(abs(first_num), abs(second_num)) - min(abs(first_num), abs(second_num))

    return result


def circle_area_exact(radius):
    area = pi * (radius ** 2)

    return area


def sphere_volume_exact(radius):
    volume = (4/3) * pi * (radius ** 3)

    return volume


def add_numbers_return(first_num, second_num):
    result = first_num + second_num

    return result


def add_numbers_print(first_num, second_num):
    result = first_num + second_num

    print(result)
