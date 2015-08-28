#!/usr/local/bin/python3
# coding: UTF-8

from words import *
from zakon import *
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
import easy_date
import tkinter
from tkinter import *
import base64
from PIL import Image
from PIL import ImageTk
import io
from math import *
from operator import itemgetter, attrgetter
from requests.utils import quote
# cgitb.enable()

# print('Content-type: text/html')
# print()
# https://api.vk.com/method/photos.get?owner_id=-77093415&album_id=wall&count=40&access_token=00af0cff7458595045e1893775acf9b561dad00d6df9de580f9839e2722d5090e3fbf819a471461094666
# User and app info
vkapi = vk.API( access_token = 'c578c314eb08a60f03ac64ad2567aecfd2c1acd7378f16506d4a81d7473b0050a0cccccf5ee3f8d727cb4')
# vkapi = vk.API( access_token = '8c214f76b9870dcc6af61507afd364ebd060ffbb60ec1a495398e9507a143d6622f8322127dbd338d0617')
# vkapi = vk.API( access_token = 'aa0d8008ce0ef760746439bac0415bb0b577857a142e2de8c26d3b803e8eb5e724416ff684579ad5c3944')
# vkapi = vk.API( access_token = '9a57a431b60318aa06ce1e6624761a9a539f14c4979a165f57c598f9347bd6e7476022e5265d74d2212df')
other = [-72580409, -61330688]
person = [179349317]
# person = [319258436]
# person = [319315119]
# app_id = 4967352
app_id = 5040349
accTok = 'c578c314eb08a60f03ac64ad2567aecfd2c1acd7378f16506d4a81d7473b0050a0cccccf5ee3f8d727cb4'
# accTok = 'aa0d8008ce0ef760746439bac0415bb0b577857a142e2de8c26d3b803e8eb5e724416ff684579ad5c3944'
# accTok = '8c214f76b9870dcc6af61507afd364ebd060ffbb60ec1a495398e9507a143d6622f8322127dbd338d0617'
# accTok = '9a57a431b60318aa06ce1e6624761a9a539f14c4979a165f57c598f9347bd6e7476022e5265d74d2212df'
supercitat = []
end = 0
key=str
# VK groups info for reading

public = { 'items' : [
						{	'name' : 'techtroit', 
							'id' : -69107269 	},
						{	'name' : 'mnmlsm', 
							'id' : -80982654	},
						{	'name' : 'sklr', 
							'id' : -45327998	},
						{	'name' : 'IMAGE',
							'id' : 	-54179178	},				
						{	'name' : 'SKYFALL',	
							'id' : -39669294	}
					]
		}
citat = { 'items' : [
						{	'name' : 'cfb',	
							'id' : -31164499	}
					]
		}
images = { 'items' : [
						{	'name' : 'VILLAN',
							'id': -46773594		}
					

					]
		}
# List text sources 		

pub = list(i['id'] for i in public['items'] if i['name']=='techtroit')


mypost = '''Привет. Одиноко? Грустно? Скучно? Нужен собеседник понимающий? - Забудь эти проблемы! Я их решу за тебя. Всего за 100$ в час. Без интима. Предоплата - 20$, без возврата. \n\nP.S. Детям не беспокоить без родителей.'''


class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)
      self.count = 0
   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

# Main Programm Classes and Functions

