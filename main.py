import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLineEdit,QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *


class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'idontknowwhy'
        self.left = 100
        self.top = 200
        self.width = 300
        self.height = 100
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        
        self.show()
    

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        layout.setColumnStretch(1, 2)
        layout.setColumnStretch(7, 3)
        reg_button = QPushButton('Регистрация')
        auth_button = QPushButton('Войти')
        cancel_button = QPushButton('Отмена')
        restore_button = QPushButton('Забыли пароль?')
        cancel_button.setStyleSheet('QPushButton {background-color: green; color: white;}')
        auth_button.setStyleSheet('QPushButton {background-color: red; color: white;}')
        restore_button.setStyleSheet('QPushButton {border: none; color: blue; text-decoration: underline}')
        self.login = QLineEdit(self)
        self.password = QLineEdit(self)
        self.login.setPlaceholderText("Enter login")
        self.password.setPlaceholderText("Enter password")
        #self.remember_toggle = False
        #self.show_toggle = False

        remember_cb = QCheckBox('Запомнить', self)
        self.show_cb = QCheckBox('Показать пароль', self)
        self.password.setEchoMode(QLineEdit.Password)
       #print(pw_status)
        

        #layout.addWidget(QLabel("Type:"),0,0)
        layout.addWidget(self.login,0,0,1,3)
        layout.addWidget(self.password,1,0,1,3)
        layout.addWidget(auth_button,2,0)
        layout.addWidget(reg_button,2,1)
        layout.addWidget(cancel_button,2,2)
        layout.addWidget(remember_cb,3,1,1,3)
        layout.addWidget(self.show_cb,4,1,1,3)
        layout.addWidget(restore_button,5,0,1,3)
        #layout.addWidget(self.to_hex,2,1)
        #layout.addWidget(QLabel("Copy:"),2,0)
        #layout.addWidget(QLabel(""),3,1)
        

        self.horizontalGroupBox.setLayout(layout)
        auth_button.clicked.connect(self.slot_method)
        self.pw_status = self.show_cb.isChecked()
        self.show_cb.stateChanged.connect(self.show_pass)






    @pyqtSlot()
    def slot_method(self):
        print("hello")

    def show_pass(self):
        print(self.pw_status)
        if self.show_cb.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

#   def show_pass(self, cb_state, pw):
#       if (cb_state == True):
#           self.pw.setEchoMode(QLineEdit.Normal)
#       else:
#           self.pw.setEchoMode(QLineEdit.Password)


#       b = self.a.text()
 #      hex_str = ""

        
        #for i in range(len(b)):
        #   hex_str +="%"+str(b[i].encode("utf-8").hex())

#       self.to_hex.setText(hex_str)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())