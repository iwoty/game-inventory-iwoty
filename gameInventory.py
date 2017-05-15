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
    pass


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inventory)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