class Comb:
	'''Super VK combain making collecting and post any data'''

	def __init__( self ):

		self.max = 'dd'
		self.ok = 'dd'
		self.group_ids = [-60409637, -72580409, -52521233, -34783798, -80822106, -35376525]
		self.group_Ids_ToString = str.join(',', [str(abs(x)) for x in self.group_ids])
		self.groupsNoDumps = vkapi.groups.getById(group_ids=self.group_Ids_ToString, indent=4, sort_keys=True, ensure_ascii=False)
		self.groupsWithDumps = json.dumps(vkapi.groups.getById(group_ids=self.group_Ids_ToString),indent=4, sort_keys=True, ensure_ascii=False)
		self.group_names = [i['name'] for i in json.loads(self.groupsWithDumps)]
		self.group_screen_names=[i['screen_name'] for i in json.loads(self.groupsWithDumps)]
		self.dict_names_and_ids=[];
		self.captchaSid=None
		self.captchaKey=None
		for i,x,y in zip(self.group_names, self.group_ids, self.group_screen_names):
				self.dict_names_and_ids.append({'name':i, 'id':x, 'screen_name':y})


	def dateChecker(self):

		# Waiting for the post to give parametrs of group walls and date of current post

		while 1:
			Comb.getWall('self', 'no', person[0], 'text', 1)
			time.sleep(0.8)

	def getWall( self, offset,  ioffset, wall_id, dtype, remove, count = 1, bot='no', sdate='no', likes='no', user_id = 179349317,  ):
		'''Get music, image, text data from the wall'''
		rid = []
		text=[]
		ids = []
		i = 0
		new=[]
		step = -50
		date = []
		formattime = '%y-%m-%d %H:%M:%S'
		now = datetime.strptime(datetime.strftime(datetime.now(), '%y-%m-%d %H:%M:%S'), '%y-%m-%d %H:%M:%S')

		# Looking for Post IDs without offset 
		if offset =='yes' and dtype == 'photo':
			urls = []
			step = -10
			dros = []
			
			while step < 10:
				step+=10
				wall = vkapi.wall.get( owner_id = wall_id, count = count, offset = step)
				dros.append(json.dumps(wall))
				time.sleep(0.6)
			print(json.loads(dros))
				
		if offset == 'no' and dtype == 'photo' :
			urls = []

			wall = vkapi.wall.get( owner_id = wall_id, count = count )
			for i in wall['items']:
				# print(json.dumps(i['attachments']['photo'], sort_keys=True, indent=4,ensure_ascii=False))
				# urls.append(i)
				if 'attachments' in i:
					for a in i['attachments']:
						if 'photo' in a:
							urls.append(a['photo']['photo_604'])

			return urls

			# 			if a['photo']:
			# 				urls.append(a['photo']['photo_604'])
			# return print(urls)

		if offset == 'no' and dtype == 'id':
			if type(wall_id) == dict:
				items = wall_id['items']
				for i in items:
					wall = vkapi.wall.get( owner_id = i['id'], count = count )
					ids.append(wall)

				if likes == 'yes':
					for i in ids:
						for a in i['items']:
							if a['likes']['count'] > 10:
								new.append( str(a['owner_id']) + '_'+  str(a['id']) )
				return ids

			if type(wall_id) == int:

				wall = vkapi.wall.get(owner_id=wall_id, count=count)
				for i in wall['items']:
					ids.append(i['id'])

					return  ids

				if likes == 'yes':
					for i in ids:
						for a in i['items']:
							if a['likes']['count'] > 10:
								new.append( str(a['owner_id']) + '_'+  str(a['id']) )

					return


		# Looking for text in posts without offset

		elif offset == 'no' and dtype == 'text' :

			if type(wall_id) == dict:
				items = wall_id['items']
				for i in items:
					wall = vkapi.wall.get( owner_id = i['id'], count = count )
					ids.append(wall)	
				for i in ids:
					for a in i['items']:
						text.append(str(a['text']))
						print(text)
			if type(wall_id) == int:
				if remove == True:
					wall = vkapi.wall.get(owner_id=wall_id, count = count)['items']
					for i in wall:
						if i['from_id'] == user_id:
							vkapi.wall.delete(owner_id=wall_id, post_id=i['id'])
							time.sleep(0.5)
				if remove == False:
					wall = vkapi.wall.get(owner_id=wall_id, count = count)['items']
					for i in wall:
						if i['from_id'] == user_id:
							print(i['text'])

						# return 

			elif type(wall_id) == int and bot == 'yes':

				wall = vkapi.wall.get( owner_id = wall_id, count = count )
				text.append(wall)
				for i in text[0]['items']:
					timeToPlus = datetime.strptime(datetime.fromtimestamp(i['date']).strftime('%d.%m.%y %H:%M:%S'), "%d.%m.%y %H:%M:%S")
					plusTime = dd+timedelta(seconds=5)

					if plusTime == now:
						comment1 = vkapi.wall.addComment( owner_id=wall_id, post_id=i['id'], text=random.choice(phrases) )
						post = comment1['comment_id']
						hoo = Comb.getWall('self', 'no', person[0], 'id', 1)
						getcomm = vkapi.wall.getComments( owner_id=wall_id, post_id=hoo[0] )
						if getcomm:
							print(getcomm)



			elif type(wall_id) == int and bot == 'no':
				wall = vkapi.wall.get( owner_id = wall_id, count = count )
				text.append(wall)
				for i in text[0]['items']:
					print(i['text'])



		elif offset == 'yes' and dtype == 'text':
			if type(wall_id) == dict:
				items = wall_id['items']
				for i in items:
					while step < 100:
						step+=50
						wall = vkapi.wall.get( owner_id = i['id'], count = count, offset = step )
						ids.append(wall)
						time.sleep(1)
				for i in ids:
					for a in i['items']:
						text.append(str(a['text']))
						supercitat.append(str(a['text']))
				return text
			if type(wall_id) == int:
				while step < ioffset:
					step+=50
					wall = vkapi.wall.get( owner_id = wall_id, count = count, offset = step )
					ids.append(wall)
					# time.sleep(1)
				for i in ids:
					for a in i['items']:
						if a['from_id']==user_id: 
							print(json.dumps(a['text'], indent=4, sort_keys=True, ensure_ascii=False), '\n')
					# print(j)



	# def getCitat( self ):

	# 	items = Comb.getWall('self', 'yes', citat, 'text', 50)
	# 	return items

	def rePost( self ):
		pids = Comb.getWall('self', 'no', public, 'id', 1)
		lol = []
		for i in pids:
			vkapi.wall.repost( object = 'wall' + str(i))
			time.sleep(1)


	def getTopic():
		
		topic_ids = []
		topics = vkapi.board.getTopics( group_id = 53664217 )

		for i in topics['items']:
			if i['title'] == 'ЧАТ':
				topic_ids.append(i['id'])
		return topic_ids
	

	def getPhoto( self, wall_id, album, count, download='no', path='./', dtype='id', multi='no', wall='no' ):

		pho = []
		
		groupName = vkapi.groups.getById( group_id = abs(wall_id))[0]['name']


		if wall == 'yes':
			if download=='yes':
				photoFromWall = Combain.getWall('no', wall_id, 'photo', count)
				for i in photoFromWall:
					if not os.path.exists(path+groupName):
						os.mkdir(path=path+groupName)

					elif not os.path.exists( path+groupName ):
						os.mkdir( path=path+groupName ) 
					else:	
						wget.download( i, out=path+groupName )
			elif download == 'no':
				ids=[]
				photoFromWall = Comb.getWall('no', 'no', wall_id, 'photo', 'no', count)  
				for i in photoFromWall:
					ids.append(i)
				return ids
		else:

			if multi == 'no' and type(album)==int:
				photos = vkapi.photos.get( owner_id = wall_id, album_id = album['id'], count = count ,  v=5.34 )	
				for i in photos['items']:
					if i['photo_604']:
						if download == 'yes':
							
						# pho.append(i['photo_604'])
							wget.download(i['photo_604'], out=path)
						if dtype == 'id':
							pho.append(i['id'])
						elif dtype == 'url':
							pho.append(i['photo_604'])
			
				return print(pho)

			elif multi == 'yes' and type(album) == list:
				urls=[]
				step = 1		
				offs=0	
				if download == 'yes':
					for i in album:
						if i['count'] >= 1000:

							offs = i['count']-800
							step = step - offs
							while step < i['count']:
								step+=1
								for a in vkapi.photos.get( owner_id=wall_id, album_id=i['id'], count=i['count'], offset=0, v=5.34 )['items']:
									if i['id'] == a['album_id']:
										print(i)
						elif i['count']<1000:
								for a in vkapi.photos.get( owner_id=wall_id, album_id=i['id'], count=i['count'], offset=0, v=5.34 )['items']:
									# if i['id'] == a['album_id']:

							
									if not os.path.exists(path+groupName):
										os.mkdir(path=path+groupName)

									elif not os.path.exists( path+groupName + '/' +str(i['title'] ) ):
										os.mkdir( path=path+groupName + '/' + str(i['title'])  ) 
									else:
										wget.download( a['photo_604'], out=path+groupName+'/'+str(i['title']) )
								os.system("rm ./*.tmp")		
						print('\n\n--------------------------\n\nDownload is complete\n\n')
				if download == 'no':
					ids = []
					for i in album:
						for a in vkapi.photos.get( owner_id=wall_id, album_id=i['id'], count=i['count'], v=5.34 )['items']:
							if i['id'] == a['album_id']:
								if 'photo_604' in a:
									ids.append(a['id'])
								else:
									ids.append(a['id'])
					return ids

	def getAlbums(self, public_id):
		titles = []
		ids= []
		albums = vkapi.photos.getAlbums( owner_id = public_id)['items']
		for y,i in zip(range(len(albums)), albums):
			ids.append(dict(number=y+1, id=i['id'], title=i['title'], count=i['size']))
		return ids

	def photoUpdateData(self, fromId, date):
		names=[]
		publicName = vkapi.groups.getById( group_id = abs(fromId))[0]['name']
		if os.path.isfile('updatePhotoData.json'):
			with open('updatePhotoData.json') as f:
				data = json.load(f)
			for i in data:
				names.append(i['name'])
			if publicName in names:
				for i in data:
					if i['name']==publicName:
						i['date']=date
			elif publicName not in names:
				data.append({"id":fromId, "date": date,"name":publicName})

			with open('updatePhotoData.json', 'w') as f:
				json.dump(data, f, indent=4, ensure_ascii=False)

		else:
			file1 = open('updatePhotoData.json', 'a+')
			data=[{"id":fromId, "date": date,"name":publicName}]
			file1.write(json.dumps(data, indent=4, sort_keys=True))
			file1.close()

	def delPhotos(self):
		photos = vkapi.photos.get(owner_id=person[0], album_id='saved')['items']
		for i in photos:
			vkapi.photos.delete(owner_id=person[0], photo_id=i['id'])
			time.sleep(0.4)

	def copyPhotoToAlbum( self, to_id, from_id, albumNameToCopyTo, albumIdToCopyFrom, countPhotos ):
		album_id = []
		photo_id = []
		albumsFromIds = []
		photosToCopy = []
		updateDate=int
		# getAlbumsFromId = Comb.getAlbums('self', from_id)
		step=-100
		getAlbumsTo = Comb.getAlbums('self', to_id)
		if albumIdToCopyFrom=='wall':
			rev = 1
		else:
			rev = 0
		for i in getAlbumsTo:
			if i['title'] == albumNameToCopyTo:
				album_id.append(i['id'])
		with open("updatePhotoData.json") as f:
				data = json.load(f)	
				for i in data:
					if i['id']==from_id:
						updateDate=i['date']

		if countPhotos>1000:
			photosGet=requests.get("https://api.vk.com/method/photos.get?owner_id="+str(from_id)+"&album_id="+str(albumIdToCopyFrom)+"&count=100&v=5.35&rev="+str(rev)+"&access_token="+accTok).json()
			Comb.photoUpdateData('self', from_id, photosGet['response']['items'][0]['date'])

			while step<countPhotos:
				step+=100
			
				photosGet=requests.get("https://api.vk.com/method/photos.get?owner_id="+str(from_id)+"&album_id="+str(albumIdToCopyFrom)+"&count=100&offset="+str(step)+"&v=5.35&rev="+str(rev)+"&access_token="+accTok).json()
				time.sleep(1)
				for a in photosGet['response']['items']:
				
					copyPhotos = requests.get("https://api.vk.com/method/photos.copy?owner_id="+str(from_id)+"&photo_id="+str(a['id'])+"&v=5.35&access_token="+accTok).json()
					
					if 'error' in copyPhotos:
						if copyPhotos['error']['error_code'] == 14:
							self.captchaSid=copyPhotos['error']['captcha_sid']
							# webbrowser.open_new_tab(copyPhotos['error']['captcha_img'])
							# self.captchaKey=input('enter captcha: ')
							self.captchaKey = Comb.captcha('self', copyPhotos['error']['captcha_img'])
							copyPhotos = requests.get("https://api.vk.com/method/photos.copy?owner_id="+str(from_id)+"&photo_id="+str(a['id'])+"&v=5.35&captcha_sid="+str(self.captchaSid)+"&captcha_key="+str(self.captchaKey)+"&access_token="+accTok).json()
							movePhotos = requests.get("https://api.vk.com/method/photos.move?owner_id="+str(to_id)+"&target_album_id="+str(album_id[0])+"&photo_id="+str(copyPhotos['response'])+"&v=5.35&access_token="+accTok).json()
							time.sleep(1)

		
					movePhotos = requests.get("https://api.vk.com/method/photos.move?owner_id="+str(to_id)+"&target_album_id="+str(album_id[0])+"&photo_id="+str(copyPhotos['response'])+"&v=5.35&access_token="+accTok).json()
					time.sleep(1)
		else:	
			
			photosGet=requests.get("https://api.vk.com/method/photos.get?owner_id="+str(from_id)+"&album_id="+str(albumIdToCopyFrom)+"&extended=1&count="+str(countPhotos)+"&v=5.35&rev="+str(rev)+"&access_token="+accTok).json()

			Comb.photoUpdateData('self', from_id, photosGet['response']['items'][0]['date'])

			for a in photosGet['response']['items']:
				# copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'])

				copyPhotos = requests.get("https://api.vk.com/method/photos.copy?owner_id="+str(from_id)+"&photo_id="+str(a['id'])+"&access_token="+accTok).json()
				time.sleep(0.4)
				if updateDate:
					if a['date']==updateDate:
						break
				if 'error' in copyPhotos:
					if copyPhotos['error']['error_code'] == 14:
						self.captchaSid=copyPhotos['error']['captcha_sid']
						# webbrowser.open_new_tab(copyPhotos['error']['captcha_img'])
						# self.captchaKey=input('enter captcha: ')
						self.captchaKey = Comb.captcha('self', copyPhotos['error']['captcha_img'])
						# print(self.captchaKey)
						copyPhotos = requests.get("https://api.vk.com/method/photos.copy?owner_id="+str(from_id)+"&photo_id="+str(a['id'])+"&captcha_sid="+str(self.captchaSid)+"&captcha_key="+str(self.captchaKey)+"&access_token="+accTok).json()
						movePhotos = requests.get("https://api.vk.com/method/photos.move?owner_id="+str(to_id)+"&target_album_id="+str(album_id[0])+"&photo_id="+str(copyPhotos['response'])+"&access_token="+accTok).json()
						time.sleep(1)

				movePhotos = requests.get("https://api.vk.com/method/photos.move?owner_id="+str(to_id)+"&target_album_id="+str(album_id[0])+"&photo_id="+str(copyPhotos['response'])+"&access_token="+accTok).json()
				time.sleep(1)

			Comb.delPhotos('self')	

	
	def getTopicCommentIds(self):
		topic_id=Comb.getTopic()
		ids = []
		offset=-10
		while offset<100:
			offset+=10
			topics = vkapi.board.getComments(group_id=53664217, offset=offset, topic_id=topic_id[0], count=10, sort='desc')['items']
			for i in topics:
				if (i['from_id']==person[0]):
					ids.append(i['id'])
			time.sleep(0.4)
		
		
		return ids
	def delTopicComments(self):
		topic_id=Comb.getTopic()
		ids=Comb.getTopicCommentIds('self')
		for i in ids:
			vkapi.board.deleteComment(group_id=53664217, topic_id=topic_id[0], comment_id=i)
			time.sleep(0.4)
	def postTopicComment( self ):
		'''Post comment into topic block of group'''

		topic_id = Comb.getTopic() 
		vkapi.board.addComment( group_id = 53664217, topic_id = topic_id[0], text = str( random.choice( slist ) ) )
		sys.stdout=open('MyLog.txt', 'a+')
		print(' TOPIC ID: ' + str(topic_id[0]) + '\n\n' + "{:-^50}".format("") +'\n') 
		return


	def postMulti( self, feed, mins ):
		
		i=-1
		group = str
		period = 0
		# print('Computer make post photos now... \nTotal number of posts: ' + str(i+1))
		while 1:
			i+=1
			period+=1
			if i == len(self.group_ids)-1:
				Comb.postTopicComment('self')
				i=-1
			group_id = str(self.dict_names_and_ids[i]['id'])	
			ok2 = group_id[:]
			group_name=self.dict_names_and_ids[i]['name'][:]
			screen_name = self.dict_names_and_ids[i]['screen_name'][:]
			if type(feed) == list:
				words = random.choice( feed )
				ok = words[:]
			elif type(feed) == str and not 'wiki':
				words = feed
				ok = words
			elif type(feed) == str or 'wiki':
					words=wiki()
					ok=words

			vkapi.wall.post( owner_id = ok2,  message = ok )
			sys.stdout=open('MyLog.txt', 'a+')
			print(' PUBLIC: ' + str(ok2) + '      |      ' + group_name + '       |      https://vk.com/' + screen_name + '\n\n TEXT: \n\n  ' + str(ok) + '\n\n' + "{:-^50}".format("")+ '\n')

			if period == 80:
				return period
			time.sleep(60*mins)

		
	
	def postOne( self ):

		dd = getPhoto( 'self', -73484869, 'wall', 10 )
		i=0
		while i < len( dd ):
			i+=1	
			vkapi.wall.post( owner_id = person[0],  attachments = 'photo179349317_4967352, photo-73484869_' + str( dd[i] ) )
			time.sleep(10)
		# return print(self.groups)	
		# 
	def getDialogs(self, delete='no', count=1, unread =1):
		dialogs = vkapi.messages.getDialogs(count=200, unread =unread)
		ids = [i['message']['user_id'] for i in dialogs['items']]
		# texts = [i['message']['text'] for i in dialogs['items']]
		if delete == 'yes':
			for i in ids:
				vkapi.messages.deleteDialog(user_id=i)
				time.sleep(0.6)
		elif delete == 'no' and unread==1:
			for i in dialogs['items']:

					print(i['message']['user_id'],'\n',i['message']['body'],'\n')
	def crossDeletingPosts(self, group_ids):
		ids = []
		selectedId=int
		countPosts = int
		offset=-100
		for i,y in zip(range(len(group_ids)), group_ids):
			if i == 0:
				print(str(1)+'.', group_ids[0]['id'], group_ids[0]['screen_name'])
			else:
				print(str(i+1)+'.', y['id'], y['screen_name'])
				ids.append({"number":str(i+1),"id":str(y['id'])})
		selector = input('select public to delete posts: ')
		if selector:
			for i in ids:
				if i['number'] == selector:
					selectedId=int(i['id'])
		if int(selector)==1:
			selectedId=group_ids[0]['id']

		countPosts = int(input('count of posts to delete: '))
		selectedOffset = int(input('offset: '))
		
		while offset < selectedOffset:
			offset+=100
			time.sleep(0.5)
			for post in vkapi.wall.get(owner_id=selectedId, count=countPosts, offset=offset, v=5.35)['items']:
				if post['from_id'] == person[0]:
					vkapi.wall.delete(owner_id=selectedId, post_id=post['id'], v=5.35)
					print(post['owner_id'], post['text'])
					time.sleep(0.4)	
	def downlPhotos(self, public_id, album_id, title, path, albumCountPhotos):
		p=re.compile("/")
		step=0
		if album_id=='wall':
			rev=1
		else:
			rev=0	
		if public_id==person[0]:
			publicName="179349317"
		else:
			publicName = vkapi.groups.getById( group_id = abs(public_id))[0]['name']
			publicName = p.sub('',publicName)
		if albumCountPhotos > 1000:
			while step<albumCountPhotos:
				step+=10
				for a in vkapi.photos.get( owner_id=public_id, album_id=album_id, count=10, offset=step, rev=rev, v=5.37 )['items']:

					if not os.path.exists(path+publicName):
						os.mkdir(path=path+publicName)

					elif not os.path.exists( path+publicName + '/' + str(title) ):
						os.mkdir( path=path+publicName + '/' + str(title)  ) 
					else:
						wget.download( a['photo_604'], out=path+publicName+'/'+str(title) )
					os.system("rm ./*.tmp")		

		else:
			for a in vkapi.photos.get( owner_id=public_id, album_id=album_id, count=albumCountPhotos, rev=rev, v=5.37 )['items']:

				if not os.path.exists(path+publicName):
					os.mkdir(path=path+publicName)

				elif not os.path.exists( path+publicName + '/' + str(title) ):
					os.mkdir( path=path+publicName + '/' + str(title)  ) 
				else:
					wget.download( a['photo_604'], out=path+publicName+'/'+str(title) )
				os.system("rm ./*.tmp")		
		print('\n\n--------------------------\n\nDownload is complete\n\n')

	def addLikes(self, action, action2, owner, count):

		posts = requests.get('https://api.vk.com/method/wall.get?owner_id='+owner+'&count='+count+'&v=5.35&access_token='+accTok).json()
		if action == 'add':
			for i in posts['response']['items']:
				addLikes = requests.get('https://api.vk.com/method/likes.add?owner_id='+owner+'&type=post&item_id='+str(i['id'])+'&access_token='+accTok).json()
				time.sleep(0.5)

				if 'error' in addLikes:
					if addLikes['error']['error_code']==14:
						webbrowser.open_new_tab(addLikes['error']['captcha_img'])
						self.captchaKey = input('enter captcha: ')
						self.captchaSid = addLikes['error']['captcha_sid']
						addLikes = requests.get('https://api.vk.com/method/likes.add?owner_id='+owner+'&item_id='+str(i['id'])+'&captcha_key='+str(self.captchaKey)+'&captcha_sid='+str(self.captchaSid)+'&access_token='+accTok).json()
						time.sleep(0.5)
					elif addLikes['error']['error_code'] == 9:
						print(addLikes['error']['error_msg'])
						break
						
		elif action == 'checkLikes':
			for i in posts['response']['items']:
				checkLikes = requests.get('https://api.vk.com/method/likes.isLiked?owner_id='+owner+'&type=post&item_id='+str(i['id'])+'&access_token='+accTok).json()
				if 'error' in checkLikes:
					if checkLikes['error']['error_code']==14:
						webbrowser.open_new_tab(checkLikes['error']['captcha_img'])
						self.captchaKey = input('enter captcha: ')
						self.captchaSid = checkLikes['error']['captcha_sid']
						checkLikes = requests.get('https://api.vk.com/method/likes.isLiked?user_id='+str(person[0])+'&owner_id='+owner+'&type=post&item_id='+str(i['id'])+'&captcha_key='+str(self.captchaKey)+'&captcha_sid='+str(self.captchaSid)+'&access_token='+accTok).json()
						print(checkLikes)
				else:
					if checkLikes['response'] == 1 and action2 == 'del':
						delLikes = requests.get('https://api.vk.com/method/likes.delete?owner_id='+owner+'&type=post&item_id='+str(i['id'])+'&access_token='+accTok)
						if 'error' in delLikes:
							if delLikes['error']['error_code']==14:
								webbrowser.open_new_tab(delLikes['error']['captcha_img'])
								self.captchaKey=input('enter captcha: ')
								self.captchSid = delLikes['error']['captcha_sid']
								delLikes = requests.get('https://api.vk.com/method/likes.delete?owner_id='+owner+'&type=post&item_id='+str(i['id'])+'&captcha_sid='+str(self.captchaSid)+'&captcha_key='+str(self.captchaKey)+'&access_token='+accTok)
	def uploadOwnerPhoto(self, photo):
		ids=[]
		headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36", "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"}
		uploadUrl = requests.get("https://api.vk.com/method/photos.getOwnerPhotoUploadServer?access_token="+accTok, headers=headers).json()['response']['upload_url']
		r = requests.post(uploadUrl, files={ 'file' : open('/Users/hal/Pictures/179349317/Трипофобия/'+photo, 'rb') }).json()
		# photoSave = vkapi.photos.saveOwnerPhoto(server=r['server'], photo=r['photo'], hash=r['hash'], v=5.37)
		photoSave = requests.get("https://api.vk.com/method/photos.saveOwnerPhoto?server="+str(r['server'])+"&photo="+str(r['photo'])+"&hash="+str(r['hash'])+"&v=5.37&access_token="+accTok).json()
		if 'error' in photoSave:
			self.captchaSid=photoSave['error']['captcha_sid']
			# webbrowser.open_new_tab(photoSave['error']['captcha_img'])
			# self.captchaKey=input('enter captcha: ')
			self.captchaKey=Comb.captcha('self', photoSave['error']['captcha_img'])
			photoSave = requests.get("https://api.vk.com/method/photos.saveOwnerPhoto?server="+str(r['server'])+"&photo="+str(r['photo'])+"&hash="+str(r['hash'])+"&v=5.37&captcha_key="+str(self.captchaKey)+"&captcha_sid="+str(self.captchaSid)+"&access_token="+accTok).json()
		for i in vkapi.wall.get(owner_id=person[0], count=1)['items']:
			if 'copy_history' not in i and i['text']=='':
				vkapi.wall.delete(owner_id=person[0], post_id=i['id'])

		for i in vkapi.photos.get(owner_id=person[0], album_id='profile')['items']:
			ids.append(i['id'])

		vkapi.photos.delete(owner_id=person[0], photo_id=ids[0])

	def statusSet(self, timer):
		step=0
		text = """▲▼▲▼▲▼・●⦿◎◉ ▲▼▲▼▲▼ ・●⦿◎◉ ▲▼▲▼▲▼ ・●⦿◎◉ ▲▼▲▼▲▼・●⦿◎◉ ▲▼▲▼▲▼ ・●⦿◎◉ ▲▼▲▼▲▼ ・●⦿◎◉ """
		while True: 
			step+=1
			# if step==1:
			# 	# vkapi.status.set(owner_id=person[0], text=text)
			# 	req=requests.get("https://api.vk.com/method/status.set?owner_id="+str(person[0])+"&text="+text+"&v=5.37&access_token="+accTok).json()
			# 	time.sleep(5)
			# 	if 'error' in req and req['error']['error_code'] == 14:
			# 		self.captchaSid=req['error']['captcha_sid']
			# 		webbrowser.open_new_tab(req['error']['captcha_img'])
			# 		self.captchaKey = input('enter captcha: ')
			# 		req = requests.get('https://api.vk.com/method/status.set?owner_id='+str(person[0])+'&text='+text+'&captcha_sid='+str(self.captchaSid)+'&captcha_key='+str(self.captchaKey)+'&access_token='+accTok)
			# 		time.sleep(5)
			if step==1:
				# vkap.status.set(owner_id=person[0], text=weather('Майами', 'current'))
				req=requests.get('https://api.vk.com/method/status.set?owner_id='+str(person[0])+'&text='+weather('Майами', 'current')+'&v=5.37&access_token='+accTok).json()
				time.sleep(timer)
				if 'error' in req and req['error']['error_code'] == 14:
					self.captchaSid=req['error']['captcha_sid']
					# webbrowser.open_new_tab(req['error']['captcha_img'])
					# self.captchaKey = input('enter captcha: ')
					Comb.captcha(req['error']['captcha_img'])
					req = requests.get('https://api.vk.com/method/status.set?owner_id='+str(person[0])+'&text='+equake()+'&captcha_sid='+str(self.captchaSid)+'&captcha_key='+str(self.captchaKey)+'&access_token='+accTok)
					time.sleep(60*2)

			elif step==2:
				req=requests.get('https://api.vk.com/method/status.set?owner_id='+str(person[0])+'&text='+equake()+'&v=5.37&access_token='+accTok).json()
				time.sleep(timer)
				if 'error' in req and req['error']['error_code'] == 14:
					self.captchaSid=req['error']['captcha_sid']
					# webbrowser.open_new_tab(req['error']['captcha_img'])
					# self.captchaKey = input('enter captcha: ')
					Comb.captcha(req['error']['captcha_img'])
					req = requests.get('https://api.vk.com/method/status.set?owner_id='+str(person[0])+'&text='+equake()+'&captcha_sid='+str(self.captchaSid)+'&captcha_key='+str(self.captchaKey)+'&access_token='+accTok)
					time.sleep(60*2)
			elif step>2:
				step=0
				time.sleep(5)
	def getVideoAlbums(self, public_id):
		arr=[]
		videos = vkapi.video.getAlbums(owner_id=public_id, count=100, extended=1)
		for x,y in zip(range(videos['count']), videos['items']):
			# if x==0:
			# 	str(1), y['title'], y['count'])
			# else:
			arr.append({'number': x+1, "title":y['title'], "count":y['count'], "id":y['id']})
		return arr

	


	def captcha(self, urlImg):

		def getKey(event):
			global key
			key = e1.get()
		url = urlImg
		u = urlopen(url)
		raw_data=u.read()
		u.close()
		root = Tk()
		s = io.BytesIO(raw_data)
		pil_image = Image.open(s)
		image = ImageTk.PhotoImage(pil_image)
		root.title('Captcha')
		root.geometry('200x200+500+200')
		root.resizable(False, False)
		root.configure(bg='#ccc')
		e1=Entry(root)
		e1.place(x=15, y=100)
		# e1.pack()
		button1 = Button(root, text='Button1')
		button1.bind('<Button-1>', getKey)
		button1.place(x=50, y=150)

		label=Label(root, image = image).place(x=40, y=20)
		root.call('wm', 'attributes', '.', '-topmost', True)							
		root.mainloop()		
		# print(posts)
		return(key)

	def getGifs(self, ownerId, count):
		step=-10
		while step<count:
			step+=10
			wall = vkapi.wall.get(owner_id=ownerId, offset=step, count=10)
			for i in wall['items']:
				if 'attachments' in i:
					for a in i['attachments']:
						if a['type']=='doc' and a['doc']['ext']=='gif':
							req = requests.get("https://api.vk.com/method/docs.add?owner_id="+str(a['doc']["owner_id"])+"&doc_id="+str(a['doc']['id'])+"&v=5.37&access_token="+accTok).json()
							time.sleep(1)
							if 'error' in req and req['error']['error_code']==14:
								self.captchaSid=req['error']['captcha_sid']
								self.captchaKey=Comb.captcha('self', req['error']['captcha_img'])
								req = requests.get("https://api.vk.com/method/docs.add?owner_id="+str(a['doc']["owner_id"])+"&doc_id="+str(a['doc']['id'])+"&captcha_sid="+str(self.captchaSid)+"&captcha_key="+str(self.captchaKey)+"&access_token="+accTok).json()
								time.sleep(1)
