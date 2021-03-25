import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


from PyQt5 import QtCore,  QtWidgets


class Ui_Login(object):



    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(367, 148)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.butonSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.butonSubmit.setGeometry(QtCore.QRect(20, 100, 331, 28))
        self.butonSubmit.setAutoDefault(False)
        self.butonSubmit.setDefault(True)
        self.butonSubmit.setObjectName("butonSubmit")

        self.textName = QtWidgets.QTextEdit(self.centralwidget)
        self.textName.setGeometry(QtCore.QRect(100, 20, 251, 31))
        self.textName.setObjectName("textName")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 70, 55, 21))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 30, 55, 21))
        self.label2.setObjectName("label2")
        self.textPassword = QtWidgets.QTextEdit(self.centralwidget)
        self.textPassword.setGeometry(QtCore.QRect(100, 60, 251, 31))
        self.textPassword.setObjectName("textPassword")
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)



    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.butonSubmit.setText(_translate("Login", "Submit"))
        self.textName.setHtml(_translate("Login", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label1.setText(_translate("Login", "Password"))
        self.label2.setText(_translate("Login", "Name"))

        def clickLog():
            from Presenter.loginP import LoginP
            p = LoginP(self)
            p.login()
            Login.close()

        self.butonSubmit.clicked.connect(clickLog)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
