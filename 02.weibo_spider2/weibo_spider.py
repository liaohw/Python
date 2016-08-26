#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
修改自己的微博账户cookie替代xxx:
    cookie = {"Cookie": "xxx"}
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
img_size = 1    #0 small, 1 bmiddle, 2 large(url_default)
user_id = 2729521310    #simba 2626761705,yy 2729521310,meitui 1994294027,daoman 2797679040 或 hzguidedog
cookie = {"Cookie": "xxx"}
weibo_count = 0
image_count = 0
ok_count = 0
URL_FLAG = 1
IMG_FLAG = 2
RETRY_NBR = 11  #retry 11 times


def do_image_url(url):
    if img_size < 2 :
        return re.sub('large',img_size_str,url)
    return url

def retry_requests_header(url):
    for i in range(1,RETRY_NBR):
        time.sleep((i-1)%3)
        url_html = requests.get("%s1"%(url), cookies = cookie).content
        if len(url_html) == 0:
            print '[访问失败,将重试!]－－ retry %d time'%i
            continue
        else:
            if i > 1:
                print '[重试成功!!!]－－ retry ok'
            return url_html
    print '[重试失败]:%s1 , continue'%(url)
    return 0

def retry_requests_get(url,flag = 0):
    try:
        retult = ''
        for i in range(1,RETRY_NBR):
            if flag == URL_FLAG:
                retult = requests.get(url, cookies = cookie).url
            elif flag == IMG_FLAG:
                retult = requests.get(url, cookies = cookie).url
                #页面需要调整
                if retult.rfind(".jpg") == -1:
                    print '[JPG地址错误,将重试!]－－ retry %d time'%i
                    continue
            else:
                retult = requests.get(url, cookies = cookie).content
            if len(retult) == 0:
                print '[访问失败,将重试!]－－ retry %d time'%i
                continue
            else:
                if i > 1:
                    print '[重试成功!!!]－－ retry ok'
                return retult
        print '[重试失败]－－ continue'
        return 0
    except:
        print '[异常失败]－－ continue'

def retry_requests_download(imgurl):
    for i in range(1,3):
        try:
            req = urllib2.Request(imgurl, headers={'User-Agent' : "Magic Browser"})
            response = urllib2.urlopen(req)
            open(image_name, "wb").write(response.read())
            # urllib.urlretrieve(response.geturl(),image_name,callbackfunc)
            response.close()
            return 0
        except urllib2.URLError,e:
            print '[下载失败,将重试!]－－ retry %d time'%i
            print e.fp.read()
        except:
            print '[下载失败,将重试!]－－ retry %d time'%i
    print " 该图片下载失败: %s"%imgurl.encode('utf-8')
    return 1


#参数输入
# user_id = raw_input(u"请输入微博ID(数字或字符串): ")
user_id = sys.argv[1]

page_num = 0
# 获取微博名
try:
    # 普通微博ID
    base_url = 'http://weibo.cn/u/%s?filter=1&page='%user_id
    head_html = retry_requests_header(base_url)
    selector = etree.HTML(head_html)
    page_num = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
    text = selector.xpath('//span[@class="ctt"]')[0].xpath('string(.)')
    user_name = text[0 : text.find(' ')].encode('utf-8')    #中间不是普通空格
    print "\n@微博名 :<%s> 总共页数: %d\n"%(user_name,page_num)
except :
    try:
        #修改过的微博ID或域名号
        base_url = 'http://weibo.cn/%s?filter=1&page='%user_id
        head_html = retry_requests_header(base_url)
        # print requests.get("%s1"%(base_url), cookies = cookie).content
        selector = etree.HTML(head_html)
        page_num = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
        text = selector.xpath('//span[@class="ctt"]')[0].xpath('string(.)')
        user_name = text[0 : text.find(' ')].encode('utf-8')    #中间不是普通空格
        print "\n@微博名 :<%s> 总共页数: %d\n"%(user_name,page_num)
    except :
        print '\t查询微博名失败，请检查并从新输入!'
        exit (0)

if len(sys.argv) == 3 and sys.argv[2] == '1' :
    exit (0)

run_path = "%s/%s_%s"%(os.getcwd(),user_id,user_name)
if os.path.exists(run_path) is False:
    os.mkdir(run_path)
word_path= "%s/weibo.txt"%(run_path)
image_url_path= "%s/image_urls.txt"%(run_path)
redo_path= '%s/%s.redo'%(run_path,user_id)
image_path=run_path

