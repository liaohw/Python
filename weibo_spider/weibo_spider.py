#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
修改自己的微博账户cookie替代xxx:
    cookie = {"Cookie": "xxx"}
执行脚步:
1、输入要获取对象的微博ID(数字或字符串)，如2797679040 或 hzguidedog
2、选择图片质量: 0 缩略图, 1 普通图, 2 高清原图

之后开始爬虫，获取原创微博文本和和图片连接，再统一开始下载所有图片
'''

import re
import string
import sys
import os
import time
import urllib
import urllib2
import requests
from bs4 import BeautifulSoup
from lxml import etree


reload(sys)
sys.setdefaultencoding('UTF-8')
img_size = 1            #0 small, 1 bmiddle, 2 large(url_default)
user_id = 2797679040    #或 hzguidedog
if(len(sys.argv)>=2):
    user_id = sys.argv[1]
elif(len(sys.argv)>=3):
    user_id = sys.argv[1]
    img_size = (int)(sys.argv[2])
else:
    user_id = raw_input(u"请输入微博ID(数字或字符串): ")
    img_size = (int)(raw_input(u"图片质量: 0 缩略图, 1 普通图, 2 高清原图\n请输入: "))

cookie = {"Cookie": "xxx"}

# 获取微博名
try:
    # 普通微博ID
    url = 'http://weibo.cn/u/%s?filter=1&page=1'%user_id
    head_html = requests.get(url, cookies = cookie).content
    selector = etree.HTML(head_html)
    page_num = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
    # page_num = 1
    text = selector.xpath('//span[@class="ctt"]')[0].xpath('string(.)')
    user_name = text[0 : text.find(' ')].encode('utf-8')    #中间不是普通空格
    print "\n@微博名 :<%s> 总共页数: %d"%(user_name,page_num)
except :
    try:
        #修改过的微博ID或域名号
        url = 'http://weibo.cn/%s?filter=1&page=1'%user_id
        head_html = requests.get(url, cookies = cookie).content
        open('./tt.html','wb').write(head_html)
        selector = etree.HTML(head_html)
        page_num = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
        # page_num = 1
        text = selector.xpath('//span[@class="ctt"]')[0].xpath('string(.)')
        user_name = text[0 : text.find(' ')].encode('utf-8')    #中间不是普通空格
        print "\n@@微博名 :<%s> 总共页数: %d"%(user_name,page_num)
    except :
        print '\t查询微博名失败，请检查并从新输入!'

if page_num == 50:
    input_flag = (int)(raw_input(u"微博名获取是否有错: 1 离开, 2 重命名继续\n"))
    user_name = 'weibo'
    if input_flag == 1 :
        exit (0)
elif page_num > 5:
    _page_num = (int)(raw_input(u"该微博页数太多，只趴取前面的多少页: \n"))
    if _page_num < page_num and _page_num > 0 :
        page_num = _page_num
    else:
        print '输入页数有误!'
        exit (0)
if img_size == 0 :
    img_size_str = 'small'
elif img_size == 1 :
    img_size_str = 'bmiddle'
else :
    img_size_str = 'large'

result = '－－－－－微博用户ID : %s\n'%user_id
urllist_set = set()
weibo_count = 0
image_count = 0
filter_flag = 1 #1原创，0所有

run_path = "%s/%s_%s"%(os.getcwd(),user_id,user_name)
if os.path.exists(run_path) is False:
    os.mkdir(run_path)
word_path= run_path +'/weibo.txt'
fw = open(word_path.encode('utf-8'), "wb")
fi = open("%s/image_urls.txt"%run_path, "wb")
image_path=run_path

def do_image_url(url):
    if img_size < 2 :
        return re.sub('large',img_size_str,url)
    return url

print '－－－－－爬虫准备就绪－－－－－'
for page in range(1,page_num+1):
    print '－－－－－抓取页面:%d－－－－－'%page

    #获取lxml页面
    url = 'http://weibo.cn/u/%s?filter=%d&page=%d'%(user_id,filter_flag,page)
    print "URL => %s"%url
    page_html = requests.get(url, cookies = cookie).content

    print '正在文字爬取...'
    #文字爬取
    selector = etree.HTML(page_html)
    text_content = selector.xpath('//span[@class="ctt"]')
    # date_content = selector.xpath('//span[@class="ct"]')  #时间
    for i in range(0,len(text_content)):
        text = text_content[i].xpath('string(.)')
        if weibo_count == 0:
            text = "信息 : %s\n"%text
        elif weibo_count == 1:
            text = "签名 : %s\n"%text
        else:
            # text_date = date_content[i-2].xpath('string(.)')
            # text = "%d : %s\n\t——%s\n"%(weibo_count-1,text,text_date)
            text = "%d : %s\n"%(weibo_count-1,text)
        print " %s"%text.encode('utf-8')
        weibo_count += 1
        result = result + text
    fw.write(result)
    result = ''

    print '正在图片信息爬取...'
    #图片爬取
    soup = BeautifulSoup(page_html, "lxml")
    url_list = soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/oripic',re.I))
    for imgurl in url_list:
        # <a href="http://weibo.cn/mblog/oripic?id=DqZ4qlfOv&amp;u=a2b1309ejw1f2wmjmulamj20ku112du2">原图</a>
        imgurl = imgurl['href']
        # http://weibo.cn/mblog/oripic?id=DqZ4qlfOv&amp;u=a2b1309ejw1f2wmjmulamj20ku112du2
        imgurl = requests.get(imgurl, cookies = cookie).url
        # http://ww1.sinaimg.cn/large/a2b1309ejw1f2wmjmulamj20ku112du2.jpg
        imgurl = do_image_url(imgurl)
        urllist_set.add(imgurl)
        print ' －获取Page%d 的图片信息: %s'%(page,imgurl.encode('utf-8'))

    #图片组信息爬取
    url_group_list = soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/picAll',re.I))
    hh = 1
    for img_group_url in url_group_list:
        # 遍历每个分组图片
        img_group_url = requests.get(img_group_url['href'], cookies = cookie).url
        group_page_html = requests.get(img_group_url, cookies = cookie).content
        group_soup = BeautifulSoup(group_page_html, "lxml")
        url_list = group_soup.find_all('a',href=re.compile(r'^/mblog/oripic',re.I))
        for imgurl in url_list:
            imgurl = "http://weibo.cn%s"%imgurl['href']
            imgurl = requests.get(imgurl, cookies = cookie).url
            imgurl = do_image_url(imgurl)
            urllist_set.add(imgurl)
            print ' －获取Page%d 的图片信息: %s'%(page,imgurl.encode('utf-8'))

    if urllist_set:
        for imgurl in urllist_set:  
            image_count +=1
            fi.write('%s\n'%imgurl)
        print ' －该页面不计重复链接的有效链接数: %d'%len(urllist_set)
        urllist_set.clear()

#关闭打开的文件
fw.close()
fi.close()

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
        @blocknum: 已经下载的数据块
        @blocksize: 数据块的大小
        @totalsize: 远程文件的大小
    '''
    if totalsize <= 0:
        print "下载文件失败：文件大小是空!"
        return
    else:
        percent = 100.0 * blocknum * blocksize / totalsize
        if percent > 100:
            print "下载100%完成！"
        else:
            print "下载%.2f%%..."% percent

