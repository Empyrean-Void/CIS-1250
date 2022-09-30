from math import pi


# TODO 1: Define the constants as instructed in the writeup and assign them
#         the correct values.
TABLE_TOP_LENGTH = 63.0
TABLE_TOP_WIDTH = 23.6
TABLE_TOP_HEIGHT = 1.5
TABLE_LEG_BASE_RADIUS = 0.8
TABLE_LEG_HEIGHT = 29.5

# TODO 2: Implement the `box_vol` and `cylinder_vol` functions.all


def box_vol(length, width, height):
    volume = length * width * height

    return volume


def cylinder_vol(base_radius, height):
    area = pi * (base_radius ** 2)
    volume = area * height

    return volume

# TODO 3: Implement the `table_vol` function.


def table_vol(tt_length, tt_width, tt_height, leg_base_rad, leg_height):
    tt_vol = box_vol(tt_length, tt_width, tt_height)
    leg_vol = 4 * cylinder_vol(leg_base_rad, leg_height)
    table_volume = tt_vol + leg_vol

    return table_volume


# TODO 4: Define the `table_volume` variable and assign it the value as
#         instructed in the writeup.
table_volume = table_vol(TABLE_TOP_LENGTH, TABLE_TOP_WIDTH, TABLE_TOP_HEIGHT, TABLE_LEG_BASE_RADIUS, TABLE_LEG_HEIGHT)

if __name__ == '__main__':
    print(table_volume)
    a = 63 * 23.6 * 1.5 + 4 * pi * 0.8**2 * 29.5
    assert round(table_volume, 2) == round(a, 2)
