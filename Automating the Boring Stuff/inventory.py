stuff = {'rope': 1, 'torch': 6, 'gold coin': 42,
        'dagger': 1, 'arrow': 12}

def displayInventory(dict1):
    total_num_items = 0
    print('Inventory: ')
    for key, value in dict1.items():
        print(str(value) + ' ' + str(key))
        total_num_items += value
    print('Total number of values: ' + str(total_num_items) + '\n')

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory: 
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(stuff, dragonLoot)

displayInventory(stuff)


