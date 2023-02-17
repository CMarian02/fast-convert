from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 600))
        MainWindow.setMaximumSize(QtCore.QSize(500, 600))
        MainWindow.setStyleSheet("background-color: rgb(100, 86, 81);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(-4, 2, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.input_line = QtWidgets.QLineEdit(self.centralwidget)
        self.input_line.setGeometry(QtCore.QRect(130, 320, 241, 51))
        self.input_line.setText("")
        self.input_line.setMaxLength(30)
        self.input_line.setObjectName("input_line")
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(140, 470, 211, 71))
        self.convert_button.setObjectName("convert_button")
        self.convert_button.clicked.connect(lambda:self.take_element())
        
        #In List

        self.in_convert_list = QtWidgets.QListWidget(self.centralwidget)
        self.in_convert_list.setGeometry(QtCore.QRect(10, 80, 121, 231))
        self.in_convert_list.setObjectName("in_convert_list")
        item_in_1 = QtWidgets.QListWidgetItem()
        item_in_1.setData(QtCore.Qt.UserRole, '1')
        self.in_convert_list.addItem(item_in_1)
        item_in_2 = QtWidgets.QListWidgetItem()
        item_in_2.setData(QtCore.Qt.UserRole, '10')
        self.in_convert_list.addItem(item_in_2)
        item_in_3 = QtWidgets.QListWidgetItem()
        item_in_3.setData(QtCore.Qt.UserRole, '100')
        self.in_convert_list.addItem(item_in_3)
        item_in_4 = QtWidgets.QListWidgetItem()
        item_in_4.setData(QtCore.Qt.UserRole, '1000')
        self.in_convert_list.addItem(item_in_4)
        item_in_5 = QtWidgets.QListWidgetItem()
        item_in_5.setData(QtCore.Qt.UserRole, '10000')
        self.in_convert_list.addItem(item_in_5)
        item_in_6 = QtWidgets.QListWidgetItem()
        item_in_6.setData(QtCore.Qt.UserRole, '100000')
        self.in_convert_list.addItem(item_in_6)
        item_in_7 = QtWidgets.QListWidgetItem()
        item_in_7.setData(QtCore.Qt.UserRole, '1000000')
        self.in_convert_list.addItem(item_in_7)

        #Out List

        self.out_convert_list = QtWidgets.QListWidget(self.centralwidget)
        self.out_convert_list.setGeometry(QtCore.QRect(370, 80, 121, 221))
        self.out_convert_list.setObjectName("out_convert_list")
        item_out_1 = QtWidgets.QListWidgetItem()
        item_out_1.setData(QtCore.Qt.UserRole, '1')
        self.out_convert_list.addItem(item_out_1)
        item_out_2 = QtWidgets.QListWidgetItem()
        item_out_2.setData(QtCore.Qt.UserRole, '10')
        self.out_convert_list.addItem(item_out_2)
        item_out_3 = QtWidgets.QListWidgetItem()
        item_out_3.setData(QtCore.Qt.UserRole, '100')
        self.out_convert_list.addItem(item_out_3)
        item_out_4 = QtWidgets.QListWidgetItem()
        item_out_4.setData(QtCore.Qt.UserRole, '1000')
        self.out_convert_list.addItem(item_out_4)
        item_out_5 = QtWidgets.QListWidgetItem()
        item_out_5.setData(QtCore.Qt.UserRole, '10000')
        self.out_convert_list.addItem(item_out_5)
        item_out_6 = QtWidgets.QListWidgetItem()
        item_out_6.setData(QtCore.Qt.UserRole, '100000')
        self.out_convert_list.addItem(item_out_6)
        item_out_7 = QtWidgets.QListWidgetItem()
        item_out_7.setData(QtCore.Qt.UserRole, '1000000')
        self.out_convert_list.addItem(item_out_7)

        self.display = QtWidgets.QLCDNumber(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(10, 370, 481, 81))
        self.display.setObjectName("display")
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
        self.menubar.setStyleSheet("background-color: rgb(118, 103, 78);")
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
        item.setText(_translate("MainWindow", "mm"))
        item = self.in_convert_list.item(1)
        item.setText(_translate("MainWindow", "cm"))
        item = self.in_convert_list.item(2)
        item.setText(_translate("MainWindow", "dm"))
        item = self.in_convert_list.item(3)
        item.setText(_translate("MainWindow", "m"))
        item = self.in_convert_list.item(4)
        item.setText(_translate("MainWindow", "dam"))
        item = self.in_convert_list.item(5)
        item.setText(_translate("MainWindow", "hm"))
        item = self.in_convert_list.item(6)
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
                pass
            elif out_select[0].data(QtCore.Qt.UserRole) == "10":
                pass
            elif out_select[0].data(QtCore.Qt.UserRole) == "100":
                pass
            elif out_select[0].data(QtCore.Qt.UesrRole) == "1000":
                pass
            elif out_select[0].data(QtCore.Qt.UserRole) == "10000":
                pass
            elif out_select[0].data(QtCore.Qt.UserRole) == "100000":
                pass
            elif out_select[0].data(QtCore.Qt.UserRole) == "1000000":
                pass
            else:
                print('Error, probably nothing select in Out List')

        #Take selected items.

        in_select = self.in_convert_list.selectedItems()
        out_select = self.out_convert_list.selectedItems()

        if len(in_select) == 1 and len(out_select) == 1:
            if in_select[0].data(QtCore.Qt.UserRole) == "1":
                out_selection(out_select)
            elif in_select[0].data(QtCore.Qt.UserRole) == "10":
                out_selection(out_select)
            elif in_select[0].data(QtCore.Qt.UserRole) == "100":
                out_selection(out_select)
            elif in_select[0].data(QtCore.Qt.UserRole) == "1000":
                out_selection(out_select)
            elif in_select[0].data(QtCore.Qt.UserRole) == "10000":
                out_selection(out_select)
            elif in_select[0].data(QtCore.Qt.UserRole) == "100000":
                out_selection(out_select)
            elif in_select[0].data(QtCore.Qt.UserRole) == "1000000":
                out_selection(out_select)
            else:
                prit('Error, probably nothing select in In List')
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
