import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(
            r"C:/Users/Vira_Bakhovska/Desktop/python_basics/repository/aqa_with_python/automation_testing_with_python"
            + r"/become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "Select sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products set quantity = {qnt} where id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        quary = f"SELECT quantity FROM products where id = {product_id}"
        self.cursor.execute(quary)
        record = self.cursor.fetchall()
        return record

    def select_product_qnt(self):
        quary = "SELECT quantity FROM products"
        self.cursor.execute(quary)
        record = self.cursor.fetchall()
        return record

    def select_postal_codes(self):
        quary = "SELECT postalCode FROM customers"
        self.cursor.execute(quary)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                        products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id "
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_data_into_non_existent_table(self):
        query = f"INSERT INTO non_existent (discount_id, discount_name, castomer_id, discount_value) VALUES (1, '15%  discount', 1, 15 )"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_with_invalid_encoding(self):
        encoded_data = "é".encode("iso-8859-1")
        query = "INSERT OR REPLACE INTO products (id, name, description, quantity) VALUES (?, ?, ?, ?)"
        params = (999, encoded_data, "string in ISO-8859-1 encoding", 0)
        self.cursor.execute(query, params)
        self.connection.commit()

    def select_product_name_by_id(self, product_id):
        query = f"SELECT name FROM products where id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        return record

    def get_data_consistency(self):
        query = "SELECT product_id FROM orders EXCEPT SELECT id FROM products \
                 UNION ALL \
                 SELECT customer_id FROM orders EXCEPT SELECT id FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
