import sqlite3


class DBManager:
    def __init__(self, path):
        self.path = path
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.path)
            print('connected to DB')
            return True
        except:
            print('not connected')
            return False

    def create_table(self, table_name):
        if table_name == 'studenti':
            create_query = f"""CREATE TABLE {table_name} (
                'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'kurz' STRING,
                'jmeno' STRING,
                'prijmeni' STRING,
                'vek' INTEGER,
                'adresa' STRING,
                'znalost' STRING
            );"""
        elif table_name == 'ucastnici':
            create_query = f"""CREATE TABLE {table_name} (
                  'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                  'kurz' STRING,
                  'jmeno' STRING,
                  'prijmeni' STRING,
                  'vek' INTEGER,
                  'adresa' STRING,
                  'konicky' STRING
              );"""

        self.conn.execute(create_query)

    def does_table_exist(self, table_name):
        return self.conn.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'").fetchone()



