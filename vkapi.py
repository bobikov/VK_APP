#!/usr/local/bin/python3
import vk
import urllib
import oauth2
from urllib.parse import urlencode
from urllib.request import urlopen
try:	
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
	headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
	req = urllib.request.Request(url+params, headers = headers)
	resp = urlopen(req)
	respData = resp.read()
	saveFile = open('withHeaders.txt', 'w')
	saveFile.write(str(respData))
	saveFile.close()
except Exception as e:
	print(str(e))