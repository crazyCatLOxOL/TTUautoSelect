# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentArrangeUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(710, 562)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(400, 400))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.classTable = QtWidgets.QTableWidget(Form)
        self.classTable.setMinimumSize(QtCore.QSize(0, 0))
        self.classTable.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.classTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.classTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.classTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.classTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.classTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.classTable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.classTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.classTable.setObjectName("classTable")
        self.classTable.setColumnCount(6)
        self.classTable.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.classTable.setItem(5, 2, item)
        self.classTable.horizontalHeader().setCascadingSectionResizes(False)
        self.classTable.horizontalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.classTable, 0, 0, 1, 9)
        self.depBrowser = QtWidgets.QTextBrowser(Form)
        self.depBrowser.setMaximumSize(QtCore.QSize(16777215, 60))
        self.depBrowser.setObjectName("depBrowser")
        self.gridLayout.addWidget(self.depBrowser, 1, 0, 1, 9)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 7, 1, 1)
        self.fileNameInput = QtWidgets.QLineEdit(Form)
        self.fileNameInput.setObjectName("fileNameInput")
        self.gridLayout.addWidget(self.fileNameInput, 4, 8, 1, 1)
        self.loadSelfTableButton = QtWidgets.QPushButton(Form)
        self.loadSelfTableButton.setObjectName("loadSelfTableButton")
        self.gridLayout.addWidget(self.loadSelfTableButton, 4, 0, 1, 1)
        self.errorBrowser = QtWidgets.QTextBrowser(Form)
        self.errorBrowser.setMaximumSize(QtCore.QSize(16777215, 50))
        self.errorBrowser.setObjectName("errorBrowser")
        self.gridLayout.addWidget(self.errorBrowser, 3, 0, 1, 9)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 4, 5, 1, 1)
        self.loadButton = QtWidgets.QPushButton(Form)
        self.loadButton.setObjectName("loadButton")
        self.gridLayout.addWidget(self.loadButton, 4, 3, 1, 2)
        self.clearButton = QtWidgets.QPushButton(Form)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 4, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "本人課表"))
        item = self.classTable.verticalHeaderItem(0)
        item.setText(_translate("Form", "第一節"))
        item = self.classTable.verticalHeaderItem(1)
        item.setText(_translate("Form", "第二節"))
        item = self.classTable.verticalHeaderItem(2)
        item.setText(_translate("Form", "第三節"))
        item = self.classTable.verticalHeaderItem(3)
        item.setText(_translate("Form", "第四節"))
        item = self.classTable.verticalHeaderItem(4)
        item.setText(_translate("Form", "中午"))
        item = self.classTable.verticalHeaderItem(5)
        item.setText(_translate("Form", "第五節"))
        item = self.classTable.verticalHeaderItem(6)
        item.setText(_translate("Form", "第六節"))
        item = self.classTable.verticalHeaderItem(7)
        item.setText(_translate("Form", "第七節"))
        item = self.classTable.verticalHeaderItem(8)
        item.setText(_translate("Form", "第八節"))
        item = self.classTable.verticalHeaderItem(9)
        item.setText(_translate("Form", "傍晚"))
        item = self.classTable.verticalHeaderItem(10)
        item.setText(_translate("Form", "第九節"))
        item = self.classTable.verticalHeaderItem(11)
        item.setText(_translate("Form", "第10節"))
        item = self.classTable.verticalHeaderItem(12)
        item.setText(_translate("Form", "第11節"))
        item = self.classTable.verticalHeaderItem(13)
        item.setText(_translate("Form", "第12節"))
        item = self.classTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "星期一"))
        item = self.classTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "星期二"))
        item = self.classTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "星期三"))
        item = self.classTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "星期四"))
        item = self.classTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "星期五"))
        item = self.classTable.horizontalHeaderItem(5)
        item.setText(_translate("Form", "星期六"))
        __sortingEnabled = self.classTable.isSortingEnabled()
        self.classTable.setSortingEnabled(False)
        self.classTable.setSortingEnabled(__sortingEnabled)
        self.depBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" width=\"98%\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\">大樓編號</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\">A1:經營大樓</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\">A2:實驗大樓</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\">A3:挺生大樓</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\">A4:機材大樓</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\"> </span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\">A5:尚志大樓</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\">A6:德惠大樓</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\">A7:新德惠大樓</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\">A8:尚志教育館</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\"> </span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'新細明體\',\'arial\';\">A9:北設工大樓</span></p></td>\n"
"<td></td>\n"
"<td></td>\n"
"<td></td></tr></table></body></html>"))
        self.label.setText(_translate("Form", "檔案名稱:"))
        self.loadSelfTableButton.setText(_translate("Form", "匯入自己課表"))
        self.saveButton.setText(_translate("Form", "匯出"))
        self.loadButton.setText(_translate("Form", "匯入"))
        self.clearButton.setText(_translate("Form", "清除"))
