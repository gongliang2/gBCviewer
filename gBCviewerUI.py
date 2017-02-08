# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gBCviewerUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 46)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_diff = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_diff.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cb_diff.setChecked(True)
        self.cb_diff.setObjectName("cb_diff")
        self.horizontalLayout.addWidget(self.cb_diff)
        self.cb_csv = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_csv.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cb_csv.setObjectName("cb_csv")
        self.horizontalLayout.addWidget(self.cb_csv)
        self.label_format = QtWidgets.QLabel(self.centralwidget)
        self.label_format.setObjectName("label_format")
        self.horizontalLayout.addWidget(self.label_format)
        self.le_format = QtWidgets.QLineEdit(self.centralwidget)
        self.le_format.setEnabled(True)
        self.le_format.setObjectName("le_format")
        self.horizontalLayout.addWidget(self.le_format)
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setObjectName("label_file")
        self.horizontalLayout.addWidget(self.label_file)
        self.le_file = QtWidgets.QLineEdit(self.centralwidget)
        self.le_file.setDragEnabled(True)
        self.le_file.setObjectName("le_file")
        self.horizontalLayout.addWidget(self.le_file)
        self.label_filter = QtWidgets.QLabel(self.centralwidget)
        self.label_filter.setObjectName("label_filter")
        self.horizontalLayout.addWidget(self.label_filter)
        self.le_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.le_filter.setObjectName("le_filter")
        self.horizontalLayout.addWidget(self.le_filter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gBCviewer"))
        self.cb_diff.setText(_translate("MainWindow", "diff"))
        self.cb_csv.setText(_translate("MainWindow", "CSV"))
        self.label_format.setText(_translate("MainWindow", "format"))
        self.label_file.setText(_translate("MainWindow", "file"))
        self.label_filter.setText(_translate("MainWindow", "filter"))

