#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
	environment ：python2.7
'''
import csv
import sys
import urllib.request
auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password('pypi','http://pypi.python.org','username','password')
opener = urllib.request.build_opener(auth)
r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')
u = opener.open(r)
resp = u.read()