def wiki():
	try:
		wikipedia.set_lang('ru')
		# wpage = wikipedia.summary('Билл Клинтон', sentences=5)
		wpage = wikipedia.random(pages=1)
		summ = wikipedia.summary(wpage, sentences=8)
		# wpage2 = wikipedia.page(wpage)
		# images = wpage2.images
		# box = {'text':summ, 'images':images}
		
	except:
		wpage = wikipedia.random(pages=1)
		summ = wikipedia.summary(wpage, sentences=5)
	
	return summ
def equake():
	now = easy_date.convert_from_timestamp(time.time(), '20'+'%y-%m-%d')
	p=re.compile('(?<=\d{4}-\d{2}-)(\d+)')
	result1 = re.search(p, now)
	mags=[]
	yesterdayDay=str(int(result1.group(0))-1)
	yestedayDate = re.sub(p, yesterdayDay, now)
	url = "http://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=4.5&maxmagnitude=10&starttime="+yestedayDate
	req = requests.get(url).json()
	for i in req['features']:
		mags.append(('Маг: '+str(i['properties']['mag']), 'Место: '+re.sub("M\s\d\.\d\s-\s.*\s", '', i['properties']['title']), 'Угроза: '+str(i['properties']['alert'])))

	quakes = re.sub("\[|\]|'|\)|\(",'',str(sorted(mags, reverse=True, key=itemgetter(0))[:3])).replace('None','Нет').replace('green', 'зелёный').replace('yellow', 'жёлтый').replace('orange', 'оранжевый').replace('red', 'красный').replace('of', 'от').replace('km', 'км')
	return quakes
	# for i in quakes:
	# 	print(i[1])

		# print(i['properties']['mag'],'\n',i['properties']['title'], i['properties']['alert'])


		# 	for b in a['properties']:
		# 		print(b['mag'])

