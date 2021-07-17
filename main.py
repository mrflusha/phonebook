import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QLabel, QCalendarWidget, QDateEdit,QMessageBox, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLineEdit,QCheckBox, QTableWidget, QTableWidgetItem,QAbstractItemView
from PyQt5.QtGui import QIcon,QCursor
from PyQt5.QtCore import *
from datetime import datetime
import calendar
import db_func
import func


class output_window(QDialog):                           # <===
    def __init__(self,parent=None):
        super().__init__(parent, Qt.Window)
        self.setWindowTitle("Телефонная Книжка")
        self.left = 100
        self.top = 100
        self.width = 550
        self.height = 500
        self.initUI()
    def initUI(self):
        #widget = QWidget(self)

        #self.setCentralWidget(widget)

        #grid = QGridLayout(widget)

        self.setWindowTitle("Телефонная Книжка")
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createOutputWindow()
        
        self.windowLayout = QGridLayout()



        self.windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.windowLayout)

        
        self.show()

    def createOutputWindow(self):
        output_layout = QGridLayout()
        output_layout.setColumnStretch(4, 2)
        self.buttons_arr = list()
        for i in func.dictonary:
            self.buttons_arr.append(QPushButton(i))
        for i in range(len(self.buttons_arr)):
            self.buttons_arr[i].setStyleSheet('QPushButton {background-color:blue; color:white}')
            print(self.buttons_arr)
            output_layout.addWidget(self.buttons_arr[i],i,0)
            
        self.horizontalGroupBox = QGroupBox("")
        
        self.add_button = QPushButton('Добавить Контакт')
        self.edit_button = QPushButton('Редактировать Контакт')
        self.delete_button = QPushButton('Удалить Контакт')
        
        self.delete_button.setStyleSheet('QPushButton {background-color: red; color: white;}')
        self.edit_button.setStyleSheet('QPushButton {background-color: gray; color: white;}')
        self.add_button.setStyleSheet('QPushButton {background-color: green; color: white;}')


        self.table = QTableWidget(self) 
        self.table.setColumnCount(3)     # Устанавливаем три колонки
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(["ФИО", "Номер телефона", "Дата рождения"])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setItem(0, 0, QTableWidgetItem("Хованский Юрий Михайлович"))
        self.table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        self.table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
        
        self.table.setItem(1, 1, QTableWidgetItem(""))
        self.table.setItem(2, 2, QTableWidgetItem("Text in column 3"))
        self.table.setMinimumWidth(300)
        self.table.resizeColumnsToContents()

        
        output_layout.addWidget(self.table,0,1,11,4)
        output_layout.addWidget(self.add_button,11,2)
        output_layout.addWidget(self.edit_button,11,3)
        output_layout.addWidget(self.delete_button,11,4)

        self.horizontalGroupBox.setLayout(output_layout)


        self.delete_button.clicked.connect(self.cancel_click)


    @pyqtSlot()
    def cancel_click(self):
            self.close()




