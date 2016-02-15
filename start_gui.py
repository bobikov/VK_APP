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
import threading
# from threading import Timer,Thread,Event
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
from tkinter import ttk
#from tkinter.ttk import *
import base64
from PIL import Image
from PIL import ImageTk
import io
from math import *
from operator import itemgetter, attrgetter
from requests.utils import quote
from urllib.parse import urlparse
from pync import Notifier
import functools
from prettytable import PrettyTable

session = vk.Session( access_token = 'f98576da13f80eb5b3ab0949e1527ef48c9da72155005b7140362908471415d707eecb765bea05aa2852f')
vkapi = vk.API(session, v=5.44 , timeout=50)
vkerror = vk.api.VkAPIError
person = [179349317]
app_id = 5040349
key=str
running=True

class myapp():
		def __init__(self, master):
			self.master = master
			self.actions_list = ['Multi-post', 'Download photos', 'Copy photos', 'Copy video', 'Copy Audio']
			self.radiovar=IntVar()
			self.master.geometry("1000x800+300+0")
			# self.image = ImageTk.PhotoImage(Image.open("captcha.png"))
			
			self.frame1 = Frame(self.master, height=2, bg='#F7F7F7', bd=1,  padx=5, pady=5, relief=SUNKEN)
			self.frame2 = Frame(self.master, height=2, bg='#F7F7F7', bd=1,  padx=5, pady=5, relief=SUNKEN)
			self.frame3 = Frame(self.master, height=2, bg='#F7F7F7', bd=1,  padx=5, pady=5, relief=SUNKEN)
			self.frame4 = Frame(self.master, height=2, bg='#F7F7F7', bd=1,  padx=5, pady=5, relief=SUNKEN)
			# self.superFrame = Frame(self.master, height=2, b=1)
			self.frame1.pack(side = LEFT, fill=Y)
			self.frame2.pack(side = LEFT, fill=Y)
			self.frame3.pack(side = LEFT, fill=Y)
			self.frame4.pack(side = LEFT, fill=Y)
			self.actions_label=Label(self.frame1, text = "Action:", bg="#f7f7f7")
			self.actions_label.pack()

			self.options_label = Label(self.frame2, text="Options:", bg="#f7f7f7")

			self.list1 = Listbox(self.frame1, height = 400, bd=0)
			self.from_album_label = Label(self.frame3, text="From album:", bg="#f7f7f7" )
			self.from_album_label.pack()
			self.list3 = Listbox(self.frame3, height = 400, width=30, bd=0)
			self.to_album_label = Label(self.frame4, text="To album:", bg="#f7f7f7")
			self.to_album_label.pack()
			self.list4 = Listbox(self.frame4, height = 400, width=70, bd=0)

			self.public_id_copyphoto_label = Label(self.frame2, text="Public Id:", bg="#f7f7f7")
			self.public_id_copyphoto_enter = Entry(self.frame2)
			self.album_id_copyphoto_from_label = Label(self.frame2, text="AlbumID from copy: ", bg="#f7f7f7")
			self.album_name_from_copyphoto_enter=Entry(self.frame2)
			self.album_id_to_copyphoto_label = Label(self.frame2, text = "AlbumID to copy:", bg="#f7f7f7")
			self.album_name_copyphoto_to_enter=Entry(self.frame2)
			self.new_album_copyphoto_label = Label(self.frame2, text='New album title:', bg='#f7f7f7')
			self.new_album_name_copyphoto_enter=Entry(self.frame2)
			self.count_copyphoto_label = Label(self.frame2, text="count", bg='#f7f7f7')
			self.count_photoalbums_enter = Entry(self.frame2)
			self.create_photoalbum_label = Label(self.frame2, text="Create album:", bg="#f7f7f7")

			self.list1.bind('<<ListboxSelect>>', functools.partial(self.CurSelet, param1="list1", maction=True))
			self.list3.bind('<<ListboxSelect>>', functools.partial(self.CurSelet, param1="list3", maction=False))
			self.list4.bind('<<ListboxSelect>>', functools.partial(self.CurSelet, param1="list4", maction=False))
			self.master.bind("<Return>", functools.partial(self.CurSelet, param1="load", maction=False))
			self.list1.pack()
			self.list3.pack()
			self.list4.pack()

			self.photoAlbumsToCopyFrom=[]
			self.photoAlbumsToCopyTo=[]
			self.titleAlbumToCopyTo=str
			self.countPhotosToCopyTo=int
			self.photo_public_name=str
			self.titleAlbumToCopyTo=str
			self.albumIdToCopyFrom = int
			self.countPhotosToCopyFrom=int
			self.countPhotosToCopyTo=int
			self.albumIdToCopyTo=int
			self.titleAlbumToCopyTo=str
			self.fromId=int
			self.create_photo_album_state=int
			self.public_id_to_copy=str
			self.menu=self.menu()
			self.offset=None
			self.captcha_key=None
			self.captcha_sid=None
			self.captcha_send=False
			self.postCounter=-1
			self.photoCounter=0
			self.leftCount=None
			self.maxCount=None
			self.processStatus=False
			self.restart=False
			self.stop=False
			self.readPoint=self.savepointRead()
			self.selector=0

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
						data.append({"id":fromId, "date": date,"name":publicName, 'album':albumName, 'album_id_from':None})

					with open(updatesPath, 'w') as f:
						json.dump(data, f, indent=4, ensure_ascii=False)

				else:
					file1 = open(updatesPath, 'a+')
					data=[{"id":fromId, "date": date,"name":publicName, 'album':albumName}]
					file1.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
					file1.close()

		def savepointWrite(self, data):
			with open("photoSavepoint.json", "w") as file:
				file.write(json.dumps(data, indent=4, ensure_ascii=False))

		def savepointRead(self):
			if os.stat("photoSavepoint.json").st_size != 0:
				with open("photoSavepoint.json", "r") as file:
					data = json.load(file)	
					if data:
						self.offset=data['offset']
						self.postCounter=self.offset
						self.fromId=data['id']
						self.leftCount=data['left_count']
						self.countPhotosToCopyFrom=data['max_count']
						self.albumIdToCopyTo=data['album_id']
						if data['album_id_from']:
							self.photoCounter=self.offset
							self.photo_public_name=data['public_name'] 
							self.titleAlbumToCopyTo=data['album_title_from']
							self.albumIdToCopyFrom=data['album_id_from']
						self.public_id_copyphoto_enter.delete(0, END)
						self.public_id_copyphoto_enter.insert(END, self.fromId)
						self.count_photoalbums_enter.delete(0, END)
						self.count_photoalbums_enter.insert(END, self.leftCount)
			else:
				self.photoCounter=0
				self.leftCount=None
				self.offset=None
				self.postCounter=-1
				#self.count=None			

		def captcha(self):
			def getKey(event):
				global key
				key = e1.get()
				threading.Thread(target=self.copyPhotoToAlbum2, args=(person[0], self.fromId, self.albumNameToCopyTo, self.albumIdToCopyFrom, self.countPhotosToCopyFrom, self.captcha_sid, key, self.offset, False, self.captcha_send, self.albumIdToCopyTo)).start()
				window2.destroy()

			image = ImageTk.PhotoImage(Image.open("captcha.png"))
			window2 = Toplevel(self.master)
			window2.geometry("200x200+600+200")
			window2.bind('<Return>', getKey)
			window2.title('Captcha')
			label=Label(window2, image=image)
			label.image=image
			label.pack()
			e1=Entry(window2)
			e1.pack(side=TOP)
			e1.focus_set()
			button1 = Button(window2, text='Send')
			button1.bind('<Button-1>', getKey)
			button1.pack(side=TOP)
			return key

		def copyPhotoToAlbum2(self, to_id, from_id, albumNameToCopyTo,  albumIdToCopyFrom, countPhotos, captcha_sid=None, captcha_key=None, offset=None, text=False, captcha_send=False, albumIdToCopyTo=None):	
			def copyAction():
				self.stop=False
				album_id = []
				photo_id = []
				albumsFromIds = []
				photosToCopy = []
				updateDate=int
				text1=str
				toFile=[]
				phlist=[]
				st=0
				getAlbumsTo = self.getAlbums(to_id)
				if albumIdToCopyFrom=='wall':
					source='wall'
				else:
					source='album'
				if self.album_name_copyphoto_to_enter.get() != '':
					album_id.append(int(self.album_name_copyphoto_to_enter.get()))
				else:
					album_id.append(albumIdToCopyTo)


				#with open(os.path.join('updates', source, "updatePhotoData.json")) as f:
				#	data = json.load(f)	
				#	for i in data:
				#		if i['id']==from_id:
				#			updateDate=i['date']
				#	date1=[i['date'] for i in vkapi.wall.get(owner_id=from_id, count=10)['items'] if 'is_pinned' not in i][0]
				#	if albumIdToCopyFrom=='wall':
				#		self.UpdateData(from_id, date1, 'photo', 'wall')
				if offset:
					step=offset
				else:
					step=-1
				while step<countPhotos:
					step+=1
					if self.stop==True:
						break

					time.sleep(1)
					photosGet=vkapi.wall.get(owner_id=from_id, count=1, offset=step)
					time.sleep(0.5)
					self.postCounter+=1
					if self.postCounter==countPhotos: 
						complete=True
						self.processStatus=complete
						self.restart=True
					else:
						complete=False
					self.savepointWrite({'id':from_id, 'offset':step, 'album_id':album_id[0], 'left_count':countPhotos-self.postCounter, 'max_count':countPhotos, 'complete': complete, 'album_id_from': None, 'public_name': self.photo_public_name})
					for i in photosGet['items']:
						
						self.pb['value']+=1
						self.pb_label.configure(text="%s of %s" % (self.postCounter, self.countPhotosToCopyFrom))
						#if i['date']==updateDate:
						#		self.stop=True
						if 'attachments' in i:
							for a in i['attachments']:
								if a['type']=='photo':
									try:
										if captcha_send:
											copyPhotos = vkapi.photos.copy(owner_id=a['photo']['owner_id'], photo_id=a['photo']['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)
										else:
											copyPhotos = vkapi.photos.copy(owner_id=a['photo']['owner_id'], photo_id=a['photo']['id'])
										# print(copyPhotos)
										if  copyPhotos and text1!=None:
												toFile.append({"id":copyPhotos, "text":text1})
										movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
										time.sleep(1)
									except vkerror as e:
										if e.code==15:
											time.sleep(1)
											continue
										
										self.offset=self.postCounter
										self.albumIdToCopyTo=album_id[0]
										self.captcha_send=True
										self.download_captcha(e.captcha_img)
										self.captcha_sid=e.captcha_sid
										self.captcha_key=self.captcha()
										self.stop=True
										break
									
			copyAction()

		def copyPhotoToAlbum(self, to_id, from_id, albumNameToCopyTo, albumIdToCopyTo, albumIdToCopyFrom, countPhotos, offset=None, text=False, captcha_send=False, captcha_sid=None, captcha_key=None):
			album_id = []
			photo_id = []
			albumsFromIds = []
			photosToCopy = []
			updateDate=int
			text1=str
			toFile=[]
			rev=0
			self.stop=False
			# getAlbumsFromId = Comb.getAlbums('self', from_id)
			if offset:
				step=offset
			else:
				step=-1
			album_id.append(albumIdToCopyTo)

			while step<countPhotos:
				step+=1
				if self.stop==True:
					break
				if self.photoCounter==countPhotos: 
					complete=True
					self.processStatus=complete
					self.restart=True
				else:
					complete=False
					self.processStatus=False

				self.savepointWrite({'id':from_id, 'offset':step, 'album_id':album_id[0], 'left_count':countPhotos-self.photoCounter, 'max_count':countPhotos, 'complete': complete, 'album_id_from': albumIdToCopyFrom, 'public_name': self.photo_public_name, 'album_title_from': self.titleAlbumToCopyTo })
				try:
					photosGet=vkapi.photos.get(owner_id=from_id, album_id=albumIdToCopyFrom, count=1, offset=step, rev=rev)
					for a in photosGet['items']:
						self.photoCounter+=1
						self.pb['value']+=1
						self.pb_label.configure(text="%s of %s" % (self.photoCounter, self.countPhotosToCopyFrom))
						if captcha_send:
							copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)

						else:
							copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'])
						movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
						time.sleep(1)

				except vkerror as e:

					self.albumIdToCopyTo=album_id[0]
					self.download_captcha(e.captcha_img)
					self.captcha_sid=e.captcha_sid
					self.captcha_key=self.captcha()
					self.captcha_send=True
					self.stop=True
					break

		def menu(self):
			for i,y in zip(range(len(self.actions_list)), self.actions_list):
				if i == 0:
					self.list1.insert(END, '1. %s' % (self.actions_list[0]))
				else:
					self.list1.insert(END, '%s. %s' % (i+1, y))


		def delPhotos(self):
			photos = vkapi.photos.get(owner_id=person[0], album_id='saved')['items']
			for i in photos:
				vkapi.photos.delete(owner_id=person[0], photo_id=i['id'])
				time.sleep(0.4)

		def getAlbums(self, public_id):
			titles = []
			ids= []
			albums = vkapi.photos.getAlbums( owner_id = public_id)['items']
			for y,i in zip(range(len(albums)), albums):
				ids.append(dict(number=y+1, id=i['id'], title=i['title'], count=i['size']))
			return ids
		

		def download_captcha(self, url):
				readurl = urlopen(url).read()
				with open("captcha.png", 'wb') as captcha:
					captcha.write(readurl)

		def CurSelet(self, event, param1, maction ):
						
			def test_album(event):
				webbrowser.open_new("https://vk.com/album%s_%s" % (self.public_id_to_copy, self.albumIdToCopyFrom))

			def selradio():
				self.create_photo_album_state = self.radiovar.get()

			def resetSavePoint():
				#self.offset=None
				#self.photoCounter=0
				#self.processStatus=False
				#self.leftCount=None
				self.restart=True
				with open('photoSavepoint.json', 'w'): pass
				self.savepointRead()

			def stopCopy():
				self.savepointRead()
				self.stop=True
				print(self.photoCounter)
				print(self.leftCount)
				print(self.offset)
				print(self.postCounter)
				print(self.maxCount)	

			def copyphoto(event):
				#if self.album_name_copyphoto_to_enter.get()=='':
				#	self.create_album=True
				#else:
				#	self.create_album=False

				title = self.photo_public_name + ' ' + self.titleAlbumToCopyTo
				if self.leftCount==None and self.album_name_from_copyphoto_enter.get!='' and self.album_name_copyphoto_to_enter.get()=='':

					self.albumIdToCopyTo=vkapi.photos.createAlbum(owner_id=person[0], title=title, privacy_view='nobody')['id']
				self.albumNameToCopyTo = self.photo_public_name + ' ' + self.titleAlbumToCopyTo

				if type(self.albumIdToCopyFrom)==str:
					if self.leftCount==None and self.processStatus==False:
						self.public_id_to_copy=self.public_id_copyphoto_enter.get()
						self.offset=-1
						self.postCounter=-1
						self.countPhotosToCopyFrom=int(self.count_photoalbums_enter.get())

					print(self.leftCount, self.processStatus)
				if type(self.albumIdToCopyFrom)==int:

					if self.processStatus==False and self.leftCount: 
							
						self.pb.configure(maximum=self.countPhotosToCopyFrom)
						self.pb.configure(value=self.countPhotosToCopyFrom-self.leftCount)
						threading.Thread(target=self.copyPhotoToAlbum, args=(person[0], self.fromId, self.albumNameToCopyTo, self.albumIdToCopyTo, self.albumIdToCopyFrom, self.countPhotosToCopyFrom, self.offset, False, False, None, None)).start()
					else:
						self.photoCounter=0
						self.offset=0
						self.pb.configure(maximum=self.countPhotosToCopyFrom)
						self.pb.configure(value=0)
						threading.Thread(target=self.copyPhotoToAlbum, args=(person[0], self.fromId, self.albumNameToCopyTo, self.albumIdToCopyTo, self.albumIdToCopyFrom, self.countPhotosToCopyFrom, None, False, None, None)).start()
				else: 
					
					if self.leftCount and self.processStatus==False: 
						self.pb.configure(maximum=self.countPhotosToCopyFrom)
						self.pb.configure(value=self.countPhotosToCopyFrom-self.leftCount)
						threading.Thread(target=self.copyPhotoToAlbum2, args=(person[0], self.fromId, self.albumNameToCopyTo, self.albumIdToCopyFrom, self.countPhotosToCopyFrom, None, None, self.offset, False, False, self.albumIdToCopyTo)).start()
					else:
						self.pb.configure(maximum=self.countPhotosToCopyFrom)
						self.pb.configure(value=0)
						threading.Thread(target=self.copyPhotoToAlbum2, args=(person[0], self.fromId, self.albumNameToCopyTo, self.albumIdToCopyFrom,  self.countPhotosToCopyFrom, False, None, None, None, False, self.albumIdToCopyTo)).start()

			if param1=="list1":	
				selection=self.list1.curselection()
				selection = int(re.findall("[0-9]", self.list1.get(selection[0]))[0])
				if selection==3:
					self.selector=3
				elif selection==4:
					self.selector=4
				
				if self.selector==3:
					for i in self.frame2.winfo_children(): i.pack_forget()
					if len(self.frame2.winfo_children())<14:
						self.rdb1=Radiobutton(self.frame2, text="Yes", value=1, variable=self.radiovar, command=selradio, bg="#F7F7F7")
						self.rdb2=Radiobutton(self.frame2, text="No", value=2, variable=self.radiovar, command=selradio, bg="#F7F7F7")
						self.cbut_photo=Button(self.frame2, text="Copy", bg="#f7f7f7").bind("<Button-1>", copyphoto)
						self.link=Button(self.frame2, text='test link', bg="#f7f7f7")
						self.resetBut=Button(self.frame2, text='reset', command=resetSavePoint)
						self.stopBut=Button(self.frame2, text='stop', command=stopCopy)
						self.privatesList=ttk.Combobox(self.frame2, values=[u"all", u"friends", u"nobody"])
						self.privatesList.set(u"nobody")

						self.pb_label=Label(self.frame2, text='', bg="#f7f7f7")
						self.pb = ttk.Progressbar(self.frame2, orient ="horizontal", length = 150, value=0, maximum=500, mode ="determinate")
						#self.pb.pack()
						if self.leftCount:
							self.pb['maximum']=self.countPhotosToCopyFrom
							self.pb['value']=self.countPhotosToCopyFrom-self.leftCount

						self.link.bind('<Button-1>', test_album)
						self.rdb2.select()
					for i in self.frame2.winfo_children(): i.pack()
					if self.leftCount: self.CurSelet('dd', 'load', False)
				elif self.selector==4:
					for i in self.frame2.winfo_children(): i.pack_forget()
					print(self.selector)
					
			if param1=="load":

				self.list3.delete(0, END)
				self.list4.delete(0, END)
				self.list3.insert(0, "----- wall -----")
				self.list3.insert(0, "---- profile -----")
				if self.selector==3 and not maction:
					if self.public_id_copyphoto_enter.get() != '':
						self.fromId=int(self.public_id_copyphoto_enter.get())
						self.photo_public_name = vkapi.groups.getById(group_id=str(abs(self.fromId)))[0]['name']
						self.photoAlbumsToCopyFrom = self.getAlbums(int(self.public_id_copyphoto_enter.get()))
						for i in self.photoAlbumsToCopyFrom:
							self.list3.insert(END, str(i['number'])+'. '+re.search('[\w\s]+', i['title']).group(0))
						self.photoAlbumsToCopyTo=self.getAlbums(person[0])
						for i in self.photoAlbumsToCopyTo:
							self.list4.insert(END, str(i['number'])+'. '+re.search('[\w\s]+', i['title']).group(0))
			#OPTIONS 2
			if param1=="list3":
				selection=self.list3.curselection()
				if self.selector==3 and not maction:
					self.public_id_to_copy=self.public_id_copyphoto_enter.get()
					# print(public_id_enter.get())
					# print(type(public_id_to_copy))
					if "wall" in self.list3.get(selection[0]):
						self.albumIdToCopyFrom=str
						self.albumIdToCopyFrom="wall"
						self.album_name_from_copyphoto_enter.delete(0, END)
						self.album_name_from_copyphoto_enter.insert(END, str(self.albumIdToCopyFrom))
						self.titleAlbumToCopyTo='wall'
					else:
						self.selectedAlbumToCopyFrom=int(re.search("\d+", self.list3.get(selection[0])).group(0))
						if self.selectedAlbumToCopyFrom:
							for i in self.photoAlbumsToCopyFrom:
								if self.selectedAlbumToCopyFrom==i['number']:
									self.albumIdToCopyFrom = i['id']
									self.countPhotosToCopyFrom=i['count']
									self.titleAlbumToCopyTo=i['title']
							self.album_name_from_copyphoto_enter.delete(0, END)
							self.album_name_from_copyphoto_enter.insert(END, str(self.albumIdToCopyFrom))
					

						
			if param1=="list4":
				selection=self.list4.curselection()
				if self.selector==3 and not maction:
					self.selectedAlbumToCopyTo=int(re.search("\d+", self.list4.get(selection[0])).group(0))
					if self.selectedAlbumToCopyTo:

						for i in self.photoAlbumsToCopyTo:
							if self.selectedAlbumToCopyTo==i['number']:
								self.albumIdToCopyTo = i['id']
								self.countPhotosToCopyTo=i['count']
								self.titleAlbumToCopyFrom=i['title']
						self.album_name_copyphoto_to_enter.delete(0, END)
						self.album_name_copyphoto_to_enter.insert(END, str(self.albumIdToCopyTo))	
				
window=Tk()
my_app=myapp(window)
window.mainloop()		
	