def weather(city_name, mode):
	headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36", "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"}
	appId="26641b63856d78bdbc1c25643f3bebee"
	if mode == 'forecast':
		text=[]
		weatherUrl = "http://api.openweathermap.org/data/2.5/forecast?q=%s&lang=ru&units=metric&APPID=%s" % (city_name, appId)
		getWeather = requests.get(weatherUrl).json()
		d = getWeather
		for i,y in zip(range(len(d['list'])), d['list']):
			if i%8==1:
				# print(y)
				text.append('Дата: '+easy_date.convert_from_timestamp(y['dt'], "%d.%m.%y"))
				text.append('Описание: ' + str(y['weather'][0]['description']))
				text.append('Температура: ' + str(y['main']['temp']) + ' C˚')
				text.append('Влажность: ' + str(y['main']['humidity']) + '%')
				text.append('Давление: ' + str(y['main']['pressure']) + 'мм')
				text.append('Скорость ветра: ' + str(y['wind']['speed'])+'м/с')
				text.append(' ')
				# text.append('Восход солнца: ' + str(easy_date.convert_from_timestamp(y['sys']['sunrise'], " %H:%M:%S")))
				# text.append('Закат солнца: ' + str(easy_date.convert_from_timestamp(y['sys']['sunset'], " %H:%M:%S")))
			# print(json.dumps(y[1], indent=4, ensure_ascii=False))	
		text =str(text).replace(', ','\n')
		p = re.compile("\[|\]|'")
		# print(p.sub('', text))
		text = p.sub('', text)
		# text = 'Дата:%s\nОписание: %s\nТемпература: %s С˚\nВлажность: %s%s\nДавление: %s мм\nСкорость ветра: %s м/с\nВосход солнца: %s\nЗакат солнца: %s\n' % (easy_date.convert_from_timestamp(d['list']['dt'], "%d.%m.%y %H:%M:%S"), d['list']['weather'][0]['description'], d['list']['main']['temp'], d['list']['main']['humidity'],'%',d['list']['main']['pressure'], d['list']['wind']['speed'], easy_date.convert_from_timestamp(d['list']['sys']['sunrise'], " %H:%M:%S"),easy_date.convert_from_timestamp(d['list']['sys']['sunset'], " %H:%M:%S"))


	elif mode == 'current':
		weatherUrl= "http://api.openweathermap.org/data/2.5/weather?q=%s&lang=ru&units=metric&APPID=%s" % (city_name, appId)
		getWeather = requests.get(weatherUrl).json()
		d = getWeather
		# text =  'Описание: %s\nТемпература: %s С˚\nВлажность: %s%s\nДавление: %s мм\nСкорость ветра: %s м/с\nВосход солнца: %s\nЗакат солнца: %s\n' % (d['weather'][0]['description'], d['main']['temp'], d['main']['humidity'],'%',d['main']['pressure'], d['wind']['speed'], easy_date.convert_from_timestamp(d['sys']['sunrise'], " %H:%M:%S"),easy_date.convert_from_timestamp(d['sys']['sunset'], " %H:%M:%S"))
		text =  'Описание: %s\nТемпература: %s С˚\nВлажность: %s%s\nДавление: %s мм\nСкорость ветра: %s м/с' % (d['weather'][0]['description'], d['main']['temp'], d['main']['humidity'],'%',d['main']['pressure'], d['wind']['speed'])
	

	return text
	
