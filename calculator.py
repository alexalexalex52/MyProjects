from PyQt5 import QtWidgets, QtCore, QtGui, QtWinExtras
import math

class MyWindow(QtWidgets.QWidget):
    firstNum = None
    UserIsWritingSecondNumber = False
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent, QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.btnWin = QtWinExtras.QWinTaskbarButton(parent = self)
        self.btnWin.setOverlayIcon(QtGui.QIcon("png.png"))
        self.pal = QtWidgets.QWidget.palette(self)
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QColor("#9999cc"))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window, QtGui.QColor("#9999cc"))
        self.setPalette(self.pal)
        self.label = QtWidgets.QLabel("0")
        self.label.setStyleSheet("background-color: #ffffff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnChanger = QtWidgets.QPushButton("+/-")
        self.btnChanger.setStyleSheet("background-color: #ccffff;")
        self.btnCl = QtWidgets.QPushButton("C")
        self.btnCl.setStyleSheet("background-color: #ccffff;")
        self.btn7 = QtWidgets.QPushButton("7")
        self.btn7.setStyleSheet("background-color: #0099cc;")
        self.btn8 = QtWidgets.QPushButton("8")
        self.btn8.setStyleSheet("background-color: #0099cc;")
        self.btn9 = QtWidgets.QPushButton("9")
        self.btn9.setStyleSheet("background-color: #0099cc;")
        self.btnDel = QtWidgets.QPushButton("/")
        self.btnDel.setStyleSheet("background-color: #ccffff;")
        self.btn4 = QtWidgets.QPushButton("4")
        self.btn4.setStyleSheet("background-color: #0099cc;")
        self.btn5 = QtWidgets.QPushButton("5")
        self.btn5.setStyleSheet("background-color: #0099cc;")
        self.btn6 = QtWidgets.QPushButton("6")
        self.btn6.setStyleSheet("background-color: #0099cc;")
        self.btnMult = QtWidgets.QPushButton("*")
        self.btnMult.setStyleSheet("background-color: #ccffff;")
        self.btn1 = QtWidgets.QPushButton("1")
        self.btn1.setStyleSheet("background-color: #0099cc;")
        self.btn2 = QtWidgets.QPushButton("2")
        self.btn2.setStyleSheet("background-color: #0099cc;")
        self.btn3 = QtWidgets.QPushButton("3")
        self.btn3.setStyleSheet("background-color: #0099cc;")
        self.btnSub = QtWidgets.QPushButton("-")
        self.btnSub.setStyleSheet("background-color: #ccffff;")
        self.btn0 = QtWidgets.QPushButton("0")
        self.btn0.setStyleSheet("background-color: #0099cc;")
        self.btnDischarge = QtWidgets.QPushButton(".")
        self.btnDischarge.setStyleSheet("background-color: #ccffff;")
        self.btnPlus = QtWidgets.QPushButton("+")
        self.btnPlus.setStyleSheet("background-color: #ccffff;")
        self.btnEqq = QtWidgets.QPushButton("=")
        self.btnEqq.setStyleSheet("background-color: #ccffff;")
        self.btnSin = QtWidgets.QPushButton("sin")
        self.btnSin.setStyleSheet("background-color: #ccffff;")
        self.btnCos = QtWidgets.QPushButton("cos")
        self.btnCos.setStyleSheet("background-color: #ccffff;")
        self.btnTg = QtWidgets.QPushButton("tg")
        self.btnTg.setStyleSheet("background-color: #ccffff;")
        self.btnCtg = QtWidgets.QPushButton("ctg")
        self.btnCtg.setStyleSheet("background-color: #ccffff;")
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.label, 0, 0, 1, 2)
        self.grid.addWidget(self.btnChanger, 0, 2)
        self.grid.addWidget(self.btnCl, 0, 3, 1, 1)
        self.grid.addWidget(self.btn7, 1, 0)
        self.grid.addWidget(self.btn8, 1, 1)
        self.grid.addWidget(self.btn9, 1, 2)
        self.grid.addWidget(self.btnDel, 1, 3)
        self.grid.addWidget(self.btn4, 2, 0)
        self.grid.addWidget(self.btn5, 2, 1)
        self.grid.addWidget(self.btn6, 2, 2)
        self.grid.addWidget(self.btnMult, 2, 3)
        self.grid.addWidget(self.btn1, 3, 0)
        self.grid.addWidget(self.btn2, 3, 1)
        self.grid.addWidget(self.btn3, 3, 2)
        self.grid.addWidget(self.btnSub, 3, 3)
        self.grid.addWidget(self.btn0, 4, 0)
        self.grid.addWidget(self.btnDischarge, 4, 1)
        self.grid.addWidget(self.btnPlus, 4, 2)
        self.grid.addWidget(self.btnEqq, 4, 3)
        self.grid.addWidget(self.btnSin, 5, 0)
        self.grid.addWidget(self.btnCos, 5, 1)
        self.grid.addWidget(self.btnTg, 5, 2)
        self.grid.addWidget(self.btnCtg, 5, 3)
        self.setLayout(self.grid)
        self.setWindowIcon(QtGui.QIcon('png.png'))

        self.btn7.clicked.connect(self.clickedNumbers)
        self.btn8.clicked.connect(self.clickedNumbers)
        self.btn9.clicked.connect(self.clickedNumbers)
        self.btn4.clicked.connect(self.clickedNumbers)
        self.btn5.clicked.connect(self.clickedNumbers)
        self.btn6.clicked.connect(self.clickedNumbers)
        self.btn1.clicked.connect(self.clickedNumbers)
        self.btn2.clicked.connect(self.clickedNumbers)
        self.btn3.clicked.connect(self.clickedNumbers)
        self.btn0.clicked.connect(self.clickedNumbers)

        self.btnChanger.clicked.connect(self.clickedChanger)

        self.btnDischarge.clicked.connect(self.clickedDischarge)

        self.btnPlus.clicked.connect(self.clickedActions)
        self.btnSub.clicked.connect(self.clickedActions)
        self.btnMult.clicked.connect(self.clickedActions)
        self.btnDel.clicked.connect(self.clickedActions)

        self.btnEqq.clicked.connect(self.clickedEqqual)

        self.btnCl.clicked.connect(self.clicked_clear)

        self.btnSin.clicked.connect(self.clickedTrigonometric)
        self.btnCos.clicked.connect(self.clickedTrigonometric)
        self.btnTg.clicked.connect(self.clickedTrigonometric)
        self.btnCtg.clicked.connect(self.clickedTrigonometric)

        self.btnSub.setCheckable(True)
        self.btnPlus.setCheckable(True)
        self.btnMult.setCheckable(True)
        self.btnDel.setCheckable(True)

    def clickedNumbers(self):
        button = self.sender()
        if (self.btnSub.isChecked() or self.btnPlus.isChecked() or self.btnMult.isChecked() or self.btnDel.isChecked())\
                and (not self.UserIsWritingSecondNumber):
            self.UserIsWritingSecondNumber = True
            newlabel = format(float(button.text()),'.15g')
        else:
            if (("." in self.label.text()) and (button.text() == "0")):
                newlabel = format(self.label.text() + button.text(),'.15')
            else:
                newlabel = format(float(self.label.text() + button.text()),'.15g')
        self.label.setText(newlabel)

    def clickedDischarge(self):
        self.label.setText(self.label.text() + ".")

    def clickedChanger(self):
        labelNumber = float(self.label.text())
        labelNumber = labelNumber * -1
        newLabel = format(labelNumber,'.15g')
        self.label.setText(newLabel)

    def clickedTrigonometric(self):
        button = self.sender()
        labelNumber = float(self.label.text())
        if button.text() == "sin":
            labelNumber = math.sin(labelNumber)
        elif button.text() == "cos":
            labelNumber = math.cos(labelNumber)
        elif button.text() == "tg":
            labelNumber = math.tan(labelNumber)
        else:
            labelNumber = math.cos(labelNumber)/math.sin(labelNumber)
        newLabel = format(labelNumber,'.15g')
        self.label.setText(newLabel)


    def clickedActions(self):
        button = self.sender()
        self.firstNum = float(self.label.text())
        button.setChecked(True)

    def clickedEqqual(self):
        secondNum = float(self.label.text())
        if self.btnPlus.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            self.btnPlus.setChecked(False)
        elif self.btnSub.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            self.btnSub.setChecked(False)
        elif self.btnMult.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber,'.15g')
            self.label.setText(newLabel)
            self.btnMult.setChecked(False)
        elif self.btnDel.isChecked():
            if secondNum != 0:
                labelNumber = self.firstNum / secondNum
                newLabel = format(labelNumber,'.15g')
                self.label.setText(newLabel)
                self.btnDel.setChecked(False)
            else:
                self.label.setText("Деление на ноль невозможно")
                self.btnDel.setChecked(False)
                self.btn1.setDisabled(True)
                self.btn2.setDisabled(True)
                self.btn3.setDisabled(True)
                self.btn4.setDisabled(True)
                self.btn5.setDisabled(True)
                self.btn6.setDisabled(True)
                self.btn7.setDisabled(True)
                self.btn8.setDisabled(True)
                self.btn9.setDisabled(True)
                self.btn0.setDisabled(True)
                self.btnPlus.setDisabled(True)
                self.btnSub.setDisabled(True)
                self.btnMult.setDisabled(True)
                self.btnDischarge.setDisabled(True)
                self.btnDel.setDisabled(True)
                self.btnChanger.setDisabled(True)
                self.btnSin.setDisabled(True)
                self.btnCos.setDisabled(True)
                self.btnTg.setDisabled(True)
                self.btnCtg.setDisabled(True)
                self.btnEqq.setDisabled(True)

        self.UserIsWritingSecondNumber = False

    def clicked_clear(self):
        self.btnDel.setChecked(False)
        self.btnMult.setChecked(False)
        self.btnSub.setChecked(False)
        self.btnPlus.setChecked(False)
        self.btn1.setDisabled(False)
        self.btn2.setDisabled(False)
        self.btn3.setDisabled(False)
        self.btn4.setDisabled(False)
        self.btn5.setDisabled(False)
        self.btn6.setDisabled(False)
        self.btn7.setDisabled(False)
        self.btn8.setDisabled(False)
        self.btn9.setDisabled(False)
        self.btn0.setDisabled(False)
        self.btnPlus.setDisabled(False)
        self.btnSub.setDisabled(False)
        self.btnMult.setDisabled(False)
        self.btnDischarge.setDisabled(False)
        self.btnDel.setDisabled(False)
        self.btnChanger.setDisabled(False)
        self.btnSin.setDisabled(False)
        self.btnCos.setDisabled(False)
        self.btnTg.setDisabled(False)
        self.btnCtg.setDisabled(False)
        self.btnEqq.setDisabled(False)
        self.label.setText("0")
        self.UserIsWritingSecondNumber = False

    def showEvent(self, evt):
        self.btnWin.setWindow(self.windowHandle())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Калькулятор")
    window.resize(420,200)
    window.show()
    sys.exit(app.exec_())
