#!/usr/local/bin/python3
#coding: utf-8
import urllib
from urllib.parse import urlencode
from urllib.request import urlparse
from urllib.request import urlunparse
from urllib.request import urlopen
from urllib.request import Request
from http import cookies
from http import cookiejar
from bs4 import BeautifulSoup
import requests
import os 
import json
import wikipedia

# c = cookies.SimpleCookie()
# # header = {'User-agent'}
# user = 'Bobikov'
# passw = 'immortal'
# params = urlencode(dict(action='login', lgname=user, lgpassword=passw, format='json' ))
url = 'https://ru.wikipedia.org/w/api.php?'
# baseurl = urlparse(url).netloc
headers = {}
headers['User-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

# r1=requests.post(url+params)
# token = r1.json()['login']['token']
# params2 = params +'&lgtoken=%s' % (token)
# r2 = requests.post(url+params2, cookies=r1.cookies)
# r3 = requests.get('https://'+baseurl+'/index.php/PrivateTest', cookies=r2.cookies)
# print(r3.text)
# print(r2.cookies)

def getWiki():
	params = urlencode(dict(action='query', titles='Modern Talking', format='json'))

	# params = 'action=query&list=search&format=json&srsearch=modern%20talking&srwhat=text&srprop=snippet&indexpageids=&rawcontinue=&titles=modern%20talking'

	req = requests.get(url+params)
	f = req.json()
	dd = [i for i in f['query']['pages']]
	return dd[0]




def getRev(ids=getWiki()):
	params = 'action=query&prop=revisions&format=json&rvprop=content&rawcontinue=&pageids=%s&rvsection=0' % (ids)
	req = requests.get(url+params)
	f = req.json()
	# fr = json.dumps(f, sort_keys=True, indent=4, ensure_ascii=False)
	print(json.dumps(f['query']['pages'][ids]['revisions'][0]['*'], ensure_ascii=False))
# getRev()		

wikipedia.set_lang('ru')
page = wikipedia.page('язва')

try:
	print(wikipedia.summary('Привет', sentences=5))
except:
	print('ddd')
# print(page.summary)
