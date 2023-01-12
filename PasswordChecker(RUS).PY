import sys
import random
import re
import sqlite3
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QMessageBox
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Проверка пароля')
        hboxmain = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox2 = QVBoxLayout()        
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        hbox7 = QHBoxLayout()
        hbox8 = QHBoxLayout()
        hbox9 = QHBoxLayout()
        hbox10 = QHBoxLayout()
        hbox11 = QHBoxLayout()
        hbox12 = QHBoxLayout()
        hbox13 = QHBoxLayout()
        hbox14 = QHBoxLayout()
        hbox15 = QHBoxLayout()
        hbox16 = QHBoxLayout()
        hbox17 = QHBoxLayout()
        hbox18 = QHBoxLayout()
        hbox19 = QHBoxLayout()
        hbox20 = QHBoxLayout()
        hbox21 = QHBoxLayout()
        
        self.start = QLabel('<b>Проверьте сложность вашего пароля!<b>')
        self.start.setAlignment(Qt.AlignCenter) 
        self.timeend = QLabel('<b>Сгенерируйте свой пароль<b>')
        self.timeend.setAlignment(Qt.AlignCenter) 
        
        hbox1.addWidget(self.start)
        hbox2.addWidget(self.timeend)

        self.wod = QLabel('Ваш пароль:')
        self.passwordEdit = QLineEdit()
        self.length = QLabel('Длина:')
        self.lengthEdit = QLineEdit()
        
        hbox3.addWidget(self.wod)
        hbox3.addWidget(self.passwordEdit)
        hbox4.addWidget(self.length)
        hbox4.addWidget(self.lengthEdit)
        
        self.digitsAdd = QCheckBox('Добавить цифры')
        self.passwordCheck = QPushButton('                                       Проверить!                                        ')
        self.passwordCheck.clicked.connect(self.Check)

        hbox5.addWidget(self.passwordCheck)
        hbox6.addWidget(self.digitsAdd)

        self.lowercaseAdd = QCheckBox('Добавить строчные буквы')
        self.rules = QLabel('<b>Критерии пароля:<b>')
        
        self.rules.setAlignment(Qt.AlignCenter)

        hbox7.addWidget(self.rules)
        hbox8.addWidget(self.lowercaseAdd)

        self.uppercaseAdd = QCheckBox('Добавить прописные буквы')
        self.rules = QLabel('- Длина пароля')
        hbox21.addWidget(self.rules)
        self.rules = QLabel('- Наличие цифр')

        hbox9.addWidget(self.rules)
        hbox10.addWidget(self.uppercaseAdd)

        self.symbolAdd = QCheckBox('Добавить специальные символы')
        self.rules = QLabel('- Наличие строчных и прописных букв')

        hbox11.addWidget(self.rules)
        hbox12.addWidget(self.symbolAdd)

        self.generate = QPushButton('           Сгенерировать!           ')
        self.rules = QLabel('- Наличие специальных символов')
        self.generate.clicked.connect(self.Generate)

        hbox13.addWidget(self.rules)
        hbox14.addWidget(self.generate)

        self.iss = QLabel('Сгенерированный пароль:')
        self.rules = QLabel('- Отсутствие повторов')

        hbox15.addWidget(self.rules)
        hbox16.addWidget(self.iss)

        self.itog = QLineEdit()
        self.rules = QLabel('- Отсутствие простых комбинаций')

        hbox17.addWidget(self.rules)
        hbox18.addWidget(self.itog)

        self.diff = QLabel('')

        hbox19.addWidget(self.diff)

        self.error = QLabel('')

        hbox20.addWidget(self.error)


        
        vbox.addLayout(hbox1)
        vbox2.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox2.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox2.addLayout(hbox6)
        vbox.addLayout(hbox7)
        vbox2.addLayout(hbox8)
        vbox.addLayout(hbox21)
        vbox.addLayout(hbox9)
        vbox2.addLayout(hbox10)
        vbox.addLayout(hbox11)
        vbox2.addLayout(hbox12)
        vbox.addLayout(hbox13)
        vbox2.addLayout(hbox14)
        vbox.addLayout(hbox15)
        vbox2.addLayout(hbox16)
        vbox.addLayout(hbox17)
        vbox2.addLayout(hbox18)
        vbox.addLayout(hbox19)
        vbox.addLayout(hbox20)
        
        hboxmain.addLayout(vbox)
        hboxmain.addLayout(vbox2)
        
        centralWidget = QWidget()
        centralWidget.setLayout(hboxmain)
        self.setCentralWidget(centralWidget)
        self.statusBar().showMessage('Создал Егор Васильев')
        self.show()

    def Generate(self):
        self.x = self.lengthEdit.text()
        if self.x == '':
            return
        else:
            leng = int(self.x)
            gen = ''
        if leng > 32 or leng  < 12:
            msg = QMessageBox()
            msg.setInformativeText('Пожалйста напишите другую  длину пароля, больше 12 и меньше 32')
            msg.setWindowTitle("Ошибка длинны пароля")
            msg.exec_()
            return
        digitscheck, lowercasescheck, uppercasescheck, symbolcheck = False, False, False, False
        if self.digitsAdd.isChecked():
            gen += '123456789'
            digitscheck  = True
        if self.lowercaseAdd.isChecked():
            gen += 'qwertyuiopasdfghjklzxcvbnm'
            lowercasescheck  = True
        if self.uppercaseAdd.isChecked():
            gen += 'QWERTYUIOPASDFGHJKLZXCVBNM'
            uppercasescheck  = True
        if self.symbolAdd.isChecked():
            gen += '~!@#$%*_-'
            symbolcheck  = True
        if not(digitscheck or lowercasescheck or uppercasescheck or symbolcheck):
            gen = ' '

        psw = ''.join([random.choice(gen) for x in range(leng)])
        while digitscheck or lowercasescheck or uppercasescheck or symbolcheck:
            while digitscheck:
                for i in '123456789':
                    if i in psw:
                        digitscheck = False
                        break
                if digitscheck:
                    psw = ''.join([random.choice(gen) for x in range(leng)])
            while lowercasescheck:
                for i in 'qwertyuiopasdfghjklzxcvbnm':
                    if i in psw:
                        lowercasescheck = False
                        break
                if lowercasescheck:
                    psw = ''.join([random.choice(gen) for x in range(leng)])
            while uppercasescheck:
                for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                    if i in psw:
                        uppercasescheck = False
                        break
                if uppercasescheck:
                    psw = ''.join([random.choice(gen) for x in range(leng)])
            while symbolcheck:
                for i in '~!@#$%*_-':
                    if i in psw:
                        symbolcheck = False
                        break
                if symbolcheck:
                    psw = ''.join([random.choice(gen) for x in range(leng)])
            
        self.itog.setText(psw)
    def Check(self):
        self.pas = self.passwordEdit.text()
        pasw = self.pas
        if  len(pasw) ==  0:
            return
        strong =  0
        lowlen, nodig, nolower, noupper, nosymbol, repet, simp = 1, 1, 1, 1, 1, 0, 0
        if len(pasw) > 8:
            strong += 1
            lowlen = 0
        if len(pasw) > 12:
            strong +=  1
        for i in '123456789':
            if i in pasw:
                strong += 1
                nodig = 0
                break
        for i in 'qwertyuiopasdfghjklzxcvbnm':
            if i in pasw:
                strong += 1
                nolower = 0
                break
        for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            if i in pasw:
                strong += 1
                nolower = 0
                break
        for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            if i in pasw:
                strong += 1
                noupper = 0
                break
        for i in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            if i in pasw:
                strong += 1
                noupper = 0
                break
        for i in '~!@#$%*_-.':
            if i in pasw:
                strong += 1
                nosymbol = 0
                break
        for i in range(len(pasw)-2):
            if  pasw[i] == pasw[i+1] and pasw[i] ==  pasw[i+2]:
                strong -= 2
                repet =  1
        prov = ['qwe','123' , '228' ,'1337' , 'zxc', 'abc', '012' , '987', 'йцу']
        for i in prov:
            if i in pasw:
                strong -= 2
                simp =  1
        if strong  < 2:
            diffc = 'Лёгкая'
            self.diff.setText(f'<b>Сложность пароля: {diffc}<b>')
            self.diff.setStyleSheet("""color: green;""")
        elif strong < 4:
            diffc = 'Нормальная'
            self.diff.setText(f'<b>Сложность пароля: {diffc}<b>')
            self.diff.setStyleSheet("""color: orange;""")
        elif strong < 6:
            diffc = 'Сложная'
            self.diff.setText(f'<b>Сложность пароля: {diffc}<b>')
            self.diff.setStyleSheet("""color: red;""")
        else:
            diffc = 'Наивысшая'
            self.diff.setText(f'<b>Сложность пароля: {diffc}<b>')
            self.diff.setStyleSheet("""color: purple;""")
        
        if strong  < 5:
            if repet == 0 and simp == 0:
                self.error.setText('Пожалуйста, добавьте ' + 'цифры, '*nodig + 'строчные буквы, '*nolower + 'прописные буквы, ' *noupper +'специальные символы, '*nosymbol + 'увеличьте длину'*lowlen)
            elif repet == 1 and simp == 0:
                self.error.setText('Пожалуйста, добавьте ' + 'цифры, '*nodig + 'строчные буквы, '*nolower + 'прописные буквы, '*noupper + 'специальные символы, '*nosymbol + 'увеличьте длину, '*lowlen + 'уберите повторы')
            elif repet == 0 and simp == 1:
                self.error.setText('Пожалуйста, добавьте ' + 'цифры, '*nodig + 'строчные буквы, '*nolower + 'прописные буквы, '*noupper + 'специальные символы, '*nosymbol + 'увеличьте длину, '*lowlen + 'уберите простые комбинации')
            else:
                self.error.setText('Пожалуйста, добавьте ' + 'цифры, '*nodig + 'строчные буквы, '*nolower + 'прописные буквы, '*noupper + 'специальные символы, '*nosymbol + 'увеличьте длину, '*lowlen + 'уберите повторы и уберите простые комбинации')
        else:
            self.error.setText('')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
