import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(
            r"C:/Users/Vira_Bakhovska/Desktop/python_basics/repository/automation_testing_with_python"
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
