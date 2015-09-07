#!/usr/local/bin/python3
#coding: utf-8
import vk
import urllib
import oauth2
import webbrowser
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.request import urlparse
from html.parser import HTMLParser
from urllib.request import pathname2url
from bs4 import BeautifulSoup 
import os
# import timer

url = 'https://oauth.vk.com/authorize?'
app_id = '5040349'
# app_id = '5031468'
# app_id = '5038329'
# app_id = '5038789'
scope = 'wall, offline, status, messages, ads, groups, notes, photos, video, docs, friends, audio'
redirect_url = 'https://oauth.vk.com/blank.html'
api_version = 5.35
display = 'page'
params = urlencode({
	'client_id' : app_id,
	'scope' : scope,
	'redirect_url' : redirect_url,
	'v' : api_version,
	'response_type' : 'token'
	})
headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36", "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"}

# headers['Content-type'] = 'charset=utf-8'

def auth_user():		 	
	try:		
		req = urllib.request.Request(url+params, headers=headers, method = "GET")
		resp = urlopen(req)
		respData = resp.read()
		result = respData
		array = []
		soup = BeautifulSoup(respData, 'html.parser')

		parent = soup.find_all('input')
		# for i in parent:
		# 	if i.get('name') == "pass":
		# 		i['value']='Immortal1988'
		# 		print(i)
		# 	if i.get('name') == 'email':
		# 		i['value'] = '+79826245318'
		# 		print(i)
		# a = soup.find_all('div')	
		# for i in a:
		# 	if i.get('class') == ['fi_row']:
		# 	# # 	print(i['href'])
		# 		print(i)
		html = soup
		saveFile = open('subb.html', 'w')
		saveFile.write(str(html))
		saveFile.close()
		webbrowser.open_new_tab('file:{}'.format(pathname2url(os.path.abspath('subb.html'))))
		# url_action = soup.form['action']
		# print(url_action)
		# print(headers)
	except Exception as e:
		print(str(e))
auth_user()

