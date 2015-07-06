#!/usr/local/bin/python3
import vk
import urllib
import oauth2
import webbrowser
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.request import urlparse
from html.parser import HTMLParser
from bs4 import BeautifulSoup 
import timer

url = 'https://oauth.vk.com/authorize?'
app_id = '4967352'
scope = 'wall, offline'
redirect_url = 'https://oauth.vk.com/blank.html'
api_version = '5.34'
display = 'popup'
params = urlencode({
	'client_id' : app_id,
	'scope' : scope,
	'redirect_url' : redirect_url,
	'v' : api_version,
	'response_type' : 'token'
	})
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
headers['Content-type'] = 'charset=utf-8'

def auth_user():		 	
	try:		
		req = urllib.request.Request(url+params, headers = headers, method = "GET")
		resp = urlopen(req)
		respData = resp.read()
		result = respData
		array = []
		soup = BeautifulSoup(respData, 'html.parser')

		parent = soup.find_all('input')
		for i in parent:
			if i.get('name') == "pass":
				i['value']='Immortal1988'
				print(i)
			if i.get('name') == 'email':
				i['value'] = '+79826245318'
				print(i)

		html = soup.prettify()
		saveFile = open('subb.html', 'w')
		saveFile.write(str(html))
		# saveFile.close()
		webbrowser.open('subb.html')
		url_action = soup.form['action']
		print(url_action)
		print(headers)
	except Exception as e:
		print(str(e))
auth_user()

