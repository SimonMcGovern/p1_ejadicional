def add_item(inventory, item_name, item_quantity):
   '''This module add an item to the inventory'''
   if item_name in inventory:
        print("The item is already on the inventory!!!!!!")
   else:
        inventory[item_name] = item_quantity

def delete_item(inventory, item_name):
    '''This module delete an item from the inventory'''
    if not item_name in inventory:
       print("The item isn't in the inventory!!!!!")
    else:
       del(inventory[item_name])
         
def show_inventory(inventory):
    '''This module show the items on the inventory'''
    if len(inventory) == 0:
        print("The inventory is empty!!!!!")
    else:
        print(f"Our items and their stock are: {inventory}")

if __name__ == "__main__":
    print(f"You are executing inventory on main {__name__}")
