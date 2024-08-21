import psycopg2
from psycopg2 import sql

class MenuItem:
    """ Represents an item in a menu with a name and price."""
    def __init__ (self, name:str, price: int | float)  -> None:
        self.name = name
        self.price = price 

    def __repr__(self) -> str: #Returns a string representation of the MenuItem object.
        return f"MenuItem(name='{self.name}', price={self.price})"
    
    #Now, we’re going to add methods to the MenuItem class that allow users to interact with the Menu_Items table in PostgreSQL. 
    # Remember to conenct Python to SQL we will use the psycopg2 library.
    # And yes we will write SQL queries inside Python!

    def save(self) -> None:
        """ Saves the MenuItem to the database.
        Inserts a new row into the Menu_Items table with the current name and price."""

        try:
            # Establish connection to the database
            connection = psycopg2.connect(
                dbname="menu_db", user="postgres", password="koliko22", host="localhost", port="5432"
            )
            cursor = connection.cursor()
            
            # SQL query to insert a new item
            insert_query = """
                INSERT INTO Menu_Items (item_name, item_price)
                VALUES (%s, %s);
            """
            # Execute query with current item data
            cursor.execute(insert_query, (self.name, self.price))
            
            # Commit the changes to the database
            connection.commit()

            print(f"Item '{self.name}' saved to the database successfully.")
        
        except Exception as error:
            print(f"Error saving item: {error}")

        finally:
            # Close the cursor and connection materless of try and except, this is a security thing
            cursor.close()
            connection.close()

    def delete(self, item_id: int) -> None:
        """ Deletes the MenuItem from the database based on its item_id"""
        try:
            # Establish connection to the database
            connection = psycopg2.connect(
                dbname="menu_db", user="postgres", password="koliko22", host="localhost", port="5432"
            )
            cursor = connection.cursor()
            
            # SQL query to delete an item by its ID
            delete_query = """
                DELETE FROM Menu_Items WHERE item_id = %s;
            """
            # Execute the query with the provided item_id
            cursor.execute(delete_query, (item_id,))
            
            # Commit the deletion
            connection.commit()

            print(f"Item with ID '{item_id}' deleted from the database.")
        
        except Exception as error:
            print(f"Error deleting item: {error}")
        
        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def update(self, item_id: int, new_name: str, new_price: int) -> None:
        connection = None
        cursor = None
        try:
            # Establish connection to the database
            connection = psycopg2.connect(
                dbname="menu_db", user="postgres", password="koliko22", host="localhost", port="5432"
            )
            cursor = connection.cursor()

            # SQL query to update the item
            update_query = """
                UPDATE Menu_Items
                SET item_name = %s, item_price = %s
                WHERE item_id = %s;
            """
            # Execute the update query with the provided values
            cursor.execute(update_query, (new_name, new_price, item_id))

            # Commit the update
            connection.commit()

            print(f"Item with ID '{item_id}' updated in the database to name '{new_name}' and price {new_price}.")
        
        except Exception as error:
            print(f"Error updating item: {error}")
        
        finally:
            # Close the cursor and connection if they exist
            if cursor:
                cursor.close()
            if connection:
                connection.close()
