import sqlite3
from PyQt5 import uic, QtWidgets


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('coffee.sqlite')
        self.cursor = self.conn.cursor()
        self.initUI()

    def initUI(self):
        uic.loadUi('main.ui', self)
        self.load_data()
        self.addButton.clicked.connect(self.openAddEditForm)

    def load_data(self):
        query = "SELECT * FROM coffee"
        result = self.cursor.execute(query).fetchall()
        for row in result:
            print(row)

    def openAddEditForm(self):
        self.addEditForm = AddEditForm(self)
        self.addEditForm.show()


class AddEditForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = CoffeeApp()
    window.show()
    app.exec_()
