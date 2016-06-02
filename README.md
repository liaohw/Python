# 一、Python
    liaohw's python

## 1.1、`encode_conv`
* python实现的编码格式批量转换脚步[python3.4]
* 如：encode_conv.py conv_test_path GB2312 utf-8

## 1.2、`weibo_spider`

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

## 1.2、`enjoy_py`

# 二、PyQt5
    通过PyQt5将写好的python脚步在Py2exe下转换成可以在windows下可执行的工具；
    可以通过Eric开发更方便；
    【PyQt5.base】基础版本，PyQt5+Py2exe+Eric+Python3.4
## 2.1、`EncodeConv`
* py2exe.bat批处理，通过ui生成界面代码，并生成可执行工具dist\EncodeConv.exe；

    编译过程如下图：

![py2exe.bat批处理](https://github.com/liaohw/Python/blob/master/EncodeConv/res/py2exe.jpg)

* EncodeConv.py实现了编码格式转换逻辑；

    执行过程如下图：

![EncodeConv.exe执行](https://github.com/liaohw/Python/blob/master/EncodeConv/res/runExe.jpg)



