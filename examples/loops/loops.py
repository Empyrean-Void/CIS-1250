# Basics of loops #

# While loop
x = 1
while x <= 5: # <- Conditional statement
    print(x)
    x += 1 # <- Counter to prevent infinite loop

name = ''
while not name:
    name = input('Please enter name: ')
print(f'\nHello {name}!')

do_another = 'y'
while do_another == 'y':
    print('\nDo some stuff\n')
    do_another = input('Do another (y/n): ')[0].lower()
print(f'\nThank you for using my program.')
