# Imports #
from math import sin, cos, atan2, sqrt, radians

# Constants #
RADIUS = 6371  # <- Radius of Earth
KM_TO_MILE = 0.621371  # <- Convert Kilometers to Miles

# Functions #


def header():
    print('\nDistance Calculator\nVersion: 1.0')

# Get location from user


def get_location():
    lat = float(input('Enter latitude in decimal form: '))
    long = float(input('Enter longitude in decimal form: '))
    location = lat, long  # <- Store input as tuple

    return location

# Calculate distance using haversine formula


def haversine(origin, destination):
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
# Enable multiple claculations


def calc_agian():
    print('\n# Please enter starting point information #\n')
    origin = get_location()

    print('\n# Please enter destination point information #\n')
    destination = get_location()

    distance = haversine(origin, destination)
    distance_mile = distance * KM_TO_MILE

    print('\nThe distance to destination is:\n\n{distance:.2f} km\n{distance_mile:.2f} miles')

# Main #


# Display welcome message
header()

# Get location input from user
print('\n# Please enter starting point information #\n')
origin = get_location()

print('\n# Please enter destination point information #\n')
destination = get_location()

# Calculate distance
distance = haversine(origin, destination)
distance_mile = distance * KM_TO_MILE

print('\nThe distance to destination is:\n\n{distance:.2f} km\n{distance_mile:.2f} miles\n')

# Loop program
run_again = ''

while run_again != 'n':
    # <- Make input case insensitive and enable default option
    run_again = input('Run calculator again (y/n): ').lower() or 'y'

    if run_again == 'y':
        calc_agian()

    elif run_again == 'n':
        print('\nExiting...')
        break

    else:
        print(f'{run_again} is not a valid option!')
