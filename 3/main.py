import sqlite3
from PyQt5 import uic

class CoffeeApp:
    def __init__(self):
        self.conn = sqlite3.connect('coffee.sqlite')
        self.cursor = self.conn.cursor()
        self.initUI()

    def initUI(self):
        self.ui = uic.loadUi('main.ui')
        self.ui.show()
        self.load_data()

    def load_data(self):
        query = "SELECT * FROM coffee"
        result = self.cursor.execute(query).fetchall()
        for row in result:
            print(row)

if __name__ == "__main__":
    app = CoffeeApp()
