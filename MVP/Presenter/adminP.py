import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from PyQt5 import QtWidgets
from View.loginGUI import Ui_Login
from Model.utilizatorPersistenta import UtilizatorPersistenta
from Model.utilizator import Utilizator

class AdminP:
    def __init__(self,AdminGUI):
        self.view=AdminGUI
        self.utilizator=UtilizatorPersistenta("utilizatori.xml")

    def deconect(self):
        self.view.window = QtWidgets.QMainWindow()
        self.view.ui = Ui_Login()
        self.view.ui.setupUi(self.view.window)
        self.view.window.show()

    def creareBibliotecar(self):
        self.utilizator.createUtilizator(Utilizator(self.view.textCreateNume.toPlainText(),
                                                    self.view.textCreateParola.toPlainText(),"bibliotecar",
                                                    self.view.textCreateCont.toPlainText()))

    def vizualizareBibliotecari(self):
        self.view.textAfisareReadBibliotecar.setText(str(self.utilizator.readUtilizator("bibliotecar")))

    def updateBibliotecar(self):
        self.utilizator.updateUtilizator(Utilizator(self.view.textUpdateOldNume.toPlainText(),
                                                    self.view.textUpdateOldParola.toPlainText(),"bibliotecar",
                                                    self.view.textUpdateOldCont.toPlainText()),
                                        Utilizator(self.view.textUpdateNewNume.toPlainText(),
                                                   self.view.textUpdateNewParola.toPlainText(), "bibliotecar",
                                                   self.view.textUpdateNewCont.toPlainText()))
    def deleteBibliotecar(self):
        self.utilizator.deleteUtilizator(Utilizator(self.view.textStergereNume.toPlainText(),
                                                   self.view.textStergereParola.toPlainText(), "bibliotecar",
                                                   self.view.textStergereCont.toPlainText()))
