# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(417, 520)
        Form.setMinimumSize(QtCore.QSize(417, 520))
        Form.setMaximumSize(QtCore.QSize(417, 520))
        self.remainedBrowser = QtWidgets.QTextBrowser(Form)
        self.remainedBrowser.setGeometry(QtCore.QRect(50, 30, 321, 111))
        self.remainedBrowser.setObjectName("remainedBrowser")
        self.selectedBrowser = QtWidgets.QTextBrowser(Form)
        self.selectedBrowser.setGeometry(QtCore.QRect(50, 190, 321, 111))
        self.selectedBrowser.setObjectName("selectedBrowser")
        self.errorBrowser = QtWidgets.QTextBrowser(Form)
        self.errorBrowser.setGeometry(QtCore.QRect(50, 350, 321, 101))
        self.errorBrowser.setObjectName("errorBrowser")
        self.secondLine = QtWidgets.QFrame(Form)
        self.secondLine.setGeometry(QtCore.QRect(0, 310, 421, 16))
        self.secondLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.secondLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.secondLine.setObjectName("secondLine")
        self.firstLine = QtWidgets.QFrame(Form)
        self.firstLine.setGeometry(QtCore.QRect(0, 150, 421, 20))
        self.firstLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.firstLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.firstLine.setObjectName("firstLine")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 10, 321, 21))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ramainedLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ramainedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ramainedLabel.setObjectName("ramainedLabel")
        self.verticalLayout.addWidget(self.ramainedLabel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 170, 321, 21))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selectedLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.selectedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectedLabel.setObjectName("selectedLabel")
        self.verticalLayout_2.addWidget(self.selectedLabel)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(50, 330, 321, 21))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.errorLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout_3.addWidget(self.errorLabel)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 460, 321, 48))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.intervalTimeTitle = QtWidgets.QLabel(self.formLayoutWidget)
        self.intervalTimeTitle.setObjectName("intervalTimeTitle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.intervalTimeTitle)
        self.startTimeTitle = QtWidgets.QLabel(self.formLayoutWidget)
        self.startTimeTitle.setObjectName("startTimeTitle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.startTimeTitle)
        self.intervalTime = QtWidgets.QLabel(self.formLayoutWidget)
        self.intervalTime.setText("")
        self.intervalTime.setObjectName("intervalTime")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.intervalTime)
        self.startTime = QtWidgets.QLabel(self.formLayoutWidget)
        self.startTime.setText("")
        self.startTime.setObjectName("startTime")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.startTime)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "status window"))
        self.ramainedLabel.setText(_translate("Form", "remained"))
        self.selectedLabel.setText(_translate("Form", "selected"))
        self.errorLabel.setText(_translate("Form", "error"))
        self.intervalTimeTitle.setText(_translate("Form", "距離下次執行的剩餘時間"))
        self.startTimeTitle.setText(_translate("Form", "距離設定執行的剩餘時間"))