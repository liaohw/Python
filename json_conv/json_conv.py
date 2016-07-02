#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
	environment ：python2.7
'''
import os
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
	jf = file("EmployeeList.json");
	fw = open("employee.csv","w+")
	readtext = json.load(jf)

	esize = len(readtext["data"])
	print "Total employee_number : %s"%esize
	print "begin transfer..."
	fw.write("姓名,	账号,	Email地址,	员工号,	手机号码,	上级姓名\n");
	for i in range(0,esize):
		_data = readtext["data"][i];
		out_str = "%s,	%s,	%s,	%s,	%s,	%s\n"%(_data["last_name"],_data["nt_account"],_data["email_address"],_data["employee_number"],_data["mobile"],_data["supervisor_name"])
		print out_str
		fw.write(out_str);

	jf.close
	fw.close
	print "deal ok..."