# do_flag = (int)(raw_input(u"处理方式: 0下载信息和图片, 1下载信息, 2下载图片\n请输入: "))
do_flag = 0
if do_flag != 2:
    print "***********下载信息**************"
    page_being = 1
    # img_size = (int)(raw_input(u"图片质量: 0 缩略图, 1 普通图, 2 高清原图\n请输入: "))
    img_size = 2
    if img_size == 0 :
        img_size_str = 'small'
    elif img_size == 1 :
        img_size_str = 'bmiddle'
    else :
        img_size_str = 'large'

    result = '－－－－－微博用户ID : %s\n'%user_id
    image_url_list = []
    page_id_list = []
    redo_page_list = []

    fWeibo = open(word_path.encode('utf-8'), "wb")
    fImgUrl = open(image_url_path.encode('utf-8'), "wb")


    print '－－－－－爬虫准备Page－－－－－'
    if len(sys.argv) == 3 and sys.argv[2] == '2' :
        # 重新读取加载页
        fRedo = open(redo_path.encode('utf-8'), "r") 
        while True :
            page = fRedo.readline()
            if page:        
                page_id_list.append(int(page[0 : len(page)-1])) #尾部有换行符
            else:
                break
        fRedo.close()
    else:
        for i in range(page_being,page_num+1):
            page_id_list.append(i)

    print '－－－－－爬虫准备就绪 : %d'%len(page_id_list)
    for page in page_id_list:
        print '－－－－－抓取页面:P%d/%d－－－－－'%(page,page_num)
        url = "%s%d"%(base_url,page)
        print "URL => %s"%url
        #获取lxml页面
        # page_html = requests.get(url, cookies = cookie).content
        page_html = retry_requests_get(url)
        if page_html == 0:
            redo_page_list.append(page)
            print '需要重新获取页面...'
            continue
        print '正在文字爬取...'
        #文字爬取
        selector = etree.HTML(page_html)
        text_content = selector.xpath('//span[@class="ctt"]')
        # date_content = selector.xpath('//span[@class="ct"]')  #时间
        for i in range(0,len(text_content)):
            text = text_content[i].xpath('string(.)')
            if weibo_count == 0:
                text = "信息 : %s"%text
            elif weibo_count == 1:
                text = "签名 : %s"%text
            else:
                text = "%d : %s"%(weibo_count-1,text)
            print " %s"%text.encode('utf-8')
            weibo_count += 1
            result = result + text + '\n'
        fWeibo.write(result)
        result = ''

        print '正在图片信息爬取...'
        #图片爬取
        soup = BeautifulSoup(page_html, "lxml")
        isGroup = 0
        #图片组信息爬取
        url_group_list = soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/picAll',re.I))
        for img_group_url in url_group_list:
            isGroup = 1
            # 遍历每个分组图片
            # img_group_url = requests.get(img_group_url['href'], cookies = cookie).url
            # group_page_html = requests.get(img_group_url, cookies = cookie).content
            img_group_url = retry_requests_get(img_group_url['href'],URL_FLAG)
            if img_group_url == 0:
                continue
            group_page_html = retry_requests_get(img_group_url)
            if group_page_html == 0:
                continue
            group_soup = BeautifulSoup(group_page_html, "lxml")
            url_list = group_soup.find_all('a',href=re.compile(r'^/mblog/oripic',re.I))
            for imgurl in url_list: #原图列表
                imgurl = "http://weibo.cn%s"%imgurl['href']
                # imgurl = requests.get(imgurl, cookies = cookie).url
                imgurl = retry_requests_get(imgurl,IMG_FLAG)
                if imgurl == 0:
                    continue
                imgurl = do_image_url(imgurl)
                if(image_url_list.count(imgurl) == 0):
                    image_url_list.append(imgurl)
                    print ' －G获取Page%d 的图片信息: %s'%(page,imgurl.encode('utf-8'))
        if isGroup == 0:
            url_list = soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/oripic',re.I))
            for imgurl in url_list:
                # <a href="http://weibo.cn/mblog/oripic?id=DqZ4qlfOv&amp;u=a2b1309ejw1f2wmjmulamj20ku112du2">原图</a>
                imgurl = imgurl['href']
                # http://weibo.cn/mblog/oripic?id=DqZ4qlfOv&amp;u=a2b1309ejw1f2wmjmulamj20ku112du2
                # imgurl = requests.get(imgurl, cookies = cookie).url
                imgurl = retry_requests_get(imgurl,IMG_FLAG)
                if imgurl == 0:
                    continue
                # http://ww1.sinaimg.cn/large/a2b1309ejw1f2wmjmulamj20ku112du2.jpg
                imgurl = do_image_url(imgurl)
                if(image_url_list.count(imgurl) == 0): #查重
                    image_url_list.append(imgurl)
                    print ' －S获取Page%d 的图片信息: %s'%(page,imgurl.encode('utf-8'))

        if image_url_list:
            for imgurl in image_url_list:  
                image_count +=1
                fImgUrl.write('%s\n'%imgurl)
            print ' －该页面不计重复链接的有效链接数: %d'%len(image_url_list)
            image_url_list[:] = []

    if redo_page_list:
        print '－－－－－保存获取失败页面 : %s.redo'%user_id
        fRedo = open(redo_path.encode('utf-8'), "wb")
        for i in redo_page_list:  
            fRedo.write('%s\n'%i)
        fRedo.close()
    elif os.path.exists(redo_path) is True:
        print '－－－－－删除redo文件 : %s'%redo_path
        os.remove(redo_path)

    #关闭打开的文件
    fWeibo.close()
    fImgUrl.close()
    print '－－－－－结果－－－－－'
    print '* 原创微博爬取完毕，共%d条，保存路径%s\n\n'%(weibo_count-2,word_path.encode('utf-8'))

if do_flag != 1:
    print "***********下载图片**************"
    x = 1
    local_time = time.localtime(int(time.time()))
    date_time = time.strftime("%Y%m%d%H%M%S",local_time)
    print '－－－－－开始下载图片－－－－－'
    f_img = open("%s/image_urls.txt"%run_path, "r")
    while True :
        imgurl = f_img.readline()
        if imgurl:
            post_fix = imgurl[imgurl.rfind('.')+1 : len(imgurl)-1] #尾部有换行符
            image_name = image_path + '/%s_%d.%s' % (date_time,x,post_fix)
            print '-第%s张图片 正在下载...' % x
            if retry_requests_download(imgurl) == 0:
                ok_count += 1
            x += 1
        else:
            break
    f_img.close()
    print '－－－－－结果－－－－－'
    print '* 微博图片爬取完毕，共%d张，保存路径%s\n'%(image_count,image_path.encode('utf-8'))
    if ok_count < image_count :
        print ' -图片下载成功:%d, 失败:%d\n\n'%(ok_count,image_count - ok_count)

