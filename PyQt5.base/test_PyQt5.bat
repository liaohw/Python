
:����PyQt5�������ļ�

:�ر���ʾ���ʹ����������ִ��ǰ����ʾ
@ echo off

cd E:\BaiduYunSyncDisk\SyncForBak\GitHub\Python\PyQt5.base
e:
echo ----complied pyqt5.ui to *.py
call C:\Python34\Lib\site-packages\PyQt5\pyuic5.bat test.ui -o Ui_test.py


echo ----py2exe
python setup.py


cd dist
echo ----begin test.exe
test

:pause

