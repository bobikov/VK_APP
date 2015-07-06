#!/usr/local/bin/python3
import vk
import sys
import urllib
from urllib.request import urlopen
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import random
import time
vkapi = vk.API(access_token='2c3a0f63ea9b7cce502015d6a8a92e9fe46e3da708074407891c646e1cffac0858755a5737a8b77af6cfc')
groups = [-57014305, -72580409, -61330688]
person = [179349317]
pho = []
def getwall(wall_id, user_id, count):
	wall = vkapi.wall.get(owner_id=wall_id, count=count)
	myitems = []
	dtype = dtype
	for i in wall['items']:
		if i['from_id'] == user_id:
			print(dict(id=i['from_id'], value= i['text']))
# getwall(-61330688, 179349317, 2)

def photoget(wall_id, album, count):
	photos = vkapi.photos.get(owner_id=wall_id, album_id=album, count=count)
	for i in photos['items']:
		if i['photo_604']:
			pho.append(i['id'])
photoget(-73484869, 'wall', 90)


# print(pho)

def post():
	i=-1
	print('Computer make post photos now... \nTotal number of posts: ' + str(i+1))
	while 1:
		i+=1
		if i == len(pho)-1:
			i=-1
		vkapi.wall.post(owner_id=groups[0], attachments='photo179349317_4967352, photo-73484869_'+str(random.choice(pho)))
		time.sleep(60)
gg = post()
gg.start()

