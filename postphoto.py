#!/usr/local/bin/python3
from threading import Timer,Thread,Event
import time
import threading
import vk
import random
groups = [-57014305, -72580409]
person = [179349317]
vkapi = vk.API(access_token='2c3a0f63ea9b7cce502015d6a8a92e9fe46e3da708074407891c646e1cffac0858755a5737a8b77af6cfc')


def getphoto():
	vkapi.photo.get

def postphoto():

	i=-1
	print('Computer make posts now... \nTotal number of posts: ' + str(i+1))
	while 1:
		# i+=1
		# if i == len(sexwords)-1:
		# 	i=-1

		vkapi.wall.post(owner_id=groups[0], message=random.choice(sexwords))
		time.sleep(60*15)
gg = postphoto()
gg.start()