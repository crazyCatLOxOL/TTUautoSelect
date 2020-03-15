# -*- coding: utf-8 -*-
"""
@author: CrazyCatOxO
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget,\
 QLineEdit, QTabWidget, QTableWidget, QAction, QMainWindow
from multiprocessing import Process

from mainWindowUi import Ui_tab
from schoolArrangeModule import MainArrangeUi
from statusModule import StatusWindow
from tatungSpider import tatungSpider


class myUi(QTabWidget):
    def __init__(self):
        super(myUi, self).__init__()    
		
        self.ui = Ui_tab()
        self.ui.setupUi(self)
        

        #--------------------page1 start------------------#
        self.ui.startButton.clicked.connect(self.start)
        self.ui.passwordInput.setEchoMode(QLineEdit.Password)
        #--------------------page1 end--------------------#
    
    
        #--------------------page2 start------------------#
        self.ui.arrangeButton.clicked.connect(self.startArrange)
        #--------------------page2 end--------------------#
    
    
    #--------------------page1 module start------------------#
    def start(self):
        account = self.ui.accountInput.text()
        password = self.ui.passwordInput.text()
        codeSet = set(self.ui.codeInput.toPlainText().split())
        intervalTime = None
        startDateTime = None
        
        if self.ui.intervalTimeCheckBox.isChecked():
            intervalTime = self.ui.intervalTimeEdit.time()
        if self.ui.startTimeCheckBox.isChecked():
            startDateTime = self.ui.startTimeEdit.dateTime()
        
        p = Process(target=myUi.startHandle, args=(account, password, codeSet, startDateTime, intervalTime),
                    daemon=True)
        p.start()
        
        
    def startHandle(account, password, codeSet, startDateTime, intervalTime):
        app = QtWidgets.QApplication([])
        statusWindow = StatusWindow(account, password, codeSet, startDateTime, intervalTime)
        statusWindow.show()
        app.exec_()
    #--------------------page1 module end--------------------#
    
    
    #--------------------page1 module start------------------#
    def startArrange(self):
        p = Process(target=MainArrangeUi.start, daemon=True)
        p.start()
    #--------------------page1 module end--------------------#
 
    


