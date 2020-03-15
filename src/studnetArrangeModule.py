# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from studentArrangeUi import Ui_Form
import os
import json


class StudentWindow(QtWidgets.QWidget):
    def __init__(self, loadSelfTableSignal):
        super(StudentWindow, self).__init__()    
		
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.widgetCount = [[0] * 6 for i in range(14)]
        self.rowWidgetCountMax = [0] * 14
        self.possessedContainer = dict()
        
        for i in range(14):
            for j in range(6):
                widget = QtWidgets.QWidget()
                layout = QtWidgets.QVBoxLayout()
                widget.setLayout(layout)
                self.ui.classTable.setCellWidget(i, j, widget)
        
        header = self.ui.classTable.horizontalHeader()
        for i in range(6):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            
        self.ui.loadSelfTableButton.clicked.connect(loadSelfTableSignal)
        self.ui.clearButton.clicked.connect(self.clearButtonClicked)
        self.ui.loadButton.clicked.connect(self.loadbuttonClicked)
        self.ui.saveButton.clicked.connect(self.savebuttonClicked)
       
        
    def loadbuttonClicked(self):
        path = os.getcwd()
        saveDir = path+'\\save\\'
        fileName = self.ui.fileNameInput.text()
        
        if not os.path.exists(saveDir):
            os.mkdir(saveDir)
            
        if fileName == '':
            fileName = saveDir + 'codeJson'
        else:
            fileName = saveDir + fileName + 'Json'
        
        try:
            with open(fileName+'.txt', 'r', encoding='utf-8') as f:
                self.ui.errorBrowser.clear()
                
                for code in self.possessedContainer:
                    for button in self.possessedContainer[code]['buttonList']:
                        button.deleteLater()
                        
                self.widgetCount = [[0] * 6 for i in range(14)]
                self.rowWidgetCountMax = [0] * 14
                self.possessedContainer = dict()
                i = 0
                for line in f:
                    if i == 0:
                        code = line.strip()
                    elif i == 1:
                        text = json.loads(line)
                    elif i == 2:
                        colRowList = json.loads(line)
                        self.createButton(code, text, colRowList)
                    i = (i + 1) % 3
        except Exception as e:
            self.ui.errorBrowser.clear()
            self.ui.errorBrowser.append(str(e))
    
    
    def savebuttonClicked(self):
        path = os.getcwd()
        saveDir = path + '\\save\\'
        fileName = self.ui.fileNameInput.text()
        
        if not os.path.exists(saveDir):
            os.mkdir(saveDir)
        
        if fileName == '':
            fileName = saveDir + 'code'
        else:
            fileName = saveDir + fileName
        
        with open(fileName+'.txt', 'w') as f:
            for code in self.possessedContainer:
                f.write(code+'\n')
        
        with open(fileName+'Json.txt', 'w', encoding='utf-8') as f:
            for code in self.possessedContainer:
                f.write(code+'\n')
                json.dump(self.possessedContainer[code]['text'], f, ensure_ascii=False)
                f.write('\n')
                json.dump(self.possessedContainer[code]['colRowList'], f, ensure_ascii=False)
                f.write('\n')
                
    
    def clearButtonClicked(self):
        self.widgetCount = [[0] * 6 for i in range(14)]
        self.rowWidgetCountMax = [0] * 14
        self.possessedContainer = dict()
        
        #clean class table
        for i in range(14):
            self.ui.classTable.verticalHeader().resizeSection(i, 30)
            
            for j in range(6):
                widget = self.ui.classTable.cellWidget(i, j)
                layout = widget.layout()
                buttonList = widget.findChildren(QtWidgets.QPushButton)
                
                for button in buttonList:
                    layout.removeWidget(button)
                    button.deleteLater()
    
    
    def createButton(self, code, text, colRowList):
        if code in self.possessedContainer:
            return

        self.possessedContainer[code] = {}
        self.possessedContainer[code]['colRowList'] = colRowList
        self.possessedContainer[code]['text'] = text
        self.possessedContainer[code]['buttonList'] = []
        
        for i in range(len(colRowList)):
            row = int(colRowList[i].split()[0])
            col = int(colRowList[i].split()[1])
            
            self.widgetCount[row][col] = self.widgetCount[row][col] + 1
            self.rowWidgetCountMax[row] = max(self.rowWidgetCountMax[row], self.widgetCount[row][col])
            self.ui.classTable.verticalHeader().resizeSection(row, self.rowWidgetCountMax[row]*80)
            
            widget = self.ui.classTable.cellWidget(row, col)  
            button = QtWidgets.QPushButton(text)
            button.clicked.connect(lambda _: self.buttonClicked(self.possessedContainer.pop(code)))
            widget.layout().addWidget(button)
            self.possessedContainer[code]['buttonList'].append(button)
        

    def buttonClicked(self, subContainer):
        colRowList = subContainer['colRowList']
        buttonList = subContainer['buttonList']
    
        for button in buttonList:
            button.deleteLater()
        
        for code in colRowList:
            row = int(code.split()[0])
            col = int(code.split()[1])
            self.widgetCount[row][col] = self.widgetCount[row][col] - 1
            self.rowWidgetCountMax[row] = self.widgetCount[row][5]
            for i in range(5):
                self.rowWidgetCountMax[row] = max(self.rowWidgetCountMax[row], self.widgetCount[row][i])
            
            if self.rowWidgetCountMax[row] == 0:
                self.ui.classTable.verticalHeader().resizeSection(row, 30)
            else:
                self.ui.classTable.verticalHeader().resizeSection(row, self.rowWidgetCountMax[row]*80)
    
    