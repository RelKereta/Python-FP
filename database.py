import sqlite3

class productDB:
    def __init__(self):
        self.create_table()
    
    def create_table():
        # Connect to the SQLite database
        connection = sqlite3.connect("Products.db")
        cursor = connection.cursor()

        # Create table with specified columns
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id TEXT PRIMARY KEY,
                name TEXT,
                in_stock INTEGER
            )
        """)

        # Commit changes and close the connection
        connection.commit()
        connection.close()

    def fetch_products():
        # Connect to the SQLite database
        connection = sqlite3.connect("Products.db")
        cursor = connection.cursor()

        # Retrieve all rows from the Products table
        cursor.execute("SELECT * FROM Products")

        # Fetch all retrieved rows as a list of tuples
        Products = cursor.fetchall()

        # Close the connection
        connection.close()
        return Products

    def insert_product(id, name, in_stock):
        # Connect to the SQLite database
        connection = sqlite3.connect('Products.db')

        # Prepare SQL query to insert a new product
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Products VALUES (?, ?, ?)", (id, name, in_stock))

        # Commit changes and close the connection
        connection.commit()
        connection.close()

    def delete_product(id):
        connection = sqlite3.connect('Products.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Products WHERE id = ?', (id,))

        # Commit changes and close the connection
        connection.commit()
        connection.close()

    def update_product(new_name, new_stock, id):
        connection = sqlite3.connect('Products.db')
        cursor = connection.cursor()
        cursor.execute('UPDATE Products SET name = ?, in_stock = ? WHERE id = ?', (new_name, new_stock, id))

        # Commit changes and close the connection
        connection.commit()
        connection.close()

    def id_exists(id):
        connection = sqlite3.connect('Products.db')
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(*) FROM Products WHERE id = ?', (id,))
        result = cursor.fetchone()
        connection.close()
        return result[0] > 0