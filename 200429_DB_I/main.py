import db_manager as dbm

path = 'db/students.sqlite3'

db = dbm.DBManager(path)

if db.connect():
    table_name = 'studenti'
    # pokud tabulka neexistuje, vytvor novou
    if not db.does_table_exist(table_name):
        db.create_table(table_name)
        print('table created')

