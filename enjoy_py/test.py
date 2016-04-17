#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2016-04-05 16:45:59
# @Author  : liaohw (liaohw@asiainfo.com)
# @Version : python2.7
'''
'''
print ('====================')
import os

split_path='.svn'

path="g:\\test"
for root,dirs,files in os.walk(path):
	print("============================================")
	print("Root = ", root)
	print("dirs = ", dirs)
	print("files = ", files)
	for file in files:
		if len(root.split(split_path)) > 1 :
			print ("inclue .svn will split")
		else:
			path_file = os.path.join(root,file)
			print("*** "+path_file)
