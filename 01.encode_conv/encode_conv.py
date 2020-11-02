#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-02 18:18:27
# @Author  : liaohw (liaohw@asiainfo.com)
'''
this python deal with file encode format
environment : python3.4
example 1:
	./encode_conv.py conv_test_path GB2312 utf-8
	**this is a path:
	--detect: conv_test_path\test.h is GB2312
	convert conv_test_path\test.h : GB2312 --> utf-8
	--detect: conv_test_path\test.h is utf-8
example 2:
	./encode_conv.py conv_test_path
	**this is a path:
	--detect: conv_test_path\test.h is utf-8
	convert conv_test_path\test.h : utf-8 --> GB2312
	--detect: conv_test_path\test.h is GB2312
'''
import os
import sys
import chardet
import codecs

#global var
# ORI_DECODE = 'utf-8'
# DST_ENCODE = 'GB2312'
ORI_DECODE = 'GB2312'
DST_ENCODE = 'utf-8'

def file_detect(file):
	fcode = chardet.detect(open(file,'rb').read())['encoding']
	print ('--detect:',file,'is',fcode)
	return fcode

def file_convert(file, decode, encode):
	fcode = file_detect(file)
	if fcode == None:
		print ('empty file will not convert!')
		return 
	elif fcode == decode:
		try:
			print ('convert', file, ':', fcode, '-->', encode)
			f=codecs.open(file,'r',fcode)
			file_content=f.read()
			f.close()
			codecs.open(file,'w',encode,errors="strict").write(file_content)
			#check new file
			fcode = file_detect(file)
			if fcode == None:
				print ('convert failed ! file resotre!')
				codecs.open(file,'rb',fcode).write(file_content)
		except IOError as err:
			print ('I/O ERROR:{0}'.format(err))
		except:
			print (traceback.print_exc())

def path_explore(path):
	for root,dirs,files in os.walk(path):
		for file in files:
			path_file = os.path.join(root,file)
			convert(path_file)

# https://docs.python.org/3.4/library/codecs.html#module-codecs
#ascii,utf-8,GB2312
#convert utf-8 to GB2312 for source insight
def convert(argv):
	if(os.path.isfile(argv)):
		file_convert(argv,ORI_DECODE,DST_ENCODE)
		# file_convert(argv,'GB2312','utf-8')
	elif(os.path.isdir(argv)):
		print ("**this is a path:")
		path_explore(argv)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		convert(sys.argv[1])
	elif len(sys.argv) == 4:
		ORI_DECODE = sys.argv[2]
		DST_ENCODE = sys.argv[3]
		convert(sys.argv[1])
	else:
		print ('Usage:')
		print (sys.argv[0],'file_path(or file_name) [ori decode] [dst encode]')
		# for test
		convert('conv_test_path')
