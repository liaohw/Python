# -*- coding: utf-8 -*-

"""
Module implementing MyForm.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from Ui_EncodeConv import Ui_MyForm
import sys
import os
import chardet
import codecs

    
class MyForm(QWidget, Ui_MyForm):
    ori_decode = None
    dst_encode = None
    split_path = None
    is_convert = 1
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    
    def get_transParam(self):
        self.ori_decode = self.comboBox_ori.currentText()
        self.dst_encode = self.comboBox_new.currentText()
        self.split_path = self.comboBox_split.currentText()
        self.report_trace("[oriDecode]: "+self.ori_decode)
        self.report_trace("[dstEncode]: "+self.dst_encode)
        self.report_trace("[splitPath]: "+self.split_path)
    def report_trace(self, str):
        self.plainTextEdit.appendPlainText(str)
        myApp.processEvents();
    def file_detect(self, file):
        #过滤压缩文件
        if len(file.split(".zip")) > 1 or len(file.split(".rar")) > 1 or len(file.split(".tar")) > 1:
            return None
        fcode = chardet.detect(open(file,'rb').read())['encoding']
        if fcode == None:
            self.report_trace('--detect: file is empty')
        else:
            self.report_trace('--detect: '+fcode)
        return fcode

    def file_convert(self, file, decode, encode):
        fcode = self.file_detect(file)
        if self.is_convert == 0:
            return 
        if fcode == None:
            #self.report_trace ('empty file will not convert!')
            return 
        elif fcode == decode or decode == '*' :
            try:
                self.report_trace ('convert '+file+' : '+fcode+' --> '+encode)
                f=codecs.open(file,'r',fcode)
                file_content=f.read()
                f.close()
                codecs.open(file,'w',encode,errors="strict").write(file_content)
                #check new file
                if self.file_detect(file) == None:
                    self.report_trace ('@convert failed ! file resotre!')
                    codecs.open(file,'rb',fcode).write(file_content)
            except:
                self.report_trace ('@file convert exception!')
                #check new file
                if self.file_detect(file) == None:
                    self.report_trace ('@@convert failed ! file resotre!')
                    codecs.open(file,'rb','utf-8').write(file_content)

    def path_explore(self, path):
        for root,dirs,files in os.walk(path):
            for file in files:
                if len(root.split(self.split_path)) == 1 :
                    path_file = os.path.join(root,file)
                    self.report_trace ("******* "+file)
                    self.convert(path_file)

    # https://docs.python.org/3.4/library/codecs.html#module-codecs
    #ascii,utf-8,GB2312
    #convert utf-8 to GB2312 for source insight
    def convert(self, argv):
        if(os.path.isfile(argv)):
            self.file_convert(argv,self.ori_decode,self.dst_encode)
        elif(os.path.isdir(argv)):
            self.report_trace ("**this is a normal path:")
            self.path_explore(argv)
        else:
            self.report_trace("input path not exists! unknow deal!")

    @pyqtSlot()
    def on_DetectButton_clicked(self):
        """
        Slot documentation goes here.
        """
        fp = self.lineEdit.text()
        self.report_trace ("========================runing begin=====================")
        self.is_convert = 0
        self.convert(fp)
        self.report_trace ("========================detect end=====================")

    @pyqtSlot()
    def on_TransferButton_clicked(self):
        """
        Slot documentation goes here.
        """
        fp = self.lineEdit.text()
        self.report_trace ("========================runing begin=====================")
        self.get_transParam()
        self.is_convert = 1
        self.report_trace ("deal: "+fp)
        self.report_trace ("====runing transfer....")
        self.convert(fp)
        self.report_trace ("========================transfer end=====================")

    @pyqtSlot(str)
    def on_lineEdit_textEdited(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        self.report_trace("Path => "+p0)


if __name__ == "__main__":
    myApp = QtWidgets.QApplication(sys.argv)
    mainFrom = MyForm()
    mainFrom.show()
    sys.exit(myApp.exec_())
    
