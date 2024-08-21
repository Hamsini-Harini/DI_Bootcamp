from menu_manager import MenuManager  
from menu import MenuItem 

def show_user_menu() -> None:
    """
    Displays the program menu and prompts the user for an action.
    Depending on the user's choice, it calls the appropriate function.
    """
    while True:
        print("\n--- Menu ---")
        print("V: View an Item")
        print("A: Add an Item")
        print("D: Delete an Item")
        print("U: Update an Item")
        print("S: Show the Restaurant Menu")
        print("E: Exit")

        user_input = input("Choose an option: ").strip().upper()

        if user_input == "V":
            view_item()
        elif user_input == "A":
            add_item_to_menu()
        elif user_input == "D":
            remove_item_from_menu()
        elif user_input == "U":
            update_item_from_menu()
        elif user_input == "S":
            show_restaurant_menu()
        elif user_input == "E":
            print("Goodbye! Here's the current restaurant menu:")
            show_restaurant_menu()
            break
        else:
            print("Invalid option, please try again.")

def view_item() -> None:
    """
    Prompts the user for the name of the item to view and displays its details if found.
    """
    name = input("Enter the name of the item you want to view: ").strip()
    item = MenuManager.get_by_name(name)

    if item:
        print(f"Item found: {item.name} - Price: ${item.price}")
    else:
        print(f"Item '{name}' not found.")

def add_item_to_menu() -> None:
    """
    Asks the user to input the name and price of the item, then creates a MenuItem
    and saves it to the database.
    """
    name = input("Enter the item name: ").strip()
    try:
        price = int(input("Enter the item price: ").strip())
    except ValueError:
        print("Invalid price. Please enter an integer.")
        return

    item = MenuItem(name, price)
    try:
        item.save()  # Calling the save method to insert the item into the database
        print(f"Item '{name}' was added successfully.")
    except Exception as e:
        print(f"Error adding item: {e}")

def remove_item_from_menu() -> None:
    """
    Asks the user for the name of the item to remove, retrieves the item by name, and deletes it.
    """
    name = input("Enter the name of the item you want to remove: ").strip()
    item = MenuManager.get_by_name(name)

    if item:
        try:
            item.delete(item_id=item.id)  # Assuming the item has an id attribute
            print(f"Item '{name}' was deleted successfully.")
        except Exception as e:
            print(f"Error deleting item: {e}")
    else:
        print(f"Item '{name}' not found.")

def update_item_from_menu() -> None:
    """
    Asks the user for the item name they want to update, and the new name and price.
    Updates the item in the database if it exists.
    """
    name = input("Enter the name of the item you want to update: ").strip()
    item = MenuManager.get_by_name(name)

    if item:
        new_name = input("Enter the new name: ").strip()
        try:
            new_price = int(input("Enter the new price: ").strip())
        except ValueError:
            print("Invalid price. Please enter an integer.")
            return

        try:
            item.update(item_id=item.id, new_name=new_name, new_price=new_price)
            print(f"Item '{name}' was updated successfully.")
        except Exception as e:
            print(f"Error updating item: {e}")
    else:
        print(f"Item '{name}' not found.")

def show_restaurant_menu() -> None:
    """
    Displays all items currently in the Menu_Items table.
    """
    items = MenuManager.all_items()
    if items:
        print("\n--- Restaurant Menu ---")
        for item in items:
            print(f"{item.name}: ${item.price}")
    else:
        print("The menu is empty.")


if __name__ == "__main__":
    show_user_menu()
