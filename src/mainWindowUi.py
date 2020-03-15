# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tab(object):
    def setupUi(self, tab):
        tab.setObjectName("tab")
        tab.setWindowModality(QtCore.Qt.WindowModal)
        tab.resize(400, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tab.sizePolicy().hasHeightForWidth())
        tab.setSizePolicy(sizePolicy)
        tab.setMinimumSize(QtCore.QSize(400, 400))
        tab.setMaximumSize(QtCore.QSize(400, 500))
        tab.setToolTip("<html><head/><body><p><br/></p></body></html>")
        tab.setStatusTip("")
        self.page1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page1.sizePolicy().hasHeightForWidth())
        self.page1.setSizePolicy(sizePolicy)
        self.page1.setToolTip("")
        self.page1.setObjectName("page1")
        self.codeInput = QtWidgets.QTextEdit(self.page1)
        self.codeInput.setGeometry(QtCore.QRect(30, 30, 331, 181))
        self.codeInput.setToolTip("")
        self.codeInput.setObjectName("codeInput")
        self.formLayoutWidget = QtWidgets.QWidget(self.page1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 230, 186, 130))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.accountLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.accountLabel.setObjectName("accountLabel")
        self.gridLayout.addWidget(self.accountLabel, 0, 1, 1, 1)
        self.intervalTimeCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.intervalTimeCheckBox.setText("")
        self.intervalTimeCheckBox.setObjectName("intervalTimeCheckBox")
        self.gridLayout.addWidget(self.intervalTimeCheckBox, 3, 0, 1, 1)
        self.intervalTimeEdit = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.intervalTimeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.intervalTimeEdit.setObjectName("intervalTimeEdit")
        self.gridLayout.addWidget(self.intervalTimeEdit, 3, 2, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 1, 1, 1, 1)
        self.accountInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.accountInput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.accountInput.setObjectName("accountInput")
        self.gridLayout.addWidget(self.accountInput, 0, 2, 1, 1)
        self.passwordInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordInput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passwordInput.setObjectName("passwordInput")
        self.gridLayout.addWidget(self.passwordInput, 1, 2, 1, 1)
        self.intervalTimeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.intervalTimeLabel.setObjectName("intervalTimeLabel")
        self.gridLayout.addWidget(self.intervalTimeLabel, 3, 1, 1, 1)
        self.startTimeEdit = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.startTimeEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.gridLayout.addWidget(self.startTimeEdit, 2, 2, 1, 1)
        self.startTimeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.gridLayout.addWidget(self.startTimeLabel, 2, 1, 1, 1)
        self.startTimeCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.startTimeCheckBox.setText("")
        self.startTimeCheckBox.setObjectName("startTimeCheckBox")
        self.gridLayout.addWidget(self.startTimeCheckBox, 2, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 230, 121, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startButton.setToolTip("")
        self.startButton.setToolTipDuration(-1)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        tab.addTab(self.page1, "")
        self.page2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2.sizePolicy().hasHeightForWidth())
        self.page2.setSizePolicy(sizePolicy)
        self.page2.setObjectName("page2")
        self.arrangeButton = QtWidgets.QPushButton(self.page2)
        self.arrangeButton.setGeometry(QtCore.QRect(50, 30, 91, 23))
        self.arrangeButton.setObjectName("arrangeButton")
        tab.addTab(self.page2, "")

        self.retranslateUi(tab)
        tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tab)

    def retranslateUi(self, tab):
        _translate = QtCore.QCoreApplication.translate
        tab.setWindowTitle(_translate("tab", "TTUautoselect"))
        self.accountLabel.setText(_translate("tab", "     帳號"))
        self.intervalTimeEdit.setDisplayFormat(_translate("tab", "hh:mm:ss"))
        self.passwordLabel.setText(_translate("tab", "     密碼"))
        self.intervalTimeLabel.setText(_translate("tab", "時間間隔"))
        self.startTimeEdit.setDisplayFormat(_translate("tab", "yyyy/MM/dd hh:mm"))
        self.startTimeLabel.setText(_translate("tab", "開始時間"))
        self.startButton.setText(_translate("tab", "開始"))
        tab.setTabText(tab.indexOf(self.page1), _translate("tab", "選課"))
        self.arrangeButton.setText(_translate("tab", "排課"))
        tab.setTabText(tab.indexOf(self.page2), _translate("tab", "額外功能"))
