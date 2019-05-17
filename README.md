# 简要
* 个人平时开发的脚本，一般都在python2.7环境

## 01 encode_conv
* python实现的编码格式批量转换脚步[python3.4]
* 如：encode_conv.py conv_test_path GB2312 utf-8

## 02微博爬虫weibo_spider

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

## 03 匿名邮件mail_3rd
* 隐藏了发件人邮箱

## 04 json_conv
* json格式转换

## enjoy_py
* 一个例子