def newsBlock():
	while 1:
		vkapi.wall.post(owner_id=person[0], message=euronewsUSA())
		time.sleep(10)
		vkapi.wall.post(owner_id=person[0], message=euronewsNews())
		time.sleep(10)
		vkapi.wall.post(owner_id=person[0], message=vestiRss())
		time.sleep(1)
# wiki()
from_id=int
times=0
def sendMesBot(message):
	photoAlbums = Comb.getAlbums('self', person[0])
	photos=[]
	
	botMessage=str
	guid = random.randint(1, 10000)

	for i in photoAlbums:
		if i['title'] == 'space':
			for a in vkapi.photos.get(owner_id=person[0], album_id=i['id'], count=900)['items']:
				photos.append(a['id'])

	if message == 'default':
		botMessage="""
		Попробуйте написать несколько позже.\n
		Так же вы можете: \n 1. почитать Википедию, прислав слово "wiki"; \n 2. почитать конституцию РФ прислав мне текст: конст + пробел + номер статьи от 1 до 137; \n3. узнать текущую погоду в городе прислав мне: погода "название города" или для прогноза погоды на 5 дней: погода 5 "название города".
		"""
		# botMessage=""" 
		# """
		vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid, attachment='photo'+str(person[0])+'_'+str(random.choice(photos)))
		# vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid, attachment='photo179349317_374641254')
	elif message == 'wiki':
		botMessage = wiki()
		vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
		# vkapi.messages.send(user_id=from_id, message=botMessage['text'], guid=guid)
	elif re.search('конст \d+', message):
		res = re.search('\d+', message)
		state = res.group(0)
		if int(state)<=137:
			botMessage = const(state)
			vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
		else:
			botMessage='Такой статьи нет в Конституции. Повторите поиск.'
			vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
		# times=0
	elif re.search('погода', message):
		res = str.split(message,' ')
		if len(res)==3 and res[1]=='5':
			city = res[2]
			botMessage = weather(city, 'forecast')
			vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
		elif len(res)==2:	
			botMessage = weather(res[1], 'current')

			vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
	
