names = ['Alice', 'Beth', 'Cecil', 'Dee-dee', 'Earl']
numbers = ['24', '56', '654', '76', '9876543']

print(names)

name = input('Please enter the name you want the number of: ')
name_index = names.index(name)
number = numbers[name_index]

print(f'Index is {name_index}')
print(f'Corresponding number is {number}')