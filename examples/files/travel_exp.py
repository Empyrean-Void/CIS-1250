# travel_exp.py
# Programmer: Jonah Shortz
# Date: Sep 29 2022
# Get travel costs for police department

# Read file
file = open('travel_exp.csv', 'r')
header_row = file.readline()

while True:
    line = file.readline()

    if not line:
        break

    elements = line.split(',')
    print(elements[9])

file.close()
# Search for police travel

# Total travel
