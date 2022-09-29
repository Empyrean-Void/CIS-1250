auth_names = ['Rob', 'Bill', 'John', 'Linus']

while True:
    name = input('Enter you name: ').title()

    if name in auth_names:
        print('Access granted')
        break
    else:
        print('Access denied')

    do_another = input('Try again (Y/n)? ') or 'y'

    if do_another != 'y':
        break
