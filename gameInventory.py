import operator
import csv

# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification


# Displays the inventory.
def display_inventory(inventory):
    items_number = 0
    print('Inventory:')
    for key in inventory:
        print(inventory[key], key)
        items_number += inventory[key]
    print('Total number of items:', items_number)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in range(len(dragon_loot)):
        if added_items[i] in inventory:
            inventory[added_items[i]] += 1
        else:
            inventory[added_items[i]] = 1


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    if order is None:
        items_number = 0
        for key in inventory:
            items_number += inventory[key]
        max_key_length = max(map(len, inventory))
        print('Inventory:')
        print('  count    \b', ' '*(max_key_length-9), '\bitem name')
        print('-' * (11 + max_key_length))
        for key in inventory:
            print(' ' * (6-len(str(inventory[key]))), inventory[key], ' ',
                  ' ' * (max_key_length - len(key)), key)
        print('-' * (11 + max_key_length))
        print('Total number of items:', items_number)
    else:
        items_number = 0
        for key in inventory:
            items_number += inventory[key]
        max_key_length = max(map(len, inventory))
        if order == 'count,desc':
            type_of_sort = True
        elif order == 'count,asc':
            type_of_sort = False
        inventory_sorted = sorted(inventory.items(), key=operator.itemgetter(1), reverse=type_of_sort)
        # Sorting(copying) of dict changing it to list of tuples.
        print('Inventory:')
        print('  count    \b', ' '*(max_key_length-9), '\bitem name')
        print('-' * (11 + max_key_length))
        for i in range(len(inventory_sorted)):
            print(' ' * (6-len(str(inventory_sorted[i][1]))), inventory_sorted[i][1], ' ',
                  ' ' * (max_key_length - len(inventory_sorted[i][0])), inventory_sorted[i][0])
        print('-' * (11 + max_key_length))
        print('Total number of items:', items_number)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open('import_inventory.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        new_items = []
        for row in reader:
            new_items.append(row)
    new_items_dict = {i: new_items[0].count(i) for i in new_items[0]}    # make dict from list
    items_number = 0
    for key in new_items_dict:   # count how many new items added
        items_number += new_items_dict[key]
    for i in range(items_number):   # add new items to inventory
        if new_items[0][i] in inventory:
            inventory[new_items[0][i]] += 1
        else:
            inventory[new_items[0][i]] = 1


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    with open('export_inventory.csv', mode='w') as csv_file:
        write_csv = csv.writer(csv_file, delimiter=',')
        inventory_list = []
        for key, value in inventory.items():
            inventory_list += [key]*value
        write_csv.writerow(inventory_list)


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inventory)

print('---> You killed a dragon! Heres a loot')
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)

print('---> Now we will see it in a proper way!')
print_table(inventory, order=None)
print_table(inventory, "count,desc")
print_table(inventory, "count,asc")

print('---> Now we will add sth from csv file')
import_inventory(inventory)
print_table(inventory, "count,desc")

print('---> Now we will export all inventory items to a file')
export_inventory(inventory, 'export_inventory.csv')
