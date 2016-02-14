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
from urllib.parse import urlparse
from pync import Notifier
from prettytable import PrettyTable
# cgitb.enable()

# print('Content-type: text/html')
# print()
# https://api.vk.com/method/photos.get?owner_id=-77093415&album_id=wall&count=40&access_token=00af0cff7458595045e1893775acf9b561dad00d6df9de580f9839e2722d5090e3fbf819a471461094666
# User and app info
session = vk.Session( access_token = 'f98576da13f80eb5b3ab0949e1527ef48c9da72155005b7140362908471415d707eecb765bea05aa2852f')
vkapi = vk.API(session, v=5.44 , timeout=50)
vkerror = vk.api.VkAPIError
other = [-72580409, -61330688]
person = [179349317]
# person = [319258436]
# person = [319315119]
# app_id = 4967352
app_id = 5040349
accTok = 'f98576da13f80eb5b3ab0949e1527ef48c9da72155005b7140362908471415d707eecb765bea05aa2852f'

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
		self.group_ids = [-60409637, -72580409]
		self.group_Ids_ToString = str.join(',', [str(abs(x)) for x in self.group_ids])
		self.groupsNoDumps = vkapi.groups.getById(group_ids=self.group_Ids_ToString, indent=4, sort_keys=True, ensure_ascii=False)
		self.groupsWithDumps = json.dumps(vkapi.groups.getById(group_ids=self.group_Ids_ToString),indent=4, sort_keys=True, ensure_ascii=False)
		self.group_names = [i['name'] for i in json.loads(self.groupsWithDumps)]
		self.group_screen_names=[i['screen_name'] for i in json.loads(self.groupsWithDumps)]
		self.dict_names_and_ids=[];
		for i,x,y in zip(self.group_names, self.group_ids, self.group_screen_names):
				self.dict_names_and_ids.append({'name':i, 'id':x, 'screen_name':y})


	def dateChecker(self):

		# Waiting for the post to give parametrs of group walls and date of current post

		while 1:
			self.getWall('no', person[0], 'text', 1)
			time.sleep(0.8)

	def getWall( self, offset,  ioffset, wall_id, dtype, remove, count = 1, bot='no', sdate='no', likes='no', user_id = 179349317):
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
						hoo = self.getWall('no', person[0], 'id', 1)
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
		pids = self.getWall('no', public, 'id', 1)
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
				photoFromWall = self.getWall('no', 'no', wall_id, 'photo', 'no', count)  
				for i in photoFromWall:
					ids.append(i)
				return ids
		else:

			if multi == 'no' and type(album)==int:
				photos = vkapi.photos.get( owner_id = wall_id, album_id = album['id'], count = count  )	
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
								for a in vkapi.photos.get( owner_id=wall_id, album_id=i['id'], count=i['count'], offset=0 )['items']:
									if i['id'] == a['album_id']:
										print(i)
						elif i['count']<1000:
								for a in vkapi.photos.get( owner_id=wall_id, album_id=i['id'], count=i['count'], offset=0 )['items']:
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
						for a in vkapi.photos.get( owner_id=wall_id, album_id=i['id'], count=i['count'] )['items']:
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

	def UpdateData(self, fromId, date, dtype, source, album_id=False):
		names=[]

		if dtype=='photo':
			fname='updatePhotoData.json'
		if dtype=='gif':
			fname='updateGifData.json'
		if dtype=='pdf':
			fname='updatePdfData.json'
		if dtype=='audio':
			fname='updateAudioToCopy.json'
		if dtype=='video':
			fname='updateVideoToCopy.json'
		if dtype=='page':
			fname='updatePageToCopy.json'
		if dtype=='page':
			updatesPath=os.path.join('walls', 'updates', fname)
		else:
			updatesPath=os.path.join('updates',source,fname)

		if source=='wall' or source=='box':
			if fromId<0:
				publicName = re.sub("[\[\]]", '', vkapi.groups.getById( group_id = abs(fromId))[0]['name'])
			elif fromId>0:
				publicName=vkapi.users.get(user_ids=str(fromId), fields='nickname')[0]['first_name']
				publicName=publicName+' '+vkapi.users.get(user_ids=str(fromId), fields='nickname')[0]['last_name']
			if os.path.exists(updatesPath):
				with open(updatesPath) as f:
					data = json.load(f)
				for i in data:
					names.append(i['name'])
				if publicName in names:
					for i in data:
						if i['name']==publicName:
							i['date']=date
				elif publicName not in names:
					data.append({"id":fromId, "date": date,"name":publicName})

				with open(updatesPath, 'w') as f:
					json.dump(data, f, indent=4, ensure_ascii=False)
			else:
				file1 = open(updatesPath, 'a+')
				data=[{"id":fromId, "date": date,"name":publicName}]
				file1.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
				file1.close()
		elif source=='album':
			if dtype=='video':
				albumName=vkapi.video.getAlbumById(owner_id=fromId, album_id=album_id)['title']
				time.sleep(1)
			if dtype=='photo':
				albumName=vkapi.photos.getAlbums(owner_id=fromId, album_ids=album_id)['items'][0]['title']
			if fromId<0:
				publicName = vkapi.groups.getById( group_id = abs(fromId))[0]['name']
			elif fromId>0:
				publicName=vkapi.users.get(user_ids=str(fromId), fields='nickname')[0]['first_name']
				publicName=publicName+' '+vkapi.users.get(user_ids=str(fromId), fields='nickname')[0]['last_name']
			if os.path.isfile(updatesPath):
				with open(updatesPath) as f:
					data = json.load(f)
				for i in data:
					names.append({'public':i['name'],'album':i['album']})
			# print([i['public'] for i in names if i['album']=='Органы'])
				if publicName in [i['public'] for i in names if i['album']==albumName]:
					for i in data:
						if i['name']==publicName and i['album']==albumName:
							i['date']=date

				elif publicName not in [i['public'] for i in names if i['album']==albumName]:
					data.append({"id":fromId, "date": date,"name":publicName, 'album':albumName})

				with open(updatesPath, 'w') as f:
					json.dump(data, f, indent=4, ensure_ascii=False)

			else:
				file1 = open(updatesPath, 'a+')
				data=[{"id":fromId, "date": date,"name":publicName, 'album':albumName}]
				file1.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
				file1.close()
	def delPhotos(self):
		photos = vkapi.photos.get(owner_id=person[0], album_id='saved')['items']
		for i in photos:
			vkapi.photos.delete(owner_id=person[0], photo_id=i['id'])
			time.sleep(0.4)

	def copyPhotoToAlbum( self, to_id, from_id, albumNameToCopyTo, albumIdToCopyFrom, countPhotos, text=False):
		album_id = []
		photo_id = []
		albumsFromIds = []
		photosToCopy = []
		updateDate=int
		text1=str
		toFile=[]
		# getAlbumsFromId = Comb.getAlbums('self', from_id)
		step=-100
		getAlbumsTo = self.getAlbums(to_id)
		if albumIdToCopyFrom=='wall':
			rev = 1
			source='wall'
		else:
			rev = 0
			source='album'
		for i in getAlbumsTo:
			if i['title'] == albumNameToCopyTo:
				album_id.append(i['id'])


		with open(os.path.join('updates', source, "updatePhotoData.json")) as f:
				data = json.load(f)	
				for i in data:
					if i['id']==from_id:
						updateDate=i['date']

		if countPhotos>1000:
			photosGet=vkapi.photos.get(owner_id=from_id, album_id=albumIdToCopyFrom, count=100, rev=rev)
			if albumIdToCopyFrom=='wall':
				self.UpdateData(from_id, photosGet['items'][0]['date'], 'photo', 'wall')
			elif albumIdToCopyFrom!='wall':
				self.UpdateData(from_id, photosGet['items'][0]['date'], 'photo', 'album', albumIdToCopyFrom )
			
			while step<countPhotos:
				step+=100
				try:
					photosGet=vkapi.photos.get(owner_id=from_id, album_id=albumIdToCopyFrom, count=100, offset=step, rev=rev)
					time.sleep(1)
					for a in photosGet['items']:
						if text==True:
							if 'post_id' in a:
								for b in vkapi.wall.getById(posts=str(from_id)+'_'+str(a['post_id']), extended=1)['items']:
									# text1=re.sub('(?<=\n).*$','', b['text'])
									if len(b['text'])>500:
										f = re.search("[\w\W]{500}", i['text'])
										text1=f.group(0)
									else:
										text1=i['text']
						if albumIdToCopyFrom!='wall' and a['text']!=None:
							text1=re.sub('[^\s]\W', '', a['text'])
						copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'])

				except vkerror as e:
					captcha_sid=e.captcha_sid
					captcha_key=self.captcha(e.captcha_img)
					copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'], captcha_sid=captcha_sid, captcha_key=captcha_key)
					movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
					time.sleep(1)
					if text1!='':
						vkapi.photos.edit(owner_id=person[0], photo_id=copyPhotos, caption=text1)
				movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
				time.sleep(1)
				if text1:
					vkapi.photos.edit(owner_id=person[0], photo_id=copyPhotos, caption=text1)
				time.sleep(1)
		else:	
			photosGet=vkapi.photos.get(owner_id=from_id, album_id=albumIdToCopyFrom, extended=1, count=countPhotos, rev=rev)
			if albumIdToCopyFrom=='wall':
				self.UpdateData(from_id, photosGet['items'][0]['date'], 'photo', 'wall')
			elif albumIdToCopyFrom!='wall':
				self.UpdateData(from_id, photosGet['items'][0]['date'], 'photo', 'album', albumIdToCopyFrom)
			for a in photosGet['items']:
				if 'post_id' in a and "copy_history" not in a :
					req = vkapi.wall.getById(posts=str(from_id)+'_'+ a['post_id'], extended=1)
				if text == True:
					for i in req['wall']:
						if 'text' in i and i['text']!='':
							if len(i['text'])>500:
								f = re.search("[\w\W]{500}", i['text'])
								text1=f.group(0)
							else:
								text1=i['text']
				if albumIdToCopyFrom!='wall' and a['text']!=None:
					text1=a['text'].replace(',','').replace('#','')	
				try:	
					copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'])
				# 	time.sleep(1)
					if copyPhotos and text1!=None:
						toFile.append({"id":copyPhotos, "text":text1})
					
					if updateDate:
						if a['date']==updateDate:
							break
				
				except vkerror as e:
					captcha_sid=e.captcha_sid
					captcha_key=self.captcha(e.captcha_img)
					copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'], captcha_sid=captcha_sid, captcha_key=captcha_key)
					movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)

					if text1:
						vkapi.photos.edit(owner_id=person[0], photo_id=copyPhotos, caption=text1)
					time.sleep(1)
				movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
				if text1:
					vkapi.photos.edit(owner_id=person[0], photo_id=copyPhotos, caption=text1)
				time.sleep(1)

				# if re.search('#', text1):
				# 	texta = text1.replace('#', '')
				# else:
				# 	texta = text1

				# cap = requests.get("https://api.vk.com/method/photos.edit?owner_id="+str(person[0])+"&photo_id="+str(copyPhotos['response'])+"&caption="+str(texta)+"&v=5.37&access_token="+accTok).json()
				# time.sleep(1)

				# if 'error' in cap:
				# 	print(cap['error'])
				# 	self.captchaSid=cap['error']['captcha_sid']
				# 	self.captchaKey =Comb.captcha('self', cap['error']['captcha_img'])
				# 	cap = requests.get("https://api.vk.com/method/photos.edit?owner_id="+str(person[0])+"&photo_id="+str(copyPhotos['response'])+"&caption="+texta+"&captcha_key="+str(self.captchaKey)+"&captcha_sid="+str(self.captchaSid)+"&access_token="+accTok).json()
				# 	time.sleep(1)
				if text==True or albumIdToCopyFrom!='wall':
					with open("photoCaptions.json", "w") as jj:
						jj.write(json.dumps(toFile, indent=4, ensure_ascii=False))

	def copyPhotoToAlbum2(self, to_id, from_id, albumNameToCopyTo, albumIdToCopyFrom, countPhotos, text=False):
		album_id = []
		photo_id = []
		albumsFromIds = []
		photosToCopy = []
		updateDate=int
		text1=str
		toFile=[]
		phlist=[]
		st=0
		stop=False
		# getAlbumsFromId = Comb.getAlbums('self', from_id)
		step=-1
		getAlbumsTo = self.getAlbums(to_id)
		if albumIdToCopyFrom=='wall':
			source='wall'
		else:
			source='album'
		for i in getAlbumsTo:
			if i['title'] == albumNameToCopyTo:
				album_id.append(i['id'])
		with open(os.path.join('updates', source, "updatePhotoData.json")) as f:
				data = json.load(f)	
				for i in data:
					if i['id']==from_id:
						updateDate=i['date']
		date1=[i['date'] for i in vkapi.wall.get(owner_id=from_id, count=10)['items'] if 'is_pinned' not in i][0]
		# date2=[i['date'] for i in vkapi.photos.get('owner_id')]
		if albumIdToCopyFrom=='wall':
			self.UpdateData(from_id, date1, 'photo', 'wall')
		# elif albumIdToCopyFrom!='wall':
		# 	Comb.UpdateData('self', from_id, photosGet['items'][0]['date'], 'photo', 'album', from_id)

		while step<countPhotos:
			step+=1
			if stop==True:
				break
			# photosGet=vkapi.photos.get(owner_id=from_id, album_id='wall', offset=step, rev=1)
			photosGet=vkapi.wall.get(owner_id=from_id, count=1, offset=step)
			time.sleep(0.5)
			for i in photosGet['items']:
				if 'text' in i and i['text']!='':
					if len(i['text'])>500:
						f = re.search("[\w\W]{500}", i['text'])
						text1=f.group(0)
					else:
						text1=i['text']
				if i['date']==updateDate:
					stop=True
				if 'attachments' in i:
					for a in i['attachments']:
						if a['type']=='photo':
							try:

								copyPhotos = vkapi.photos.copy(owner_id=a['photo']['owner_id'], photo_id=a['photo']['id'])
								print(copyPhotos)
								if  copyPhotos and text1!=None:
										toFile.append({"id":copyPhotos, "text":text1})
								movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
								time.sleep(1)
							except vkerror as e:
								if e.code==15:
									time.sleep(1)
									continue
								captcha_sid=e.captcha_sid
								captcha_key=self.captcha(e.captcha_img)
								copyPhotos = vkapi.photos.copy(owner_id=a['photo']['owner_id'], photo_id=a['photo']['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)

								print(copyPhotos)
								movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
								time.sleep(1)
							# if text==True and text1!='':
							# 	with open("photoCaptions.json", "w") as jj:
							# 		jj.write(json.dumps(toFile, indent=4, ensure_ascii=False))
	def getTopicCommentIds(self):
		topic_id=self.getTopic()
		ids = []
		offset=-50
		while offset<10000:
			offset+=50
			topics = vkapi.board.getComments(group_id=53664217, offset=offset, topic_id=topic_id[0], count=50, sort='desc')['items']
			for i in topics:
				if (i['from_id']==person[0]):
					ids.append(i['id'])
			time.sleep(0.4)
		
		
		return ids
	def delTopicComments(self):
		topic_id=self.getTopic()
		ids=self.getTopicCommentIds()
		for i in ids:
			vkapi.board.deleteComment(group_id=53664217, topic_id=topic_id[0], comment_id=i)
			time.sleep(0.4)
	def postTopicComment( self ):
		'''Post comment into topic block of group'''

		topic_id = self.getTopic() 
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
			# time.sleep(1)

		
	
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
			for post in vkapi.wall.get(owner_id=selectedId, count=countPosts, offset=offset)['items']:
				if post['from_id'] == person[0]:
					vkapi.wall.delete(owner_id=selectedId, post_id=post['id'])
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

				for a in vkapi.photos.get( owner_id=public_id, album_id=album_id, count=10, offset=step, rev=rev)['items']:

					if not os.path.exists(path+publicName):
						os.mkdir(path=os.path.join(path,publicName))
					elif not os.path.exists( os.path.join(path, publicName, str(title)) ):
						os.mkdir( path=os.path.join(path,publicName,str(title)) )
					else:
						if requests.get(a['photo_604']).headers['content-type']=='image/jpeg':
							wget.download( a['photo_604'], out=path+publicName+'/'+str(title) )
					os.system("rm ./*.tmp")		


		else:
			for a in vkapi.photos.get( owner_id=public_id, album_id=album_id, count=albumCountPhotos, rev=rev )['items']:

				if not os.path.exists(path+publicName):
					os.mkdir(path=path+publicName)

				elif not os.path.exists( path+publicName + '/' + str(title) ):
					os.mkdir( path=path+publicName + '/' + str(title)  ) 
				else:
					wget.download( a['photo_604'], out=path+publicName+'/'+str(title) )
				os.system("rm ./*.tmp")		
		print('\n\n--------------------------\n\nDownload is complete\n\n')

	def addLikes(self, action, action2, owner, count):
		posts = vkapi.wall.get(owner_id=owner, count=count)
		if action == 'add':
			for i in posts['response']['items']:
				try:
					addLikes = vkapi.likes.add(owner_id="owner",type="post", item_id=i['id'])
					time.sleep(0.5)
				except vkerror as e:
					captcha_sid=e.captcha_sid
					captcha_key=Comb.captcha('self', e.captcha_img)
					addLikes = vkapi.likes.add(owner_id="owner",type="post", item_id=i['id'])
					time.sleep(0.5)
					if e.code == 9:
						print(e.message)
						break
						
		elif action == 'checkLikes':
			for i in posts['response']['items']:
				try:
					checkLikes = vkapi.likes.isLiked(owner_id=owner, type='post', item_id=i['id'])
				except vkerror as e:
					captcha_sid=e.captcha_sid
					captcha_key=Comb.captcha('self', e.captcha_img)
					checkLikes = vkapi.likes.isLiked(owner_id=owner, type='post', item_id=i['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)	
					print(checkLikes)
				if checkLikes == 1 and action2 == 'del':
					try:
						delLikes = requests.get('https://api.vk.com/method/likes.delete?owner_id='+owner+'&type=post&item_id='+str(i['id'])+'&access_token='+accTok)
					except vkerror as e:
						captcha_sid=e.captcha_sid
						captcha_key=Comb.captcha('self', e.captcha_img)
						delLikes = vkapi.likes.delete(owner_id=owner, type=post, item_id=i['id'], captcha_sid=captcha_sid, captcha_key=captcha_key)
						
	def uploadOwnerPhoto(self):
		ids=[]
		step=0
		dirr="/Users/hal/Pictures/179349317/МЕНТАЛЬНОЕ ПОРНО/"
		dir1 = os.listdir(dirr)
		dir1.pop(0)
		
		while 1:
			step+=1
			photo=random.choice(dir1)
			headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36", "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4"}
			uploadUrl = requests.get("https://api.vk.com/method/photos.getOwnerPhotoUploadServer?access_token="+accTok, headers=headers).json()['response']['upload_url']
			r = requests.post(uploadUrl, files={ 'file' : open(dirr+photo, 'rb') }).json()
			# photoSave = vkapi.photos.saveOwnerPhoto(server=r['server'], photo=r['photo'], hash=r['hash'])
			try:
				photoSave = vkapi.photos.saveOwnerPhoto(server=r['server'], photo=r['photo'], hash=r['hash'])
			except vkerror as e:
				captcha_sid=e.captcha_sid
				captcha_key=Comb.captcha('self', e.captcha_img)
				photoSave = vkapi.photos.saveOwnerPhoto(server=r['server'], photo=r['photo'], hash=r['hash'], captcha_key=captcha_key, captcha_sid=captcha_sid)
				
			for i in vkapi.wall.get(owner_id=person[0], count=1)['items']:
				if 'copy_history' not in i and i['text']=='':
					vkapi.wall.delete(owner_id=person[0], post_id=i['id'])

			for i in vkapi.photos.get(owner_id=person[0], album_id='profile')['items']:
					ids.append(i['id'])
			
			vkapi.photos.delete(owner_id=person[0], photo_id=ids[-2])
			time.sleep(60*5)

	def statusSet(self, timer):
		step=0
		# text = """▲▼▲▼▲▼・●⦿◎◉ ▲▼▲▼▲▼ ・●⦿◎◉ ▲▼▲▼▲▼ ・●⦿◎◉ ▲▼▲▼▲▼・●⦿◎◉ ▲▼▲▼▲▼ ・●⦿◎◉ ▲▼▲▼▲▼ ・●⦿◎◉ """
		text = """ Я каждый день думаю о тебе и поэтому прихожу сюда. а ты? :)🏦✌ Берегитесь снегопадов и морозов❄⚠  Не болейте Эболой и H1N1 📢"""
		while True: 
			step+=1
			# if step==1:
			# 	# vkapi.status.set(owner_id=person[0], text=text)
			# 	req=requests.get("https://api.vk.com/method/status.set?owner_id="+str(person[0])+"&text="+text+"&v=5.37&access_token="+accTok).json()
			# 	time.sleep(5)
			# 	if 'error' in req and req['error']['code'] == 14:
			# 		self.captchaSid=req['error']['captcha_sid']
			# 		webbrowser.open_new_tab(req['error']['captcha_img'])
			# 		self.captchaKey = input('enter captcha: ')
			# 		req = requests.get('https://api.vk.com/method/status.set?owner_id='+str(person[0])+'&text='+text+'&captcha_sid='+str(self.captchaSid)+'&captcha_key='+str(self.captchaKey)+'&access_token='+accTok)
			# 		time.sleep(5)
			if step==1:
				# vkap.status.set(owner_id=person[0], text=weather('Майами', 'current'))
				try:
					req=vkapi.status.set(owner_id=person[0], text=weather('Майами', 'current'))
					time.sleep(timer)
				except vkerror as e:
					captcha_sid=e.captcha_sid
					captcha_key=Comb.captcha('self', e.captcha_img)
					req=vkapi.status.set(owner_id=person[0], text=weather('Майами', 'current'), captcha_sid=captcha_sid, captcha_key=captcha_key)
					time.sleep(timer)

			elif step==2:
				try:
					req=vkapi.status.set(owner_id=person[0], text=equake())
					time.sleep(timer)
				except vkerror as e:
					captcha_sid=e.captcha_sid
					captcha_key=Comb.captcha('self', e.captcha_img)
					req=vkapi.status.set(owner_id=person[0], text=equake(), captcha_sid=captcha_sid, captcha_key=captcha_key)
					time.sleep(timer)

			elif step==3:
				try:
					req=vkapi.status.set(owner_id=person[0], text=getFires())
					time.sleep(timer)
				except vkerror as e:
					captcha_sid=e.captcha_sid
					captcha_key=Comb.captcha('self', e.captcha_img)
					req=vkapi.status.set(owner_id=person[0], text=getFires(), captcha_sid=captcha_sid, captcha_key=captcha_key)
					time.sleep(60*2)
			elif step>3:
				step=0
				time.sleep(5)
	def statusSet2(self):
		text=self.videoStat() + self.photoStat() + self.audioStat()
		vkapi.status.set(owner_id=person[0], text=text)
	def getVideoAlbums(self, public_id):
		arr=[]
		videos = vkapi.video.getAlbums(owner_id=public_id, count=100, extended=1)
		for x,y in zip(range(videos['count']), videos['items']):
			# if x==0:
			# 	str(1), y['title'], y['count'])
			# else:
			arr.append({'number': x+1, "title":y['title'], "count":y['count'], "id":y['id']})
		return arr

	def copyAudio(seld, public_id, count, source='wall'):
		if public_id>0:
			publicName=vkapi.users.get(user_ids=str(public_id), fields='nickname')[0]['nickname']
		elif public_id<0:
			 publicName = vkapi.groups.getById( group_id = abs(public_id))[0]['name']
		albumTitles=[]
		fname='updateAudioToCopy.json'
		dtype='audio'
		updateDate=int
		countSameNameAlbums=0
		fulledAlbums=[]
		nonFulledAlbums=[]
		if source=='wall':
			source2='wall'
		elif source=='audiobox':
			source2='box'
		if os.path.isfile(os.path.join('updates',source2,fname)):
			with open(os.path.join('updates',source2,fname)) as f:
					data = json.load(f)	
					for i in data:
						if i['id']==public_id and i['name']==publicName:
							updateDate=i['date']
		for i in vkapi.audio.getAlbums(owner_id=person[0])['items']:
				albumTitles.append(i['title'])
		if publicName not in albumTitles:
			TargetAlbumId=vkapi.audio.addAlbum(owner_id=person[0], title=publicName)['album_id']
		elif publicName in albumTitles:
			for i in vkapi.audio.getAlbums(owner_id=person[0])['items']:
				if re.search(re.search('[^0-9\+][а-яa-z\W]+',publicName, flags=re.IGNORECASE).group(0), i['title']):
					countSameNameAlbums+=1
					time.sleep(1)
					if vkapi.audio.get(owner_id=person[0], album_id=i['id'])['count']==1000:
						fulledAlbums.append(i['id'])
						
					else:
						nonFulledAlbums.append(i['id'])
					if len(nonFulledAlbums)==1:
						TargetAlbumId=nonFulledAlbums[0]
					else:
						TargetAlbumId=vkapi.audio.addAlbum(owner_id=person[0], title=publicName + ' ' + str(countSameNameAlbums))['album_id']
					
		if source=='audiobox':
			Comb.UpdateData('self', public_id, [i['date']  for i in vkapi.audio.get(owner_id=public_id, count=1)['items']][0], dtype, 'box')
			for i in vkapi.audio.get(owner_id=public_id, count=count)['items']:
				if updateDate!=None:
					if updateDate==i['date']:
						break
				try:
					add=vkapi.audio.add(owner_id=public_id, audio_id=i['id'])
					move=vkapi.audio.moveToAlbum(owner_id=person[0], album_id=TargetAlbumId, audio_ids=add)
					time.sleep(1)
				except vkerror as e:
					print(add)
					captcha_sid=e.captcha_sid
					captcha_key=Comb.captcha('self', e.captcha_img)
					add=vkapi.audio.add(owner_id=public_id, audio_id=i['id'], captcha_sid=captcha_sid, captcha_key=captcha_key)
					time.sleep(1)
		elif source=='wall':
			ld=[]
			for dd in vkapi.wall.get(owner_id=public_id, count=count, filter='owner')['items']:
				if 'attachments' in dd and 'is_pinned' not in dd:
					for bb in dd['attachments']:
						if bb['type']=='audio':
							ld.append(dd['date'])		
			Comb.UpdateData('self', public_id, ld[0], dtype, 'wall')	
			for i in vkapi.wall.get(owner_id=public_id, count=count, filter='owner')['items']:
				if updateDate!=None:
					if updateDate==i['date']:
						break
				if 'attachments' in i and 'is_pinned' not in i: 
					for jo in i['attachments']:
						if jo['type']=='audio':
							print(jo['audio']['id'])
							try:
								add=vkapi.audio.add(owner_id=jo['audio']['owner_id'], audio_id=jo['audio']['id'])
								move=vkapi.audio.moveToAlbum(owner_id=person[0], album_id=TargetAlbumId, audio_ids=add)
								time.sleep(1)
							except vkerror as e:
								captcha_sid=e.captcha_sid
								captcha_key=Comb.captcha('self', e.captcha_img)
								add=vkapi.audio.add(owner_id=jo['audio']['owner_id'], audio_id=jo['audio']['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)
								move=vkapi.audio.moveToAlbum(owner_id=person[0], album_id=TargetAlbumId, audio_ids=add)
								time.sleep(1)

	def copyVideo(seld, public_id, count, source):
		if public_id>0:
			publicName=vkapi.users.get(user_ids=str(public_id), fields='nickname')[0]['first_name']
			publicName=publicName+' '+vkapi.users.get(user_ids=str(public_id), fields='nickname')[0]['last_name']

		elif public_id<0:
			publicName = vkapi.groups.getById( group_id = abs(public_id))[0]['name']
			print(publicName)
		albumTitles=[]
		fname='updateVideoToCopy.json'
		dtype='video'
		updateDate=int
		albumIds=[]
		if os.path.isfile(fname):
			with open(fname) as f:
					data = json.load(f)	
					for i in data:
						if i['id']==public_id and i['name']==publicName:
							updateDate=i['date']
		if source=='wall' or source=='videobox':
			# for i in vkapi.video.getAlbums(owner_id=person[0])['items']:
			# 		albumTitles.append(i['title'])
			# if publicName not in albumTitles:
				# TargetAlbumId=vkapi.video.addAlbum(owner_id=person[0], privacy='nobody', title=publicName)['album_id']

			# elif publicName in albumTitles:
			for i in vkapi.video.getAlbums(owner_id=person[0], extended=1, count=100)['items']:
				# if publicName in i['title']:
				# 	if re.findall('\s[0-9]$', i['title']):
				# 		pat=re.sub('\s[0-9]$', '', i['title'])
				# print(re.sub('[0-9]', '', publicName))
				# print(i['title'])
				# if re.findall(r'[\w\W]+(?=\d?)', publicName)[0] == i['title']:
				# if publicName == re.findall(r'.+[^\d$]', i['title'])[0] :
				if re.sub('[0-9]', '', publicName) == re.sub('\s[0-9]*$', '', i['title']):
						# print(i['title'])
						# TargetAlbumId=i['id']
						albumIds.append(i['id'])
			# print(publicName)
			if len(albumIds)==0:

				print('0 albums found')
				create_album=input('create album?[y/n]:')
				privacy=input('privacy[all, nobody, friends]:')
				if create_album =='y':
					TargetAlbumId=vkapi.video.addAlbum(owner_id=person[0], privacy=privacy, title=publicName+' '+str(len(albumIds)+1))['album_id']
				else:
					print('stopped')

			else:
				for i in albumIds:
					if vkapi.video.getAlbumById(album_id=i)['count']<1000:
						TargetAlbumId=i
						# print('target id %s' % (i))
						break

					else:
						TargetAlbumId=vkapi.video.addAlbum(owner_id=person[0], privacy='all', title=publicName+' '+str(len(albumIds)+1))['album_id']
						# print('album created')
		if type(source)==int:

			albumName=vkapi.video.getAlbumById(owner_id=public_id, album_id=source)['title']

			for i in vkapi.video.getAlbums(owner_id=person[0])['items']:
					albumTitles.append(i['title'])
			if publicName+'_'+albumName not in albumTitles:
				TargetAlbumId=vkapi.video.addAlbum(owner_id=person[0], title=publicName+'_'+albumName)['album_id']
			elif publicName+'_'+albumName in albumTitles:
				for i in vkapi.video.getAlbums(owner_id=person[0])['items']:
					if i['title']==publicName+'_'+albumName:
						TargetAlbumId=i['id']

		if type(source)==int:
			print(source)
			Comb.UpdateData('self', public_id, [i['date']  for i in vkapi.video.get(owner_id=public_id, album_id=source, count=1)['items']][0], dtype, 'album', source)	
			time.sleep(1)
			step=-200
			while step<1000:
				step+=200
				for i in vkapi.video.get(owner_id=public_id, album_id=source, offset=step, count=200)['items']:
					if updateDate!=None:
						if updateDate==i['date']:
							break
					try:
						add=vkapi.video.addToAlbum(target_id=peprson[0], owner_id=i['owner_id'], album_id=TargetAlbumId, video_id=i['id'])
					except vkerror as e:
						captcha_sid=e.captcha_sid
						captcha_key=Comb.captcha('self', e.captcha_img)
						add=vkapi.video.addToAlbum(target_id=peprson[0], owner_id=i['owner_id'], album_id=TargetAlbumId, video_id=i['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)
						time.sleep(1)
		elif source=='videobox':
			Comb.UpdateData('self', public_id, [i['date']  for i in vkapi.video.get(owner_id=public_id, count=2)['items']][0], dtype, 'box')	
			time.sleep(2)
			step=98
			stop=False
			while step<count:
				step+=1
				if stop==True:
					break
				for i in vkapi.video.get(owner_id=public_id, offset=step, count=1)['items']:
					if updateDate!=None:
						if updateDate==i['date']:
							stop=True
					print(i['title'])
					print(i['owner_id'])
					try:
						add=vkapi.video.addToAlbum(target_id=person[0], owner_id=i['owner_id'], album_id=TargetAlbumId, video_id=i['id'])
						time.sleep(1)
					except vkerror as e:
						if e.code==800 or e.code==6:
							time.sleep(1)
							continue

						captcha_sid=e.captcha_sid
						captcha_key=Comb.captcha('self', e.captcha_img)
						add=vkapi.video.addToAlbum(target_id=person[0], owner_id=i['owner_id'], album_id=TargetAlbumId, video_id=i['id'], captcha_sid=captcha_sid, captcha_key=captcha_key)
						time.sleep(1)
				
		elif source=='wall':
			ld=[]

			for dd in vkapi.wall.get(owner_id=public_id, count=count, album_id='wall', filter='owner')['items']:
				if 'attachments' in dd:
					for bb in dd['attachments']:
						if bb['type']=='video':
							ld.append(dd['date'])
								
			Comb.UpdateData('self', public_id, ld[0], dtype, 'wall')	
			for i in vkapi.wall.get(owner_id=public_id, count=count, filter='owner')['items']:
				time.sleep(1)
				if updateDate!=None:
					if updateDate==i['date']:
						break

				if 'attachments' in i:
					for jo in i['attachments']:
						if jo['type']=='video':
							# if jo['video']['title'] not in [i['title'] for i in vkapi.video.get(owner_id=person[0], album_id=TargetAlbumId)['items'] if 'title' in i]:
							try:
								add=vkapi.video.addToAlbum(target_id=person[0], owner_id=jo['video']['owner_id'], album_id=TargetAlbumId, video_id=jo['video']['id'])
								time.sleep(1)
							except vkerror as e:
								if e.code==800:
									continue
								captcha_sid=e.captcha_sid
								captcha_key=Comb.captcha('self', e.captcha_img)
								add=vkapi.video.addToAlbum(target_id=person[0], owner_id=jo['video']['owner_id'], album_id=TargetAlbumId, video_id=jo['video']['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)
								time.sleep(1)

	def getSubs(self, userId):
				names=[]
				count = vkapi.users.getSubscriptions(user_id=userId, extended=1)['count']
				if count > 1000:
					step=-200
					while step<count:
						step+=200
						for i in vkapi.users.getSubscriptions(user_id=userId, extended=1, offset=step, count=200)['items']:
							if 'name' in i:
								names.append({"name":i['name'], "id":i['id']})
								# time.sleep(0.1)
							# print(i['name'])
							# time.sleep(0.3)
				with open("subscribes.json", "w") as o:
					o.write(str(json.dumps(names, indent=4, sort_keys=True, ensure_ascii=False)))

	def getDocs(self, ownerId, count, dtype, path, addToMyDocs=False, download=False):
		publicName = vkapi.groups.getById( group_id = abs(ownerId))[0]['name']
		step=-1
		nameNumber=0
		updateDate=int
		fname=str
		stop=False
		if dtype=='gif':
			fname="updateGifData.json"
		elif dtype=='pdf':
			fname="updatePdfData.json"
		elif dtype=="djvu":
			fname="updateDjvuData.json"
		elif dtype=="audio":
			fname="updateAudioData.json"
		elif dtype=='video':
			fname="updateVideoData.json"
		if os.path.isfile(os.path.join('updates', 'wall', fname)):
			with open(os.path.join('updates', 'wall', fname)) as f:
					data = json.load(f)	
					for i in data:
						if i['id']==ownerId:
							updateDate=i['date']

		Comb.UpdateData('self', ownerId, [i['date']  for i in vkapi.wall.get(owner_id=ownerId, count=5)['items'] if 'is_pinned' not in i][0], dtype, 'wall')				
		while step<count:
			step+=1
			if stop==True:
				break
			wall = vkapi.wall.get(owner_id=ownerId, offset=step, count=1)
			for i in wall['items']:
				# print(i['date'])
				if 'is_pinned' not in i:
					if updateDate:
						if i['date']==updateDate:
							stop=True
					if 'attachments' in i:
						for a in i['attachments']:
							if a['type']=='doc' and a['doc']['ext']==dtype:
								if addToMyDocs==True:
									try:
										req = vkapi.docs.add(owner_id=a['doc']["owner_id"], doc_id=a['doc']['id'])
										time.sleep(1)
									except vkerror as e:
										captcha_sid=e.captcha_sid
										captcha_key=Comb.captcha('self', e.captcha_img)
										req = vkapi.docs.add(owner_id=a['doc']["owner_id"], doc_id=a['doc']['id'], captcha_key=captcha_sid, captcha_sid=captcha_sid)
										time.sleep(1)
								elif addToMyDocs==False:
									# print(a['doc']['title'])
									# time.sleep(0.3)
									if download==True:
										print(a['doc']['title'])
										# print(a['doc']['url'],a['doc']['title'])
										if not os.path.exists(os.path.join(path,publicName)):
												os.mkdir(path=os.path.join(path, publicName))

										elif not os.path.exists(os.path.join(path, publicName, dtype)):
											os.mkdir( path=os.path.join(path, publicName, dtype) ) 
										else:
											if re.search('^.{1,100}', i['text']):
												fname1=re.search('^.{1,100}', i['text'])
												fname2=re.sub("\/|:", '',fname1.group(0).replace('.', ''))
											else:
												fname2=urlparse(a['doc']['url']).path.replace('/', '')
											if dtype=='pdf':
												# if requests.get(a['doc']['url']).headers['content-type']=='application/pdf':
													wget.download( a['doc']['url'], out=os.path.join(path,publicName,dtype) )
													path2=os.path.join(path,publicName,dtype)+'/'

													if re.search('...$', a['doc']['title']).group(0)=='pdf':
														[os.rename(path2+f, path2+a['doc']['title']) for f in os.listdir(path2) if f==(urlparse(a['doc']['url']).path.replace('/',''))]
													else:
														[os.rename(path2+f, path2+a['doc']['title']+'.pdf') for f in os.listdir(path2) if f==(urlparse(a['doc']['url']).path.replace('/',''))]
											elif dtype=='gif':
												wget.download( a['doc']['url'], out=os.path.join(path,publicName,dtype) )
												path2=os.path.join(path,publicName,dtype)+'/'

												[os.rename(path2+f, path2+fname2+'.'+dtype) for f in os.listdir(path2) if f==(urlparse(a['doc']['url']).path.replace('/',''))]

											elif dtype=="djvu":
												if requests.get(a['doc']['url']).headers['content-type']=='application/djvu':
													wget.download( a['doc']['url'], out=os.path.join(path,publicName,dtype) )
													path2=os.path.join(path,publicName,dtype)+'/'

													if re.search('....$', a['doc']['title']).group(0)=='djvu':
														[os.rename(path2+f, path2+a['doc']['title']) for f in os.listdir(path2) if f==(urlparse(a['doc']['url']).path.replace('/',''))]
													else:
														[os.rename(path2+f, path2+a['doc']['title']+'.djvu') for f in os.listdir(path2) if f==(urlparse(a['doc']['url']).path.replace('/',''))]



									os.system("rm ./*.tmp")
							elif a['type']=='audio' and dtype=='audio':
								if download==True:

									if not os.path.exists(os.path.join(path,publicName)):
											os.mkdir(path=os.path.join(path,publicName))
									elif not os.path.exists( os.path.join(path,publicName, dtype)):
										os.mkdir(path=os.path.join(path,publicName,dtype)) 
									else:
										wget.download(a['audio']['url'], out=os.path.join(path,publicName,dtype))
										path3=os.path.join(path,publicName,dtype)+'/'
										parseURL=urlparse(a['audio']['url']).path
										cfname=re.sub("^(.[^\/]*){1,50}\/", '', parseURL)
										nfname=a['audio']['artist']+'-'+a['audio']['title']+'.mp3'
										# [os.rename(path3+f, path3+nfname) for f in os.listdir(path3) if f==cfname]
										if dtype=='audio':
											[os.rename(path3+f, path3+nfname) for f in os.listdir(path3) if f==cfname]
								os.system("rm ./*.tmp")
			time.sleep(0.5)
	def getDiffGroups(self, userId):
		ids=[]
		with open("groups.json", "r") as o:
			data1 = json.load(o)
		for i in data1:
			ids.append(i['id'])
		with open("subscribes.json", "r") as a:
			data2=json.load(a)
		for i in data2:
			ids.append(i['id'])
		return ids
	def getGroups(self, userId, count, mode):

		groups=[]
		sexgroups=[]
		count=10000

		if os.path.isfile('groups.json'):
			if count > 1000:
				step=-1000
				while step < count:
					step+=1000
					for i in vkapi.groups.get(user_id=person[0], extended=1, offset=step, fields='description', count=1000)['items']:
						if 'description' in i:
							groups.append({"name":i['name'], "id":i['id'], 'description':i['description']})

						# print(i)
					time.sleep(0.5)

			else:
				for i in vkapi.groups.get(user_id=person[0], extended=1, count=1000)['items']:
						groups.append({"name":i['name'], "id":i['id']})
			with open("groups.json", "w") as o:
				o.write(json.dumps(groups, indent=4, sort_keys=True, ensure_ascii=False))
		if os.path.isfile('subscribes.json'):
			Comb.getSubs('self', person[0])

		with open("friendList.json", 'r') as aa:
			data=json.load(aa)


		if mode=='allFriends':
			for fr in vkapi.friends.get(owner_id=userId, fields='nickname', order='random')['items']:
				if count > 1000:
					step=-1000
					while step < count:
						step+=1000
						for i in vkapi.groups.get(user_id=fr['id'], extended=1, offset=step, fields='members_count', count=1000)['items']:
							if i['id'] not in Comb.getDiffGroups('self', person[0]) and not re.search('[а-яА-Я]+', i['name']):
								print(i['id'],i['name'])
								time.sleep(0.5)
				else:
					for i in vkapi.groups.get(user_id=fr['id'], extended=1, fields='members_count', filter='publics, groups', count=1000)['items']:
						if "members_count" in i:
							if i['id'] not in self.getDiffGroups(person[0]) and not re.search('[а-яА-Я]+', i['name']) and i['members_count']>500:
								print(i['id'],i['name'], i['members_count'])
								try:
									req=groups.join(group_id=i['id'])
									time.sleep(0.5)
								except vkerror as e:
									print(req)
									captcha_sid=e.captcha_sid
									captcha_key=self.captcha(e.captcha_img)
									req=groups.join(group_id=i['id'], captcha_sid=captcha_sid, captcha_key=captcha_key)
									time.sleep(0.5)
					time.sleep(0.5)
		elif mode=='oneFriend':
				if count > 1000:
					step=-1000
					while step < count:
						step+=1000
						for i in vkapi.groups.get(user_id=userId, extended=1, offset=step, fields='members_count', filter='publics, groups', count=1000)['items']:
							if "members_count" in i:
								if i['id'] not in self.getDiffGroups(person[0]) and not re.search('[a-zA-Z]+', i['name']) and i['members_count']>500:
									print(i['id'],i['name'],i['members_count'])
									try:
										req = vkapi.groups.join(group_id=i['id'])
										time.sleep(0.5)
									except vkerror as e:
										print(req)
										captcha_key=e['key']
										captcha_sid=e['sid']
										req = vkapi.groups.join(group_id=i['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)
										time.sleep(0.5)

				else:
					for i in vkapi.groups.get(user_id=userId, extended=1, fields='members_count', filter='publics, groups', count=1000)['items']:
						if "members_count" in i:
							if i['id'] not in self.getDiffGroups(person[0]) and not re.search('[a-zA-Z]+', i['name']) and i['members_count']>500:
								print(i['id'],i['name'], i['members_count'])
								try:
									req = vkapi.groups.join(group_id=i['id'])
									time.sleep(0.5)
								except vkerror as e:
									print(req)
									captcha_key=e['key']
									captcha_sid=e['sid']
									req = vkapi.groups.join(group_id=i['id'], captcha_sid=captcha_sid, captcha_key=captcha_key)
									time.sleep(0.5)
	def LikesProfilePhoto(self):
		for i in vkapi.friends.get(owner_id=person[0], fields='nickname')['items']:
			if 'deactivated' not in i:
				for a in vkapi.photos.get(owner_id=i['id'], album_id='profile', count=1, rev=1)['items']:
					try:
						req= vkapi.likes.add(type=photo, owner_id=i['id'], item_id=a['id'])
						time.sleep(1)
					except vkerror as e:
						captcha_sid=e.captcha_sid
						captcha_key=self.captcha(e.captcha_img)
						req= vkapi.likes.add(type=photo, owner_id=i['id'], item_id=a['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)
						time.sleep(1)
	def friendsAdd(self, source):
		friendList=[]
		today = datetime.fromtimestamp(time.time())
		yesterday=today-timedelta(days=1)
		today=easy_date.convert_from_timestamp(round(time.mktime(today.timetuple())), '%y-%m-%d')
		yesterday=easy_date.convert_from_timestamp(round(time.mktime(yesterday.timetuple())),'%y-%m-%d')
		if source=='search':
			req=vkapi.users.get(user_ids=person[0], fields='country, city, sex')
			city=req[0]['city']['id']
			sex=req[0]['sex']
			country=req[0]['country']['id']
			citiesUSA=[]
			citiesRU=[]
			users=[]
			usersIds=[]
			# print(json.dumps(vkapi.users.search(sex=1, country=country, count=10), indent=4, ensure_ascii=False))
			for i in vkapi.database.getCities(count=200, need_all=0, country_id=country)['items']:
				citiesUSA.append(i['id'])
			for i in vkapi.database.getCities(count=200, need_all=0, country_id=1)['items']:
				citiesRU.append(i['id'])
			for a in random.sample(citiesRU,10):
				for b in [{"id":i['id'],"fn":i['first_name'],"ln":i['last_name'],"city":i['city']['title'], "bdate":i['bdate']} for i in vkapi.users.search(count=1000, city=a, status=1, has_photo=1, age_from=18, age_to=27, fields='nickname,bdate,city,country,last_seen')['items'] if 'city' in i and 'bdate' in i and 'last_seen' in i and easy_date.convert_from_timestamp(i['last_seen']['time'], '%y-%m-%d')==today ]:

						users.append(b)
				time.sleep(1)
			print(len(users))
			users=random.sample(users, 50)
			
			for i in users:
				if i['id'] not in [i for i in vkapi.friends.get(owner_id=person[0])['items']] and vkapi.friends.areFriends(user_ids=i['id'], need_sign=1)[0]['friend_status']!=1:
					print(i['id'],i['fn'],i['ln'], i['city'],i['bdate'] )
					try:
						add= vkapi.friends.add(user_id=i['id'], text='Привет, '+i['fn'])
						time.sleep(1)
					except vkerror as e:
						print(add['error'])
						captcha_sid=e.captcha_sid
						captcha_key=self.captcha(e.captcha_img)
						add= vkapi.friends.add(user_id=i['id'], text='Привет, '+i['fn'], captcha_key=captcha_key, captcha_sid=captcha_sid)
						time.sleep(1)
					# users.append(b['id'])
					# if b not in [i for i in vkapi.friends.get(owner_id=person[0])['items']]:
					# 	if 'city' in b:
					# 		print(b['id'], b['first_name'],b['last_name'],b['city']['title'],b['country']['title'])
					# 		time.sleep(1)
	


	

		# if not os.path.isfile('friendList.json'):
		# 	for i in vkapi.friends.get(user_id=person[0], fields='nickname', order='random')['items']:
		# 		if 'deactivated' in i:
		# 			status=i['deactivated']
		# 		else:
		# 			status=None
		# 		friendList.append({'id':i['id'], 'fn':i['first_name'], 'ln':i['last_name'], 'deactivated':status})
		# 	with open('friendList.json', 'w') as o:
		# 		o.write(json.dumps(friendList, indent=4, ensure_ascii=False))
		# 	with open('friendList.json', 'r') as o:
		# 		data = json.load(o)
		# 	for i in data:
		# 		if i['deactivated'] == None:
		# 			i['count']=vkapi.friends.get(user_id=i['id'], count=1)['count']
		# 			time.sleep(0.5)
		# 	with open('friendList.json', 'w') as l:
		# 		l.write(json.dumps(data, indent=4, ensure_ascii=False))

		# with open('friendList.json', "r") as a:
		# 	data =json.load(a)
		elif source=='frlist':
			for i in vkapi.friends.get(owner_id=person[0], fields='nickname', order='random')['items']:
				if 'deactivated' not in i:
				# if i['deactivated']==None:
					for us in vkapi.friends.get(user_id=i['id'], order='random', fields='nickname, last_seen', count=1)['items']:
						if 'last_seen' in us:
							# print(easy_date.convert_from_timestamp(us['last_seen']['time'], '20'+'%y-%m-%d'))
							# time.sleep(1)
							# if 'deactivated' not in us:
								if easy_date.convert_from_timestamp(us['last_seen']['time'], '%y-%m-%d')==yesterday or easy_date.convert_from_timestamp(us['last_seen']['time'], '%y-%m-%d')==today :
									try:
										add=vkapi.friends.add(user_id=us['id'],text='Привет, '+us['first_name'])
									except vkerror as e:
										print(req['error'])
										captcha_sid=e.captcha_sid
										captcha_key=self.captcha(e.captcha_img)
										add=vkapi.friends.add(user_id=us['id'],text='Привет, '+us['first_name'], captcha_key=captcha_key, captcha_sid=captcha_sid)
										time.sleep(1)
	def videoStat(self):
		total_albums=0
		total_videos=0
		step=-100
		while step<400:
			step+=100
			for i in vkapi.video.getAlbums(owner_id=person[0],  count=100, offset=step, extended=1)['items']:
				# print(i['count'], i['title'])
				total_albums+=1
				total_videos+=i['count']

		# text='Total video albums: %s\nTotal videos: %s' % (total_albums, total_videos)
		text='In %s video albums %s videos 📹 ' % (total_albums, total_videos)
		time.sleep(1)
		return text

	def photoStat(self):
		total_albums=vkapi.photos.getAlbumsCount(user_id=person[0])
		total_photos=0
		for i in vkapi.photos.getAlbums(owner_id=person[0])['items']:
			total_photos+=i['size']
	# text='Total photo albums: %s\nTotal photos: %s' % (total_albums, total_photos)
		text='In %s photo albums %s photos 📷 ' % (total_albums, total_photos)
		time.sleep(1)
		return text

	def audioStat(self):
		total_albums=vkapi.audio.getAlbums(owner_id=person[0])['count']
		time.sleep(1)
		total_audios=vkapi.audio.getCount(owner_id=person[0])
		text='In %s audio albums %s audios 💿 ' % (total_albums, total_audios)
		return text

	def getGroupCategories(self):
		adult=[]
		instagram=[]
		science=[]
		citates=[]
		books=[]
		music=[]
		step=-200
		step2=-1000
		data=[]
		while step2<5000:
			step2+=1000
			for i in vkapi.groups.get(user_id=person[0], extended=1, fields='description', offset=step2, count=1000)['items']:
				if 'description' in i:
					data.append({'id':i['id'], 'name':i['name'], 'desc':i['description']})
				else:
					data.append({'id':i['id'], 'name':i['name'], 'desc':None})

		while step<5000:
			step+=200
			for i in vkapi.users.getSubscriptions(user_id=person[0], extended=1, count=200,fields='description', offset=step)['items']:
				if 'description' in i:
					data.append({'id':i['id'], 'name':i['name'],'desc':i['description']})
		for i in data:
			if re.search('порн|porn|erotic|эроти[ч,к]|sex|секс', i['name'], flags=re.IGNORECASE):
			# print(i['name'], i['id'])
				adult.append(i['id'])
			elif re.search('инстаграм|instagram', i['name'], flags=re.IGNORECASE):
				instagram.append(i['id'])
			elif re.search('scienc|нау[к,ч]', i['name'], flags=re.IGNORECASE):
					science.append(i['id'])	
			elif re.search('цитаты|мудрост[ь,и]', i['name'], flags=re.IGNORECASE):
					citates.append(i['id'])
			elif re.search('книги|литература|books', i['name'], flags=re.IGNORECASE):
					books.append(i['id'])
			elif re.search('музыка|music', i['name'], flags=re.IGNORECASE):
					music.append(i['id'])
			if i['desc']!=None:
				if re.search('порн|porn|erotic|эроти[ч,к]|sex|секс', i['desc'], flags=re.IGNORECASE):
					adult.append(i['id'])
				elif re.search('scienc|нау[к,ч]', i['desc'], flags=re.IGNORECASE):
					science.append(i['id'])
				elif re.search('цитаты|мудрост[ь,и]', i['desc'], flags=re.IGNORECASE):
					citates.append(i['id'])
				elif re.search('книги|литература|books', i['desc'], flags=re.IGNORECASE):
					books.append(i['id'])
				elif re.search('музыка|music', i['desc'], flags=re.IGNORECASE):
					music.append(i['id'])
		print(len(data))
		print('adult', len(adult), '\n', 'instagram', len(instagram), '\n', 'science', len(science), '\n', 'citates',len(citates), '\n' 'books', len(books), '\n', 'music', len(music), '\n', 'other', len(data)-len(citates+instagram+science+adult+books+music))
		print(citates)

	def deleteAudioAlbum(self):
		count=vkapi.audio.getAlbums(owner_id=person[0])['count']
		for i,a in zip(range(count), vkapi.audio.getAlbums(owner_id=person[0])['items']):
			i+=1
			print(i, a['title'])
		selectAlbum=int(input('select album to delete: '))
		for i,a in zip(range(count), vkapi.audio.getAlbums(owner_id=person[0])['items']):
			i+=1
			if i==selectAlbum:
				selectedAlbumId=a['id']
		for i in vkapi.audio.get(owner_id=person[0], album_id=selectedAlbumId)['items']:		
			vkapi.audio.delete(owner_id=person[0], audio_id=i['id'])
			time.sleep(1)

	
	def readPhotoCaptions(self):
		with open("photoCaptions.json", "r") as jo:
			data = json.load(jo)
			# for i in data:

			for i in data:
				if i['text']!=None:
					try:
						cap = vkapi.photos.edit(owner_id=person[0], photo_id=i['id'], caption=i['text'])
						time.sleep(1)
					# if re.search('#', text1):
					# 	texta = text1.replace('#', '')
					# else:
					# 	texta = text1
					except vkerror as e:
						captcha_sid=e.captcha_sid
						captcha_key=Comb.captcha('self', e.captcha_img)
						cap = vkapi.photos.edit(owner_id=person[0], photo_id=i['id'], caption=i['text'], captcha_sid=captcha_sid, captcha_key=captcha_key)
						time.sleep(1)
	def saveWalls(self, public):
		links=[]
		
		for i in [i for i in os.listdir("walls") if not re.search('src|Store|updates', i)]:
			links.append("<a href='../%s/wall.html'>%s</a>" % (re.sub('\?', '', i), re.sub('\?','',i)))

		links2=re.sub('[\[\]]|(?<="),', '', str(links)).replace('"','')
		# print(links2)
		divs=[]
		imgs=[]
		step=-80
		docs=0
		phsize='60%'
		# public=int(input('public: '))
		updateDate=int
		if public<0:
			publicName = vkapi.groups.getById( group_id = abs(public))[0]['name'].replace('/', ' ')
		elif public>0:
			publicName=vkapi.users.get(user_ids=str(public), fields='nickname')
		path=os.path.join('walls',publicName)
		if not os.path.exists(path):
			os.mkdir(path=path)
			os.mkdir(path=os.path.join(path,'imgs'))
		if os.path.exists(os.path.join('walls', 'updates', 'updatePageToCopy.json')):
			with open(os.path.join('walls', 'updates', 'updatePageToCopy.json'), 'r') as o:
				data = json.load(o)	
			for i in data:
				if i['id']==public:
					updateDate=i['date']

		html="""<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <link rel="stylesheet" href="../src/Magnific-Popup/dist/magnific-popup.css"><link rel='stylesheet' href="../src/main.css"><link rel='stylesheet' href="../src/fa/css/font-awesome.min.css"><title>"""+publicName+"""</title> </head><body><div class="menu">"""+links2+"""</div><div class='wall'> </div><script src='../../bower_components/jquery/dist/jquery.js'></script><script src='../src/main.js'></script><script src="../src/Magnific-Popup/dist/jquery.magnific-popup.js"></script></body> </html> """

		fa = "<link rel='stylesheet' href='../src/fa/css/font-awesome.css'>"
		loading="""<div class="sk-circle"> <div class="sk-circle1 sk-child"></div> <div class="sk-circle2 sk-child"></div> <div class="sk-circle3 sk-child"></div> <div class="sk-circle4 sk-child"></div> <div class="sk-circle5 sk-child"></div> <div class="sk-circle6 sk-child"></div> <div class="sk-circle7 sk-child"></div> <div class="sk-circle8 sk-child"></div> <div class="sk-circle9 sk-child"></div> <div class="sk-circle10 sk-child"></div> <div class="sk-circle11 sk-child"></div> <div class="sk-circle12 sk-child"></div> </div>"""
		# logo="""<a href='https://vk.com/'><img src="../VK.com-logo.svg" width='50px' height='50px' alt='перейти на вк' title='Перейти в социальную сеть Вконтакте' class='vklogo'></a>"""
		logo="""<a href='https://vk.com'><div class='vklogo'><i class='fa fa-vk fa-2x'></i></div></a>"""
		Comb.UpdateData('self', public, [i['date'] for i in vkapi.wall.get(owner_id=public, count=5)['items'] if 'is_pinned' not in i][0], 'page', 'wall')
		for i in vkapi.wall.get(owner_id=public, count=80)['items']:
			if 'is_pinned' not in i:
				if updateDate:
					if i['date']==updateDate:
						break
				# print(i['date'])
				divs.append('<div class="post"><div class="date">%s</div>%s</div>' % (easy_date.convert_from_timestamp(i['date'], "%d.%m.%y %H:%M:%S"), re.sub('[^\s\n\w:,\.;\$#£–—-]', '',i['text'])))

				divs.append('<p style="display:none;">Показать полностью</p><div style="width: 500px; height: 250px">')
				if 'attachments' in i:
					for a in i['attachments']:
						if len(i['attachments']):
							phwidth='40%'
							phheight='40%'
						else:
							phwidth='80%'
							phheight='80%'
						if a['type']=='photo':
							parseURL=urlparse(a['photo']['photo_604']).path
							fname = re.sub('^(.[^\/]*){1,50}\/', '', parseURL)

							divs.append('<a class="photos" href="%s"><img src="%s" style="%s;%s"></a>' % (os.path.join('imgs', fname), os.path.join('imgs', fname), 'max-width:'+phwidth, 'max-height:'+phheight))
							if fname not in [i for i in os.listdir(os.path.join('walls', publicName, 'imgs'))]:
								wget.download(a['photo']['photo_604'], out=os.path.join(path,'imgs'))
				divs.append('</div>')

				
		# print(divs)
		if not os.path.isfile(os.path.join(path, 'wall.html')):
			html = re.sub("(?<=<div class='wall'>).*(?=</div>)", re.sub("[\[\],']", '', loading+str(divs)), html).replace('\n', '<br>')
			with open(os.path.join(path, 'wall.html'), 'w') as o:
				o.write(html)


		else:
			with open(os.path.join(path, 'wall.html'), 'r') as o:
				data=o.read()
			html = re.sub("""(?<=<div class='wall'>).+?(?=<div class="post">)""",re.sub("[\[\],']", '', loading+str(divs)), data).replace('\n', '<br>')
			html = re.sub("(?<=<body>).*(?=<div class='wall'>)", logo+"<div class='menu'>"+links2+"</div>", html)
			html = re.sub('(?<=<head> <meta charset="UTF-8">).+?(?=<link)', fa, html)
			with open(os.path.join(path, 'wall.html'), 'w') as o:
				o.write(html)
	def captcha(self, urlImg):

		def getKey(event):
			global key
			key = e1.get()
			root.destroy()
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
		e1.place(x=15, y=100, width=100)
		# e1.pack()
		button1 = Button(root, text='Send')
		button1.bind('<Button-1>', getKey)
		root.bind('<Return>', getKey)
		button1.place(x=50, y=150)
		
		label=Label(root, image = image).place(x=40, y=20)
		root.call('wm', 'attributes', '.', '-topmost', True)                            
		e1.focus_set()
		root.focus()
		root.mainloop()     
		# print(posts)
		return key
		# getDiffGroups(person[0])
		# with open("subscribes.txt", "w") as o:
		# 	o.write(str(vkapi.users.getSubscriptions(user_id=person[0], extended=0)['groups']['items']+vkapi.users.getSubscriptions(user_id=person[0], extended=0)['users']['items']))	
def wiki(stype, word):
	if stype=='word':
			wikipedia.set_lang('ru')
		# try:
			summ = wikipedia.summary(word, sentences=10)
		# except:
			# summ = wikipedia.summary(word, sentences=5)

	elif stype=='auto':
		# try:
			wikipedia.set_lang('ru')
			# wpage = wikipedia.summary('Билл Клинтон', sentences=5)
			wpage = wikipedia.random(pages=1)
			summ = wikipedia.summary(wpage, sentences=8)
			# wpage2 = wikipedia.page(wpage)
			# images = wpage2.images
			# box = {'text':summ, 'images':images}
			
		# except:
		# 	wpage = wikipedia.random(pages=1)
		# 	summ = wikipedia.summary(wpage, sentences=5)
	
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
def exists(path):
	r = requests.head(path)
	return r.status_code == requests.codes.ok

def getArtistsFromWall():
	artists=[]
	count=1000
	step=-100
	while step<count:
		step+=100
		for i in vkapi.wall.get(owner_id=person[0], count=100, offset=step)['items']:
			if 'copy_history' in i:
				for a in i['copy_history']:
					if 'attachments' in a:
						for b in a['attachments']:
							if 'audio' in b['type']:
								artists.append(b['audio']['artist'])
		# time.sleep(0.3)
	text = re.sub("FRISKY|\||'|\[|\]|Artist of the Week,|Frisky",'',str(list(set(artists))))
	print(text)

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
def sendMesBot(message, word):
	photoAlbums = Comb.getAlbums('self', person[0])
	photos=[]
	botMessage=str
	guid = random.randint(1, 10000)

	for i in photoAlbums:
		if i['title'] == 'la':
			for a in vkapi.photos.get(owner_id=person[0], album_id=i['id'], count=900)['items']:
				photos.append(a['id'])

	if message == 'default':
		# botMessage="""
		
		# Попробуйте написать несколько позже.\n
		# Так же вы можете: \n 1. почитать Википедию, прислав слово "wiki"; \n 2. почитать конституцию РФ прислав мне текст: "конст статья (от 1 до 137); \n3. узнать текущую погоду в городе прислав мне:  "погода город" или для прогноза погоды на 5 дней: "погода 5 город".

		# """
		botMessage=''
		# vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid, attachment='photo'+str(person[0])+'_'+str(random.choice(photos)))
		vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid, attachment='photo'+str(person[0])+'_'+str(random.choice(photos)))
		# vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid, attachment='photo179349317_374641254')
	elif message == 'wiki':
		botMessage = wiki('auto', 'nothing')
		vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
		# vkapi.messages.send(user_id=from_id, message=botMessage['text'], guid=guid)
	elif message=='wiki2':
		botMessage = wiki('word', word)
		vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
	elif re.search('конст \d+', message, flags=re.IGNORECASE):
		res = re.search('\d+', message)
		state = res.group(0)
		if int(state)<=137:
			botMessage = const(state)
			vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
		else:
			botMessage='Такой статьи нет в Конституции. Повторите поиск.'
			vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
		# times=0
	elif re.search('погода', message, flags=re.IGNORECASE):
		res = str.split(message,' ')
		if len(res)==3 and res[1]=='5':
			city = res[2]
			botMessage = weather(city, 'forecast')
			vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
		elif len(res)==2:	
			botMessage = weather(res[1], 'current')

			vkapi.messages.send(user_id=from_id, message=botMessage, guid=guid);
def getFires():
		tuples=[]
		arr=[]
		names=[]
		# query=%22Timestamp%22%3E=%272014-11-07%27%20%20and%20%22Timestamp%22%3C%272014-11-08%27%20&api_key=7GRVU2S7I5
		urlBase ="http://maps.kosmosnimki.ru/rest/ver1/layers/F2840D287CD943C4B1122882C5B92565/search?query="
		# urlBase ="http://maps.kosmosnimki.ru/rest/ver1/layers/C13B4D9706F7491EBC6DC70DFFA988C0/search?query="
		apiKey="&api_key=7GRVU2S7I5"
		now=easy_date.convert_from_timestamp(time.time(), '20'+"%y-%m-%d")
		p=re.compile('(?<=\d{4}-\d{2}-)(\d+)')
		result1 = re.search(p, now)
		yesterdayDay=str(int(result1.group(0))-1)
		yestedayDate = re.sub(p, yesterdayDay, now)
		# params=quote(""""DateTime">='"""+yestedayDate+""""' and "DateTime"<'"""+now+""""'""")
		params=quote(""""DateTime">='"""+yestedayDate+""""' and "DateTime"<'"""+now+""""'""")
		# params=quote(""""Timestamp">='"""+yestedayDate+""""' and "Timestamp"<'"""+now+""""'""")
		req=requests.get(urlBase+params+apiKey).json()
		for i in req['features']:
			if i['properties']['Power']>200:
				arr.append((round(i['properties']['Power'], 3), str.split(requests.get("http://nominatim.openstreetmap.org/reverse?format=json&lat=%s&lon=%s&zoom=%s&addressdetails=1" % (round(i['geometry']['coordinates'][1], 3), round(i['geometry']['coordinates'][0],3), 12) ).json()['display_name'],',')[-1:]))
				# print((round(i['properties']['Power'], 3), str.split(requests.get("http://nominatim.openstreetmap.org/reverse?format=json&lat=%s&lon=%s&zoom=%s&addressdetails=1" % (round(i['geometry']['coordinates'][1], 3), round(i['geometry']['coordinates'][0],3), 12) ).json()['display_name'],',')[-1:]))
				# print({"power":round(i['properties']['Power'], 3), "location":str.split(requests.get("http://nominatim.openstreetmap.org/reverse?format=json&lat=%s&lon=%s&zoom=%s&addressdetails=1" % (round(i['geometry']['coordinates'][1], 3), round(i['geometry']['coordinates'][0], 3), 12) ).json()['display_name'],',')[-1:]})
				# print(round(i['properties']['Power'], 3), i['geometry']['coordinates'] )

		for i in arr:
			names.append(i[1][0].replace(' ',''))
		res=list(set(names))
		for i in res:
			tuples.append(((names.count(i),i)))
		text = "Пожары: "+re.sub("\(|\)|'|\[|\]|(?<=\d),", '', str(sorted(tuples, reverse=True, key=itemgetter(0))))
		return text
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

		url = 'http://%s?act=a_check&key=%s&ts=%s&wait=25&mode=2' % (params['server'], params['key'], ts)
		global from_id
		global times

		while True:
			# try:
			
			req = requests.get(url).json()

			# except:
			# 	req = requests.get(url).json()

			# if req!=None and 'updates' in req and req['updates']!='':
				# os.system('clear')
			if 'updates' in req and req['updates']!='':
					for i in req['updates']:
						if len(i)>6:
							if i[0]==4 and i[6] and not re.search('wiki', i[6], flags=re.IGNORECASE) and not re.search('конст \d+',i[6], flags=re.IGNORECASE) and not re.search('погода ', i[6], flags=re.IGNORECASE):
								if easy_date.convert_from_timestamp(i[4], "%H:%M:%S") == easy_date.convert_from_timestamp(time.time(), "%H:%M:%S"):
									sys.stdout=open('MessagesBotLog.txt', 'a+')
									from_id=i[3]
									# sendMesBot('default', 'nothing')
									vkapi.account.setOffline()
									print(i, '\n')
									time.sleep(1)
							# elif i[0]==4 and i[6] and re.search('wiki', i[6], flags=re.IGNORECASE):
							# # elif i[6] =='wiki' or i[6]=='WIKI':
							# 	if easy_date.convert_from_timestamp(i[4], "%H:%M:%S") == easy_date.convert_from_timestamp(time.time(), "%H:%M:%S"):
							# 		sys.stdout=open('MessagesBotLog.txt', 'a+')
							# 		from_id=i[3]
							# 		sendMesBot('wiki', 'nothing')
							# 		print(i, '\n')
							# 		time.sleep(1)
							# elif i[0]==4  and i[6] and re.search('wiki\s[а-яА-Я]+', i[6], flags=re.IGNORECASE):
							# 	if easy_date.convert_from_timestamp(i[4], "%H:%M:%S") == easy_date.convert_from_timestamp(time.time(), "%H:%M:%S"):
							# 		sys.stdout=open('MessagesBotLog.txt', 'a+')
							# 		from_id=i[3]
							# 		# saa=re.search('[а-яА-Я]+', i[6])
							# 		# print(saa)
							# 		sendMesBot('wiki2', re.search('(?<=wiki\s)[а-яА-Я\s]+', i[6]).group(0))
							# 		print(i, '\n')
							# 		time.sleep(1)
							# elif i[0]==4 and i[6] and re.search('конст \d+', i[6], flags=re.IGNORECASE):
							# 	if easy_date.convert_from_timestamp(i[4], "%H:%M:%S") == easy_date.convert_from_timestamp(time.time(), "%H:%M:%S"):
							# 		sys.stdout=open('MessagesBotLog.txt', 'a+')
							# 		from_id=i[3]
							# 		sendMesBot(i[6], 'nothing')
							# 		print(i, '\n')
							# 		time.sleep(1)
							# elif i[6] and re.search('погода ', i[6], flags=re.IGNORECASE):
							# 	if easy_date.convert_from_timestamp(i[4], "%H:%M:%S") == easy_date.convert_from_timestamp(time.time(), "%H:%M:%S"):
							# 		sys.stdout=open('MessagesBotLog.txt', 'a+')
							# 		from_id=i[3]
							# 		sendMesBot(i[6], 'nothing')
							# 		print(i, '\n')
							# 		time.sleep(1)
			elif 'failed' in req:
				# print(req['failed'])
				# break
				os.system("python3 start.py poll")

def garber(wall_id):
	while True:
		for i in vkapi.wall.get(owner_id=wall_id, count=5)['items']:
				# sys.stdout = open("words/sapienti.txt", "a+")
			if re.search('123|лох|хуй|пизд|пид.*?р|пид.*ра.*|оху|аху|ху.?и|бля|бл[еи].*ь|шлю.*|пошлую|пошлого|пошлый|пошлая|пох|нах', i['text']):

					# print('b'+i['text'])
				vkapi.wall.delete(owner_id=wall_id, post_id=i['id'])
		time.sleep(1)		

if __name__ == "__main__":
	Combain = Comb()

	def actions():
		print('{:=^80}'.format(" Wellcome to VK API combain ") + '\n\n  Please type kind of action would you like to do with this program.\n\n'+'{:=^80}'.format('=')+'\n')

		actions = ['Multi-post', 'Download photos', 'Copy photos', 'Comments Bot', 'Get text from wall', 'Cross delete posts', 'Delete from board', 'Messages Bot', 'Delete photos', 'Likes', 'wheather test', 'test tkinter', 'Upload owner photo', 'Status change', 'Get Videos', 'equake', 'Copy docs', 'Download docs', 'get subscriptions', 'Friends Add', 'Get Fires', 'Get Artists', 'Set Photos captions', 'Copy Audio', 'Copy video', 'Get groups', 'Delete video album', 'Delete audio album']

		
		for i,y in zip(range(len(actions)), actions):
			if i == 0:
				print(str(1)+'.', actions[0])
			else:
				print(str(i+1)+'.', y)

		action = input('\nEnter action: ')
		if int(action) == 1:
			mins = int(input('Time delay in minutes: '))
			try:
				Combain.postMulti(psy+psy2+mudreci2+mudreci+XXvek+davch+science+atlant+prosv+space+other+zeland+cuts+slovo+sapienti, mins)
			except:
				Combain.postMulti(psy+psy2+mudreci2+mudreci+XXvek+davch+science+atlant+prosv+space+other+zeland+cuts+slovo+sapienti, mins)
		elif int(action) == 5:
			# ioffset = int(input('Offset: '))
			wall_id = int(input('Wall_id: '))
			count = int(input('Count: '))
			keyword=input("keyword: ")
			if count>100:
				step=-50
				while step<count:
					step+=50
					for i in vkapi.wall.get(owner_id=wall_id, offset=step, count=50)['items']:
						# sys.stdout = open("words/sapienti.txt", "a+")
						
						if keyword!='':
							if keyword in i['text']:
								# print('b'+i['text'])
								print(i['text'])
							time.sleep(0.3)
						elif keyword=='':
							print('b'+i['text'])
							time.sleep(0.3)

			if count<100:
				for i in vkapi.wall.get(owner_id=wall_id, count=count)['items']:
						# sys.stdout = open("words/sapienti.txt", "a+")
						if keyword!='':
							if keyword in i['text']:
								print('b'+i['text'])
								# vkapi.wall.delete(owner_id=wall_id, post_id=i['id'])
						elif keyword=='':
							print('b'+i['text'])

			# print(Combain.getWall('yes', ioffset, wall_id, 'text', 'no', count))
			# Combain.getWall('no', 0, wall_id, 'text', False, count)
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
					vkapi.photos.createAlbum(owner_id=person[0], title=title, privacy_view='nobody')
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
					vkapi.photos.createAlbum(owner_id=person[0], title=title, privacy_view='nobody')
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
			if type(albumIdToCopyFrom)==int:
				Combain.copyPhotoToAlbum(person[0], fromId, albumNameToCopyTo, albumIdToCopyFrom, countPhotosToCopyFrom, False)	
			else:
				Combain.copyPhotoToAlbum2(person[0], fromId, albumNameToCopyTo, albumIdToCopyFrom, countPhotosToCopyFrom, True)	
			# print(person[0], fromId, albumNameToCopyTo, albumIdToCopyFrom, countPhotosToCopyFrom )
		elif int(action) == 7:
			Combain.delTopicComments()

		elif int(action) == 8:
			getPollingServer()

		elif int(action) == 9:
			Combain.delPhotos()

		elif int(action) == 10:
			print('1. Add\n2. Del\n')
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
			Combain.uploadOwnerPhoto()
		

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
			dtype = input("type: ")
			add=input("add to your docs?: ")
			if add=='y':
				Combain.getDocs(ownerId, count, dtype, addToMyDocs=True)
			elif add=='n':	
				Combain.getDocs(ownerId, count, dtype)

		elif int(action)==18:
			ownerId=int(input('public id: '))
			count = int(input('count of wall post: '))
			dtype = input("type: ")
			path=input("path: ")
			if path=='':
				path='/Users/hal'
			Combain.getDocs(ownerId, count, dtype, path, download=True)
		elif int(action)==19:
			# getFests()
			# Combain.getSubs(person[0])
			# with open('subscribes.json', 'r') as o:
				# data=json.load(o)
			users=vkapi.friends.getRequests(out=1,sort=1)['items']
			users=re.sub('[\]\[]', '', str(users))
			users=vkapi.users.get(user_ids=users, count=200)
			for num,user in zip(range(len(users)),users):
				num+=1
				print(num, user['first_name'], user['last_name'], user['id'])
				vkapi.friends.delete(user_id=user['id'])
				time.sleep(1)
			# print()

		elif int(action)==20:
			print('1 from search friends\n2 from friend list')
			source=int(input('source: '))
			if source==1:
				Combain.friendsAdd('search')
			elif source==2:
				Combain.friendsAdd('frlist')
				# for i in friendList:
				# 	i['count']='there will be count'
			# print(json.dumps(friendList, indent=4, ensure_ascii=False))

		elif int(action)==21:
			getFires()
			# garber(-101190616)
		elif int(action)==22:
			getArtistsFromWall()
		# 	requests.get("https://api.vk.com/method/photos.edit?owner_id="+str(person[0])+"&photo_id=377608717&caption=sexysexey&v=5.37&access_token="+accTok).json()
			# req2=requests.get("http://nominatim.openstreetmap.org/reverse?format=json&lat=%s&lon=%s&zoom=%s&addressdetails=1" % (43.611, 24.153, 12) ).json()['address']
			# print(req2)
		elif int(action)==23:
			Combain.readPhotoCaptions()
		elif int(action)==24:
			public_id=int(input('public id: '))
			count=int(input('count: '))
			source=input('source[wall or audiobox]: ')
			Notifier.notify('Copying of audio files is starting')
			Combain.copyAudio(public_id, count, source)
		elif int(action)==25:
			public_id=int(input('public id: '))
			print('1 wall\n2 album\n3 videobox')
			source=int(input('source: '))
			if source==2:
				count=vkapi.video.getAlbums(owner_id=public_id, extended='count')['count']
				for i,a in zip(range(count), vkapi.video.getAlbums(owner_id=public_id, extended='count')['items']):
					i+=1
					print(i, a['title'], a['count'])
				source=int(input('select: '))
				for i,a in zip(range(count), vkapi.video.getAlbums(owner_id=public_id)['items']):
					i+=1
					if i==source:
						source=a['id']
			elif source==1:
				source='wall'
				count=int(input('count: '))
			elif source==3:
				source='videobox'
				count=int(input('count: '))
			# Notifier.notify('Copying of video files is starting')
			Combain.copyVideo(public_id, count, source)
		elif int(action)==26:
			print('1 groups of all friends\n2 groups of one friend')
			selectMode=int(input('select: '))
			if selectMode==2:
				count=vkapi.friends.get(owner_id=person[0])['count']
				for i,a in zip(range(count), vkapi.friends.get(owner_id=person[0], fields='nickname')['items']):
					i+=1
					print(i, a['first_name'], a['last_name'], a['id'])

				user=int(input('user id:'))
				for i,a in zip(range(count), vkapi.friends.get(owner_id=person[0], fields='nickname')['items']):
					i+=1
					if user==i:
						user=a['id']
					else:
						user=user
				Combain.getGroups(user, 10, 'oneFriend')
			elif selectMode==1:
				Combain.getGroups(user,10, 'allFriends')

		elif int(action)==27:
			count=vkapi.video.getAlbums(owner_id=person[0])['count']
			for i,a in zip(range(count), vkapi.video.getAlbums(owner_id=person[0], count=100)['items']):
				i+=1
				print(i, a['title'], a['id'])
			select=input('select: ')
			select=select.split(',')
			for i,a in zip(range(count), vkapi.video.getAlbums(owner_id=person[0])['items']):
				i+=1
				for b in select:
					if i==int(b):
						# print(a['id'])
						vkapi.video.deleteAlbum(owner_id=person[0], album_id=a['id'])
						time.sleep(0.5)
					# req=requests.get('https://api.vk.com/method/likes.delete?type=photo&owner_id='+str(i)+'&item_id='+str(a['id'])+'&access_token='+accTok)

					# if 'error' in req:
					# 	captchaSid=req['error']['captcha_sid']
					# 	captchaKey=Combain.captcha(req['error']['captcha_img'])
					# 	req=requests.get('https://api.vk.com/method/likes.delete?type=photo&owner_id='+str(i)+'&item_id='+str(a['id'])+'&captcha_sid='+str(captchaSid)+'&captcha_key='+str(captchaKey)+'&access_token='+accTok)
				# time.sleep(1)
		elif int(action)==28:
			Combain.deleteAudioAlbum()
		elif int(action)==29:
			wiki('word', 'лондон')
		elif int(action)==30:
			count=vkapi.video.getAlbums(owner_id=person[0])['count']
			for i,a in  zip(range(count), vkapi.video.getAlbums(owner_id=person[0])['items']):
				i+=1
				print(i, a['title'])
			select=int(input('select: '))
			films=[]
			for i,a in  zip(range(count), vkapi.video.getAlbums(owner_id=person[0])['items']):
				i+=1
				if i == select:
					step=-200
					while step<1000:
						step+=200
						for l in vkapi.video.get(album_id=a['id'], count=200, offset=step)['items']:
							if re.search('([а-яА-Я]+\s){1,10}', l['title']):
								films.append(re.search('([а-яА-Я]+\s){1,10}', l['title']).group(0))
			print(re.sub("[\]\[']+",'',str(random.sample(films, 100))))
		elif int(action)==31:
			Combain.getGroupCategories()
		elif int(action)==32:
			print('1 update all\n2 add')
			select=int(input('select: '))
			if select==1:
				with open('walls/updates/updatePageToCopy.json', 'r') as o:
					data=json.load(o) 
				for i in data:
					Combain.saveWalls(i['id'])
					time.sleep(1)
			elif select==2:
				public=int(input('public: '))
				Combain.saveWalls(public)
		elif int(action)==33:
			for i in vkapi.account.getBanned(count=200)['items']:
				vkapi.account.unbanUser(user_id=i['id'] )
				time.sleep(0.5)
		elif int(action)==34:
			# text=input('text: ')
			# text="""Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺Добавлю✅🚹🚺"""
			text="""📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 """
			# text="""Добавлю """
			public=int(input('public: '))
			post_or_comment=int(input('post[1] or comment[2]: '))
			if post_or_comment==2:
				post_after_comment=int(input('number of post after do comment: '))
				for i in vkapi.wall.get(owner_id=public, count=post_after_comment, extended=1)['items']:
					post_id=i['id']
					print(i['id'])
				while 1:
					try:
						addComment = vkapi.wall.addComment(owner_id=public, post_id=post_id, text=text)
						time.sleep(1)
					except vkerror as e:
						captcha_sid=e.captcha_sid
						captcha_key=Combain.captcha(e.captcha_img)
						addComment = vkapi.wall.addComment(owner_id=public, post_id=post_id, text=text, captcha_sid=captcha_sid, captcha_key=captcha_key)
						time.sleep(1)
			elif post_or_comment==1:
				while 1:
					try:
						vkapi.wall.post(owner_id=public, message=text, from_group=0, friends_only=0)
						time.sleep(1)
					except vkerror as e:
						captcha_sid=e.captcha_sid
						captcha_key=Combain.captcha(e.captcha_img)
						vkapi.wall.post(owner_id=public, message=text, captcha_key=captcha_key, captcha_sid=captcha_sid,from_group=0, friends_only=0)
						time.sleep(1)
				
			
			
		elif int(action)==35:
			privacy=input('privacy: ')
			for a in  vkapi.video.getAlbums(owner_id=person[0], count=100, offset=50)['items']:
				try:
					vkapi.video.editAlbum(owner_id=person[0], album_id=a['id'], title=a['title'], privacy=privacy)
					time.sleep(0.5)	
				except vkerror as e:
					captcha_sid = e.captcha_sid
					captcha_key = Combain.captcha(e.captcha_img)
					vkapi.video.editAlbum(owner_id=person[0], album_id=a['id'], title=a['title'], privacy=privacy, captcha_key=captcha_key, captcha_sid=captcha_sid )
					time.sleep(0.5)
		elif int(action)==36:
			count=vkapi.video.get()['count']
			step=-200
			while step < count:
				step+=200
				for i in vkapi.video.get(count=200, offset=step)['items']:
					# if vkapi.video.getAlbumsByVideo(target=person[0], owner_id=i['owner_id'], video_id=i['id'])[0]==-2:
					try:
						# vkapi.video.removeFromAlbum(target=person[0], album_id=-1, owner_id=i['owner_id'], video_id=i['id'])
						vkapi.video.delete(target=person[0],  owner_id=i['owner_id'], video_id=i['id'])
						time.sleep(1)
					except vkerror as e:

						captcha_sid=e.captcha_sid
						captcha_key=Combain.captcha(e.captcha_img)
						vkapi.video.delete(target=person[0],  owner_id=i['owner_id'], video_id=i['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)
					# try:
					# 	vkapi.video.addToAlbum(owner_id=i['owner_id'], album_id=55651188, video_id=i['id'])
					# 	time.sleep(1)
					# except vkerror as e:
					# 	if e.code==100:
					# 		time.sleep(1)
					# 		continue

						# captcha_sid=e.captcha_sid
						# captcha_key=Combain.captcha(e.captcha_img)
						# vkapi.video.addToAlbum(owner_id=i['owner_id'], album_id=55651188, video_id=i['id'], captcha_sid=captcha_sid, captcha_key=captcha_key )
						# time.sleep(1)
		elif int(action)==37:
			total_deleted = 0
			total_without_profile_photo = 0
			total_friends = 0
			for i in vkapi.friends.get(user_id=person[0], fields='name, nickname, city')['items']:
				try:
					total_friends+=1
					if 'deactivated' in i:
						vkapi.friends.delete(user_id=i['id'])
					# count=vkapi.photos.get(owner_id=i['id'], album_id='profile')['count']
					# print('%s has %s profile photos' % (i['id'], count))
					# if count < 1:
					# 	total_without_profile_photo+=1
					# time.sleep(0.5)
				except vkerror as e:
					if e.code==15:
						total_deleted+=1
						vkapi.friends.delete(user_id=i['id'])
						print('%s is deleted or banned' % (i['id']))
						continue

			print('Total friends: %s\nTotal deleted: %s\nTotal without photo: %s ' % (total_friends, total_deleted, total_without_profile_photo))
		elif int(action) == 38:
			while 1:
				Combain.statusSet2()
				time.sleep(60*5)

		
	if sys.argv[1] == 'manual':
		actions()

	elif sys.argv[1] == 'auto':
		Combain.postMulti(psy+psy2+mudreci2+mudreci+XXvek+davch+science+atlant+prosv+space+psy+other+zeland+slovo+cuts, int(sys.argv[2]))
	
	elif sys.argv[1] == 'poll':
		getPollingServer()
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
