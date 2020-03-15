# -*- coding: utf-8 -*-
"""
@author: CrazyCatOxO
"""

from PyQt5 import QtWidgets, QtCore
from lxml import html
import requests

from studnetArrangeModule import StudentWindow
from schoolArrangeUi import Ui_Form
from tatungSpider import tatungSpider

class MainArrangeUi(QtWidgets.QWidget):
    loadSelfTableSignal = QtCore.pyqtSignal()
    
    def __init__(self):
        super(MainArrangeUi, self).__init__()    
		
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.accountInput.setMaxLength(9)
        self.ui.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.depComboBox.currentTextChanged.connect(self.depComboBoxChanged)
        self.ui.classComboBox.currentTextChanged.connect(self.classComboBoxChanged)
        self.ui.updateComboBoxButton.clicked.connect(self.updateComboBoxButtonClicked)
        self.loadSelfTableSignal.connect(self.loadSelfTable)
        self.studentWindow = StudentWindow(self.loadSelfTableSignal)
        self.studentWindow.show()
        
        self.spider = tatungSpider()      #for tatung spider
        self.isInitial = False   #prevent combobox from changing when window is open
        
        header = self.ui.classTable.horizontalHeader()
        for i in range(6):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        for i in range(14):
            for j in range(6):
                widget = QtWidgets.QWidget()
                layout = QtWidgets.QVBoxLayout()
                widget.setLayout(layout)
                self.ui.classTable.setCellWidget(i, j, widget)
        
        try:
            with open('./departmentCode/departmentCodeAndName.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    self.ui.depComboBox.addItem(line.strip())
                self.ui.depComboBox.addItem('general 通識')
        except Exception as e:
            self.ui.errorBrowser.append(str(e))

        
    def depComboBoxChanged(self, text):  
        self.ui.classComboBox.clear()
        depName = text.split()[0]
        
        if depName == 'general':
            self.viewGeneral()
        else:
            try:
                with open('./departmentCode/'+depName+'.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        self.ui.classComboBox.addItem(line.strip())
            except Exception as e:
                self.ui.errorBrowser.append(str(e))
    
    def loadSelfTable(self):
        selfTableUrl = 'https://stucis.ttu.edu.tw/selcourse/Schedule.php'
        response = self.spider.get(selfTableUrl)
        
        if not self.checkLogin(response): #if login fail
            return
    
        tree = html.fromstring(response.content)
        rows = tree.xpath('//table[@class="cistab"]/tr[position() > 1]')
        
        numOfCols = len(tree.xpath('//table[@class="cistab"]/tr[1]/td')) - 2
        container = dict()
        rowIndex = self.findStartingRowNum(rows[0].xpath('./td[last()]/text()')[0])
        
        for row in rows:
            cols = row.xpath('./td[position() < last()]')
            rowWidgetCountMax = 0
            colIndex = numOfCols
            
            for col in cols:
                codeNamePlaceList = col.xpath('./text()')   #containes code, name and place
                if len(codeNamePlaceList) != 1:
                    codeNamePlaceList = listRemoveAll(codeNamePlaceList, '\n')
                    codeNamePlaceList = listRemoveAll(codeNamePlaceList, '\n ')
                    
                    for i in range(0, len(codeNamePlaceList), 3):
                        code = codeNamePlaceList[i]
                        name = codeNamePlaceList[i + 1]
                        place = codeNamePlaceList[i + 2]
                        text = code + '\n' + name + '\n' + place
                        colRow = str(rowIndex) + ' ' + str(colIndex)
                        if code not in container:
                            container[code] = {'text': text,
                                               'colRowList': [colRow]}
                        else:
                            container[code]['colRowList'].append(colRow)
                            
                colIndex = colIndex - 1
            rowIndex = rowIndex + 1
            
        for code in container:
            #self.studentWindow.createButtonSignal.emit(code, container[code]['text'], container[code]['colRowList'])
            self.studentWindow.createButton(code, container[code]['text'], container[code]['colRowList'])
            



    def classComboBoxChanged(self, text):
        if not self.isInitial:  #prevent initial preparation from triggering this event
            self.isInitial = True
            return
        
        if text == '': #prevent empty text if depComboBox is changed
            return
            
        viewClassUrl = 'https://stucis.ttu.edu.tw/selcourse/ViewClass.php'
        data = {'SelDepNo': self.ui.depComboBox.currentText().split()[0], 
                'SelClassNo': text.split()[0]}
        response = self.spider.post(viewClassUrl, data=data)
        
        if not self.checkLogin(response): #if login fail
            return

        self.arrangeTable(response)
    
    
    def viewGeneral(self):
        viewGeneralUrl = 'https://stucis.ttu.edu.tw/selcourse/ViewGeneral.php'
        response = self.spider.get(viewGeneralUrl)
        
        if not self.checkLogin(response): #if login fail
            return
        
        self.arrangeTable(response)
        
        
    def arrangeTable(self, response):
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
        
        tree = html.fromstring(response.content)
        rows = tree.xpath('//table[@class="cistab"]/tr[position() > 1]')
        numOfCols = len(tree.xpath('//table[@class="cistab"]/tr[1]/td')) - 2
        rowIndex = self.findStartingRowNum(rows[0].xpath('./td[last()]/text()')[0])
        self.colRowContainer = dict()
        
        for row in rows:
            cols = row.xpath('./td[position() < last()]')
            rowWidgetCountMax = 0
            colIndex = numOfCols
            
            for col in cols:
                codeAndPlaceList = col.xpath('./text()') #containes code and place
                nameList = col.xpath('./a/text()')       #containes course name
                length = len(nameList)
                rowWidgetCountMax = max(rowWidgetCountMax, length)
                
                widget = QtWidgets.QWidget()
                layout = QtWidgets.QVBoxLayout()
                
                for i in range(length):
                    code = codeAndPlaceList[i*2].strip()
                    
                    if code not in self.colRowContainer:
                        self.colRowContainer[code] = [str(rowIndex)+' '+str(colIndex)]
                    else:
                        self.colRowContainer[code].append(str(rowIndex)+' '+str(colIndex))
                    
                    place = codeAndPlaceList[i*2+1]
                    text = code + '\n' + nameList[i] + '\n' + place
                    button = QtWidgets.QPushButton(text)
                    button.clicked.connect(lambda _,code=code,text=text,codeList=self.colRowContainer[code]: self.studentWindow.createButton(code,text,codeList))
 
                    layout.addWidget(button)
                    
                widget.setLayout(layout)
                self.ui.classTable.setCellWidget(rowIndex, colIndex, widget)
                colIndex = colIndex - 1
            
            if rowWidgetCountMax == 0:
                self.ui.classTable.verticalHeader().resizeSection(rowIndex, 30)
            else:
                self.ui.classTable.verticalHeader().resizeSection(rowIndex, rowWidgetCountMax*80)
            rowIndex = rowIndex + 1
    
    
    def updateComboBoxButtonClicked(self):
        checkExpiredUrl = 'https://stucis.ttu.edu.tw/selcourse/ListClassCourse.php'
        response = self.spider.get(checkExpiredUrl)
        
        if not self.checkLogin(response): #if login fail
            return
        
        self.spider.updateAllData()
        
        try:
            with open('./departmentCode/departmentCodeAndName.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    self.ui.depComboBox.addItem(line.strip())
                self.ui.depComboBox.addItem('general 通識')
        except Exception as e:
            self.ui.errorBrowser.append(str(e))


    def checkLogin(self, response):
        isLoginSuccessed = False
        try:
            self.spider.checkExpire(response)
        except Exception as e:
            try:
                self.spider.login(self.ui.accountInput.text(),
                                  self.ui.passwordInput.text())
                isLoginSuccessed = True
            except Exception as e:
                self.ui.errorBrowser.append(str(e))
                return False
        
        if isLoginSuccessed:
            self.ui.errorBrowser.append('login successfully')
            return False
            
        return True
        
    
    def findStartingRowNum(self, word):
        if word == '第一節':
            return 0
        elif word == '第二節':
            return 1
        elif word == '第三節':
            return 2
        elif word == '第四節':
            return 3
        elif word == '中\u3000午':
            return 4
        elif word == '第五節':
            return 5
        elif word == '第六節':
            return 6
        elif word == '第七節':
            return 7
        elif word == '第八節':
            return 8
        elif word == '傍\u3000晚':
            return 9
        elif word == '第九節':
            return 10
        elif word == '第10節':
            return 11
        elif word == '第11節':
            return 12
        elif word == '第12節':
            return 13
    

    def start():
        app = QtWidgets.QApplication([])
        window = MainArrangeUi()
        window.show()
        app.exec_()
        
    
def listRemoveAll(myList, value):
    return list(filter((value).__ne__, myList))