class reg_window(QDialog):                           # <===
    def __init__(self,parent=None):
        super().__init__(parent, Qt.Window)
        self.setWindowTitle("Регистрация")
        self.left = 300
        self.top = 200
        self.width = 300
        self.height = 150
        self.initUI()
    def initUI(self):
        #widget = QWidget(self)

        #self.setCentralWidget(widget)

        #grid = QGridLayout(widget)

        self.setWindowTitle("Регистрация")
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createRegWindow()
        
        self.windowLayout = QGridLayout()
        

        self.windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.windowLayout)

        
        self.show()

    def createRegWindow(self):

        self.horizontalGroupBox = QGroupBox("")
        reg_layout = QGridLayout()
        reg_layout.setColumnStretch(4, 3)
        self.login = QLineEdit(self)
        self.mail = QLineEdit(self)
        self.pw = QLineEdit(self)
        self.re_pw = QLineEdit(self)
        #self.date = QLineEdit(self)
        self.reg_button = QPushButton('Регистрация')
        self.cancel_button = QPushButton('Отмена')
        self.date_c = QDateEdit()
        self.login.setPlaceholderText("Имя пользователя")
        self.mail.setPlaceholderText("email")
        self.pw.setPlaceholderText("Пароль")
        self.re_pw.setPlaceholderText("Повторите пароль")
        self.date_label = QLabel("Дата рождения:")
        #self.calendar = QCalendarWidget()
        #self.date_c.setMaximumDateTime()

        self.reg_button.setStyleSheet('QPushButton {background-color: green; color: white;cursor:pointer}')
        self.reg_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button.setStyleSheet('QPushButton {background-color: red; color: white;}')
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.pw.setEchoMode(QLineEdit.Password)
        self.re_pw.setEchoMode(QLineEdit.Password)
 
        reg_layout.addWidget(self.login,0,1,1,3)
        reg_layout.addWidget(self.mail,1,1,1,3)
        reg_layout.addWidget(self.pw,2,1,1,3)
        reg_layout.addWidget(self.re_pw,3,1,1,3)
        #reg_layout.addWidget(self.date,4,1,1,3)
        reg_layout.addWidget(self.date_label,4,1,1,3)
        reg_layout.addWidget(self.date_c,5,1,1,3)
        #reg_layout.addWidget(self.calendar,4,3,1,3)
        reg_layout.addWidget(self.reg_button,6,1)
        reg_layout.addWidget(self.cancel_button,6,2)
        self.horizontalGroupBox.setLayout(reg_layout)
        print(self.date_c)
        self.cancel_button.clicked.connect(self.cancel_click)
        self.reg_button.clicked.connect(self.reg_click)

#    @pyqtSlot()





class restore_window(QDialog):                           # <===
    def __init__(self,parent=None):
        super().__init__(parent, Qt.Window)
        self.setWindowTitle("Востановление пароля")
        self.left = 300
        self.top = 200
        self.width = 300
        self.height = 150
        self.initUI()
    def initUI(self):
        #widget = QWidget(self)

        #self.setCentralWidget(widget)

        #grid = QGridLayout(widget)

        self.setWindowTitle("Востановление")
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createRestoreWindow()
        
        self.windowLayout = QGridLayout()



        self.windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.windowLayout)

        
        self.show()

    def createRestoreWindow(self):
        self.horizontalGroupBox = QGroupBox("")
        output_layout = QGridLayout()
        output_layout.setColumnStretch(4, 3)
        self.mail = QLineEdit(self)
        self.new_button = QPushButton('Сменить пароль')
        self.cancel_button = QPushButton('Отмена')
        self.mail.setPlaceholderText("Введите email")
        self.cancel_button.setStyleSheet('QPushButton {background-color: red; color: white;}')
        self.new_button.setStyleSheet('QPushButton {background-color: gray; color: white;}')

        output_layout.addWidget(self.mail,0,1,1,2)
        output_layout.addWidget(self.new_button,6,1)
        output_layout.addWidget(self.cancel_button,6,2)

        self.horizontalGroupBox.setLayout(output_layout)


        self.cancel_button.clicked.connect(self.cancel_click)


    @pyqtSlot()
    def cancel_click(self):
            self.close()




