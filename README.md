# 简要
    个人平时开发的脚本(python2.7)和程序(pyqt5+python3.4)
## 一、Python
    python2.7

### 1.1、encode_conv
    python实现的编码格式批量转换脚步[python3.4]
    如：encode_conv.py conv_test_path GB2312 utf-8

### 1.2、weibo_spider

    python实现的微博爬虫
    *说明：
        修改自己的微博账户cookie替代xxx，如cookie = {"Cookie": "xxx"}
    *执行脚步:
        1、输入要获取对象的微博ID(数字或字符串)，如2797679040 或 hzguidedog
        2、选择图片质量: 0 缩略图, 1 普通图, 2 高清原图
    之后开始爬虫，获取原创微博文本和和图片连接，再统一开始下载所有图片
        
    *效果如下：
        liaohw@lhw-ubuntu:~/python$ python weibo_spider.py
        请输入微博ID(数字或字符串): 1994294027
        图片质量: 0 缩略图, 1 普通图, 2 高清原图
        请输入: 2
        @微博名 :<美腿欣赏> 总共页数: 93
        该微博页数太多，只趴取前面的多少页: 
        2
        －－－－－爬虫准备就绪－－－－－
        －－－－－抓取页面:1－－－－－
        URL => http://weibo.cn/u/1994294027?filter=1&page=1
        正在文字爬取...
        ....省略开头.....
        -第30张图片 正在下载...
        -第31张图片 正在下载...
        －－－－－结果－－－－－
        1.原创微博爬取完毕，共20条，保存路径/home/liaohw/python/1994294027_美腿欣赏/weibo.txt
        2.微博图片爬取完毕，共31张，保存路径/home/liaohw/python/1994294027_美腿欣赏

### 1.3、匿名邮件
    隐藏了发件人邮箱

### 1.4、json_conv
    json格式转换

### 1.*、`enjoy_py`
    一个例子

## 二、PyQt5
    通过PyQt5将写好的python脚步在Py2exe下转换成可以在windows下可执行的工具；
    开发说明：
    1、安装python3.4
        设置环境变量3.4版本为默认
    2、安装PyQt5
        PyQt5 Desinger设计ui界面
    3、通过pip安装py2exe
        【开发方式1】：运行test_PyQt5.bat，进行ui转换和py转exe并运行测试
        【PyQt5.base】：基础版本，PyQt5+Py2exe+Eric+Python3.4
    4、eric6-6.1.4
        可以通过Eric开发更方便；
        通过eric6.py运行（第一次配置：
        1.点击编辑器->自动完成->QScintilla。勾上显示单条和使用填充符号。
        2.点击编辑器->API。语言：选择python3。
        然后从C:\Python34\Lib\site-packages\PyQt5\qsci\api\python导入eric6.api，点击编译api，点击ok）
        【开发方式2】：在eric6中直接进入PyQt5 Desinger，回到eric 6将刚才的界面文件编译，py2exe打包成exe文件
    

* [以上软件下载地址](http://pan.baidu.com/s/1c1GVhgk "百度云盘")


### 2.1、`EncodeConv`
* py2exe.bat批处理，通过ui生成界面代码，并生成可执行工具dist\EncodeConv.exe；

    编译过程如下图：

![py2exe.bat批处理](https://github.com/liaohw/Python/blob/master/EncodeConv/res/py2exe.jpg)

* EncodeConv.py实现了编码格式转换逻辑；

    执行过程如下图：

![EncodeConv.exe执行](https://github.com/liaohw/Python/blob/master/EncodeConv/res/runExe.jpg)