def getFests():
	headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36", "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"}
	req = requests.get("https://www.fest300.com/festivals", headers=headers).content
	parsed = BeautifulSoup(req, "html.parser")
	with open('tempFest.html', 'w') as a:
		a.write(parsed.prettify())
	# print(parsed)
def getPollingServer():
		headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36", "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"}
		params = vkapi.messages.getLongPollServer()	
		# params = requests.get("https://api.vk.com/method/messages.getLongPollServer?use_ssl=0&access_token="+accTok, headers=headers).json()

		ts = params['ts']

		url = 'http://%s?act=a_check&key=%s&ts=%s&wait=0&mode=2' % (params['server'], params['key'], params['ts'])
		global from_id
		global times

		while True:
			try:
				req = requests.get(url).json()
			except:
				req = requests.get(url).json()
			if req!=None:
				# os.system('clear')
				if 'updates' in req and req['updates']!='':
					for i in req['updates']:
						if len(i)>6:
							if i[6] and i[6]!='wiki' and not re.search('конст \d+',i[6]) and not re.search('погода ', i[6]):
								if easy_date.convert_from_timestamp(i[4], "%H:%M:%S") == easy_date.convert_from_timestamp(time.time(), "%H:%M:%S"):
									sys.stdout=open('MessagesBotLog.txt', 'a+')
									from_id=i[3]
									sendMesBot('default')
									print(i, '\n')
									time.sleep(5)
							elif i[6] and i[6]=='wiki':
								if easy_date.convert_from_timestamp(i[4], "%H:%M:%S") == easy_date.convert_from_timestamp(time.time(), "%H:%M:%S"):
									sys.stdout=open('MessagesBotLog.txt', 'a+')
									from_id=i[3]
									sendMesBot('wiki')
									print(i, '\n')
									time.sleep(5)
							elif i[6] and re.search('конст \d+', i[6]):
								if easy_date.convert_from_timestamp(i[4], "%H:%M:%S") == easy_date.convert_from_timestamp(time.time(), "%H:%M:%S"):
									sys.stdout=open('MessagesBotLog.txt', 'a+')
									from_id=i[3]
									sendMesBot(i[6])
									print(i, '\n')
									time.sleep(5)
							elif i[6] and re.search('погода ', i[6]):
								if easy_date.convert_from_timestamp(i[4], "%H:%M:%S") == easy_date.convert_from_timestamp(time.time(), "%H:%M:%S"):
									sys.stdout=open('MessagesBotLog.txt', 'a+')
									from_id=i[3]
									sendMesBot(i[6])
									print(i, '\n')
									time.sleep(5)
				elif 'error' in req:
					print('error')


