# Display header
print(f'\nWelcome to Pyramid Calculator\nVersion 1.0\n')

# Get input from user
base = float(input('Enter pyramid base (in meters): '))
height = float(input('Enter pyramid height(in meters): '))

# Get volume of pyramid
volume = (base **2 * height)/3

# Display results
print(f'\nPyramid volume is {volume:.2f} cubic meters')

# Display exit message
print(f'\nExiting...')
