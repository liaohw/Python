#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="mail.asiainfo.com"  #设置服务器
mail_user="liaohw"    #用户名
mail_pass=raw_input("Please input password : ")   #口令 

sender = 'liaohw@asiainfo.com'
receivers = ['pengft@asiainfo.com']  # 接收邮件

message = MIMEText('Python send mail...', 'plain', 'utf-8')
message['From'] = Header("Admin")
message['To'] =  Header("MyTester")
message['Subject'] = Header("Hello 九妹好人！" + receivers[0], 'utf-8')
num=5
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    for i in range(1,num+1):
    	smtpObj.sendmail(sender, receivers, message.as_string())
    	print("Send %d mail!" % i)
    print("Send mail ok!")
except smtplib.SMTPException:
    print("Error: Send mail failed!")