if __name__ == "__main__":
	Combain = Comb()

	def actions():
		print('{:=^80}'.format(" Wellcome to VK API combain ") + '\n\n  Please type kind of action would you like to do with this program.\n\n'+'{:=^80}'.format('=')+'\n')

		actions = ['Multi-post', 'Download photos', 'Copy photos', 'Comments Bot', 'Get text from wall', 'Cross delete posts', 'Delete from board', 'Messages Bot', 'Delete photos', 'Likes', 'wheather test', 'test tkinter', 'Upload owner photo', 'status', 'Get Videos', 'equake', 'GetGifs', 'getFests']

		for i,y in zip(range(len(actions)), actions):
			if i == 0:
				print(str(1)+'.', actions[0])
			else:
				print(str(i+1)+'.', y)

		action = input('\nEnter action: ')

		if int(action) == 1:
			mins = int(input('Time delay in minutes: '))
			try:
				Combain.postMulti(psy+psy2+mudreci2+mudreci+XXvek+davch+science+atlant+prosv+space+other+zeland+cuts+slovo, mins)
			except:
				Combain.postMulti(psy+psy2+mudreci2+mudreci+XXvek+davch+science+atlant+prosv+space+other+zeland+cuts+slovo, mins)
		elif int(action) == 5:
			ioffset = int(input('Offset: '))
			wall_id = int(input('Wall_id: '))
			count = int(input('Count: '))
			print(Combain.getWall('yes', ioffset, wall_id, 'text', 'no', count))
			# Combain.getWall('no', 0, wall_id, 'text', False, count, )
		elif int(action) == 2:
			print('1. Albums\n2. Wall')
			selectedSource = int(input('select source will be copied from: '))
			if selectedSource==1:
				publicId = int(input('public id: '))
				albums = Combain.getAlbums(publicId)
				for i in albums:
					print(str(i['number'])+'. '+i['title'],i['count'])
				selectedAlbum = int(input('select number with album: '))
				for i in albums:
					if selectedAlbum == i['number']:
						print(i['title'])
						albumId=i['id']
						albumTitle=i['title']
						albumCountPhotos = i['count']
				path = input('path to save photos[default is your HOME directory]: ')
				if not path: path = os.environ['HOME']+'/'
				Combain.downlPhotos(publicId, albumId, albumTitle, path, albumCountPhotos)
			elif selectedSource==2:
				albumId='wall'
				albumTitle='Wall'
				publicId = int(input('public id: '))
				countPhotos=int(input('count photos to download: '))
				path = input('path to save photos[default is your HOME directory]: ')
				if not path: path = os.environ['HOME']+'/'
				Combain.downlPhotos(publicId, albumId, albumTitle, path, countPhotos)
		elif int(action) == 6:
			# list_ids = input("Enter list of groups use ','. Default multi-post group ids list is used ")
			# makeListToDir = 
			Combain.crossDeletingPosts(Combain.dict_names_and_ids)
		elif int(action) == 3:
			sources = [{'number':1, 'title':'Albums'}, {'number':2,'title':'Wall'}];
			for i in sources:
				print(str(i['number'])+'. '+i['title'])
			selectedSource = int(input('select source will be copied from: '))
			if selectedSource==1:
				fromId = int(input("Pubic either user will be copied from: "))
				albumsToCopyFrom = Combain.getAlbums(fromId)
				for i in albumsToCopyFrom:
					print(str(i['number'])+'. '+i['title'], i['count'])
				selectedAlbumToCopyFrom = int(input('Select number of album will be copied from: '))
				for i in albumsToCopyFrom:
					if selectedAlbumToCopyFrom==i['number']:
						albumIdToCopyFrom = i['id']
						countPhotosToCopyFrom=i['count']
						titleAlbumToCopyTo=i['title']
				print('Dow you want to create new album to place new photos in to it?')
				createAlbumState=input('[n]default[y/n]:')
				if createAlbumState == 'y':
					title = input('title [default inherits donor group name]: ')
					if not title:
						publicName = vkapi.groups.getById(group_id=str(abs(fromId)))[0]['name']
						title = publicName+' '+titleAlbumToCopyTo
					vkapi.photos.createAlbum(owner_id=person[0], title=title, privacy_view='nobody', v=5.35)
					albumNameToCopyTo = publicName+' '+titleAlbumToCopyTo
				elif createAlbumState == 'n':
					albumsToCopyTo = Combain.getAlbums(person[0])
					for i in albumsToCopyTo:
						print(str(i['number'])+'. '+i['title'], i['count'])
					selectedAlbumNameToCopyTo = int(input("Select number of album where will be copied to: "))
					for i in albumsToCopyTo:
						if selectedAlbumNameToCopyTo==i['number']:
							albumNameToCopyTo=i['title']
			elif selectedSource==2:
				albumIdToCopyFrom='wall'
				fromId=int(input('from id: '))
				print('Dow you want to create new album to place new photos in to it?')
				createAlbumState=input('[n]default[y/n]:')
				if createAlbumState == 'y':
					title = input('title [default inherits donor group name]: ')
					if not title:
						publicName = vkapi.groups.getById(group_id=str(abs(fromId)))[0]['name']
						title = publicName
					vkapi.photos.createAlbum(owner_id=person[0], title=title, privacy_view='nobody', v=5.35)
					countPhotosToCopyFrom = int(input('count: '))
					albumNameToCopyTo = publicName
				elif createAlbumState == 'n':
					albumsToCopyTo = Combain.getAlbums(person[0])
					for i in albumsToCopyTo:
						print(str(i['number'])+'. '+i['title'], i['count'])
					selectedAlbumNameToCopyTo = int(input("Select number of album where will be copied to: "))
					for i in albumsToCopyTo:
						if selectedAlbumNameToCopyTo==i['number']:
							albumNameToCopyTo=i['title']
					countPhotosToCopyFrom = int(input('count: '))
			Combain.copyPhotoToAlbum(person[0], fromId, albumNameToCopyTo, albumIdToCopyFrom, countPhotosToCopyFrom)	
			# print(person[0], fromId, albumNameToCopyTo, albumIdToCopyFrom, countPhotosToCopyFrom )
		elif int(action) == 7:
			Combain.delTopicComments()
		elif int(action) == 8:
			getPollingServer()
		elif int(action) == 9:
			Combain.delPhotos()
		elif int(action) == 10:
			print('1. Add\n2. Del')
			selectedAction = int(input('select number of action: '))
			owner = input('public or user id: ')
			count = input('count: ') 
			if selectedAction == 1:
				Combain.addLikes('add','no', owner, count)
			elif selectedAction == 2:
				Combain.addLikes('checkLikes', 'del', owner, count)
		elif int(action) == 11:
			weather('Новоуральск', 'forecast')
		elif int(action) == 12:
			Combain.captcha('http://api.vk.com/captcha.php?sid=986265422898&s=1')
		elif int(action) == 13:
			dir1 = os.listdir('/Users/hal/Pictures/179349317/Трипофобия/')
			dir1.pop(0)
			while True:
				Combain.uploadOwnerPhoto(random.choice(dir1))
				time.sleep(60*10)
		elif int(action) == 14:
			Combain.statusSet(60*2)
		elif int(action) == 15:
			public_id = input("public_id: ")
			for i in Combain.getVideoAlbums(public_id):
				print(i['number'],i['title'],i['count'])
			selectedAlbum = input("enter number of album: ")
			for i in Combain.getVideoAlbums(public_id):
				if i['number'] == int(selectedAlbum):
						album_id=i['id']
						count=i['count']
			titles=[]
			# for x,y in zip(range(i['count']), vkapi.video.get(owner_id=public_id, album_id=album_id, count=count)['items']):
			for x in vkapi.video.get(owner_id=public_id, album_id=album_id, count=50)['items']:
				titles.append(x['title'])

			print(len(titles))
		elif int(action) == 16:
			equake()
		elif int(action)==17:
			ownerId=int(input('public id: '))
			count = int(input('count of wall posts: '))
			Combain.getGifs(ownerId, count)
		elif int(action)==18:
			# getFests()
			
			
			with open("subscribes.txt", "w") as o:
				o.write(str(vkapi.users.getSubscriptions(user_id=person[0], extended=0)['groups']['items']+vkapi.users.getSubscriptions(user_id=person[0], extended=0)['users']['items']))

	if sys.argv[1] == 'manual':
		actions()

	elif sys.argv[1] == 'auto':
		Combain.postMulti(psy+psy2+mudreci2+mudreci+XXvek+davch+science+atlant+prosv+space+psy+other+zeland+slovo+cuts, int(sys.argv[2]))
		
	# Combain.getPhoto(-682618, Combain.getAlbums(-682618, 1)[0], 1 )
	# 	aa = Combain.getAlbums(-40485321)
	# # Combain.postOne()
	# Combain.getWall('no', -32149661, 'photo', 20, 'yes') #args (offset, wall_id, dtype, count = 1, bot='no', sdate='no', likes='no')
	# Combain.getWall('yes', -32149661, 'photo', 20) #args (offset, wall_id, dtype, count = 1, bot='no', sdate='no', likes='no')
	# Combain.crossDeletingPosts(Combain.dict_names_and_ids)
	# Combain.dateChecker()
	# Combain.getCitat()
	# Combain.getAlbums(-57014305, 1)
	# Combain.getTopicCommentIds()
	# Combain.delTopicComments()
	# Combain.getPhoto( -57014305, Combain.getAlbums(-57014305, 3), 1, 'yes', '/Users/hal/', 'id', 'yes', 'no')
	# Combain.getPhoto( -57014305, 'none', 50, 'yes', '/Users/hal/', 'id', 'yes', 'yes')
	# Combain.rePost()
	# Combain.copyPhoto( person[0], 'JOsdfasdfKER', -32149661 )
	# Combain.changeOwnPhoto()
	# Combain.getDialogs()
	# Combain.crossDeletingPosts(Combain.dict_names_and_ids)
