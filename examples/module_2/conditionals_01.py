def get_numbers():
    num_1 = float(input('Num 1: '))
    num_2 = float(input('Num 2: '))
    num_3 = float(input('Num 3: ')) 
    
    return num_1, num_2, num_3

results = get_numbers()
val_1, val_2, val_3 = results

print(results)
