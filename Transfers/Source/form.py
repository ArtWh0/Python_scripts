from PyQt5 import QtCore, QtGui, QtWidgets
from Wind import Ui_Dialog
from Pars import Del_Duplicate, Parsing, settings, valid_num
import sys

f=open(settings.main_file())
lines=f.readlines()
#Del_Duplicate(lines)

class window(QtWidgets.QDialog):
    def __init__(self):
        super(window, self).__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.onlyInt=QtGui.QIntValidator()

def on_button_clicked(window):
    try:
        #xls_create()
        if valid_num(win.ui.num_card.text())==5:
            i=Parsing(win.ui.num_card.text(), Del_Duplicate(lines), win.ui.name_xls.text())
            win.ui.log.setText('Всего выгружено: '+i+' карт(ы)')
        else:
            win.ui.log.setText('Некорректный номер карты!')
            print(valid_num(win.ui.num_card.text()))
    except Exception:
        win.ui.log.setText('Непредвиденная ошибка!')
        #f.close()
    win.show()

if __name__=='__main__':
    app=QtWidgets.QApplication([])
    win=window()
    b=win.ui.redb
    b.clicked.connect(lambda: on_button_clicked(win))
    win.show()
    sys.exit(app.exec_())
