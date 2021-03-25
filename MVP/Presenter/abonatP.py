import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from PyQt5 import QtWidgets
from View.loginGUI import Ui_Login
from Model.cartePersistenta import CartePersistenta

class AbonatP:
    def __init__(self,AbonatGui):
        self.view=AbonatGui
        self.carte=CartePersistenta("biblioteca.xml")

    def deconect(self):
        self.view.window = QtWidgets.QMainWindow()
        self.view.ui = Ui_Login()
        self.view.ui.setupUi(self.view.window)
        self.view.window.show()

    def viewCarti(self):
        self.view.textAfisare.clear()
        self.view.textAfisare.setText(str(self.carte.readCarti()))

    def gasesteCarte(self):
        self.view.textAfisare.clear()
        self.view.textAfisare.setText(str(self.carte.findCarte(self.view.textCautare.toPlainText())))

    def viewStatistici(self):
        self.carte.viewStatistici(self.view.comboBoxStatistici.currentText())

    def filtrareCarti(self):
        self.view.textAfisare.clear()
        self.view.textAfisare.setText(str(self.carte.filterCarti(self.view.comboBoxFiltrare.currentText(),
                                                                 self.view.textFiltrare.toPlainText() )))

