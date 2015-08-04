#!/usr/local/bin/python3
# coding: UTF-8

from words import *
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
from itertools import islice
from newsBlock import euronewsNews, vestiRss, euronewsUSA
# cgitb.enable()

# print('Content-type: text/html')
# print()

# User and app info
vkapi = vk.API( access_token = '00af0cff7458595045e1893775acf9b561dad00d6df9de580f9839e2722d5090e3fbf819a471461094666')
other = [-72580409, -61330688]
person = [179349317]
app_id = 4967352

supercitat = []
end = 0

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
		self.group_ids = [-57014305, -60409637, -33881737, -72580409, -52521233, -34783798]
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
			photoFromWall = Combain.getWall('no', wall_id, 'photo', count)
			for i in photoFromWall:
				if not os.path.exists(path+groupName):
					os.mkdir(path=path+groupName)

				elif not os.path.exists( path+groupName ):
					os.mkdir( path=path+groupName ) 
				else:	
					wget.download( i, out=path+groupName )
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
					print(ids)

	def getAlbums(self, public_id, count):
		titles = []
		ids= []
		albums = vkapi.photos.getAlbums( owner_id = public_id, count = count)['items']
		for i in albums:
			ids.append(dict(id=i['id'], title=i['title'], count=i['size']))
		return ids


	def copyPhotoToAlbum( self, to_id, titleNewAlbum, from_id, albumNameToCopy ):
		album_id = []
		photo_id = []
		albumsFromIds = []
		photosToCopy = []
		getAlbumsFromId = Comb.getAlbums('self', from_id, 4)
		getAlbumsTo = Comb.getAlbums('self', person[0], 1)
		for i in getAlbumsTo:
			if i['title'] == albumNameToCopy:
				album_id.append(i['id'])
		# for i in getAlbumsFromId:

		for i,y in zip(range(len(getAlbumsFromId)), getAlbumsFromId):
			if i == 0:
				print(str(1)+'.', y['title'])
			else:
				print(str(i+1)+'.', y['title'])
			if i==len(getAlbumsFromId)-1:
				albumChoice = input('Choice the album you want to be copied [default: all]: ')
				if albumChoice == 'all':
					for a in vkapi.photos.get(owner_id=from_id, album_id=i['id'], count=i['count'])['items']:
							copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'], v=5.35)
							movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos, v=5.35)
							time.sleep(1)
		
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
			print(' PUBLIC: ' + str(ok2) + '      |      ' + group_name + '       |      https://vk.com/' + screen_name + '\n\n TEXT: \n\n  ' + str(ok) + '\n\n' + "{:-^50}".format("")+ '\n')

			if period == 40:
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
	def changeOwnPhoto( self ):
		result = vkapi.photos.getOwnerPhotoUploadServer(owner_id=person[0])
		# webbrowser.open_new_tab(result['upload_url'])
		# save = vkapi.saveOwnerPhoto(server=result['upload_url'])

		print (result)
		return
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

	
def wiki():
	try:
		wikipedia.set_lang('ru')
		# wpage = wikipedia.summary('Билл Клинтон', sentences=5)
		wpage = wikipedia.random(pages=1)
		summ = wikipedia.summary(wpage, sentences=5)
	except:
		wpage = wikipedia.random(pages=1)
		summ = wikipedia.summary(wpage, sentences=5)
	return summ

def newsBlock():
	while 1:
		vkapi.wall.post(owner_id=person[0], message=euronewsUSA())
		time.sleep(10)
		vkapi.wall.post(owner_id=person[0], message=euronewsNews())
		time.sleep(10)
		vkapi.wall.post(owner_id=person[0], message=vestiRss())
		time.sleep(1)


if __name__ == "__main__":
	Combain = Comb()

	def actions():
		print('{:=^80}'.format(" Wellcome to VK API combain ") + '\n\n  Please type kind of action would you like to do with this program.\n\n'+'{:=^80}'.format('=')+'\n')

		actions = ['Multi-post', 'Download photos', 'Copy photos', 'Auto reply', 'Get text from wall', 'Cross delete posts', 'Delete from board']

		for i,y in zip(range(len(actions)), actions):
			if i == 0:
				print(str(1)+'.', actions[0])
			else:
				print(str(i+1)+'.', y)

		action = input('\nEnter action: ')

		if int(action) == 1:
			mins = int(input('Time delay in minutes: '))
			try:
				Combain.postMulti(psy+psy2+mudreci2+mudreci+XXvek+davch+science+atlant+prosv+space+other+zeland, mins)
			except:
				Combain.postMulti(psy+psy2+mudreci2+mudreci+XXvek+davch+science+atlant+prosv+space+other+zeland, mins)
		elif int(action) == 5:
			ioffset = int(input('Offset: '))
			wall_id = int(input('Wall_id: '))
			count = int(input('Count: '))
			Combain.getWall('no', 0, wall_id, 'text', False, count, )
		elif int(action) == 2:
			groupId = int(input('group id: '))
			countAlbums = int(input('count albums: '))
			countPhotos = int(input('count photos: '))
			path = input('path to save photos[default is your HOME directory]: ')
			if not path: path = os.environ['HOME']+'/'
			print('\n\nDownload is starting\n\n--------------------------\n\n')
			Combain.getPhoto( groupId, Combain.getAlbums(groupId, countAlbums), 'none', 'yes', path, 'id', 'yes', 'no')
		elif int(action) == 6:
			# list_ids = input("Enter list of groups use ','. Default multi-post group ids list is used ")
			# makeListToDir = 
			Combain.crossDeletingPosts(Combain.dict_names_and_ids)
		elif int(action) == 3:
			from_id = int(input("Pubic either user where will be copied from: "))
			albumNameToCopy = input("Album name will be copied to: ")
			Combain.copyPhotoToAlbum(person[0], '', from_id, albumNameToCopy)
		elif int(action) == 7:
			Combain.delTopicComments()

	if sys.argv[1] == 'manual':
		actions()

	elif sys.argv[1] == 'auto':
		Combain.postMulti(psy+psy2+mudreci2+mudreci+XXvek+davch+science+atlant+prosv+space+psy+other+zeland, int(sys.argv[2]))
	

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
