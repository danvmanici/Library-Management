import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from PyQt5 import QtCore, QtWidgets


class Ui_Bibliotecar(object):
    def setupUi(self, Bibliotecar):
        Bibliotecar.setObjectName("Bibliotecar")
        Bibliotecar.resize(1024, 943)
        self.centralwidget = QtWidgets.QWidget(Bibliotecar)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonCreateCarte = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCreateCarte.setGeometry(QtCore.QRect(0, 220, 151, 71))
        self.buttonCreateCarte.setObjectName("buttonCreateCarte")
        self.buttonReadCarte = QtWidgets.QPushButton(self.centralwidget)
        self.buttonReadCarte.setGeometry(QtCore.QRect(0, 350, 151, 71))
        self.buttonReadCarte.setObjectName("buttonReadCarte")
        self.buttonUpdateCarte = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUpdateCarte.setGeometry(QtCore.QRect(0, 420, 151, 121))
        self.buttonUpdateCarte.setObjectName("buttonUpdateCarte")
        self.buttonDeleteCarte = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDeleteCarte.setGeometry(QtCore.QRect(0, 290, 151, 61))
        self.buttonDeleteCarte.setObjectName("buttonDeleteCarte")
        self.texTitlu = QtWidgets.QTextEdit(self.centralwidget)
        self.texTitlu.setGeometry(QtCore.QRect(150, 260, 111, 31))
        self.texTitlu.setObjectName("texTitlu")
        self.textAutor = QtWidgets.QTextEdit(self.centralwidget)
        self.textAutor.setGeometry(QtCore.QRect(260, 260, 104, 31))
        self.textAutor.setObjectName("textAutor")
        self.textEditura = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditura.setGeometry(QtCore.QRect(470, 260, 104, 31))
        self.textEditura.setObjectName("textEditura")
        self.textAnAparitie = QtWidgets.QTextEdit(self.centralwidget)
        self.textAnAparitie.setGeometry(QtCore.QRect(570, 260, 104, 31))
        self.textAnAparitie.setObjectName("textAnAparitie")
        self.textDomeniu = QtWidgets.QTextEdit(self.centralwidget)
        self.textDomeniu.setGeometry(QtCore.QRect(360, 260, 111, 31))
        self.textDomeniu.setObjectName("textDomeniu")
        self.buttonImprumutareCarte = QtWidgets.QPushButton(self.centralwidget)
        self.buttonImprumutareCarte.setGeometry(QtCore.QRect(870, 230, 151, 101))
        self.buttonImprumutareCarte.setObjectName("buttonImprumutareCarte")
        self.buttonReturnareCarte = QtWidgets.QPushButton(self.centralwidget)
        self.buttonReturnareCarte.setGeometry(QtCore.QRect(870, 330, 151, 91))
        self.buttonReturnareCarte.setObjectName("buttonReturnareCarte")
        self.buttonSalvareRapoarte = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSalvareRapoarte.setGeometry(QtCore.QRect(310, 560, 561, 51))
        self.buttonSalvareRapoarte.setObjectName("buttonSalvareRapoarte")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 230, 111, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 230, 101, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 230, 101, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 230, 101, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 230, 111, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.butonVizualizareCarti = QtWidgets.QPushButton(self.centralwidget)
        self.butonVizualizareCarti.setGeometry(QtCore.QRect(0, 0, 281, 51))
        self.butonVizualizareCarti.setObjectName("butonVizualizareCarti")
        self.comboBoxFiltrare = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxFiltrare.setGeometry(QtCore.QRect(150, 50, 131, 41))
        self.comboBoxFiltrare.setObjectName("comboBoxFiltrare")
        self.comboBoxFiltrare.addItem("")
        self.comboBoxFiltrare.addItem("")
        self.comboBoxFiltrare.addItem("")
        self.comboBoxFiltrare.addItem("")
        self.textCautareCarte = QtWidgets.QTextEdit(self.centralwidget)
        self.textCautareCarte.setGeometry(QtCore.QRect(150, 160, 131, 41))
        self.textCautareCarte.setObjectName("textCautareCarte")
        self.butonStatistici = QtWidgets.QPushButton(self.centralwidget)
        self.butonStatistici.setGeometry(QtCore.QRect(0, 120, 151, 41))
        self.butonStatistici.setObjectName("butonStatistici")
        self.textFiltrareCarti = QtWidgets.QTextEdit(self.centralwidget)
        self.textFiltrareCarti.setGeometry(QtCore.QRect(150, 90, 131, 31))
        self.textFiltrareCarti.setObjectName("textFiltrareCarti")
        self.butonCautareCarte = QtWidgets.QPushButton(self.centralwidget)
        self.butonCautareCarte.setGeometry(QtCore.QRect(0, 160, 151, 41))
        self.butonCautareCarte.setObjectName("butonCautareCarte")
        self.butonFiltrareCarti = QtWidgets.QPushButton(self.centralwidget)
        self.butonFiltrareCarti.setGeometry(QtCore.QRect(0, 50, 151, 71))
        self.butonFiltrareCarti.setObjectName("butonFiltrareCarti")
        self.comboBoxStatistici = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxStatistici.setGeometry(QtCore.QRect(150, 120, 131, 41))
        self.comboBoxStatistici.setObjectName("comboBoxStatistici")
        self.comboBoxStatistici.addItem("")
        self.comboBoxStatistici.addItem("")
        self.comboBoxStatistici.addItem("")
        self.comboBoxStatistici.addItem("")
        self.textAfisareCarti = QtWidgets.QTextEdit(self.centralwidget)
        self.textAfisareCarti.setGeometry(QtCore.QRect(280, 0, 741, 201))
        self.textAfisareCarti.setObjectName("textAfisareCarti")
        self.textAfisareReadCarte = QtWidgets.QTextEdit(self.centralwidget)
        self.textAfisareReadCarte.setGeometry(QtCore.QRect(150, 290, 721, 131))
        self.textAfisareReadCarte.setObjectName("textAfisareReadCarte")
        self.textUpdateEdituraOld = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateEdituraOld.setGeometry(QtCore.QRect(610, 450, 104, 31))
        self.textUpdateEdituraOld.setObjectName("textUpdateEdituraOld")
        self.textUpdateDomeniuOld = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateDomeniuOld.setGeometry(QtCore.QRect(500, 450, 111, 31))
        self.textUpdateDomeniuOld.setObjectName("textUpdateDomeniuOld")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(500, 420, 111, 31))
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(610, 420, 101, 31))
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.textUpdateTitluOld = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateTitluOld.setGeometry(QtCore.QRect(290, 450, 111, 31))
        self.textUpdateTitluOld.setObjectName("textUpdateTitluOld")
        self.textUpdateAutorOld = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateAutorOld.setGeometry(QtCore.QRect(400, 450, 104, 31))
        self.textUpdateAutorOld.setObjectName("textUpdateAutorOld")
        self.textUpdateAnAparitieOld = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateAnAparitieOld.setGeometry(QtCore.QRect(710, 450, 104, 31))
        self.textUpdateAnAparitieOld.setObjectName("textUpdateAnAparitieOld")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(400, 420, 101, 31))
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(290, 420, 111, 31))
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(710, 420, 101, 31))
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.textUpdateEdituraNew = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateEdituraNew.setGeometry(QtCore.QRect(610, 510, 104, 31))
        self.textUpdateEdituraNew.setObjectName("textUpdateEdituraNew")
        self.textUpdateDomeniuNew = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateDomeniuNew.setGeometry(QtCore.QRect(500, 510, 111, 31))
        self.textUpdateDomeniuNew.setObjectName("textUpdateDomeniuNew")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(500, 480, 111, 31))
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(610, 480, 101, 31))
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.textUpdateTitluNew = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateTitluNew.setGeometry(QtCore.QRect(290, 510, 111, 31))
        self.textUpdateTitluNew.setObjectName("textUpdateTitluNew")
        self.textUpdateAutorNew = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateAutorNew.setGeometry(QtCore.QRect(400, 510, 104, 31))
        self.textUpdateAutorNew.setObjectName("textUpdateAutorNew")
        self.textUpdateAnAparitieNew = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateAnAparitieNew.setGeometry(QtCore.QRect(710, 510, 104, 31))
        self.textUpdateAnAparitieNew.setObjectName("textUpdateAnAparitieNew")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(400, 480, 101, 31))
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setGeometry(QtCore.QRect(290, 480, 111, 31))
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setGeometry(QtCore.QRect(710, 480, 101, 31))
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 420, 131, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 490, 131, 51))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.textAbonatCreateParola = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatCreateParola.setGeometry(QtCore.QRect(280, 660, 131, 31))
        self.textAbonatCreateParola.setObjectName("textAbonatCreateParola")
        self.buttonCreateAbonat = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCreateAbonat.setGeometry(QtCore.QRect(0, 620, 151, 71))
        self.buttonCreateAbonat.setObjectName("buttonCreateAbonat")
        self.textAbonatUpdateOldNume = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatUpdateOldNume.setGeometry(QtCore.QRect(260, 790, 101, 31))
        self.textAbonatUpdateOldNume.setObjectName("textAbonatUpdateOldNume")
        self.buttonUpdateAbonat = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUpdateAbonat.setGeometry(QtCore.QRect(0, 760, 151, 121))
        self.buttonUpdateAbonat.setObjectName("buttonUpdateAbonat")
        self.textAbonatUpdateNewCont = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatUpdateNewCont.setGeometry(QtCore.QRect(560, 850, 104, 31))
        self.textAbonatUpdateNewCont.setObjectName("textAbonatUpdateNewCont")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(360, 820, 101, 31))
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(460, 820, 101, 31))
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(150, 630, 131, 31))
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.textAbonatDeleteParola = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatDeleteParola.setGeometry(QtCore.QRect(360, 910, 111, 31))
        self.textAbonatDeleteParola.setObjectName("textAbonatDeleteParola")
        self.textAbonatUpdateOldParola = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatUpdateOldParola.setGeometry(QtCore.QRect(360, 790, 104, 31))
        self.textAbonatUpdateOldParola.setObjectName("textAbonatUpdateOldParola")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(560, 760, 101, 31))
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.buttonDeconectare = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDeconectare.setGeometry(QtCore.QRect(770, 720, 141, 81))
        self.buttonDeconectare.setObjectName("buttonDeconectare")
        self.textAbonatDeleteCont = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatDeleteCont.setGeometry(QtCore.QRect(560, 910, 101, 31))
        self.textAbonatDeleteCont.setObjectName("textAbonatDeleteCont")
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setGeometry(QtCore.QRect(260, 880, 101, 31))
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setGeometry(QtCore.QRect(560, 880, 101, 31))
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.textAbonatUpdateOldCont = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatUpdateOldCont.setGeometry(QtCore.QRect(560, 790, 104, 31))
        self.textAbonatUpdateOldCont.setObjectName("textAbonatUpdateOldCont")
        self.textAbonatCreateNume = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatCreateNume.setGeometry(QtCore.QRect(150, 660, 131, 31))
        self.textAbonatCreateNume.setObjectName("textAbonatCreateNume")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(530, 630, 131, 31))
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setGeometry(QtCore.QRect(470, 880, 91, 31))
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.buttonReadAbonat = QtWidgets.QPushButton(self.centralwidget)
        self.buttonReadAbonat.setGeometry(QtCore.QRect(0, 690, 151, 71))
        self.buttonReadAbonat.setObjectName("buttonReadAbonat")
        self.textAbonatDeleteNume = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatDeleteNume.setGeometry(QtCore.QRect(260, 910, 101, 31))
        self.textAbonatDeleteNume.setObjectName("textAbonatDeleteNume")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(260, 820, 101, 31))
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(360, 760, 101, 31))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.textAbonatUpdateNewNume = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatUpdateNewNume.setGeometry(QtCore.QRect(260, 850, 101, 31))
        self.textAbonatUpdateNewNume.setObjectName("textAbonatUpdateNewNume")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(560, 820, 101, 31))
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(360, 880, 111, 31))
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.textAbonatUpdateNewParola = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatUpdateNewParola.setGeometry(QtCore.QRect(360, 850, 104, 31))
        self.textAbonatUpdateNewParola.setObjectName("textAbonatUpdateNewParola")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(260, 760, 101, 31))
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 760, 101, 61))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.textAbonatCreateCont = QtWidgets.QTextEdit(self.centralwidget)
        self.textAbonatCreateCont.setGeometry(QtCore.QRect(530, 660, 131, 31))
        self.textAbonatCreateCont.setObjectName("textAbonatCreateCont")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(150, 820, 101, 61))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(280, 630, 131, 31))
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.textAfisareReadAbonat = QtWidgets.QTextEdit(self.centralwidget)
        self.textAfisareReadAbonat.setGeometry(QtCore.QRect(150, 690, 511, 71))
        self.textAfisareReadAbonat.setObjectName("textAfisareReadAbonat")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(410, 630, 121, 31))
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(460, 760, 101, 31))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.buttonDeleteAbonat = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDeleteAbonat.setGeometry(QtCore.QRect(0, 880, 151, 61))
        self.buttonDeleteAbonat.setObjectName("buttonDeleteAbonat")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 200, 1021, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-80, 540, 1101, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 600, 1011, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.comboBoxSalvareRapoarte = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSalvareRapoarte.setGeometry(QtCore.QRect(880, 560, 131, 51))
        self.comboBoxSalvareRapoarte.setObjectName("comboBoxSalvareRapoarte")
        self.comboBoxSalvareRapoarte.addItem("")
        self.comboBoxSalvareRapoarte.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(0, 560, 141, 51))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.textSalvareRapoarteNumeFisier = QtWidgets.QTextEdit(self.centralwidget)
        self.textSalvareRapoarteNumeFisier.setGeometry(QtCore.QRect(150, 560, 151, 51))
        self.textSalvareRapoarteNumeFisier.setObjectName("textSalvareRapoarteNumeFisier")
        self.textNrInregistrare = QtWidgets.QTextEdit(self.centralwidget)
        self.textNrInregistrare.setGeometry(QtCore.QRect(770, 260, 101, 31))
        self.textNrInregistrare.setObjectName("textNrInregistrare")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(770, 230, 101, 31))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(670, 230, 101, 31))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(810, 420, 101, 31))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.textUpdateNrInregistrareOld = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateNrInregistrareOld.setGeometry(QtCore.QRect(910, 450, 104, 31))
        self.textUpdateNrInregistrareOld.setObjectName("textUpdateNrInregistrareOld")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(910, 420, 101, 31))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(810, 480, 101, 31))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.textUpdateNrInregistrareNou = QtWidgets.QTextEdit(self.centralwidget)
        self.textUpdateNrInregistrareNou.setGeometry(QtCore.QRect(910, 510, 104, 31))
        self.textUpdateNrInregistrareNou.setObjectName("textUpdateNrInregistrareNou")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(910, 480, 101, 31))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.comboBoxDisponibilitate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxDisponibilitate.setGeometry(QtCore.QRect(670, 260, 101, 31))
        self.comboBoxDisponibilitate.setObjectName("comboBoxDisponibilitate")
        self.comboBoxDisponibilitate.addItem("")
        self.comboBoxDisponibilitate.addItem("")
        self.comboBoxUpdateDisponibilitateOld = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxUpdateDisponibilitateOld.setGeometry(QtCore.QRect(810, 450, 101, 31))
        self.comboBoxUpdateDisponibilitateOld.setObjectName("comboBoxUpdateDisponibilitateOld")
        self.comboBoxUpdateDisponibilitateOld.addItem("")
        self.comboBoxUpdateDisponibilitateOld.addItem("")
        self.comboBoxUpdateDisponibilitateNew = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxUpdateDisponibilitateNew.setGeometry(QtCore.QRect(810, 510, 101, 31))
        self.comboBoxUpdateDisponibilitateNew.setObjectName("comboBoxUpdateDisponibilitateNew")
        self.comboBoxUpdateDisponibilitateNew.addItem("")
        self.comboBoxUpdateDisponibilitateNew.addItem("")
        self.textLabelCreateAbonat = QtWidgets.QLabel(self.centralwidget)
        self.textLabelCreateAbonat.setGeometry(QtCore.QRect(410, 660, 121, 31))
        self.textLabelCreateAbonat.setAlignment(QtCore.Qt.AlignCenter)
        self.textLabelCreateAbonat.setObjectName("textLabelCreateAbonat")
        self.textAbonatUpdateOldRol = QtWidgets.QLabel(self.centralwidget)
        self.textAbonatUpdateOldRol.setGeometry(QtCore.QRect(460, 790, 101, 31))
        self.textAbonatUpdateOldRol.setAlignment(QtCore.Qt.AlignCenter)
        self.textAbonatUpdateOldRol.setObjectName("textAbonatUpdateOldRol")
        self.textAbonatUpdateNewRol = QtWidgets.QLabel(self.centralwidget)
        self.textAbonatUpdateNewRol.setGeometry(QtCore.QRect(460, 850, 101, 31))
        self.textAbonatUpdateNewRol.setAlignment(QtCore.Qt.AlignCenter)
        self.textAbonatUpdateNewRol.setObjectName("textAbonatUpdateNewRol")
        self.textAbonatDeleteRol = QtWidgets.QLabel(self.centralwidget)
        self.textAbonatDeleteRol.setGeometry(QtCore.QRect(470, 910, 91, 31))
        self.textAbonatDeleteRol.setAlignment(QtCore.Qt.AlignCenter)
        self.textAbonatDeleteRol.setObjectName("textAbonatDeleteRol")
        Bibliotecar.setCentralWidget(self.centralwidget)

        self.retranslateUi(Bibliotecar)
        QtCore.QMetaObject.connectSlotsByName(Bibliotecar)

    def retranslateUi(self, Bibliotecar):
        _translate = QtCore.QCoreApplication.translate
        Bibliotecar.setWindowTitle(_translate("Bibliotecar", "MainWindow"))
        self.buttonCreateCarte.setText(_translate("Bibliotecar", "CreateCarte"))
        self.buttonReadCarte.setText(_translate("Bibliotecar", "ReadCarti"))
        self.buttonUpdateCarte.setText(_translate("Bibliotecar", "UpdateCarte"))
        self.buttonDeleteCarte.setText(_translate("Bibliotecar", "DeleteCarte"))
        self.buttonImprumutareCarte.setText(_translate("Bibliotecar", "Imprumutare Carte"))
        self.buttonReturnareCarte.setText(_translate("Bibliotecar", "Returnare Carte"))
        self.buttonSalvareRapoarte.setText(_translate("Bibliotecar", "Salvare Rapoarte"))
        self.label_3.setText(_translate("Bibliotecar", "Titlu"))
        self.label_4.setText(_translate("Bibliotecar", "Autor"))
        self.label_5.setText(_translate("Bibliotecar", "Editura"))
        self.label_6.setText(_translate("Bibliotecar", "An Aparite"))
        self.label_7.setText(_translate("Bibliotecar", "Domeniu"))
        self.butonVizualizareCarti.setText(_translate("Bibliotecar", "Vizualizare Carti"))
        self.comboBoxFiltrare.setItemText(0, _translate("Bibliotecar", "domeniu"))
        self.comboBoxFiltrare.setItemText(1, _translate("Bibliotecar", "disponibilitate"))
        self.comboBoxFiltrare.setItemText(2, _translate("Bibliotecar", "editura"))
        self.comboBoxFiltrare.setItemText(3, _translate("Bibliotecar", "autor"))
        self.butonStatistici.setText(_translate("Bibliotecar", "Statistici"))
        self.butonCautareCarte.setText(_translate("Bibliotecar", "Cautare Carte"))
        self.butonFiltrareCarti.setText(_translate("Bibliotecar", "Filtrare Carti"))
        self.comboBoxStatistici.setItemText(0, _translate("Bibliotecar", "domeniu"))
        self.comboBoxStatistici.setItemText(1, _translate("Bibliotecar", "disponibilitate"))
        self.comboBoxStatistici.setItemText(2, _translate("Bibliotecar", "editura"))
        self.comboBoxStatistici.setItemText(3, _translate("Bibliotecar", "autor"))
        self.label_37.setText(_translate("Bibliotecar", "Domeniu"))
        self.label_38.setText(_translate("Bibliotecar", "Editura"))
        self.label_39.setText(_translate("Bibliotecar", "Autor"))
        self.label_40.setText(_translate("Bibliotecar", "Titlu"))
        self.label_41.setText(_translate("Bibliotecar", "An Aparite"))
        self.label_42.setText(_translate("Bibliotecar", "Domeniu"))
        self.label_43.setText(_translate("Bibliotecar", "Editura"))
        self.label_44.setText(_translate("Bibliotecar", "Autor"))
        self.label_45.setText(_translate("Bibliotecar", "Titlu"))
        self.label_46.setText(_translate("Bibliotecar", "An Aparite"))
        self.label.setText(_translate("Bibliotecar", "Carte Old"))
        self.label_8.setText(_translate("Bibliotecar", "Carte New"))
        self.buttonCreateAbonat.setText(_translate("Bibliotecar", "CreateAbonat"))
        self.buttonUpdateAbonat.setText(_translate("Bibliotecar", "UpdateAbonat"))
        self.label_35.setText(_translate("Bibliotecar", "Parola"))
        self.label_36.setText(_translate("Bibliotecar", "Rol"))
        self.label_30.setText(_translate("Bibliotecar", "Nume"))
        self.label_26.setText(_translate("Bibliotecar", "Cont"))
        self.buttonDeconectare.setText(_translate("Bibliotecar", "Deconectare"))
        self.label_47.setText(_translate("Bibliotecar", "Nume"))
        self.label_48.setText(_translate("Bibliotecar", "Cont"))
        self.label_31.setText(_translate("Bibliotecar", "Cont"))
        self.label_49.setText(_translate("Bibliotecar", "Rol"))
        self.buttonReadAbonat.setText(_translate("Bibliotecar", "ReadAbonati"))
        self.label_34.setText(_translate("Bibliotecar", "Nume"))
        self.label_24.setText(_translate("Bibliotecar", "Parola"))
        self.label_33.setText(_translate("Bibliotecar", "Cont"))
        self.label_50.setText(_translate("Bibliotecar", "Parola"))
        self.label_23.setText(_translate("Bibliotecar", "Nume"))
        self.label_2.setText(_translate("Bibliotecar", "Abonat Old"))
        self.label_9.setText(_translate("Bibliotecar", "Abonat New"))
        self.label_29.setText(_translate("Bibliotecar", "Parola"))
        self.label_32.setText(_translate("Bibliotecar", "Rol"))
        self.label_25.setText(_translate("Bibliotecar", "Rol"))
        self.buttonDeleteAbonat.setText(_translate("Bibliotecar", "DeleteAbonat"))
        self.comboBoxSalvareRapoarte.setItemText(0, _translate("Bibliotecar", "csv"))
        self.comboBoxSalvareRapoarte.setItemText(1, _translate("Bibliotecar", "json"))
        self.label_10.setText(_translate("Bibliotecar", "Nume fisier"))
        self.label_11.setText(_translate("Bibliotecar", "Nr.Inregistrare"))
        self.label_12.setText(_translate("Bibliotecar", "Disponibilitate"))
        self.label_13.setText(_translate("Bibliotecar", "Disponibilitate"))
        self.label_14.setText(_translate("Bibliotecar", "Nr.Inregistrare"))
        self.label_15.setText(_translate("Bibliotecar", "Disponibilitate"))
        self.label_16.setText(_translate("Bibliotecar", "Nr.Inregistrare"))
        self.comboBoxDisponibilitate.setItemText(0, _translate("Bibliotecar", "True"))
        self.comboBoxDisponibilitate.setItemText(1, _translate("Bibliotecar", "False"))
        self.comboBoxUpdateDisponibilitateOld.setItemText(0, _translate("Bibliotecar", "True"))
        self.comboBoxUpdateDisponibilitateOld.setItemText(1, _translate("Bibliotecar", "False"))
        self.comboBoxUpdateDisponibilitateNew.setItemText(0, _translate("Bibliotecar", "True"))
        self.comboBoxUpdateDisponibilitateNew.setItemText(1, _translate("Bibliotecar", "False"))
        self.textLabelCreateAbonat.setText(_translate("Bibliotecar", "abonat"))
        self.textAbonatUpdateOldRol.setText(_translate("Bibliotecar", "abonat"))
        self.textAbonatUpdateNewRol.setText(_translate("Bibliotecar", "abonat"))
        self.textAbonatDeleteRol.setText(_translate("Bibliotecar", "abonat"))

        def clickDeconectare():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.deconect()
            Bibliotecar.close()

        self.buttonDeconectare.clicked.connect(clickDeconectare)

        def clickafisareCarti():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.viewCarti()

        self.butonVizualizareCarti.clicked.connect(clickafisareCarti)

        def clickcautare():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.gasesteCarte()

        self.butonCautareCarte.clicked.connect(clickcautare)

        def clickstatistici():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.viewStatistici()

        self.butonStatistici.clicked.connect(clickstatistici)

        def clickfiltrare():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.filtrareCarti()

        self.butonFiltrareCarti.clicked.connect(clickfiltrare)

        def clickcreareAbonat():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.creareAbonat()

        self.buttonCreateAbonat.clicked.connect(clickcreareAbonat)

        def clickviewAbonat():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.vizualizareAbonat()

        self.buttonReadAbonat.clicked.connect(clickviewAbonat)

        def clickupAbonat():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.updateAbonat()

        self.buttonUpdateAbonat.clicked.connect(clickupAbonat)

        def clickdelAbonat():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.deleteAbonat()

        self.buttonDeleteAbonat.clicked.connect(clickdelAbonat)

        def clickcreareCarte():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.creareCarte()

        self.buttonCreateCarte.clicked.connect(clickcreareCarte)

        def clickviewCarte():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.vizualizareCarte()

        self.buttonReadCarte.clicked.connect(clickviewCarte)

        def clickdelCarte():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.stergeCarte()

        self.buttonDeleteCarte.clicked.connect(clickdelCarte)

        def clickborCarte():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.imprumutareCarte()

        self.buttonImprumutareCarte.clicked.connect(clickborCarte)

        def clickretCarte():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.returnareCarte()

        self.buttonReturnareCarte.clicked.connect(clickretCarte)

        def clickupCarte():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.actualizareCarte()

        self.buttonUpdateCarte.clicked.connect(clickupCarte)

        def clicksalvareRaport():
            from Presenter.bibliotecarP import BibliotecarP
            p = BibliotecarP(self)
            p.rapoarte()

        self.buttonSalvareRapoarte.clicked.connect(clicksalvareRaport)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bibliotecar = QtWidgets.QMainWindow()
    ui = Ui_Bibliotecar()
    ui.setupUi(Bibliotecar)
    Bibliotecar.show()
    sys.exit(app.exec_())