class reg_window(QDialog):                           # <===
    def __init__(self,parent=None):
        super().__init__(parent, Qt.Window)
        self.setWindowTitle("Регистрация")
        self.left = 300
        self.top = 200
        self.width = 300
        self.height = 150
        self.initUI()
    def initUI(self):
        #widget = QWidget(self)

        #self.setCentralWidget(widget)

        #grid = QGridLayout(widget)

        self.setWindowTitle("Регистрация")
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createRegWindow()
        
        self.windowLayout = QGridLayout()
        

        self.windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.windowLayout)

        
        self.show()

    def createRegWindow(self):
        self.horizontalGroupBox = QGroupBox("")
        reg_layout = QGridLayout()
        reg_layout.setColumnStretch(4, 3)
        self.login = QLineEdit(self)
        self.mail = QLineEdit(self)
        self.pw = QLineEdit(self)
        self.re_pw = QLineEdit(self)
        #self.date = QLineEdit(self)
        self.reg_button = QPushButton('Регистрация')
        self.cancel_button = QPushButton('Отмена')
        self.date_c = QDateEdit()
        self.login.setPlaceholderText("Имя пользователя")
        self.mail.setPlaceholderText("email")
        self.pw.setPlaceholderText("Пароль")
        self.re_pw.setPlaceholderText("Повторите пароль")
        self.date_label = QLabel("Дата рождения:")
        #self.calendar = QCalendarWidget()
        #self.date_c.setMaximumDateTime()

        self.reg_button.setStyleSheet('QPushButton {background-color: green; color: white;cursor:pointer}')
        self.reg_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button.setStyleSheet('QPushButton {background-color: red; color: white;}')
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.pw.setEchoMode(QLineEdit.Password)
        self.re_pw.setEchoMode(QLineEdit.Password)
 
        reg_layout.addWidget(self.login,0,1,1,3)
        reg_layout.addWidget(self.mail,1,1,1,3)
        reg_layout.addWidget(self.pw,2,1,1,3)
        reg_layout.addWidget(self.re_pw,3,1,1,3)
        #reg_layout.addWidget(self.date,4,1,1,3)
        reg_layout.addWidget(self.date_label,4,1,1,3)
        reg_layout.addWidget(self.date_c,5,1,1,3)
        #reg_layout.addWidget(self.calendar,4,3,1,3)
        reg_layout.addWidget(self.reg_button,6,1)
        reg_layout.addWidget(self.cancel_button,6,2)
        self.horizontalGroupBox.setLayout(reg_layout)
        print(self.date_c)
        self.cancel_button.clicked.connect(self.cancel_click)
        self.reg_button.clicked.connect(self.reg_click)

    @pyqtSlot()
    def cancel_click(self):
            self.close()
    def reg_click(self):
        name = self.login.text()
        mail = self.mail.text()
        pw = self.pw.text()
        re_pw = self.re_pw.text()
        tmp_date = self.date_c.date()
        date = str(tmp_date.toPyDate())
        db_mail = list()
        db_logins = list()
        registred_email = db_func.sql(db_func.mails_q,db_mail)
        registred_users = db_func.sql(db_func.users_q,db_logins)
        print (name, type(date))
        if pw != re_pw:
            QMessageBox.warning(self, "Уведомление", "Пароли не совпадают", QMessageBox.Ok)
        elif len(pw) <= 3:
            QMessageBox.warning(self, "Уведомление", "Слишком короткий пароль", QMessageBox.Ok)
        elif len(name) <= 3:
            QMessageBox.warning(self, "Уведомление", "Слишком короткий логин", QMessageBox.Ok)        
        elif len(mail) <= 3 or ("@"or".") not in mail:
            QMessageBox.warning(self, "Уведомление", "Введите email", QMessageBox.Ok)
        elif mail in registred_email:
            QMessageBox.warning(self, "Уведомление", "Данный email уже зарегестрирован \r\nПожалуйста введите другой email", QMessageBox.Ok)        
        elif name in registred_users:
            QMessageBox.warning(self, "Уведомление", "Пользователь с таким именем уже зарегестрирован \r\nПожалуйста выберите другое имя", QMessageBox.Ok)

        else:
            db_func.add_sql(name,mail,pw,date)
            





    
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
#Get button styles
        reg_button.setCursor(QCursor(Qt.PointingHandCursor))
        cancel_button.setStyleSheet('QPushButton {background-color: red; color: white;}')
        cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        auth_button.setStyleSheet('QPushButton {background-color: green; color: white;}')
        auth_button.setCursor(QCursor(Qt.PointingHandCursor))
        restore_button.setStyleSheet('QPushButton {border: none; color: blue; text-decoration: underline}')
        restore_button.setCursor(QCursor(Qt.PointingHandCursor))


        self.login = QLineEdit(self)
        self.password = QLineEdit(self)
        self.login.setPlaceholderText("Enter login")
        self.password.setPlaceholderText("Enter password")
        layout.addWidget(self.login,0,0,1,3)
        
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
        reg_button.clicked.connect(self.open_reg)
        restore_button.clicked.connect(self.open_restore)
        cancel_button.clicked.connect(self.close_btn)
        auth_button.clicked.connect(self.open_output)
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
    def open_reg(self):
        self.w = reg_window()
        self.w.show()

        
    def close_btn(self):
        self.close()
    def open_restore(self):
        self.w = restore_window()
        self.w.show()        
    def open_output(self):
        self.w = output_window()
        self.w.show()   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())