#!/usr/bin/env python
# coding:utf8

import importlib,sys
importlib.reload(sys)
import urllib.request as ur
import json

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

fr = open('../csv/films.csv', 'r')
films = []
for line in fr:
	line = json.loads(line.strip('\n'))  
	films.append(line)  
fr.close()

# 获取另外的实体 characters, planets, starships, vehicles, species
targets = ['characters', 'planets', 'starships', 'vehicles', 'species']
for target in targets:
	fw = open('../csv/' + target + '.csv', 'w')
	data = []
	for item in films:
		tmp = item[target]
		# 不同电影人可能有重复
		for t in tmp:
			if t in data:
				continue
			else:
				data.append(t)
			# 不停请求
			while (1):
				print(t)
				try:
					# 复制请求代码，t是每个人的url
					request = ur.Request(url=t, headers=headers)
					response = ur.urlopen(request, timeout=20)
					result = response.read().decode('utf-8')
				except Exception as e:
					continue
				else:
					fw.write(result + '\n')
					break  # 一定要跳出去循环
				finally:
					pass
	print(str(len(data)) + ' ' + target) 
	fw.close()