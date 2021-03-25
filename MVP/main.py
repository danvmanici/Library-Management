# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Model.cartePersistenta import CartePersistenta
from Model.carteInregistrataInBiblioteca import CarteInregistrataInBiblioteca
from View.loginGUI import Ui_Login
from PyQt5 import QtCore,  QtWidgets


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
