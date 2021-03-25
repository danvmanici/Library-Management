import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from PyQt5 import QtWidgets
from View.loginGUI import Ui_Login
from Model.cartePersistenta import CartePersistenta
from Model.utilizatorPersistenta import UtilizatorPersistenta
from Model.utilizator import Utilizator
from Model.carteInregistrataInBiblioteca import CarteInregistrataInBiblioteca

class BibliotecarP:
    def __init__(self,BibliotecarGUI):
        self.view=BibliotecarGUI
        self.carte = CartePersistenta("biblioteca.xml")
        self.utilizator = UtilizatorPersistenta("utilizatori.xml")

    def deconect(self):
        self.view.window = QtWidgets.QMainWindow()
        self.view.ui = Ui_Login()
        self.view.ui.setupUi(self.view.window)
        self.view.window.show()

    def viewCarti(self):
        self.view.textAfisareCarti.clear()
        self.view.textAfisareCarti.setText(str(self.carte.readCarti()))

    def gasesteCarte(self):
        self.view.textAfisareCarti.clear()
        self.view.textAfisareCarti.setText(str(self.carte.findCarte(self.view.textCautareCarte.toPlainText())))

    def viewStatistici(self):
        self.carte.viewStatistici(self.view.comboBoxStatistici.currentText())

    def filtrareCarti(self):
        self.view.textAfisareCarti.clear()
        self.view.textAfisareCarti.setText(str(self.carte.filterCarti(self.view.comboBoxFiltrare.currentText(),
                                                                 self.view.textFiltrareCarti.toPlainText() )))

    def creareAbonat(self):
        self.utilizator.createUtilizator(Utilizator(self.view.textAbonatCreateNume.toPlainText(),
                                                    self.view.textAbonatCreateParola.toPlainText(),"abonat",
                                                    self.view.textAbonatCreateCont.toPlainText()))

    def vizualizareAbonat(self):
        self.view.textAfisareReadAbonat.setText(str(self.utilizator.readUtilizator("abonat")))

    def updateAbonat(self):
        self.utilizator.updateUtilizator(Utilizator(self.view.textAbonatUpdateOldNume.toPlainText(),
                                                    self.view.textAbonatUpdateOldParola.toPlainText(),"abonat",
                                                    self.view.textAbonatUpdateOldCont.toPlainText()),
                                        Utilizator(self.view.textAbonatUpdateNewNume.toPlainText(),
                                                   self.view.textAbonatUpdateNewParola.toPlainText(), "abonat",
                                                   self.view.textAbonatUpdateNewCont.toPlainText()))
    def deleteAbonat(self):
        self.utilizator.deleteUtilizator(Utilizator(self.view.textAbonatDeleteNume.toPlainText(),
                                                   self.view.textAbonatDeleteParola.toPlainText(), "abonat",
                                                   self.view.textAbonatDeleteCont.toPlainText()))

    def creareCarte(self):
        self.carte.createCarte(CarteInregistrataInBiblioteca(
                                                    self.view.texTitlu.toPlainText(),
                                                    self.view.textAutor.toPlainText(),
                                                    self.view.textDomeniu.toPlainText(),
                                                    self.view.textEditura.toPlainText(),
                                                    self.view.textAnAparitie.toPlainText(),
                                                    self.view.comboBoxDisponibilitate.currentText(),
                                                    self.view.textNrInregistrare.toPlainText()
                                                    ))

    def vizualizareCarte(self):
        self.view.textAfisareReadCarte.setText(str(self.carte.readCarti()))

    def stergeCarte(self):
        self.carte.deleteCarte(CarteInregistrataInBiblioteca(
                                                    self.view.texTitlu.toPlainText(),
                                                    self.view.textAutor.toPlainText(),
                                                    self.view.textDomeniu.toPlainText(),
                                                    self.view.textEditura.toPlainText(),
                                                    self.view.textAnAparitie.toPlainText(),
                                                    self.view.comboBoxDisponibilitate.currentText(),
                                                    self.view.textNrInregistrare.toPlainText()
                                                    ))

    def imprumutareCarte(self):
        self.carte.borrowCarte(CarteInregistrataInBiblioteca(
                                                    self.view.texTitlu.toPlainText(),
                                                    self.view.textAutor.toPlainText(),
                                                    self.view.textDomeniu.toPlainText(),
                                                    self.view.textEditura.toPlainText(),
                                                    self.view.textAnAparitie.toPlainText(),
                                                    self.view.comboBoxDisponibilitate.currentText(),
                                                    self.view.textNrInregistrare.toPlainText()
                                                    ))

    def returnareCarte(self):
        self.carte.returnCarte(CarteInregistrataInBiblioteca(
                                                self.view.texTitlu.toPlainText(),
                                                self.view.textAutor.toPlainText(),
                                                self.view.textDomeniu.toPlainText(),
                                                self.view.textEditura.toPlainText(),
                                                self.view.textAnAparitie.toPlainText(),
                                                self.view.comboBoxDisponibilitate.currentText(),
                                                self.view.textNrInregistrare.toPlainText()
                                                 ))

    def actualizareCarte(self):
        self.carte.updateCarte(CarteInregistrataInBiblioteca(
                                                self.view.textUpdateTitluOld.toPlainText(),
                                                self.view.textUpdateAutorOld.toPlainText(),
                                                self.view.textUpdateDomeniuOld.toPlainText(),
                                                self.view.textUpdateEdituraOld.toPlainText(),
                                                self.view.textUpdateAnAparitieOld.toPlainText(),
                                                self.view.comboBoxUpdateDisponibilitateOld.currentText(),
                                                self.view.textUpdateNrInregistrareOld.toPlainText()
                                                 ),
                              CarteInregistrataInBiblioteca(
                                                self.view.textUpdateTitluNew.toPlainText(),
                                                self.view.textUpdateAutorNew.toPlainText(),
                                                self.view.textUpdateDomeniuNew.toPlainText(),
                                                self.view.textUpdateEdituraNew.toPlainText(),
                                                self.view.textUpdateAnAparitieNew.toPlainText(),
                                                self.view.comboBoxUpdateDisponibilitateNew.currentText(),
                                                self.view.textUpdateNrInregistrareNou.toPlainText()
                                                )
                                            )

    def rapoarte(self):
        if self.view.comboBoxSalvareRapoarte.currentText()=="csv":
            file=self.view.textSalvareRapoarteNumeFisier.toPlainText()
            self.carte.csvRaport(file)
        if self.view.comboBoxSalvareRapoarte.currentText()=="json":
            file=self.view.textSalvareRapoarteNumeFisier.toPlainText()
            self.carte.jsonRaport(file)
