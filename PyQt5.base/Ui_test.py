# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyForm(object):
    def setupUi(self, MyForm):
        MyForm.setObjectName("MyForm")
        MyForm.resize(577, 169)
        self.exitButton = QtWidgets.QPushButton(MyForm)
        self.exitButton.setGeometry(QtCore.QRect(370, 130, 75, 23))
        self.exitButton.setObjectName("exitButton")
        self.label = QtWidgets.QLabel(MyForm)
        self.label.setGeometry(QtCore.QRect(20, 30, 54, 12))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(MyForm)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 471, 31))
        self.textEdit.setObjectName("textEdit")
        self.RunButton = QtWidgets.QPushButton(MyForm)
        self.RunButton.setGeometry(QtCore.QRect(370, 100, 75, 23))
        self.RunButton.setObjectName("RunButton")

        self.retranslateUi(MyForm)
        self.exitButton.clicked.connect(MyForm.close)
        QtCore.QMetaObject.connectSlotsByName(MyForm)

    def retranslateUi(self, MyForm):
        _translate = QtCore.QCoreApplication.translate
        MyForm.setWindowTitle(_translate("MyForm", "Form"))
        self.exitButton.setText(_translate("MyForm", "Exit"))
        self.label.setText(_translate("MyForm", "转换路径"))
        self.textEdit.setHtml(_translate("MyForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">E:\\BaiduYunSyncDisk\\SyncForBak\\GitHub\\Python\\encode_conv\\conv_test_path</p></body></html>"))
        self.RunButton.setText(_translate("MyForm", "Run"))

