#!/usr/bin/local/python3
#coding: utf-8
from bs4 import BeautifulSoup
import os
import urllib
from urllib.parse import urlencode
from urllib.parse import urlparse
from urllib.request import Request
from urllib.request import urlopen
from xml.dom.minidom import *
import json
import xml.etree.ElementTree as ET
import json
import time
import webbrowser
import requests
import feedparser
import random
import copy
import warnings


url2 = "http://www.vesti.ru/vesti.rss"
url = "http://feeds.feedburner.com/euronews/ru/news"
url1="http://ru.euronews.com/news/"
url3 = "http://ru.euronews.com/news/americas/"

d = feedparser.parse(url2)

def vestiRss():
	e = d['entries']
	num = random.randint(0, (len(d['entries'])))-1
	text = str(e[num]['title'])+'\n\n'+str(e[num]['description']).replace('&mdash;', '—').replace('&quot;', '"').replace('&nbsp;', ' ').replace('&laquo;', '"').replace('&raquo;', '"')+'\n\n'
	return text
			
	
def euronewsNews():

	with urlopen(url1) as eu1:
		text = []
		enews1=BeautifulSoup(eu1.read(), 'html.parser')
		links1 = enews1.find_all('h2')
		for i in links1:
			with urlopen('http://ru.euronews.com'+i.find('a')['href']) as new:
				enews = BeautifulSoup(new.read(), 'html.parser')
				warnings.filterwarnings("ignore")
				text.append(enews.find_all(id='articleTranscript')[0].get_text())
				# print(enews.title.string,'\n\n', text,'\n\n')
		return random.choice(text)
def euronewsUSA():
	with urlopen(url3) as eu1:
		text = []
		enews1=BeautifulSoup(eu1.read(), 'html.parser')
		links1 = enews1.find_all('h2')
		for i in links1:
			with urlopen('http://ru.euronews.com'+i.find('a')['href']) as new:
				enews = BeautifulSoup(new.read(), 'html.parser')
				warnings.filterwarnings("ignore")
				text.append(enews.find_all(id='articleTranscript')[0].get_text())
				# print(enews.title.string,'\n\n', text,'\n\n')
		return random.choice(text)
 