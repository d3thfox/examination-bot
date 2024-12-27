import sqlite3



class Database:
    def __init__(self,path : str):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact INTEGER,
            complaint TEXT)
            ''')
    def insert_complaint(self,data : dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
            INSERT INTO complaints (name, contact, complaint)
            VALUES (?, ?, ?)''',
                         (data['name'], data['contact'], data['complaint'])


            )
