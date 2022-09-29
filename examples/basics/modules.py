# Imports #

from math import ceil
from math import floor
from math import sin
from math import radians

# Main #

num = float(input('Enter a decimal number: '))

result_ceil = ceil(num)

print(f'The ceiling is {result_ceil}')

result_floor = floor(num)

print(f'The floor is {result_floor}')

# Get angle in degrees
angle = float(input('Enter an angle: '))

angle_rad = radians(angle)

# Calculate the sin
sin_of_angle = sin(angle_rad)

print(f'The sin of the angle is {sin_of_angle:.5f}')
