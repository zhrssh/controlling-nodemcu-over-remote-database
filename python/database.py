import mysql.connector

# database
class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        try:
            # establish connection to database
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )

            # gets the cursor
            self.cursor = self.mydb.cursor(buffered=True)

        except mysql.connector.Error as err:
            print("Error: " + err.msg)

    def close(self):
        self.cursor.close()
        self.mydb.close()

    def get_cursor(self):
        return self.cursor

    def insert(self, table_name, columns_list, values_list):
        query = f"""INSERT INTO {table_name} ({', '.join(columns_list)}) VALUES ({', '.join(f"'{w}'" for w in values_list)});"""
        self.cursor.execute(query)
        self.mydb.commit()
        print(self.cursor.rowcount, "record(s) inserted.")

    def update(self, table_name, columns_list, values_list):
        query = f"DELETE FROM {table_name} WHERE {columns_list[0]} = '{values_list[0]}'"
        self.cursor.execute(query)

        query = f"""INSERT INTO {table_name} ({', '.join(columns_list)}) VALUES ({', '.join(f"'{w}'" for w in values_list)});"""
        self.cursor.execute(query)
        self.mydb.commit()
        print(self.cursor.rowcount, "record updated.")

    def delete(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition};"
        self.cursor.execute(query)
        self.mydb.commit()
        print(self.cursor.rowcount, "record(s) deleted.")

    def deleteall(self, table_name):
        query = f"DELETE FROM {table_name} WHERE 1 = 1;"
        self.cursor.execute(query)
        self.mydb.commit()
        print(self.cursor.rowcount, "record(s) deleted")

    def get_latest(self, table_name):
        query = f"SELECT * FROM {table_name} ORDER BY Timestamp DESC LIMIT 1;"
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        return row

    def get_last_five(self, table_name):
        query = f"SELECT * FROM {table_name} ORDER BY Timestamp DESC LIMIT 5;"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        return rows
