from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from list_manager import *
from construct_lists import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 600))
        MainWindow.setMaximumSize(QtCore.QSize(500, 600))
        MainWindow.setWindowIcon(QtGui.QIcon("img/favicon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Title

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(-4, 2, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        #Input Line

        self.input_line = QtWidgets.QLineEdit(self.centralwidget)
        self.input_line.setGeometry(QtCore.QRect(130, 320, 241, 51))
        self.input_line.setText("")
        self.input_line.setAlignment(QtCore.Qt.AlignCenter)
        self.input_line.setMaxLength(5)
        self.input_line.setObjectName("input_line")
        validator = QtGui.QIntValidator()
        validator.setBottom(0)
        self.input_line.setValidator(validator)

        #Convert Button

        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(140, 495, 220, 80))
        self.convert_button.setObjectName("convert_button")
        self.convert_button.clicked.connect(lambda:self.take_element())
        self.convert_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
       
        #Create IN/OUT Lists

        self.in_convert_list = init_in_list(self.centralwidget)
        self.out_convert_list = init_out_list(self.centralwidget)

        #DisplayZone

        self.display = QtWidgets.QLCDNumber(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(10, 390, 481, 81))
        self.display.setObjectName("display")
        self.display.setDigitCount(10)
        
        #Labels - in/out

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 52, 121, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("in_text")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 52, 121, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("out_text")
        MainWindow.setCentralWidget(self.centralwidget)
        

        #StatusBar

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fast-Convert"))
        self.title.setText(_translate("MainWindow", "Fast-Convert"))
        self.convert_button.setText(_translate("MainWindow", "Convert"))
        __sortingEnabled = self.in_convert_list.isSortingEnabled()
        self.in_convert_list.setSortingEnabled(False)

        in_list(self.in_convert_list, _translate)
        self.in_convert_list.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.out_convert_list.isSortingEnabled()
        self.out_convert_list.setSortingEnabled(False)

        out_list(self.out_convert_list, _translate)

        self.out_convert_list.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "IN"))
        self.label_3.setText(_translate("MainWindow", "OUT"))


    def take_element(self):

        def out_selection(out_select):
            if out_select[0].data(QtCore.Qt.UserRole) == "1":
                return 1
            elif out_select[0].data(QtCore.Qt.UserRole) == "10":
                return 10
            elif out_select[0].data(QtCore.Qt.UserRole) == "100":
                return 100
            elif out_select[0].data(QtCore.Qt.UserRole) == "1000":
                return 1000
            elif out_select[0].data(QtCore.Qt.UserRole) == "10000":
                return 10000
            elif out_select[0].data(QtCore.Qt.UserRole) == "100000":
                return 100000
            elif out_select[0].data(QtCore.Qt.UserRole) == "1000000":
                return 1000000
            else:
                print('Error, probably nothing select in Out List')

        def to_celsius(in_select, input_number):
            if in_select[0].data(QtCore.Qt.UserRole) == "Kelv":
                cels = input_number - 273.15
                return cels
            elif in_select[0].data(QtCore.Qt.UserRole) == "Cels":
                return input_number
            elif in_select[0].data(QtCore.Qt.UserRole) == "Far":
                cels = (input_number - 32)/1.8
                return cels
            elif in_select[0].data(QtCore.Qt.UserRole) == "Newt":
                cels = input_number/0.33
                return cels
            elif in_select[0].data(QtCore.Qt.UserRole) == "Reaum":
                cels = input_number * 1.25
                return cels
            else:
                print('Error, probably nothing select in Out List')

        #Take selected items.

        in_select = self.in_convert_list.selectedItems()
        out_select = self.out_convert_list.selectedItems()
        input_number = self.input_line.text()

        if len(in_select) == 1 and len(out_select) == 1:
            if (self.in_convert_list.row(in_select[0]) < 8 and self.out_convert_list.row(out_select[0]) < 8) or (self.in_convert_list.row(in_select[0]) > 8 and self.out_convert_list.row(out_select[0]) > 8 and self.in_convert_list.row(in_select[0]) < 16 and self.out_convert_list.row(out_select[0]) < 16):
                if len(input_number) > 0:
                    input_number = int(input_number)
                    if in_select[0].data(QtCore.Qt.UserRole) == "1":
                        out = out_selection(out_select)
                        if out < 1:
                            display = input_number * out
                            self.display.display(display)
                        else:
                            display = input_number/(out/1)
                            self.display.display(display)
                    elif in_select[0].data(QtCore.Qt.UserRole) == "10":
                        out = out_selection(out_select)
                        if out < 10:
                            display = input_number * 10/out
                            self.display.display(display) 
                        else:
                            display = input_number/(out/10)
                            self.display.display(display)
                    elif in_select[0].data(QtCore.Qt.UserRole) == "100":
                        out = out_selection(out_select)
                        if out < 100:  
                            display = input_number * (100/out)
                            self.display.display(display)
                        else:
                            display = input_number/(out/100)
                            self.display.display(display)
                    elif in_select[0].data(QtCore.Qt.UserRole) == "1000":
                        out = out_selection(out_select)
                        if out < 1000:
                            display = input_number * (1000/out)
                            self.display.display(display)
                        else:
                            display = input_number/(out/1000)
                            self.display.display(display)
                    elif in_select[0].data(QtCore.Qt.UserRole) == "10000":
                        out = out_selection(out_select)
                        if out < 10000:
                            display = input_number * (10000/out)
                            self.display.display(display)
                        else:
                            display = input_number/(out/10000)
                            self.display.display(display)
                    elif in_select[0].data(QtCore.Qt.UserRole) == "100000":
                        out = out_selection(out_select)
                        if out < 100000:
                            display = input_number * (100000/out)
                            self.display.display(display)
                        else:
                            display = input_number/(out/100000)
                            self.display.display(display)
                    elif in_select[0].data(QtCore.Qt.UserRole) == "1000000":
                        out = out_selection(out_select)
                        if out < 1000000:
                            display = input_number * (1000000/out)
                            self.display.display(display)
                        else:
                            display = input_number/(out/1000000)
                            self.display.display(display)    
                    else:
                        print('Error, probably nothing select in In List')
                else:
                    print("You don't enter something in input field!")
            
            elif (self.in_convert_list.row(in_select[0]) > 16 and self.out_convert_list.row(out_select[0]) > 16 and self.in_convert_list.row(in_select[0]) < 22 and self.out_convert_list.row(out_select[0]) < 22):
                if len(input_number) > 0:
                    input_number = int(input_number)
                    if out_select[0].data(QtCore.Qt.UserRole) == "Kelv":
                        cels = to_celsius(in_select, input_number)
                        display = cels + 273.15
                        self.display.display(display)
                    elif out_select[0].data(QtCore.Qt.UserRole) == "Cels":
                        cels = to_celsius(in_select, input_number)
                        display = cels
                        self.display.display(display)
                    elif out_select[0].data(QtCore.Qt.UserRole) == "Far":
                        cels = to_celsius(in_select, input_number)
                        display = (cels * 1.8) + 32
                        self.display.display(display)
                    elif out_select[0].data(QtCore.Qt.UserRole) == "Newt":
                        cels = to_celsius(in_select, input_number)
                        display = cels * 0.33
                        self.display.display(display)
                    elif out_select[0].data(QtCore.Qt.UserRole) == "Reaum":
                        cels = to_celsius(in_select, input_number)
                        display = cels/1.25
                        self.display.display(display)
                    else:
                        print('Error, probably nothing select in Out List!')
                else:
                    print("You don't enter something in input field!")
                
            else:
                self.display.display("error")
                print("You can't transform different messures with different domains.")
        else:
            print("You can't transform a messure in nothing !?")        

# Run App

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open('basic_styles.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
