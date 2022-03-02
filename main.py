from PyQt5 import QtCore, QtGui, QtWidgets
import RSA
import math


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261 * 3, 392 * 3)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 258 * 3, 341 * 3))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 261, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.increment = 2

        self.pushButton.clicked.connect(self.encrypt_msg)
        self.pushButton_2.clicked.connect(self.decrypt_msg)
        self.pushButton_3.clicked.connect(self.try_one_num)
        self.pushButton_4.clicked.connect(self.Brute_Force)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "What message do you want to send?"))
        self.pushButton.setText(_translate("MainWindow", "Encrypt"))
        self.label_3.setText(_translate("MainWindow", "E:"))
        self.label_5.setText(_translate("MainWindow", "N:"))
        self.pushButton_2.setText(_translate("MainWindow", "Decrypt"))
        self.pushButton_3.setText(_translate("MainWindow", "Try one number"))
        self.pushButton_4.setText(_translate("MainWindow", "Brute force all numbers"))
        self.label_2.setText(_translate("MainWindow", "Output"))

    def encrypt_msg(self):
        self.e, self.d, self.N = RSA.generateKeys(RSA.keysize)
        message = self.textEdit.toPlainText()
        self.enc_msg = RSA.encrypt(self.e, self.N, message)
        e_str = str(self.e)
        n_str = str(self.N)
        self.label_3.setText("E (encryption key): " + e_str)
        self.label_5.setText("N (modulus): " + n_str)
        self.plainTextEdit.setPlainText(self.enc_msg)

    def decrypt_msg(self):
        self.dec_msg = RSA.decrypt(self.d, self.N, self.enc_msg)
        dec = str(self.dec_msg)
        self.plainTextEdit_2.setPlainText(dec)

    def try_one_num(self):
        if self.N % self.increment == 0:
            self.p = self.increment
            self.q = math.floor(self.N / self.increment)
            d = RSA.modinv2(self.e, self.p, self.q)
            self.dec_msg = RSA.decrypt(d // 1, self.N, self.enc_msg)
            dec = str(self.dec_msg)
            message = "p = " + str(self.p) + "\nq = " + str(self.q) + "\nd (decryption key)  = " + str(
                d) + "\nmessage: "
            self.plainTextEdit_2.setPlainText(message + dec)
        else:
            self.plainTextEdit_2.setPlainText("N is not divisible by " + str(self.increment))
        self.increment += 1

    def Brute_Force(self):
        self.p, self.q = RSA.brute_force(self.N)
        d = RSA.modinv2(self.e, self.p, self.q)
        self.p = math.floor(self.p)
        self.q = math.floor(self.q)
        self.dec_msg = RSA.decrypt(d // 1, self.N, self.enc_msg)
        dec = str(self.dec_msg)
        message = "p = " + str(self.p) + "\nq = " + str(self.q) + "\nd (decryption key)  = " + str(
            d) + "\nmessage: "
        self.plainTextEdit_2.setPlainText(message + dec)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
