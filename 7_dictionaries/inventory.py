# Say you’re creating a medieval fantasy video game. The data structure to model the player’s inventory is a dictionary whose ks are strings describing the item in the inventory and whose values are integers detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has one rope, six torches, 42 gold coins, and so on.

#Write a function named display_inventory() that would take any possible “inventory” and display it like the following:

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for k, v in inventory.items():
        total_items+= v
        print(k + " " + str(v))
        
    print("Total number of items:" + str(total_items))
    

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 0)
            inventory[item] += 1


add_to_inventory(inv, dragon_loot)
display_inventory(inv)

