from PyQt5 import QtWidgets, QtCore


def init_in_list(central_widget):
    
    in_convert_list = QtWidgets.QListWidget(central_widget)
    in_convert_list.setGeometry(QtCore.QRect(10, 80, 121, 231))
    in_convert_list.setObjectName("in_convert_list")

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
    
    return in_convert_list

def  init_out_list(central_widget):
    
    out_convert_list = QtWidgets.QListWidget(central_widget)
    out_convert_list.setGeometry(QtCore.QRect(370, 80, 121, 221))
    out_convert_list.setObjectName("out_convert_list")

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

    return out_convert_list