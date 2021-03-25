import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


from PyQt5 import QtCore, QtWidgets

class AbonatGui(object):
    def setupUi(self, Abonat):
        Abonat.setObjectName("Abonat")
        Abonat.resize(851, 203)
        self.centralwidget = QtWidgets.QWidget(Abonat)
        self.centralwidget.setObjectName("centralwidget")
        self.butonVizualizareCarti = QtWidgets.QPushButton(self.centralwidget)
        self.butonVizualizareCarti.setGeometry(QtCore.QRect(0, 0, 281, 51))
        self.butonVizualizareCarti.setObjectName("butonVizualizareCarti")
        self.butonFiltrareCarti = QtWidgets.QPushButton(self.centralwidget)
        self.butonFiltrareCarti.setGeometry(QtCore.QRect(0, 50, 151, 71))
        self.butonFiltrareCarti.setObjectName("butonFiltrareCarti")
        self.comboBoxFiltrare = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxFiltrare.setGeometry(QtCore.QRect(150, 50, 131, 41))
        self.comboBoxFiltrare.setObjectName("comboBoxFiltrare")
        self.comboBoxFiltrare.addItem("")
        self.comboBoxFiltrare.addItem("")
        self.comboBoxFiltrare.addItem("")
        self.comboBoxFiltrare.addItem("")
        self.butonCautareCarte = QtWidgets.QPushButton(self.centralwidget)
        self.butonCautareCarte.setGeometry(QtCore.QRect(0, 160, 151, 41))
        self.butonCautareCarte.setObjectName("butonCautareCarte")
        self.textCautare = QtWidgets.QTextEdit(self.centralwidget)
        self.textCautare.setGeometry(QtCore.QRect(150, 160, 131, 41))
        self.textCautare.setObjectName("textCautare")
        self.butonStatistici = QtWidgets.QPushButton(self.centralwidget)
        self.butonStatistici.setGeometry(QtCore.QRect(0, 120, 151, 41))
        self.butonStatistici.setObjectName("butonStatistici")
        self.comboBoxStatistici = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxStatistici.setGeometry(QtCore.QRect(150, 120, 131, 41))
        self.comboBoxStatistici.setObjectName("comboBoxStatistici")
        self.comboBoxStatistici.addItem("")
        self.comboBoxStatistici.addItem("")
        self.comboBoxStatistici.addItem("")
        self.comboBoxStatistici.addItem("")
        self.butonDeconectare = QtWidgets.QPushButton(self.centralwidget)
        self.butonDeconectare.setGeometry(QtCore.QRect(690, 60, 151, 81))
        self.butonDeconectare.setObjectName("butonDeconectare")
        self.textAfisare = QtWidgets.QTextEdit(self.centralwidget)
        self.textAfisare.setGeometry(QtCore.QRect(280, 0, 391, 201))
        self.textAfisare.setObjectName("textAfisare")
        self.textFiltrare = QtWidgets.QTextEdit(self.centralwidget)
        self.textFiltrare.setGeometry(QtCore.QRect(150, 90, 131, 31))
        self.textFiltrare.setObjectName("textFiltrare")
        Abonat.setCentralWidget(self.centralwidget)

        self.retranslateUi(Abonat)
        QtCore.QMetaObject.connectSlotsByName(Abonat)

    def retranslateUi(self, Abonat):
        _translate = QtCore.QCoreApplication.translate
        Abonat.setWindowTitle(_translate("Abonat", "MainWindow"))
        self.butonVizualizareCarti.setText(_translate("Abonat", "Vizualizare Carti"))
        self.butonFiltrareCarti.setText(_translate("Abonat", "Filtrare Carti"))
        self.comboBoxFiltrare.setItemText(0, _translate("Abonat", "domeniu"))
        self.comboBoxFiltrare.setItemText(1, _translate("Abonat", "disponibilitate"))
        self.comboBoxFiltrare.setItemText(2, _translate("Abonat", "editura"))
        self.comboBoxFiltrare.setItemText(3, _translate("Abonat", "autor"))
        self.butonCautareCarte.setText(_translate("Abonat", "Cautare Carte"))
        self.butonStatistici.setText(_translate("Abonat", "Statistici"))
        self.comboBoxStatistici.setItemText(0, _translate("Abonat", "domeniu"))
        self.comboBoxStatistici.setItemText(1, _translate("Abonat", "disponibilitate"))
        self.comboBoxStatistici.setItemText(2, _translate("Abonat", "editura"))
        self.comboBoxStatistici.setItemText(3, _translate("Abonat", "autor"))
        self.butonDeconectare.setText(_translate("Abonat", "Deconectare"))

        def clickDeconectare():
            from Presenter.abonatP import AbonatP
            p = AbonatP(self)
            p.deconect()
            Abonat.close()

        self.butonDeconectare.clicked.connect(clickDeconectare)

        def clickAfisareCarti():
            from Presenter.abonatP import AbonatP
            p = AbonatP(self)
            p.viewCarti()

        self.butonVizualizareCarti.clicked.connect(clickAfisareCarti)

        def clickCautare():
            from Presenter.abonatP import AbonatP
            p = AbonatP(self)
            p.gasesteCarte()

        self.butonCautareCarte.clicked.connect(clickCautare)

        def clickStatistici():
            from Presenter.abonatP import AbonatP
            p = AbonatP(self)
            p.viewStatistici()

        self.butonStatistici.clicked.connect(clickStatistici)

        def clickFiltrare():
            from Presenter.abonatP import AbonatP
            p = AbonatP(self)
            p.filtrareCarti()

        self.butonFiltrareCarti.clicked.connect(clickFiltrare)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Abonat = QtWidgets.QMainWindow()
    ui = AbonatGui()
    ui.setupUi(Abonat)
    Abonat.show()
    sys.exit(app.exec_())
