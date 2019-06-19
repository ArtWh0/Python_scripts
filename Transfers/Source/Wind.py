from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(241, 180)

        self.redb = QtWidgets.QPushButton('Сформировать',Dialog)
        self.redb.setCheckable(True)
        self.redb.move(130, 140)

        self.lbl=QtWidgets.QLabel(Dialog)
        self.lbl.setText("Имя выходного файла")
        self.lbl.move(30, 70)

        self.log=QtWidgets.QLabel(Dialog)
        self.log.setText('                                                           ')
        self.log.move(30, 120)

        self.num_card = QtWidgets.QLineEdit(Dialog)
        self.num_card.setGeometry(QtCore.QRect(30, 30, 181, 21))
        self.num_card.setObjectName("num_card")

        self.name_xls = QtWidgets.QLineEdit(Dialog)
        self.name_xls.setGeometry(QtCore.QRect(30, 85, 181, 21))
        self.name_xls.setObjectName("name_xls")

        self.CardNumber = QtWidgets.QLabel(Dialog)
        self.CardNumber.setGeometry(QtCore.QRect(30, 10, 111, 16))
        self.CardNumber.setObjectName("CardNumber")
        self.retranslateUi(Dialog)
        self.redb.clicked[bool].connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Выгрузка БЭПК"))
        self.CardNumber.setText(_translate("Dialog", "Номер первой карты"))