ok_count = 0
x = 1
local_time = time.localtime(int(time.time()))
date_time = time.strftime("%Y%m%d",local_time)
print '－－－－－开始下载图片－－－－－'
f_img = open("%s/image_urls.txt"%run_path, "r")
while True :
    imgurl = f_img.readline()
    if imgurl:
        post_fix = imgurl[imgurl.rfind('.')+1 : len(imgurl)-1] #尾部有换行符
        image_name = image_path + '/%s_%d.%s' % (date_time,x,post_fix)
        print '-第%s张图片 正在下载...' % x
        try:
            req = urllib2.Request(imgurl, headers={'User-Agent' : "Magic Browser"})
            response = urllib2.urlopen(req)
            open(image_name, "wb").write(response.read())
            # urllib.urlretrieve(response.geturl(),image_name,callbackfunc)
            response.close()
            ok_count += 1
        except urllib2.URLError,e:
            print "该图片下载失败: %s,原因: %s"%(imgurl.encode('utf-8'),e.reason)
            print e.fp.read()
        except:
            print "该图片下载失败: %s"%imgurl.encode('utf-8')
        x += 1
    else:
        break
f_img.close()

print '－－－－－结果－－－－－'
print '1.原创微博爬取完毕，共%d条，保存路径%s'%(weibo_count-2,word_path.encode('utf-8'))
print '2.微博图片爬取完毕，共%d张，保存路径%s'%(image_count,image_path.encode('utf-8'))
if ok_count < image_count :
    print ' -图片下载成功:%d, 失败:%d'%(ok_count,image_count - ok_count)

