# Fantasy Game Inventory

# inventory display
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
    print('')

displayInventory(stuff)

#list items add up to a dictionary
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0) #set default value to 0 for items non-exist before
        inventory[item]+=1

    return inventory
        
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

inv = addToInventory(stuff, dragonLoot)
displayInventory(inv)