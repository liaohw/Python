
:����PyQt5�������ļ�

:�ر���ʾ���ʹ����������ִ��ǰ����ʾ
@ echo off

cd E:\BaiduYunSyncDisk\SyncForBak\GitHub\Python\EncodeConv
e:
echo ----complied pyqt5.ui to *.py
call C:\Python34\Lib\site-packages\PyQt5\pyuic5.bat EncodeConv.ui -o Ui_EncodeConv.py


echo ----py2exe
python setup.py


cd dist
echo ----begin EncodeConv.exe
EncodeConv

:pause

