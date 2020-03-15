# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schoolArrangeUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(876, 687)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.errorBrowser = QtWidgets.QTextBrowser(Form)
        self.errorBrowser.setMaximumSize(QtCore.QSize(16777215, 50))
        self.errorBrowser.setObjectName("errorBrowser")
        self.gridLayout.addWidget(self.errorBrowser, 4, 0, 1, 3)
        self.updateComboBoxButton = QtWidgets.QPushButton(Form)
        self.updateComboBoxButton.setMaximumSize(QtCore.QSize(16666, 50))
        self.updateComboBoxButton.setObjectName("updateComboBoxButton")
        self.gridLayout.addWidget(self.updateComboBoxButton, 4, 3, 1, 1)
        self.depBrowser = QtWidgets.QTextBrowser(Form)
        self.depBrowser.setMaximumSize(QtCore.QSize(16777215, 60))
        self.depBrowser.setObjectName("depBrowser")
        self.gridLayout.addWidget(self.depBrowser, 3, 0, 1, 4)
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
        self.gridLayout.addWidget(self.classTable, 2, 0, 1, 4)
        self.passwordInput = QtWidgets.QLineEdit(Form)
        self.passwordInput.setMaximumSize(QtCore.QSize(200, 16777215))
        self.passwordInput.setObjectName("passwordInput")
        self.gridLayout.addWidget(self.passwordInput, 1, 3, 1, 1)
        self.accountInput = QtWidgets.QLineEdit(Form)
        self.accountInput.setMaximumSize(QtCore.QSize(200, 16777215))
        self.accountInput.setObjectName("accountInput")
        self.gridLayout.addWidget(self.accountInput, 0, 3, 1, 1)
        self.accountLabel = QtWidgets.QLabel(Form)
        self.accountLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.accountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.accountLabel.setObjectName("accountLabel")
        self.gridLayout.addWidget(self.accountLabel, 0, 2, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(Form)
        self.passwordLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.passwordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 1, 2, 1, 1)
        self.depComboBox = QtWidgets.QComboBox(Form)
        self.depComboBox.setObjectName("depComboBox")
        self.gridLayout.addWidget(self.depComboBox, 0, 0, 1, 2)
        self.classComboBox = QtWidgets.QComboBox(Form)
        self.classComboBox.setObjectName("classComboBox")
        self.gridLayout.addWidget(self.classComboBox, 1, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.depComboBox, self.classComboBox)
        Form.setTabOrder(self.classComboBox, self.accountInput)
        Form.setTabOrder(self.accountInput, self.passwordInput)
        Form.setTabOrder(self.passwordInput, self.classTable)
        Form.setTabOrder(self.classTable, self.depBrowser)
        Form.setTabOrder(self.depBrowser, self.errorBrowser)
        Form.setTabOrder(self.errorBrowser, self.updateComboBoxButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "學校課表"))
        self.updateComboBoxButton.setText(_translate("Form", "更新下拉選單內容"))
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
        self.accountLabel.setText(_translate("Form", " 帳號"))
        self.passwordLabel.setText(_translate("Form", "密碼"))
