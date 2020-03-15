from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, QThread
from tatungSpider import tatungSpider
from statusUi import Ui_Form

import traceback


class StatusWindow(QWidget):
    startSignal = QtCore.pyqtSignal()
    
    def __init__(self, account, password, codeSet, startDateTime, intervalTime):
        super(StatusWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.modifyIntervalTime('--')
        self.modifyStartTime('--')
  
        self.account = account
        self.password = password
        self.codeSet = codeSet
        self.startDateTime = startDateTime
        self.intervalTime = intervalTime
        self.spider = None
        
        self.startStartTime()
  
  
    def startStartTime(self):
        if self.startDateTime != None:
            self.timer = StartTimer(self.startDateTime, self.startSpider,
                                    self.addError, self.modifyStartTime)
        else:
            self.timer = TempTimer(self.startSpider)

    
    def startInterval(self):
        self.timer = IntervalTimer(self.intervalTime, self.startSpider,
                                   self.modifyIntervalTime)
        
        
    def startSpider(self):
        try:
            if self.spider == None:
                self.spider = tatungSpider()
                self.spider.login(self.account, self.password)
                
            selectedCodeSet = self.spider.submitCourseCodeWithCheckExpire(self.codeSet, self.account, self.password)
            remainedCodeSet = self.codeSet.difference(selectedCodeSet)
            self.addSelected(selectedCodeSet)
            if len(remainedCodeSet) == 0:
                self.addRemained({'done'})
            else:
                self.addRemained(remainedCodeSet)
                if self.intervalTime != None:
                    self.codeSet = remainedCodeSet
                    self.startInterval()
        except Exception as e:
            self.addError(str(e))
            #self.addError(traceback.format_exc())
            
        
    def addRemained(self, codeSet):
        codeString = ''
        for code in codeSet:
            codeString = codeString + code + '\n'
        self.removeRemained()
        self.ui.remainedBrowser.append(codeString)
       
        
    def removeRemained(self):
        self.ui.remainedBrowser.clear()
       
   
    def addSelected(self, codeSet):
        codeString = ''
        for code in codeSet:
            codeString = codeString + code + '\n'
        if codeString != '':
            self.ui.selectedBrowser.append(codeString)
        else:
            self.ui.selectedBrowser.append('no selected')

        
    def removeSelected(self):
        self.ui.selectedBrowser.clear()

        
    def addError(self, text):
        self.removeError()
        self.ui.errorBrowser.append(text)

        
    def removeError(self):
        self.ui.errorBrowser.clear()
       

    def modifyIntervalTime(self, text):
        self.ui.intervalTime.setText(text)
        
        
    def modifyStartTime(self, text):
        self.ui.startTime.setText(text)

    

class TempTimer(QtCore.QObject):     #alternative solution to QThread 
    def __init__(self, nextFun):
        super(TempTimer, self).__init__()
        self.nextFun = nextFun
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkTime)
        self.timer.start(1000)
        
    def checkTime(self):
        self.timer.stop()
        self.nextFun()
        

    

class StartTimer(QtCore.QObject):
    def __init__(self, startDateTime, nextFun, errorFun, modifyStartTimeFun):
        if startDateTime < QtCore.QDateTime.currentDateTime():
            errorFun('start time error')
        else:
            super(StartTimer, self).__init__()
            self.nextFun = nextFun
            self.errorFun = errorFun
            self.modifyStartTimeFun = modifyStartTimeFun
            
            self.startDateTime = startDateTime
            self.offset = startDateTime.toSecsSinceEpoch() - QtCore.QDateTime.currentDateTime().toSecsSinceEpoch()
            self.second = self.offset % 60
            self.minute = int(self.offset / 60) % 60
            self.hour = int(self.offset / 3600)
            
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.checkTime)
            self.timer.start(1000)
        
        
    def checkTime(self):
        if self.offset == 0:
            self.timer.stop()
            self.nextFun()
        else:
            self.offset = self.offset - 1
            self.second = self.second - 1
            
            if self.second < 0:
                self.minute = self.minute - 1
                self.second = 59
                if self.minute >= 0 and self.minute % 10 == 0: #make time accurate
                    self.offset = self.startDateTime.toSecsSinceEpoch() - QtCore.QDateTime.currentDateTime().toSecsSinceEpoch()
                    self.second = self.offset % 60
                    self.minute = int(self.offset / 60) % 60
                    self.hour = int(self.offset / 3600)
                
            if self.minute < 0:
                self.hour = self.hour - 1
                self.minute = 59
                
            self.modifyStartTimeFun('{0:02d}:{1:02d}:{2:02d}'.format(self.hour, self.minute, self.second))
            
            
class IntervalTimer(QtCore.QObject):
    def __init__(self, intervalTime, nextFun, modifyIntervalTimeFun):
        super(IntervalTimer, self).__init__()
        self.intervalTime = intervalTime
        self.zeroTime = QtCore.QTime(0, 0, 0)
        self.modifyIntervalTimeFun = modifyIntervalTimeFun
        self.nextFun = nextFun
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkTime)
        self.timer.start(1000)
        
        
    def checkTime(self):
        self.modifyIntervalTimeFun('{0:02d}:{1:02d}:{2:02d}'.format(self.intervalTime.hour(),
                                    self.intervalTime.minute(), self.intervalTime.second()))
        if self.intervalTime == self.zeroTime:
            self.timer.stop()
            self.nextFun()
        else:
            self.intervalTime = self.intervalTime.addSecs(-1)



