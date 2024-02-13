import sqlite3

class DBUtil:

    def __init__(self):
        self.conn = sqlite3.connect('rinhabackend')

    def success(self):
        self.conn.commit()
        self.conn.close()

    def failure(self):
        self.conn.rollback()
        self.conn.close()