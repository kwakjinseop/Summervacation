# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilterView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilterView(object):
    def setupUi(self, FilterView):
        FilterView.setObjectName("FilterView")
        FilterView.resize(1912, 951)
        FilterView.setStyleSheet("Grid layout")
        self.centralwidget = QtWidgets.QWidget(FilterView)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 881, 751))
        self.tableWidget.setRowCount(20000)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(890, 300, 91, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(990, 10, 891, 751))
        self.tableWidget_2.setRowCount(20000)
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(890, 350, 91, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 400, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 770, 321, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 770, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        FilterView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FilterView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1912, 26))
        self.menubar.setObjectName("menubar")
        self.menuFilterView = QtWidgets.QMenu(self.menubar)
        self.menuFilterView.setObjectName("menuFilterView")
        FilterView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FilterView)
        self.statusbar.setObjectName("statusbar")
        FilterView.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFilterView.menuAction())

        self.retranslateUi(FilterView)
        QtCore.QMetaObject.connectSlotsByName(FilterView)

    def retranslateUi(self, FilterView):
        _translate = QtCore.QCoreApplication.translate
        FilterView.setWindowTitle(_translate("FilterView", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FilterView", "Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FilterView", "STX"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FilterView", "Time"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FilterView", "Checksum"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FilterView", "Reserved"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("FilterView", "Length"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("FilterView", "Payload"))
        self.comboBox.setItemText(0, _translate("FilterView", "STX"))
        self.comboBox.setItemText(1, _translate("FilterView", "Time"))
        self.comboBox.setItemText(2, _translate("FilterView", "Checksum"))
        self.comboBox.setItemText(3, _translate("FilterView", "Reserved"))
        self.comboBox.setItemText(4, _translate("FilterView", "Length"))
        self.comboBox.setItemText(5, _translate("FilterView", "Payload"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("FilterView", "Number"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("FilterView", "STX"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("FilterView", "Time"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("FilterView", "Checksum"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("FilterView", "Reserved"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("FilterView", "Length"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("FilterView", "Payload"))
        self.pushButton.setText(_translate("FilterView", "Apply"))
        self.pushButton_2.setText(_translate("FilterView", "Apply"))
        self.menuFilterView.setTitle(_translate("FilterView", "CSV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FilterView = QtWidgets.QMainWindow()
    ui = Ui_FilterView()
    ui.setupUi(FilterView)
    FilterView.show()
    sys.exit(app.exec_())

