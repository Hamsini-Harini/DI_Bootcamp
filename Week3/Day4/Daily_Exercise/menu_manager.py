import psycopg2
from menu import MenuItem  # Import the MenuItem class

class MenuManager:
    """
    Manages menu items in the database with methods to retrieve items by name and get all items.
    """

    @classmethod
    def get_by_name(cls, name: str) -> MenuItem | None:
        """
        Retrieves a single item from the Menu_Items table by its name.
        If the item is not found, returns None
        """
        try:
            # Establish connection to the database
            connection = psycopg2.connect(
                dbname="menu_db", user="postgres", password="koliko22", host="localhost", port="5432"
            )
            cursor = connection.cursor()

            # SQL query to fetch the item by name
            select_query = """
                SELECT item_name, item_price 
                FROM Menu_Items 
                WHERE item_name = %s;
            """
            cursor.execute(select_query, (name,))
            result = cursor.fetchone()  # Fetch the first matching record

            if result:
                # If an item is found, create a MenuItem object and return it
                item_name, item_price = result
                return MenuItem(item_name, item_price)
            else:
                return None

        except Exception as error:
            print(f"Error retrieving item by name: {error}")
            return None

        finally:
            cursor.close()
            connection.close()

    @classmethod
    def all_items(cls) -> list[MenuItem]:
        """
        Retrieves all items from the Menu_Items table.
        :return: A list of MenuItem objects.
        """
        items = []
        try:
            # Establish connection to the database
            connection = psycopg2.connect(
                dbname="menu_db", user="postgres", password="koliko22", host="localhost", port="5432"
            )
            cursor = connection.cursor()

            # SQL query to fetch all items
            select_query = """
                SELECT item_name, item_price 
                FROM Menu_Items;
            """
            cursor.execute(select_query)
            results = cursor.fetchall()  # Fetch all records

            # Loop through each record and create MenuItem objects
            for result in results:
                item_name, item_price = result
                items.append(MenuItem(item_name, item_price))

        except Exception as error:
            print(f"Error retrieving all items: {error}")

        finally:
            cursor.close()
            connection.close()

        return items


if __name__ == '__main__':
    # Test the functions
    
    item = MenuItem('Burger', 35)
    item.save()
    print(item)
    item.delete(1)
    print(item)
    item.update(1,'Veggie Burger', 37)
    print(item)
    item2 = MenuManager.get_by_name('Beef Stew')
    print(item)
    items = MenuManager.all_items()
    print(item)