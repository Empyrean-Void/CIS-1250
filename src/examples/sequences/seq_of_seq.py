db = [['Alice', '24'], ['Beth', '56'], ['Cecil', '654'], ['Dee-dee', '76'], ['Earl', '9876543']]

# Display names
for item in db:
    print(item[0])

# Search for name and get number
name = input('\nPlease enter the name you want the number of: ')
for item in db:
    if item[0] == name:
        print(f'\nThe corresponding number is {item[1]}.')
