#!/usr/local/bin/python3
#coding=UTF-8
import vk
import sys
import urllib
from urllib.request import urlopen
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import random
import time
from datetime import timedelta
# import datetime
from datetime import datetime
from threading import Timer,Thread,Event

# User and app info

vkapi = vk.API( access_token = '490914b5c841d81adfceca3310710a2f31f70ec56b523da6b40ef9c37effa9181b786f1504eaddc15b0fd')
vkapi.account.setOffline()
other = [-72580409, -61330688]
person = [179349317]
app_id = 4967352

supercitat = []
# VK groups  data for reading

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

# List text sources 		

pub = []


# Reading words from files

ofile = open('words/super700.txt')
rofile = ofile.read()
super700 = list(rofile.split('b'))

ofile2 = open('words/scary.txt')
rofile2 = ofile2.read()
scary = list(rofile2.split('b'))

ofile3 = open('words/films.txt')
rofile3 = ofile3.read()
films = list(rofile3.split('b'))

ofile4 = open('words/girls.txt')
rofile4 = ofile4.read()
girls = list(rofile4.split('b'))

ofile5 = open('words/mudreci.txt')
rofile5 = ofile5.read()
mudreci = list(rofile5.split('b'))

ofile6 = open('words/life.txt')
rofile6 = ofile6.read()
life = rofile6.split('b')

ofile7 = open('words/sex.txt')
rofile7 = ofile7.read()
sex = rofile7.split('b')

if '' in girls+mudreci+life+sex+films+scary+super700:
	girls.remove('')



for i in public['items']:
	pub.append(i['id'])



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
		self.groups = [-57014305, -78468103]

	def cooler(self):
		while 1:
			Comb.getWall('self', 'no', person[0], 'text', 1)
			time.sleep(0.8)



	def getWall( self, offset,  wall_id, dtype, count = 1, user_id = 179349317, sdate='no' ):
		'''Get music, image, text data from the wall'''
		rid = []
		text=[]
		ids = []
		i = 0
		new=[]
		sd = -50
		date = []
		formattime = '%y-%m-%d %H:%M:%S'
		now = datetime.strptime(datetime.strftime(datetime.now(), '%y-%m-%d %H:%M:%S'), '%y-%m-%d %H:%M:%S')
		# wnow = now[:]
		# Looking for Post IDs without offset 
		if offset == 'no' and dtype == 'id':
			items = wall_id['items']
			for i in items:
				wall = vkapi.wall.get( owner_id = i['id'], count = count )
				ids.append(wall)
			for i in ids:
				for a in i['items']:
					if a['likes']['count'] > 10:
						new.append( str(a['owner_id']) + '_'+  str(a['id']) )
			return new

		# Looking for text in posts without offset
		elif offset == 'no' and dtype == 'text' and sdate == 'yes' or 'no':

			if type(wall_id) == dict:
				items = wall_id['items']
				for i in items:
					wall = vkapi.wall.get( owner_id = i['id'], count = count )
					ids.append(wall)
				for i in ids:
					for a in i['items']:
						text.append(str(a['text']))
			elif type(wall_id) == int:

				wall = vkapi.wall.get( owner_id = wall_id, count = count )
				text.append(wall)
				for i in text[0]['items']:
					dd = datetime.strptime(datetime.fromtimestamp(i['date']).strftime('%d.%m.%y %H:%M:%S'), "%d.%m.%y %H:%M:%S")
					ddd = dd+timedelta(seconds=15)
					if ddd == now:
						vkapi.wall.addComment(owner_id=person[0], post_id=i['id'], text='Привет')

					# if i['id']
					# print('post time: '+str(dd)+'\n'+'curent time: ' + str(now))
					# else:
					# 	print('notok')

					# date.append(datetime.fromtimestamp(i['date']).strftime('%d.%m.%y %H:%M:%S'))
					# date.append(i['date'])
					
			# return print(datetime.strptime(date[0],'%d.%m.%y %H:%M:%S') - timedelta(weeks=40*17))
			# return print(datetime.strptime(datetime.strftime(now, '%d.%m.%y %H:%M:%S'), '%d.%m.%y %H:%M:%S'))
			# return print(date)

			
		
		# Looking for text in posts with offset
		elif offset == 'yes' and dtype == 'text':
			items = wall_id['items']
			for i in items:
				while sd < 100:
					sd+=50
					wall = vkapi.wall.get( owner_id = i['id'], count = count, offset = sd )
					ids.append(wall)
					time.sleep(1)
			for i in ids:
				for a in i['items']:
					text.append(str(a['text']))
					supercitat.append(str(a['text']))
			return text

		# Looking for date of post

	

	

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
	

	def getPhoto( wall_id, album, count ):

		pho = []
		photos = vkapi.photos.get( owner_id = wall_id, album_id = album, count = count )

		for i in photos['items']:
			if i['photo_604']:
				pho.append(i['id'])

		return pho



	def postTopicComment( self ):
		'''Post comment into topic block of group'''

		topic_id = Comb.getTopic() 
		# vkapi.board.addComment( group_id = 53664217, topic_id = topic_id[0], text = str( random.choice( super700 ) ) )

		return print('\n-------------------------\n\n' + 'Post complete in topic board: ' + str(topic_id[0]) + '\n\n--------------------------')



	def postMulti( self, feed ):

		i=-1
		group = str;
		print('Computer make post photos now... \nTotal number of posts: ' + str(i+1))
		while 1:
			i+=1
			if i == len(self.groups)-1:
				Comb.postTopicComment('self')
				i=-1
			group = str(self.groups[i])
			ok2 = group[:]
			# group = str(random.choice(groups))
			words = random.choice( feed )
			ok = words[:]
			# vkapi.wall.post( owner_id = ok2,  message = ok )
			print('В (' + str(ok2) + ')\nОпубликована запись: ' + str(ok) + '\n\n---------------------------\n\n')
			time.sleep(2)
		
	
	def postOne( self ):

		dd = getPhoto( -73484869, 'wall', 10 )
		i=0
		while i < len( dd ):
			i+=1	
			vkapi.wall.post( owner_id = person[0],  attachments = 'photo179349317_4967352, photo-73484869_' + str( dd[i] ) )
			time.sleep(10)
		# return print(self.groups)	
		# 
	



if __name__ == "__main__":
	Combain = Comb()
	# # Combain.postOne()
	# Combain.getWall('no', person[0], 'text', 3)
	Combain.cooler()
	# Combain.getCitat()
	# Combain.getLikes()
	# Combain.rePost()
	# Combain.postMulti(mudreci)
	# Combain.postMulti(girls)
	