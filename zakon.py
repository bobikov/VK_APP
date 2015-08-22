
import vk
import sys
import urllib
from urllib.request import urlopen
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import random
import time
from datetime import timedelta
from datetime import datetime
from threading import Timer,Thread,Event
import webbrowser
import wget
import os
import cgi
import cgitb
import wsgiref.handlers
import json
import wikipedia
import requests
import re
from itertools import islice
from newsBlock import euronewsNews, vestiRss, euronewsUSA
import date_converter
def const(state):
	konst = "http://www.zakonrf.info/konstitucia/"
	headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36", "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"}

	data = requests.get(konst, headers=headers).content.decode('utf-8')
	# webbrowser.open_new_tab("file:{}".format(os.path.abspath("zakonrf.html")))
	html1=BeautifulSoup(data, "html.parser")

	divs=html1.find('div', class_='law-nodes-tree')
	# state = str(input('Номер статьи конституции: '))
	p = re.compile('(?<=Статья )'+state+'(?=\.)')
	for i in divs.find_all('a'):
		if p.search(i.text):
			html2 = BeautifulSoup(requests.get("http://www.zakonrf.info"+i['href'], headers=headers).content.decode(), "html.parser")
			# print(i.text,'\n',html2.find('div', class_='st-content').text)
			text = i.text + '\n' + html2.find('div', class_='st-content').text
			return text


