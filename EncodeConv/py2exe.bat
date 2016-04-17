
:编译PyQt5批处理文件

:关闭显示命令，使得所有命令执行前不显示
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

