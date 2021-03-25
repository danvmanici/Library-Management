import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from Model.utilizatorPersistenta import UtilizatorPersistenta
from PyQt5 import QtWidgets
from View.abonatGUI import  AbonatGui
from View.bibliotecarGUI import  Ui_Bibliotecar
from View.adminGUI import Ui_Admin

class LoginP:
    def __init__(self,view):
        self.view=view

    def login(self):
        nume=self.view.textName.toPlainText()
        parola=self.view.textPassword.toPlainText()
        utilizatori=UtilizatorPersistenta("utilizatori.xml")
        if(utilizatori.checkUtilizator(nume, parola)):
            utilizator=utilizatori.findUtilizator(nume)
            if(utilizator.rol=="abonat"):
                self.view.window = QtWidgets.QMainWindow()
                self.view.ui = AbonatGui()
                self.view.ui.setupUi(self.view.window)
                self.view.window.show()
            if (utilizator.rol == "bibliotecar"):
                self.view.window = QtWidgets.QMainWindow()
                self.view.ui = Ui_Bibliotecar()
                self.view.ui.setupUi(self.view.window)
                self.view.window.show()
            if (utilizator.rol == "admin"):
                self.view.window = QtWidgets.QMainWindow()
                self.view.ui = Ui_Admin()
                self.view.ui.setupUi(self.view.window)
                self.view.window.show()
