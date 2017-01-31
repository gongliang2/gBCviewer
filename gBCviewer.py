# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 20:51:35 2017

@author: gongliang2
"""

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from gBCviewerUI import Ui_MainWindow
import numpy as np
import os, sys
import csv


class tableModle(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super(tableModle, self).__init__()
        self.dataIn = None
        self.__rowNumber = 0
        self.__columnNumber = 0
        self.__showDiff = False
    
    def update(self, dataIn, showDiff):
        if len(dataIn) > 0:
            self.dataIn = dataIn
            self.__showDiff = showDiff
            self.__rowNumber = len(self.dataIn)
            if type(self.dataIn) is np.ndarray:     # a binary file with fix line length and fix format
                self.__columnNumber = len(self.dataIn[0])
            elif type(self.dataIn) is list:     # a CSV file with variable line length
                lens = [len(one) for one in self.dataIn]
                self.__columnNumber = max(lens)
            else:
                self.__columnNumber = 0
                
    def updateShowDiff(self, showDiff):
        self.__showDiff = showDiff
        
    def rowCount(self, parent=QtCore.QModelIndex()):
        return self.__rowNumber
        
    def columnCount(self, parent=QtCore.QModelIndex()):
        return self.__columnNumber
            
    def data(self, index, role):
        if index.row() < len(self.dataIn) and index.column() < len(self.dataIn[index.row()]):
            if role == QtCore.Qt.DisplayRole:            
                return str(self.dataIn[index.row()][index.column()])
            elif self.__showDiff and role == QtCore.Qt.BackgroundColorRole:
                if index.row() > 0:
                    if (index.column() < len(self.dataIn[index.row()-1]) and (self.dataIn[index.row()][index.column()] != self.dataIn[index.row()-1][index.column()])) \
                    or (index.column() >= len(self.dataIn[index.row()-1]) and self.dataIn[index.row()][index.column()]):
                        return QtGui.QBrush(QtCore.Qt.yellow)


class gBCviewer(QtWidgets.QMainWindow, Ui_MainWindow):
    """ a binary and CSV file viewer!"""
    
    version = 'V0.001'
    
    def __init__(self):
        super(gBCviewer, self).__init__()
        
        # Set up the user interface from Designer.
        self.setupUi(self)
        self.setWindowTitle(self.windowTitle() + 4*' ' + '-' + 4*' ' + gBCviewer.version)
        self.le_file.returnPressed.connect(self.tryOpenFile)
        self.cb_diff.clicked.connect(self.updateShowDiffState)
        
        self.data2View = None
        
        self.__myModel = tableModle(self)
        self.__table = None
        
        self.__formatDic = {'i1':np.int8, 'i2':np.int16, 'i4':np.int32, 'i8':np.int64,
                            'u1':np.uint8, 'u2':np.uint16, 'u4':np.uint32, 'u8':np.uint64,
                            'f2':np.float16, 'f4':np.float32, 'f8':np.float64}      
        
        
        
    
    def tryOpenFile(self):
        if not self.le_format.text():
            QtWidgets.QMessageBox.information(self, 'info', 'Please input first the file format!', QtWidgets.QMessageBox.Ok)
        elif not self.le_file.text():
            self.browse_folder()
        else:
            self.openFile()        

    def browse_folder(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Pick a file")
        if file and file[0]: # if user didn't pick a directory don't continue
            self.le_file.setText(file[0])
            self.openFile()
    
    def openFile(self):
        if self.le_file.text() and os.path.isfile(self.le_file.text()):
            filePath = self.le_file.text()
            if self.cb_csv.isChecked():
                with open(filePath, 'r') as csvfile:
                    csvReader = csv.reader(csvfile, delimiter=self.le_format.text())
                    #self.data2View = [[two.strip() for two in one] for one in csvReader]
                    self.data2View = [one for one in csvReader]
            else:
                inType = self.getFormat() #np.dtype([('time', np.uint32), ('value', np.float32)])
                if inType:
                    self.data2View = np.fromfile(filePath, dtype=inType)
                else:
                    QtWidgets.QMessageBox.warning(self, 'warning', 'Can not get the right format. Please, check the inputed format.')
                    
            if len(self.data2View) > 0:
                if self.__table:
                    self.verticalLayout.removeWidget(self.__table)
                self.__myModel.update(self.data2View, self.cb_diff.isChecked())
                self.__table = QtWidgets.QTableView(self.centralwidget)
                self.__table.setModel(self.__myModel)
                self.verticalLayout.addWidget(self.__table)
                
            
    
    def getFormat(self):
        typeList = []
        if self.le_format.text():
            formatTxt = self.le_format.text().strip()
            items = formatTxt.split(';')
            for one in items:
                formats = one.split(':')
                if len(formats) == 1 and formats[0] in self.__formatDic:
                    typeList.append(('', self.__formatDic[formats[0]]))
                elif len(formats) == 2 and formats[1] in self.__formatDic:
                    typeList.append((formats[0], self.__formatDic[formats[1]]))
                else:
                    typeList.clear()
                    break
                
        return np.dtype(typeList)
        
    def updateShowDiffState(self):
        self.__myModel.updateShowDiff(self.cb_diff.isChecked())
                    
                    


def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    viewer = gBCviewer()  # We set the form to be the viewer
    viewer.show()  # Show the form
    sys.exit(app.exec_())  # and execute the app
    

if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function