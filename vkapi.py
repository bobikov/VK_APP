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

from io import BytesIO
import requests



url = 'https://oauth.vk.com/authorize?'

params = urlencode({
	'client_id' : "5040349",
	'scope' : "wall, offline, status, messages, ads, groups, notes, photos, video, docs, friends, audio",
	'redirect_url' : "https://oauth.vk.com/blank.html",
	'response_type':"token",
	'v' : "5.45",
	'display':"wap"
	})
headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}

# response=requests.post(url, data=params, headers=headers).text
webbrowser.open_new(url+params)

