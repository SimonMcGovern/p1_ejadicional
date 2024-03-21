import inventory


def main():
    products = {}



    menu_controller = int(input(" 1) Agregar un producto al inventario. \n 2) Eliminar un producto del inventario. \n 3) Visualizar el inventario. \n 4) Salir del programa.\n"))



    while True:



        match menu_controller:

            case 1:
                new_item = input("Insert the new item's name: ")
                new_item_quantity = int(input("Insert the item's stock: "))
                while new_item_quantity <= 0:
                    print("The stock can't be lower or equal than 0!!!!!")
                    new_item_quantity = int(input("Insert the item's stock: "))
                inventory.add_item(products, new_item, new_item_quantity)
            case 2:
                del_item = input("Insert the item's name you want to delete: ")
                inventory.delete_item(products, del_item)
            case 3:
                inventory.show_inventory(products)
            case 4:
                print("Thanks for use our program :)")
                break
            case _:
                print("Invalid entry. Please insert a valid value!")
        menu_controller = int(input(" 1) Agregar un producto al inventario. \n 2) Eliminar un producto del inventario. \n 3) Visualizar el inventario. \n 4) Salir del programa.\n"))


main()    
