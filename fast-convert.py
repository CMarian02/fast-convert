from PyQt5 import QtCore, QtGui, QtWidgets
from list_manager import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 600))
        MainWindow.setMaximumSize(QtCore.QSize(500, 600))
        MainWindow.setStyleSheet("background-color:#0C0C0C")
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
        self.title.setStyleSheet("color:#E6AF2E; font-family:Bebas Neue; font-size:45px;")

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
        self.input_line.setStyleSheet("border-radius:20px; background-color:#1E1E1E; font-family: Lato; color:white; font-size: 20px")

        #Convert Button

        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(140, 470, 211, 71))
        self.convert_button.setObjectName("convert_button")
        self.convert_button.clicked.connect(lambda:self.take_element())
        self.convert_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convert_button.setStyleSheet("border-radius:30px; background-color:#FF8F00 ; color:#FFFFFF")
       
        #Create IN/OUT Lists

        self.in_convert_list = init_in_list(self.centralwidget)
        self.out_convert_list = init_out_list(self.centralwidget)

        #DisplayZone

        self.display = QtWidgets.QLCDNumber(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(10, 380, 481, 81))
        self.display.setObjectName("display")
        self.display.setStyleSheet('border-radius: 15px; background-color:#FF8F00')


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 52, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 52, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        
        #MenuBar
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: #1E1E1E; color:#E6AF2E")
        self.menubar.setObjectName("menubar")
        self.menuHELP = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menuHELP.setFont(font)
        self.menuHELP.setObjectName("menuHELP")
        self.menuEXIT = QtWidgets.QMenu(self.menubar)
        self.menuEXIT.setObjectName("menuEXIT")
        MainWindow.setMenuBar(self.menubar)
        
        #StatusBar

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHELP.menuAction())
        self.menubar.addAction(self.menuEXIT.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fast-Convert"))
        self.title.setText(_translate("MainWindow", "Fast-Convert"))
        self.convert_button.setText(_translate("MainWindow", "Convert"))
        __sortingEnabled = self.in_convert_list.isSortingEnabled()
        self.in_convert_list.setSortingEnabled(False)

        #List IN
        item = self.in_convert_list.item(0)
        item.setText(_translate("MainWindow", "----Distance----"))
        item.setFlags(QtCore.Qt.NoItemFlags)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item = self.in_convert_list.item(1)
        item.setText(_translate("MainWindow", "mm"))
        item = self.in_convert_list.item(2)
        item.setText(_translate("MainWindow", "cm"))
        item = self.in_convert_list.item(3)
        item.setText(_translate("MainWindow", "dm"))
        item = self.in_convert_list.item(4)
        item.setText(_translate("MainWindow", "m"))
        item = self.in_convert_list.item(5)
        item.setText(_translate("MainWindow", "damm"))
        item = self.in_convert_list.item(6)
        item.setText(_translate("MainWindow", "hm"))
        item = self.in_convert_list.item(7)
        item.setText(_translate("MainWindow", "km"))
        self.in_convert_list.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.out_convert_list.isSortingEnabled()
        self.out_convert_list.setSortingEnabled(False)

        #LIST OUT
        item = self.out_convert_list.item(0)
        item.setText(_translate("MainWindow", "mm"))
        item = self.out_convert_list.item(1)
        item.setText(_translate("MainWindow", "cm"))
        item = self.out_convert_list.item(2)
        item.setText(_translate("MainWindow", "dm"))
        item = self.out_convert_list.item(3)
        item.setText(_translate("MainWindow", "m"))
        item = self.out_convert_list.item(4)
        item.setText(_translate("MainWindow", "dam"))
        item = self.out_convert_list.item(5)
        item.setText(_translate("MainWindow", "hm"))
        item = self.out_convert_list.item(6)
        item.setText(_translate("MainWindow", "km"))


        self.out_convert_list.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "IN"))
        self.label_3.setText(_translate("MainWindow", "OUT"))
        self.menuHELP.setTitle(_translate("MainWindow", "HELP"))
        self.menuEXIT.setTitle(_translate("MainWindow", "EXIT"))

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

        #Take selected items.

        in_select = self.in_convert_list.selectedItems()
        out_select = self.out_convert_list.selectedItems()
        input_number = self.input_line.text()

        if len(in_select) == 1 and len(out_select) == 1:
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
        else:
            print("You can't transform a messure in nothing !?")        

# Run App

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
