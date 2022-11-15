class InventoryItem:
    Id = 0
    serial_number = ""
    location = ""
    description = ""
    condition = ""
    date_in = ""
    date_out = ""
    value = None


def get_inventory_item_from_user():
    item = InventoryItem()
    item.serial_number = input('Please enter serial number: ')
    item.location = input("Please enter location: ")
    item.description = input("Please enter description: ")
    item.condition = input("Please enter condition: ")
    item.date_in = input("Please enter date in: ")
    item.date_out = input("Please enter date out: ")
    item.value = float(input("Please enter starting value: "))
    return item


def get_items_from_user(items):
    doanother = 'y'
    while doanother == 'y':
        item = get_inventory_item_from_user()
        item.Id = len(items)+1
        items.append(item)
        doanother = input("Do you want to add another item(y/n)? ")[0].lower()


def display_item(item):
    print(f"Serial Number: {item.serial_number}")
    print(f"Location: {item.location}")
    print(f"Description: {item.description}")
    print(f"Condition: {item.condition}")
    print(f"Date In: {item.date_in}")
    print(f"Date Out: {item.date_out}")
    print(f"Value: {item.value}")
    print()


def display_item_as_row(item):
    print(f"{item.Id:5} {item.serial_number:20} {item.location:20} {item.description:20}")


def display_items(items):
    print(f"{'Id':5} {'serial_number':20} {'location':20} {'description':20}")
    for item in items:
        display_item_as_row(item)


def save_items_to_file(items):
    file_name = input("PLease enter a file name: ")
    f = open(file_name, 'w')
    for item in items:
        f.write(f"{item.Id}\t")
        f.write(f"{item.serial_number}\t")
        f.write(f"{item.location}\t")
        f.write(f"{item.description}\t")
        f.write(f"{item.condition}\t")
        f.write(f"{item.date_in}\t")
        f.write(f"{item.date_out}\t")
        f.write(f"{item.value}\n")
    f.close()


def read_items_from_file():
    file_name = input("PLease enter a file name: ")
    f = open(file_name, 'r')
    items = []
    while True:
        line = f.readline()
        if not line:
            break

        elements = line.split('\t')
        item = InventoryItem()
        item.Id = int(elements[0])
        item.serial_number = elements[1]
        item.location = elements[2]
        item.description = elements[3]
        item.condition = elements[4]
        item.date_in = elements[5]
        item.date_out = elements[6]
        item.value = float(elements[7])
        items.append(item)
    f.close()
    return items


if __name__ == "__main__":
    items = []
    while True:
        display_items(items)
        choice = input("(A)dd, (D)isplay, (S)ave, (O)pen, (Q)uit: ")[0].upper()
        if choice == 'A':
            get_items_from_user(items)
        if choice == 'D':
            item_id = int(input("please enter Id: "))
            for item in items:
                if item.Id == item_id:
                    display_item(item)
        elif choice == 'S':
            save_items_to_file(items)
        elif choice == 'O':
            items = read_items_from_file()
        elif choice == 'Q':
            break
        else:
            print("I did not understand that.")
