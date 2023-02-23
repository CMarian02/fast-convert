from PyQt5 import QtWidgets, QtCore


def init_in_list(central_widget):
    
    in_convert_list = QtWidgets.QListWidget(central_widget)
    in_convert_list.setGeometry(QtCore.QRect(10, 80, 121, 231))
    in_convert_list.setObjectName("in_convert_list")

    categ_in_1 = QtWidgets.QListWidgetItem()
    categ_in_1.setData(QtCore.Qt.UserRole, "DIS")
    in_convert_list.addItem(categ_in_1)

    item_in_1 = QtWidgets.QListWidgetItem()
    item_in_1.setData(QtCore.Qt.UserRole, '1')
    in_convert_list.addItem(item_in_1)

    item_in_2 = QtWidgets.QListWidgetItem()
    item_in_2.setData(QtCore.Qt.UserRole, '10')
    in_convert_list.addItem(item_in_2)

    item_in_3 = QtWidgets.QListWidgetItem()
    item_in_3.setData(QtCore.Qt.UserRole, '100')
    in_convert_list.addItem(item_in_3)

    item_in_4 = QtWidgets.QListWidgetItem()
    item_in_4.setData(QtCore.Qt.UserRole, '1000')
    in_convert_list.addItem(item_in_4)

    item_in_5 = QtWidgets.QListWidgetItem()
    item_in_5.setData(QtCore.Qt.UserRole, '10000')
    in_convert_list.addItem(item_in_5)

    item_in_6 = QtWidgets.QListWidgetItem()
    item_in_6.setData(QtCore.Qt.UserRole, '100000')
    in_convert_list.addItem(item_in_6)

    item_in_7 = QtWidgets.QListWidgetItem()
    item_in_7.setData(QtCore.Qt.UserRole, '1000000')
    in_convert_list.addItem(item_in_7)

    categ_in_2 = QtWidgets.QListWidgetItem()
    categ_in_2.setData(QtCore.Qt.UserRole, 'MASS')
    in_convert_list.addItem(categ_in_2)

    item_in_8 = QtWidgets.QListWidgetItem()
    item_in_8.setData(QtCore.Qt.UserRole, '1')
    in_convert_list.addItem(item_in_8)

    item_in_9 = QtWidgets.QListWidgetItem()
    item_in_9.setData(QtCore.Qt.UserRole, '10')
    in_convert_list.addItem(item_in_9)

    item_in_10 = QtWidgets.QListWidgetItem()
    item_in_10.setData(QtCore.Qt.UserRole, '100')
    in_convert_list.addItem(item_in_10)

    item_in_11 = QtWidgets.QListWidgetItem()
    item_in_11.setData(QtCore.Qt.UserRole, '1000')
    in_convert_list.addItem(item_in_11)

    item_in_12 = QtWidgets.QListWidgetItem()
    item_in_12.setData(QtCore.Qt.UserRole, '10000')
    in_convert_list.addItem(item_in_12)

    item_in_13 = QtWidgets.QListWidgetItem()
    item_in_13.setData(QtCore.Qt.UserRole, '100000')
    in_convert_list.addItem(item_in_13)

    item_in_14 = QtWidgets.QListWidgetItem()
    item_in_14.setData(QtCore.Qt.UserRole, '1000000')
    in_convert_list.addItem(item_in_14)

    return in_convert_list

def  init_out_list(central_widget):
    
    out_convert_list = QtWidgets.QListWidget(central_widget)
    out_convert_list.setGeometry(QtCore.QRect(370, 80, 121, 221))
    out_convert_list.setObjectName("out_convert_list")

    categ_out_1 = QtWidgets.QListWidgetItem()
    categ_out_1.setData(QtCore.Qt.UserRole, "DIS")
    out_convert_list.addItem(categ_out_1)

    item_out_1 = QtWidgets.QListWidgetItem()
    item_out_1.setData(QtCore.Qt.UserRole, '1')
    out_convert_list.addItem(item_out_1)

    item_out_2 = QtWidgets.QListWidgetItem()
    item_out_2.setData(QtCore.Qt.UserRole, '10')
    out_convert_list.addItem(item_out_2)

    item_out_3 = QtWidgets.QListWidgetItem()
    item_out_3.setData(QtCore.Qt.UserRole, '100')
    out_convert_list.addItem(item_out_3)

    item_out_4 = QtWidgets.QListWidgetItem()
    item_out_4.setData(QtCore.Qt.UserRole, '1000')
    out_convert_list.addItem(item_out_4)

    item_out_5 = QtWidgets.QListWidgetItem()
    item_out_5.setData(QtCore.Qt.UserRole, '10000')
    out_convert_list.addItem(item_out_5)

    item_out_6 = QtWidgets.QListWidgetItem()
    item_out_6.setData(QtCore.Qt.UserRole, '100000')
    out_convert_list.addItem(item_out_6)

    item_out_7 = QtWidgets.QListWidgetItem()
    item_out_7.setData(QtCore.Qt.UserRole, '1000000')
    out_convert_list.addItem(item_out_7)

    categ_out_2 = QtWidgets.QListWidgetItem()
    categ_out_2.setData(QtCore.Qt.UserRole, 'MASS')
    out_convert_list.addItem(categ_out_2)

    item_out_8 = QtWidgets.QListWidgetItem()
    item_out_8.setData(QtCore.Qt.UserRole, '1')
    out_convert_list.addItem(item_out_8)

    item_out_9 = QtWidgets.QListWidgetItem()
    item_out_9.setData(QtCore.Qt.UserRole, '10')
    out_convert_list.addItem(item_out_9)

    item_out_10 = QtWidgets.QListWidgetItem()
    item_out_10.setData(QtCore.Qt.UserRole, '100')
    out_convert_list.addItem(item_out_10)

    item_out_11 = QtWidgets.QListWidgetItem()
    item_out_11.setData(QtCore.Qt.UserRole, '1000')
    out_convert_list.addItem(item_out_11)

    item_out_12 = QtWidgets.QListWidgetItem()
    item_out_12.setData(QtCore.Qt.UserRole, '10000')
    out_convert_list.addItem(item_out_12)

    item_out_13 = QtWidgets.QListWidgetItem()
    item_out_13.setData(QtCore.Qt.UserRole, '100000')
    out_convert_list.addItem(item_out_13)

    item_out_14 = QtWidgets.QListWidgetItem()
    item_out_14.setData(QtCore.Qt.UserRole, '1000000')
    out_convert_list.addItem(item_out_14)
    
    return out_convert_list