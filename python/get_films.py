#!/usr/bin/env python
# coding:utf8

import importlib,sys
importlib.reload(sys)


import urllib # 这个没有用上
import urllib.request as ur
import time
import json
import pprint

# 7部电影
films = []  
for x in range(1, 8):
	films.append('http://swapi.co/api/films/' + str(x) + '/')

# 伪装浏览器，防止反扒设置
headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

fw = open('films.csv', 'w')

for item in films:
	print(item)
	request = ur.Request(url=item, headers=headers)
	response = ur.urlopen(request, timeout=20)
	result = response.read().decode('utf-8')
	fw.write(result + '\n')

fw.close()	
	