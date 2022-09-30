# Imports #
from math import ceil, floor, sin, radians


# Functions #
def get_number():
    num = float(input('Enter a decimal number: '))

    return num


def ceiling_demo(num):
    result_ceil = ceil(num)

    return result_ceil


def ceiling_display(result_ceil):
    print(f'The ceiling is {result_ceil}')


def floor_demo(num):
    result_floor = floor(num)

    return result_floor


def floor_display(result_floor):
    print(f'The floor is {result_floor}')


def get_angle():
    angle = float(input('Enter an angle (in degrees): '))

    return angle


def sin_display(angle, angle_sin):
    print(f'The sin of {angle:.5f} is {angle_sin:.5f}')


# Main #
if __name__ == "__main__":
    # Get number from user
    number = get_number()

    # Ceil demo
    result_ceil = ceiling_demo(number)
    ceiling_display(result_ceil)

    # Floor demo
    result_floor = floor_demo(number)
    floor_display(result_floor)

    # Get angle from user
    angle = get_angle()

    # Convert angle to radians
    angle_rad = radians(angle)

    # Calculate the sin
    angle_sin = sin(angle_rad)

    # Dispaly sin
    sin_display(angle, angle_sin)
