#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#from words import *
#from zakon import *
import emoji
import vk
import sys
import urllib
from tumblpy import Tumblpy
from urllib.request import urlopen
from html.parser import HTMLParser
#from bs4 import BeautifulSoup
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
import tkinter.messagebox
#from tkinter.ttk import *
import base64
from PIL import Image
from PIL import ImageTk
import io
from math import *
from operator import itemgetter, attrgetter
from requests.utils import quote
from urllib.parse import urlparse
#from pync import Notifier
import functools

#from prettytable import PrettyTable

session = vk.Session( access_token = '14b115dd450f382c77849d90f62eef11c18e0c353c4ebaba0aa57f8de7495bc6656d64445692eb5fd2301')
vkapi = vk.API(session, v=5.45 , timeout=50)
vkerror = vk.api.VkAPIError
person = [179349317]
app_id = 5040349
key=str
running=True
t = Tumblpy("zpp8l7tvAl5CaNq0Z6zIBSg91kA2brPdQRF6f7bjYL75QI2rj9", "ZTJDMVXpzeRPPxEiyOvKkTLJUVZk1t2CBEvJ8ZakOKxKPjggt0", "CYVmCiHgwwpU6dgCbnVEjScPU1ZV6c5RFwHDqrjM15o3ypnwPo", "ajn0xJ8KqykaZjTEGKRgaiMDmqAkPE9xjjNDC2bh0Jqo5xekkF" )
class myapp():
		def __init__(self, master):
			self.master = master
			self.actions_list = ['Multi-post', 'Download photos', 'Copy photos', 'Copy video', 'Copy Audio', 'Wall Post', 'Delete Photo Albums', 'Tumblr copy photo']
			self.photo_radiovar=IntVar()
			self.video_radiovar=IntVar()
			self.wall_post_radiovar=IntVar()
			self.photo_cpature_radiovar=IntVar()
			self.tumblr_copyphoto_capture_radiovar=IntVar()

			self.master.geometry("1200x800+200+0")
			self.master.title('VK API')
			# self.image = ImageTk.PhotoImage(Image.open("captcha.png"))
			self.e = threading.Event()
			self.frame1 = Frame(self.master, height=2, bg='#F7F7F7', bd=0,  padx=5, pady=5)
			self.superFrame = Frame(self.master, height=2, bd=0)
			self.superFrameInner1 = Frame(self.superFrame, height=2, bd=0)
			#self.superFrameInner2 = Frame(self.superFrame, height=2, bd=0)
			self.frame2 = Frame(self.superFrame, height=2, bg='#F7F7F7', bd=1,  padx=5, pady=5)
			self.frame3 = Frame(self.superFrameInner1, height=2, bg='#F7F7F7', bd=1,  padx=1, pady=5)
			self.frame4 = Frame(self.superFrameInner1, height=2, bg='#F7F7F7', bd=1,  padx=1, pady=5)

			self.frame1.pack(side = LEFT, fill=Y)
			self.frame2.pack(side = LEFT, fill=Y)
			
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

			self.photo_radio_button_1 = Radiobutton(self.frame2, text="Yes", value=1, variable=self.photo_radiovar, command=self.PhotoSelRadio, bg="#F7F7F7")
			self.photo_radio_button_2 = Radiobutton(self.frame2, text="No", value=2, variable=self.photo_radiovar, command=self.PhotoSelRadio, bg="#F7F7F7")
			self.photo_copy_button = Button(self.frame2, text="Copy photos", bg="#f7f7f7")
			self.photo_copy_button.bind("<Button-1>", self.copyphoto)
			self.test_photoalbum_link = Button(self.frame2, text='test link', bg="#f7f7f7")
			self.photo_reset_button = Button(self.frame2, text='reset', command=self.resetSavePointPhoto)
			self.photo_stop_button = Button(self.frame2, text='stop', command=self.stopPhotoCopy)
			self.capture_copyphoto_text_label = Label(self.frame2, text="Capture text: ", bg="#f7f7f7")
			self.capture_copyphoto_text_radio_y=Radiobutton(self.frame2, text='Yes', value=1, variable=self.photo_cpature_radiovar, command=self.PhotoSelCaptureTextRadio, bg="#f7f7f7")
			self.capture_copyphoto_text_radio_n=Radiobutton(self.frame2, text='No', value=2, variable=self.photo_cpature_radiovar, command=self.PhotoSelCaptureTextRadio, bg="#f7f7f7")
			self.privates_photo_list = ttk.Combobox(self.frame2, values=[u"all", u"friends", u"nobody"])
			self.privates_photo_list.bind("<<ComboboxSelected>>", self.get_photo_privates_album)
			self.privates_photo_list.set(u"nobody")
			self.photo_progressbar_label = Label(self.frame2, text='0 of 0', bg="#f7f7f7")
			self.photo_progressbar = ttk.Progressbar(self.frame2, orient ="horizontal", length = 150, value=0, maximum=500, mode ="determinate")
			
			#self.photo_progressbar.pack()
			

			self.test_photoalbum_link.bind('<Button-1>', self.TestPhotoAlbum)
			self.photo_radio_button_2.select()



			self.public_id_copyvideo_label = Label(self.frame2, text="Public Id:", bg="#f7f7f7")
			self.public_id_copyvideo_enter = Entry(self.frame2)
			self.album_id_copyvideo_from_label = Label(self.frame2, text="AlbumID from copy: ", bg="#f7f7f7")
			self.album_name_from_copyvideo_enter=Entry(self.frame2)
			self.album_id_to_copyvideo_label = Label(self.frame2, text = "AlbumID to copy:", bg="#f7f7f7")
			self.album_name_copyvideo_to_enter=Entry(self.frame2)
			self.new_album_copyvideo_label = Label(self.frame2, text='New album title:', bg='#f7f7f7')
			self.new_album_name_copyvideo_enter=Entry(self.frame2)
			self.count_copyvideo_label = Label(self.frame2, text="count", bg='#f7f7f7')
			self.count_copyvideo_enter = Entry(self.frame2)
			self.create_videoalbum_label = Label(self.frame2, text="Create album:", bg="#f7f7f7")


			self.list1.bind('<<ListboxSelect>>', functools.partial(self.CurSelet, param1="list1", maction=True))
			self.list3.bind('<<ListboxSelect>>', functools.partial(self.CurSelet, param1="list3", maction=False))
			self.list4.bind('<<ListboxSelect>>', functools.partial(self.CurSelet, param1="list4", maction=False))
			self.master.bind("<Return>", functools.partial(self.CurSelet, param1="load", maction=False))
			self.list1.pack()
			self.list3.pack()
			self.list4.pack()

			self.post_public_id_enter_label=Label(self.frame2, text='Public Id:', bg='#f7f7f7')
			self.post_public_id_enter=Entry(self.frame2)
			self.post_number_after_do_label=Label(self.frame2, text='After post[number]:' ,bg='#f7f7f7')
			self.post_number_after_do=Entry(self.frame2)
			self.post_select_ptype_label=Label(self.frame2, text="Select post type:", bg='#f7f7f7')
			self.post_select_ptype_y=Radiobutton(self.frame2, value=1, text='comment', variable=self.wall_post_radiovar, command=self.SelectPostType, bg='#f7f7f7')
			self.post_select_ptype_n=Radiobutton(self.frame2, value=2, text='post', variable=self.wall_post_radiovar, command=self.SelectPostType, bg='#f7f7f7')
			self.post_button_send=Button(self.frame2, text='Send')
			self.post_button_send.bind("<Button-1>", self.make_post)
			self.post_button_send_stop=Button(self.frame2, text='Stop', command=self.stop_post)
			self.post_textarea=Text(self.superFrameInner1)
			
			self.photo_delete_albums_list_wrap=Frame(self.superFrameInner1, height=2, bg='#F7F7F7', bd=1,  padx=1, pady=5)
			self.photo_delete_albums_list_label=Label(self.photo_delete_albums_list_wrap, text='Photo albums', bg='#f7f7f7')
			self.photo_delete_albums_list=Listbox(self.photo_delete_albums_list_wrap, selectmode='multiple', bd=0)
			self.photo_delete_albums_list.bind("<Button-1>", functools.partial(self.CurSelet, param1="list3", maction=False))


			self.tumblr_copyphoto_albums_list_wrap=Frame(self.superFrameInner1, bg="#f7f7f7", padx=1, pady=5)
			self.tumblr_copyphoto_albums_list_label=Label(self.tumblr_copyphoto_albums_list_wrap, text='Photos albums', bg='#f7f7f7')
			self.tumblr_copyphoto_albums_list=Listbox(self.tumblr_copyphoto_albums_list_wrap, bd=0)
			self.tumblr_copyphoto_albums_list.bind("<<ListboxSelect>>", functools.partial(self.CurSelet, param1="list3", maction=False))
			self.tumblr_copyphoto_blog_url_label=Label(self.frame2, bg='#f7f7f7', text='Blog URL (http://title.tumblr.com): ')
			self.tumblr_copyphoto_blog_url_enter=Entry(self.frame2, bg='#f7f7f7')
			self.tumblr_copyphoto_public_id_label=Label(self.frame2, bg='#f7f7f7', text='Public ID:')
			self.tumblr_copyphoto_public_id_enter=Entry(self.frame2)
			self.tumblr_copyphoto_album_id_to_label=Label(self.frame2, text="Album ID to copy: ", bg='#f7f7f7')
			self.tumblr_copyphoto_album_id_to_enter=Entry(self.frame2)
			self.tumblr_copyphoto_count_label=Label(self.frame2, text='count:', bg='#f7f7f7')
			self.tumblr_copyphoto_count_enter=Entry(self.frame2)
			self.tumblr_copyphoto_tags_label=Label(self.frame2, text='tags:', bg='#f7f7f7')
			self.tumblr_copyphoto_tags_enter=Entry(self.frame2)
			self.tumblr_copyphoto_capture_text_label=Label(self.frame2, text="capture text:", bg='#f7f7f7')
			self.tumblr_copyphoto_capture_text_y=Radiobutton(self.frame2, value=1, text='yes', bg='#f7f7f7', variable=self.tumblr_copyphoto_capture_radiovar, command=self.TumblrCaptureSelect)
			self.tumblr_copyphoto_capture_text_n=Radiobutton(self.frame2, value=2, text='no', bg='#f7f7f7', variable=self.tumblr_copyphoto_capture_radiovar, command=self.TumblrCaptureSelect)
			self.tumblr_copyphoto_capture_text_n.select()
			self.tumblr_copyphoto_copy_button=Button(self.frame2, text='Copy photo', command=self.tumblrCopyPhoto)
			self.tumblr_copyphoto_stopcopy_button=Button(self.frame2, text='Stop', command=self.tumblrStopCopy)
			self.tumblr_copyphoto_reset_button=Button(self.frame2, text='Reset', command=self.tumblrReset)
			self.tumblr_copyphoto_fileformat_select=ttk.Combobox(self.frame2, values=[u'gif', u'jpg', u'png'])
			self.tumblr_copyphoto_fileformat_select.set('jpg')
			self.tumblr_copyphoto_fileformat_select.bind('<<ComboboxSelected>>', self.TumblrSelectFormat)
			self.tumblr_copyphoto_progressbar_label=Label(self.frame2, text='0 of 0', bg='#f7f7f7')
			self.tumblr_copyphoto_progressbar=ttk.Progressbar(self.frame2, orient='horizontal', length=130, value=0, maximum=500, mode='determinate')


			#self.PostOwnerId=None
			#self.photo_delete_albums_list = ttk.Treeview(self.superFrameInner1)
			#self.photo_delete_albums_list.bind("<<TreeviewSelect>>", self.printtree)
			#self.photo_delete_albums_list['show']='headings'
			#self.photo_delete_albums_list['selectmode']='extended'
		
			#self.photo_delete_albums_list['columns'] = ("one", "two")
			#self.photo_delete_albums_list.heading("one", text="Title")
			#self.photo_delete_albums_list.heading("two", text="Count")
			#self.photo_delete_albums_list.insert("" , 0,    text="Line 1", values=("1A","1b"))
			#self.photo_delete_albums_list.insert("" , 0,    text="Line 2", values=("1A","1b"))

			self.PostMessage="""📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 ДОБАВЛЮ📣📣📣📣📣📣📣 ДОБАВЛЮ 📣📣📣📣📣📣📣 """
			#self.PostMessage="Добавлю"
			self.selector=0
			self.menu=self.menu()
			self.copy_video_running=False
			self.copy_photo_running=False

			self.photoAlbumsToCopyFrom=[]
			self.photoAlbumsToCopyTo=[]

			self.CountPhotosToCopyTo=int
			self.PhotoPublicName=str
			self.TitlePhotoAlbumToCopyTo=str
			self.PhotoAlbumIdToCopyFrom  = int

			self.CountPhotosToCopyFrom=int
			self.CountPhotosToCopyTo=int
			self.PhotoAlbumIdToCopyTo=int
			self.PhotoFromId=int
			self.CreateNewPhotoAlbumState=int
			self.CreateNewVideoAlbumState=int
			self.PhotoCaptureTextState=False
			self.PhotoPublicIdToCopy=str
			self.PhotoAlbumsToDelete=None
			self.PhotoSelectedAlbumsToDelete=[]
			self.PhotoOffset=None
			self.captcha_key=None
			self.captcha_sid=None
			self.captcha_send=False
			self.PhotoPostCounter=-1
			self.photoCounter=0
			self.PhotoLeftCount=None
			self.PhotoMaxCount=None
			self.PhotoProcessStatus=False
			self.restart=False
			self.PhotoStop=False
			self.PhotoDefaultCount=1000
			self.PhotoPrivatesAlbum='nobody'
			self.photo_capture_text_captcha=False

			self.readPoint=self.savepointRead('photo')
			
			self.VideoAlbumsToCopyFrom=[]
			self.VideoAlbumsToCopyTo=[]
			self.VideoOffset=None
			self.CountVideosToCopyFrom=int
			self.CountVideosToCopyTo=int
			self.VideoMaxCount=None
			self.VideoFromId=int
			self.CreateVideoAlbumState=int
			self.VideoPublicIdToCopy=str
			self.VideoPostCounter=0
			self.VideoCounter=0
			self.VideoStop=False
			self.VideoProcessStatus=False
			self.VideoLeftCount=None
			self.TitleVideoAlbumToCopyTo=str
			self.VideoAlbumIdToCopyTo=None
			self.VideoAlbumIdToCopyFrom=None
			self.VideoDefaultCount=1000
			self.VideoPrivatesAlbum='nobody'
			self.run=True
			self.job=None
			self.ok=True
			self.t=None
			#self.readPoint=self.savepointRead()
			self.readPoint=self.savepointRead('video')

			self.PostPublicIdToSend=None
			self.PostWallType=None
			self.PostRunning=False

			self.TumblrPhotoAlbumsToCopyTo=None
			self.TumblrBlogUrl=None
			self.TumblrPhotoCount=None
			self.TumblrPhotoLeftCount=None
			self.TumblrPhotoCounter=0
			self.TumblrPhotoStop=False
			self.TumblrCaptureState=False
			self.TumblrCopyRunning=False
			self.TumblrCopyPhotoPublicId=None
			self.TumblrCopyPhotoAlbumId=int
			self.TumblrCopyPhotoOffset=None
			self.TumblrCopyPhotoProcess=False
			self.TumblrPhotoAlbumName=None
			self.savepointRead('tumblr_photo')
			self.TumblrDefaultCountPhoto=1000
			self.TumblrSelectedFormat='jpg'

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
				if type(fromId) != str:
					if fromId<0:
						publicName = re.sub("[\[\]]", '', vkapi.groups.getById( group_id = abs(fromId))[0]['name'])
					elif fromId>0:
						publicName=vkapi.users.get(user_ids=str(fromId), fields='nickname')[0]['first_name']
						publicName=publicName + ' ' + vkapi.users.get(user_ids=str(fromId), fields='nickname')[0]['last_name']
				else:
					publicName=self.TumblrBlogUrl
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

		def savepointWrite(self, data, dtype):
			if dtype=='photo':
				with open("photoSavepoint.json", "w") as file:
					file.write(json.dumps(data, indent=4, ensure_ascii=False))
			elif dtype=='video':
				with open("videoSavepoint.json", "w") as file:
					file.write(json.dumps(data, indent=4, ensure_ascii=False))
			elif dtype=='tumblr_photo':
				with open("tumblrPhotoSavepoint.json", "w") as file:
					file.write(json.dumps(data, indent=4, ensure_ascii=False))

		def savepointRead(self, dtype):
			if dtype=='video':
				fname="videoSavepoint.json"
				if os.stat(fname).st_size != 0:
					with open(fname, "r") as file:
						data = json.load(file)	
						if data:
							self.VideoOffset=data['offset']
							self.VideoPostCounter=self.VideoOffset
							self.VideoFromId=data['id']
							self.VideoLeftCount=data['left_count']
							self.CountVideosToCopyFrom=data['max_count']
							self.VideoAlbumIdToCopyTo=data['album_id']
							if data['album_id_from']:
								self.VideoCounter=self.VideoOffset
								self.VideoPublicName=data['public_name'] 
								self.TitleVideoAlbumToCopyTo=data['album_title_from']
								self.VideoAlbumIdToCopyFrom =data['album_id_from']
							self.public_id_copyvideo_enter.delete(0, END)
							self.public_id_copyvideo_enter.insert(END, self.VideoFromId)
							self.album_name_from_copyvideo_enter.delete(0, END)
							self.album_name_from_copyvideo_enter.insert(END, self.VideoAlbumIdToCopyFrom)
							self.count_copyvideo_enter.delete(0, END)
							self.count_copyvideo_enter.insert(END, self.VideoLeftCount)
				else:
					self.VideoCounter=0
					self.VideoLeftCount=None
					self.VideoOffset=None
					self.VideoPostCounter=-1
					#self.count=None		
					#
			elif dtype=='photo':
				fname="photoSavepoint.json"
				if os.stat(fname).st_size != 0:
					with open("photoSavepoint.json", "r") as file:
						data = json.load(file)	
						if data:
							self.PhotoOffset=data['offset']
							self.PhotoPostCounter=self.PhotoOffset
							self.PhotoFromId=data['id']
							self.PhotoLeftCount=data['left_count']
							self.CountPhotosToCopyFrom=data['max_count']
							self.PhotoAlbumIdToCopyTo=data['album_id']
							if data['album_id_from']:
								self.photoCounter=self.PhotoOffset
								self.PhotoPublicName=data['public_name'] 
								self.TitlePhotoAlbumToCopyTo=data['album_title_from']
								self.PhotoAlbumIdToCopyFrom =data['album_id_from']
							self.public_id_copyphoto_enter.delete(0, END)
							self.public_id_copyphoto_enter.insert(END, self.PhotoFromId)
							self.album_name_from_copyphoto_enter.delete(0, END)
							self.album_name_from_copyphoto_enter.insert(END, self.PhotoAlbumIdToCopyFrom)
							self.count_photoalbums_enter.delete(0, END)
							self.count_photoalbums_enter.insert(END, self.PhotoLeftCount)
	
				
				else:
					self.photoCounter=0
					self.PhotoLeftCount=None
					self.PhotoOffset=None
					self.PhotoPostCounter=-1
					#self.count=None			
			elif dtype=='tumblr_photo':
				fname="tumblrPhotoSavepoint.json"
				if os.stat(fname).st_size!=0:
					print('not empty')
					with open("tumblrPhotoSavepoint.json", 'r') as file:
						data = json.load(file)
					if data:
						self.TumblrPhotoOffset=data['offset']
						self.TumblrPhotoCounter=self.TumblrPhotoOffset
						self.TumblrBlogUrl=data['url']
						self.TumblrPhotoLeftCount=data['left_count']
						self.TumblrPhotoCount=data['max_count']
						self.TumblrCopyPhotoAlbumId=data['album_id']
						self.TumblrCopyPhotoPublicId=data['public_id']
						self.tumblr_copyphoto_count_enter.delete(0, END)
						self.tumblr_copyphoto_count_enter.insert(END, self.TumblrPhotoLeftCount)
						self.tumblr_copyphoto_blog_url_enter.delete(0, END)
						self.tumblr_copyphoto_blog_url_enter.insert(END, self.TumblrBlogUrl)
						self.tumblr_copyphoto_public_id_enter.delete(0, END)
						self.tumblr_copyphoto_public_id_enter.insert(END, self.TumblrCopyPhotoPublicId)
				else:
					self.TumblrPhotoCounter=0
					self.TumblrCopyPhotoOffset=None
					self.TumblrPhotoLeftCount=None

		def TumblrSelectFormat(self, event):
			self.TumblrSelectedFormat=self.tumblr_copyphoto_fileformat_select.get()


		def captcha(self, dtype):
			def getKey(event):
				global key
				key = e1.get()
				if dtype=='photo':
					threading.Thread(target=self.copyPhotoToAlbum2, args=(person[0], self.PhotoFromId, self.albumNameToCopyTo, self.PhotoAlbumIdToCopyFrom , self.CountPhotosToCopyFrom, self.captcha_sid, key, self.PhotoOffset, False, self.captcha_send, self.PhotoAlbumIdToCopyTo, self.PhotoCaptureTextState)).start()
				elif dtype=='video':
					threading.Thread(target=self.copyVideo, args=(self.VideoFromId, self.CountVideosToCopyFrom, self.VideoAlbumIdToCopyFrom, self.VideoOffset, self.captcha_send, self.captcha_sid, key)).start()
					#print(self.VideoFromId, self.CountVideosToCopyFrom, self.VideoAlbumIdToCopyFrom, self.VideoOffset, self.captcha_sid, key)
				elif dtype=="post":
					#threading.Thread(target=self.make_post, args=(self.captcha_send, self.captcha_sid, key)).start()
					#print(self.captcha_send, self.captcha_sid, key)
					#self.make_post(self.captcha_send, self.captcha_sid, key)
					self.ok=True
					self.e.set()
				elif dtype=='gif tumblr':
					threading.Thread(target=self.tumblrCopyPhotoStart, args=(self.TumblrCopyPhotoPublicId, 'tumblr gif', self.TumblrPhotoCount, self.TumblrPhotoOffset, self.captcha_send, self.captcha_sid, key, True )).start()

				window2.destroy()
			def close_window():
				#self.t.join()
				global key
				key=None
				self.e.set()
				self.ok=False
				window2.grab_release()
				window2.destroy()
			dtype=dtype
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
			window2.protocol("WM_DELETE_WINDOW", close_window)
			window2.attributes("-topmost", True)
			window2.grab_set()
			return key

		def copyPhotoToAlbum2(self, to_id, from_id, albumNameToCopyTo,  albumIdToCopyFrom, countPhotos, captcha_sid=None, captcha_key=None, offset=None, text=False, captcha_send=False, albumIdToCopyTo=None, capture_text=False):	
			def copyAction():
				self.PhotoStop=False
				album_id = []
				photo_id = []
				albumsFromIds = []
				photosToCopy = []
				updateDate=int
				text1=str
				toFile=[]
				phlist=[]
				st=0
				getAlbumsTo = self.getAlbums(to_id,'photo')
				captured_text=None
				if albumIdToCopyFrom=='wall':
					source='wall'
				else:
					source='album'
				if self.album_name_copyphoto_to_enter.get() != '':
					album_id.append(int(self.album_name_copyphoto_to_enter.get()))
				else:
					album_id.append(albumIdToCopyTo)


				with open(os.path.join('updates', source, "updatePhotoData.json")) as f:
					data = json.load(f)	
					for i in data:
						if i['id']==from_id:
							updateDate=i['date']
					date1=[i['date'] for i in vkapi.wall.get(owner_id=from_id, count=10)['items'] if 'is_pinned' not in i][0]
					if albumIdToCopyFrom=='wall':
						self.UpdateData(from_id, date1, 'photo', 'wall')
				if offset:
					step=offset
				else:
					step=-1
				while step<countPhotos:
					
					step+=1
					if self.PhotoStop==True:
						break

					#time.sleep(1)
					photosGet=vkapi.wall.get(owner_id=from_id, count=1, offset=step)
					time.sleep(0.5)
					self.PhotoPostCounter+=1
					if self.PhotoPostCounter==countPhotos: 
						complete=True
						self.PhotoProcessStatus=complete
						self.restart=True
					else:
						complete=False
					self.savepointWrite({'id':from_id, 'offset':step, 'album_id':album_id[0], 'left_count':countPhotos-self.PhotoPostCounter, 'max_count':countPhotos, 'complete': complete, 'album_id_from': albumIdToCopyFrom, 'public_name': self.PhotoPublicName, 'album_title_from': self.TitlePhotoAlbumToCopyTo}, 'photo')
					for i in photosGet['items'] :
						if 'is_pinned' not in i:
							self.photo_progressbar['value']+=1
							self.photo_progressbar_label.configure(text="%s of %s" % (self.PhotoPostCounter, self.CountPhotosToCopyFrom))
							if capture_text is True:
								if 'text' in i and i['text']!='':
									#if len(i['text'])>500:
									#	f = re.search("[\w\W]{500}", i['text'])
									#	captured_text=f.group(0)
									#else:
										captured_text=i['text']
								else:
									captured_text=None
							if i['date']==updateDate:
								self.PhotoStop=True
							if 'attachments' in i:
								for a in i['attachments']:
									if a['type']=='photo':
										try:
											if captcha_send  is True:
												copyPhotos = vkapi.photos.copy(owner_id=a['photo']['owner_id'], photo_id=a['photo']['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)
											else:
												copyPhotos = vkapi.photos.copy(owner_id=a['photo']['owner_id'], photo_id=a['photo']['id'])
											time.sleep(1)
											movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
											time.sleep(1)
											if  copyPhotos and captured_text is not None:
												try:
													if self.photo_capture_text_captcha is True:
														vkapi.photos.edit(owner_id=person[0], photo_id=copyPhotos, caption=captured_text, captcha_key=captcha_key, captcha_sid=captcha_sid)
													else:
														vkapi.photos.edit(owner_id=person[0], photo_id=copyPhotos, caption=captured_text)
													time.sleep(1)
												except vkerror as e:
													self.PhotoOffset=self.PhotoPostCounter
													self.PhotoAlbumIdToCopyTo=album_id[0]
													self.download_captcha(e.captcha_img)
													self.captcha_sid=e.captcha_sid
													self.captcha_key=self.captcha('photo')
													self.PhotoStop=True
													self.captcha_send=False
													self.photo_capture_text_captcha=True
													break

										except vkerror as e:
											if e.code==15:
												time.sleep(1)
												continue
											
											self.PhotoOffset=self.PhotoPostCounter
											self.PhotoAlbumIdToCopyTo=album_id[0]
											self.captcha_send=True
											self.download_captcha(e.captcha_img)
											self.captcha_sid=e.captcha_sid
											self.captcha_key=self.captcha('photo')
											self.PhotoStop=True
											break
									
			copyAction()

		def copyPhotoToAlbum(self, to_id, from_id, albumNameToCopyTo, albumIdToCopyTo, albumIdToCopyFrom, countPhotos,  offset=None, text=False, captcha_send=False, captcha_sid=None, captcha_key=None):
			album_id = []
			photo_id = []
			albumsFromIds = []
			photosToCopy = []
			updateDate=int
			text1=str
			toFile=[]
			rev=0
			self.PhotoStop=False
			# getAlbumsFromId = Comb.getAlbums('self', from_id)
			if offset:
				step=offset
			else:
				step=-1
			album_id.append(albumIdToCopyTo)

			while step<countPhotos:
				step+=1
				if self.PhotoStop==True:
					break
				if self.photoCounter==countPhotos: 
					complete=True
					self.PhotoProcessStatus=complete
					self.restart=True
				else:
					complete=False
					self.PhotoProcessStatus=False

				self.savepointWrite({'id':from_id, 'offset':step, 'album_id':album_id[0], 'left_count':countPhotos-self.photoCounter, 'max_count':countPhotos, 'complete': complete, 'album_id_from': albumIdToCopyFrom, 'public_name': self.PhotoPublicName, 'album_title_from': self.TitlePhotoAlbumToCopyTo }, 'photo')
				try:
					photosGet=vkapi.photos.get(owner_id=from_id, album_id=albumIdToCopyFrom, count=1, offset=step, rev=rev)
					for a in photosGet['items']:
						self.photoCounter+=1
						self.photo_progressbar['value']+=1
						self.photo_progressbar_label.configure(text="%s of %s" % (self.photoCounter, self.CountPhotosToCopyFrom))
						if captcha_send:
							copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)

						else:
							copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'])
						movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
						time.sleep(1)

				except vkerror as e:

					self.PhotoAlbumIdToCopyTo=album_id[0]
					self.download_captcha(e.captcha_img)
					self.captcha_sid=e.captcha_sid
					self.captcha_key=self.captcha('photo')
					self.captcha_send=True
					self.PhotoStop=True
					break

		def copyVideo(self, public_id, count, source, offset=None, captcha_send=False, captcha_sid=None, captcha_key=None, privates=None):
			if public_id>0:
				publicName = vkapi.users.get(user_ids=str(public_id), fields='nickname')[0]['first_name']
				publicName = publicName + ' ' + vkapi.users.get(user_ids=str(public_id), fields='nickname')[0]['last_name']

			elif public_id < 0:
				publicName = vkapi.groups.getById( group_id = abs(public_id))[0]['name']


			albumTitles=[]
			fname='updateVideoToCopy.json'
			dtype='video'
			updateDate=int
			albumIds=[]

	
			if offset:
				step=offset-1
			else:
				step=-1
			
			
			if source=='wall' or source=='videobox':
				for i in self.getAlbums(person[0], 'video'):
				
					if re.sub('[\W0-9]', '', publicName) == re.sub('[\W0-9]', '', i['title']):
							albumIds.append(i['id'])
		
				if len(albumIds)==0:
					TargetAlbumId=vkapi.video.addAlbum(owner_id=person[0], privacy=privates, title=publicName+' '+str(len(albumIds)+1))['album_id']
					#print('no albums')
				else:
					for i in albumIds:
						if vkapi.video.getAlbumById(album_id=i)['count']<1000:
							TargetAlbumId=i
							break
						else:
							TargetAlbumId=vkapi.video.addAlbum(owner_id=person[0], privacy=privates, title=publicName+' '+str(len(albumIds)+1))['album_id']
						#print('albums with < 1k not found')

			if type(source)==int:
				print(source)

			if type(source)==int:
				print(source)
	
			elif source=='videobox':

				self.VideoStop=False
				
				while step<count:
					step+=1
					if self.VideoStop==True:
						break
					if step==count: 
						complete=True
						self.VideoProcessStatus=complete
						self.restart=True
					else:
						complete=False
						self.VideoProcessStatus=False

					self.savepointWrite({'id':public_id, 'offset': step, 'album_id': TargetAlbumId, 'left_count':count-step, 'max_count':count, 'complete': complete, 'album_id_from': self.VideoAlbumIdToCopyFrom, 'public_name': publicName, 'album_title_from': self.TitleVideoAlbumToCopyTo }, 'video')
					for i in vkapi.video.get(owner_id=public_id, offset=step, count=1, extended=1)['items']:
			
						self.VideoCounter+=1
						self.video_progressbar_label.configure(text='%s of %s ' % (step, count))
						self.video_progressbar['value']+=1
						try:
							if captcha_send:
								add=vkapi.video.addToAlbum(target_id=person[0], owner_id=i['owner_id'], album_id=TargetAlbumId, video_id=i['id'], captcha_sid=captcha_sid, captcha_key=captcha_key)
							else:
								add=vkapi.video.addToAlbum(target_id=person[0], owner_id=i['owner_id'], album_id=TargetAlbumId, video_id=i['id'])

							time.sleep(1)
						except vkerror as e:
							if e.code==800 or e.code==6 or e.code==204:
								#step+=1
								time.sleep(1)
								continue
							self.VideoOffset=step
							self.VideoAlbumIdToCopyTo=TargetAlbumId
							self.download_captcha(e.captcha_img)
							self.captcha_sid=e.captcha_sid
							self.captcha_key=self.captcha('video')
							self.captcha_send=True
							self.VideoStop=True
							break
		
			elif source=='wall':
				self.VideoStop=False
				ld=[]
				#for dd in vkapi.wall.get(owner_id=public_id, count=count, album_id='wall', filter='owner')['items']:
				#	if 'attachments' in dd:
				#		for bb in dd['attachments']:
				#			if bb['type']=='video':
				#				ld.append(dd['date'])
				#time.sleep(1)
				#Comb.UpdateData('self', public_id, ld[0], dtype, 'wall')	
				while step<count:
					step+=1
					if self.VideoStop:
						break
					self.VideoPostCounter+=1
					if step==count: 
						complete=True
						self.VideoProcessStatus=complete
						self.restart=True
					else:
						complete=False
					wallget=vkapi.wall.get(owner_id=public_id, count=1, offset=step, filter='owner')['items']
					time.sleep(1)
					for i in wallget: 
						#if updateDate!=None:
						#	if updateDate==i['date']:
						#		break
						
						self.savepointWrite({'id':public_id, 'offset': step, 'album_id': TargetAlbumId, 'left_count':count-step, 'max_count':count, 'complete': complete, 'album_id_from': self.VideoAlbumIdToCopyFrom, 'public_name': publicName, 'album_title_from': self.TitleVideoAlbumToCopyTo }, 'video')	
						self.video_progressbar['value']+=1
						self.video_progressbar_label.configure(text="%s of %s" % (step, self.CountVideosToCopyFrom))
						if 'attachments' in i:
							for jo in i['attachments']:
								if jo['type']=='video':
									# if jo['video']['title'] not in [i['title'] for i in vkapi.video.get(owner_id=person[0], album_id=TargetAlbumId)['items'] if 'title' in i]:
									try:
										if captcha_send:
											add=vkapi.video.addToAlbum(target_id=person[0], owner_id=jo['video']['owner_id'], album_id=TargetAlbumId, video_id=jo['video']['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)
										else:
											add=vkapi.video.addToAlbum(target_id=person[0], owner_id=jo['video']['owner_id'], album_id=TargetAlbumId, video_id=jo['video']['id'])
										time.sleep(1)
									except vkerror as e:
										if e.code==800 or e.code==204:
											continue
										self.VideoOffset=self.VideoPostCounter
										self.VideoAlbumIdToCopyTo=TargetAlbumId
										self.download_captcha(e.captcha_img)
										self.captcha_sid=e.captcha_sid
										self.captcha_key=self.captcha('video')
										self.captcha_send=True
										self.VideoStop=True
										break

		def menu(self):
			for i,y in zip(range(len(self.actions_list)), self.actions_list):
				if i == 0:
					self.list1.insert(END, '1. %s' % (self.actions_list[0]))
				else:
					self.list1.insert(END, '%s. %s' % (i+1, y))

		def printtree(self,event):
			curItem = self.photo_delete_albums_list.focus()
			print (self.photo_delete_albums_list.item(curItem))

		def make_post(self, captcha_send=False, captcha_key=None, captcha_sid=None):			
				#public_id=-13295252
				#public_id=-60191872
				#public_id=-8337923
				public_id=int(self.post_public_id_enter.get())

				if self.PostWallType == 'comment':
					self.PostRunning=True
					if self.post_number_after_do.get():
						after_post = int(self.post_number_after_do.get())
					else:
						after_post = 2
					for i in vkapi.wall.get(owner_id=public_id, count=after_post, extended=1)['items']:
						post_id=i['id']
					try:
						while 1:
							if self.PostRunning is False:
								break
							addComment=vkapi.wall.addComment(owner_id=public_id, post_id=post_id,  text=self.PostMessage)
							time.sleep(2)
					except vkerror as e:
						print(e)
						if e.code is not 9:
							self.t=threading.Thread(target=self.waiting, args=(public_id, e.captcha_img, e.captcha_sid, post_id, 'comment'))
							self.t.daemon=True
							self.t.start()
				elif self.PostWallType == 'post':
					self.PostRunning=True
					try:
						while 1:
							if self.PostRunning==False:
								break
							print('ooooo')
							make_post=vkapi.wall.post(owner_id=public_id, message='добавлю', from_group=0, friends_only=0)
							print(make_post)
							time.sleep(3)
					except vkerror as e:
						print(e.code)
						if e.code is not 9:
							self.t=threading.Thread(target=self.waiting, args=(public_id, e.captcha_img, e.captcha_sid, None, 'post'))
							self.t.daemon=True
							self.t.start()
		
		def waiting(self, public_id, captcha_img, captcha_sid, post_id, post_type):
			self.download_captcha(captcha_img)
			self.captcha_sid=captcha_sid
			self.captcha('post')
			self.captcha_send=True
			global key
			while True:
				is_set = self.e.wait()
				print('catched')
				if post_type == 'comment':
					if post_id and key:
						try:
							addComment=vkapi.wall.addComment(owner_id=public_id, post_id=post_id,  text=self.PostMessage, captcha_key=key, captcha_sid=self.captcha_sid)

						except vkerror as e:
							self.make_post()
							self.ok=False
				elif post_type == 'post':
					if key:
						try:
							make_post=vkapi.wall.post(owner_id=public_id, message=self.PostMessage, captcha_key=key, captcha_sid=self.captcha_sid)
							print(make_post)

						except vkerror as e:
							self.make_post()
							self.ok=False

				self.captcha_send=False
				self.e.clear()
				break
			if self.ok:
				self.make_post()

		def stop_post(self):
			self.PostRunning=False
			self.ok=False
			global key
			key=None
			self.e.set()

		def delPhotos(self):
			photos = vkapi.photos.get(owner_id=person[0], album_id='saved')['items']
			for i in photos:
				vkapi.photos.delete(owner_id=person[0], photo_id=i['id'])
				time.sleep(0.4)

		def getAlbums(self, public_id, dtype):
			titles = []
			ids= []
			ids_l=[]
			step=-100
			if dtype=='photo':
				albums = vkapi.photos.getAlbums( owner_id = public_id)['items']
				for y,i in zip(range(len(albums)), albums):
					ids.append(dict(number=y+1, id=i['id'], title=i['title'], count=i['size']))

			elif dtype=='video':
				while step<200:
					step+=100
					for i in vkapi.video.getAlbums(owner_id=public_id, count=100, offset=step, extended=1)['items']: 
						ids_l.append(dict(id=i['id'], title=i['title'], count=i['count']))
				for y,i in zip(range(len(ids_l)), ids_l):
					ids.append(dict(number=y+1, id=i['id'], title=i['title'], count=i['count']))
			return ids
		
		def get_video_privates_album(self, event):
			self.VideoPrivatesAlbum=self.privates_video_list.get()

		def get_photo_privates_album(self, event):
			self.PhotoPrivatesAlbum=self.privates_photo_list.get()

		def download_captcha(self, url):
				readurl = urlopen(url).read()
				with open("captcha.png", 'wb') as captcha:
					captcha.write(readurl)

		def SelectPostType(self):
			if self.wall_post_radiovar.get()==1:
				self.PostWallType='comment'
			else:
				self.PostWallType='post'
			print(self.PostWallType)

		def TestPhotoAlbum(self, event):
			webbrowser.open_new("https://vk.com/album%s_%s" % (self.PhotoPublicIdToCopy, self.PhotoAlbumIdToCopyFrom ))

		def TestVideoAlbum(self, event):
			webbrowser.open_new("https://vk.com/videos%s?section=album_%s" % (self.VideoPublicIdToCopy, self.VideoAlbumIdToCopyFrom ))

		def PhotoSelRadio(self):
			self.CreateNewPhotoAlbumState = self.photo_radiovar.get()

		def VideoSelRadio(self):
			self.CreateNewVideoAlbumState = self.video_radiovar.get()

		def PhotoSelCaptureTextRadio(self):
			if self.photo_cpature_radiovar.get()==1:
				self.PhotoCaptureTextState=True
			else:
				self.PhotoCaptureTextState=False

		def TumblrCaptureSelect(self):
			if self.tumblr_copyphoto_capture_radiovar.get()==1:
				self.TumblrCaptureState=True
			elif self.tumblr_copyphoto_capture_radiovar.get()==2:
				self.TumblrCaptureState=False
			print(self.TumblrCaptureState)

		def resetSavePointPhoto(self):
			#self.PhotoOffset=None
			#self.photoCounter=0
			#self.PhotoProcessStatus=False
			#self.PhotoLeftCount=None
			self.photo_progressbar.configure(value=0)
			self.photo_progressbar_label.configure(text='%s of %s' % (0, 0))
			self.count_photoalbums_enter.delete(0, END)
			self.count_photoalbums_enter.insert(END, self.PhotoDefaultCount)
			self.public_id_copyphoto_enter.delete(0, END)
			self.album_name_from_copyphoto_enter.delete(0, END)
			self.restart=True
			with open('photoSavepoint.json', 'w'): pass
			self.savepointRead("photo")

		def resetSavePointVideo(self):
			#self.PhotoOffset=None
			#self.photoCounter=0
			#self.PhotoProcessStatus=False
			#self.PhotoLeftCount=None
			self.video_progressbar.configure(value=0)
			self.video_progressbar_label.configure(text='%s of %s' % (0, 0))
			self.count_copyvideo_enter.delete(0, END)
			self.count_copyvideo_enter.insert(END, self.VideoDefaultCount)
			self.public_id_copyvideo_enter.delete(0, END)
			self.album_name_from_copyvideo_enter.delete(0, END)
			self.restart=True
			self.captcha_send=False
			with open('videoSavepoint.json', 'w'): pass
			self.savepointRead("video")

		def stopPhotoCopy(self):
			self.savepointRead('photo')
			self.PhotoStop=True
			self.copy_photo_running=False
			#print(self.photoCounter)
			#print(self.PhotoLeftCount)
			#print(self.PhotoOffset)
			#print(self.PhotoPostCounter)
			#print(self.PhotoMaxCount)

		def stopVideoCopy(self):
			self.savepointRead('video')
			self.VideoStop=True
			self.copy_video_running=False

		def tumblrCopyPhotoStart(self, public_id, album_id, count, offset=None, captcha_send=False, captcha_sid=None, captcha_key=None, capture_text=False):
			if offset:
				step=offset-1
			else:
				step=-1
			if self.tumblr_copyphoto_tags_enter.get():
				tags=self.tumblr_copyphoto_tags_enter.get()
			else:
				tags='vk.com/id%s'%(public_id)
			self.TumblrPhotoStop=False
			with open(os.path.join('updates', 'wall', "updatePhotoData.json")) as f:
					data = json.load(f)	
					for i in data:
						if i['id']==self.TumblrBlogUrl:
							updateDate=i['date']
						else:
							updateDate=None
			if self.TumblrSelectedFormat=='gif':
				uploadUrl = vkapi.docs.getUploadServer(owner_id=int(public_id))['upload_url']
			else:
				uploadUrl = vkapi.photos.getUploadServer(owner_id=int(public_id), album_id=album_id)['upload_url']
			posts=t.get('posts', blog_url=self.TumblrBlogUrl, params={"limit":1})
			date1=[i['timestamp'] for i in posts['posts']][0]
			if self.TumblrSelectedFormat !='gif':
				self.UpdateData(self.TumblrBlogUrl, date1, 'photo', 'wall')
			else:
				self.UpdateData(self.TumblrBlogUrl, date1, 'gif', 'wall')

			while step < count-1:
				step+=1
				if self.TumblrPhotoStop==True:
						break
				if step==count-1: 
						complete=True
						self.TumblrCopyPhotoProcess=complete
						#self.restart=True
				else:
					complete=False
				self.TumblrPhotoCounter+=1
				self.savepointWrite({'offset':step+1, 'album_id':album_id, 'left_count':count-step-1, 'max_count':count, 'complete': complete, 'title': self.TumblrPhotoAlbumName, 'url': self.tumblr_copyphoto_blog_url_enter.get(), "public_id": public_id}, 'tumblr_photo')
				self.tumblr_copyphoto_progressbar['value']+=1
				self.tumblr_copyphoto_progressbar_label.configure(text="%s of %s" % (step+1, count))
				posts=t.get('posts', blog_url=self.TumblrBlogUrl, params={"type":"photo", "limit":1, "offset":step})
				for i in posts['posts']:
					if updateDate:
						if i['timestamp']==updateDate:
							self.TumblrPhotoStop=True
					caption=re.sub("<[^<]+?>", '', i['caption'])
					htmlparser=HTMLParser()
					caption = htmlparser.unescape(caption)
					if 'photos' in i:
						for a in i['photos']:
							if self.TumblrSelectedFormat == 'jpg':
								if re.findall("(?<=\.)\w+$", a['original_size']['url'])[0] != 'gif':
									fileto = urlopen(a['original_size']['url']).read()
									with open('image_tumblr.jpg', 'wb') as file:
										file.write(fileto)
									r = requests.post(uploadUrl, files={ 'file' : open('image_tumblr.jpg', 'rb') }).json()
									if capture_text is True:
										vkapi.photos.save(album_id=album_id, owner_id=public_id, caption=caption, hash=r['hash'], server=r['server'], photos_list=r['photos_list'])
									else:
										vkapi.photos.save(album_id=album_id, owner_id=public_id, hash=r['hash'], server=r['server'], photos_list=r['photos_list'])

							elif self.TumblrSelectedFormat == 'gif':
								if re.findall("(?<=\.)\w+$", a['original_size']['url'])[0]=='gif':
									fileto = urlopen(a['original_size']['url']).read()
									doc_name='image_doc_id%s.gif' % (public_id) 
									with open(doc_name, 'wb') as file:
										file.write(fileto)
									r = requests.post(uploadUrl, files={ 'file' : open(doc_name, 'rb') }).json()
									try:
										if captcha_send == False:
											vkapi.docs.save(file=r['file'], tags=tags, title=caption)
										else:
											vkapi.docs.save(file=r['file'], title=caption, tags=tags, captcha_sid=captcha_sid, captcha_key=captcha_key)

									except vkerror as e:
										self.TumblrPhotoOffset=step
										self.download_captcha(e.captcha_img)
										self.captcha_sid = e.captcha_sid
										self.captcha('gif tumblr')
										self.captcha_send=True
										self.TumblrPhotoStop=True
									

		def tumblrCopyPhoto(self):
			if self.TumblrCopyRunning==False:
				self.TumblrCopyRunning=True
				posts=t.get('posts', blog_url=self.tumblr_copyphoto_blog_url_enter.get(), params={"type":"photo", "limit":1})
				self.TumblrBlogUrl=self.tumblr_copyphoto_blog_url_enter.get()
				if posts['blog']['title']:
					target_album_name=posts['blog']['title']
				else:
					target_album_name = posts['blog']['name']
				self.TumblrPhotoAlbumName=target_album_name
				if self.TumblrSelectedFormat !='gif':
					if self.TumblrPhotoLeftCount is not None and self.TumblrCopyPhotoProcess==False:
						self.tumblr_copyphoto_progressbar.configure(maximum=self.TumblrPhotoCount)
						self.tumblr_copyphoto_progressbar.configure(value=self.TumblrPhotoCount-self.TumblrPhotoLeftCount)
						threading.Thread(target=self.tumblrCopyPhotoStart, args=(self.TumblrCopyPhotoPublicId, self.TumblrCopyPhotoAlbumId, self.TumblrPhotoCount, self.TumblrPhotoOffset, False, None, None, True)).start()
						#self, public_id, album_id, count, offset=None, captcha_send=False, captcha_sid=None, captcha_key=None, capture_text=False):
					elif self.TumblrCopyPhotoProcess==False and self.TumblrPhotoLeftCount is None:
						if self.tumblr_copyphoto_album_id_to_enter.get():
							album_id=int(self.tumblr_copyphoto_album_id_to_enter.get())
							
						if self.TumblrPhotoLeftCount==None and self.tumblr_copyphoto_album_id_to_enter!='' and self.tumblr_copyphoto_album_id_to_enter.get()=='':
							album_id=vkapi.photos.createAlbum(owner_id=int(self.tumblr_copyphoto_public_id_enter.get()), privacy_view='nobody', title=target_album_name)['id']
						self.TumblrPhotoCounter=0
						self.TumblrPhotoOffset=0
						self.TumblrPhotoCount=int(self.tumblr_copyphoto_count_enter.get())
						self.TumblrCopyPhotoPublicId=self.tumblr_copyphoto_public_id_enter.get()
						#self.TumblrCopyPhotoAlbumId=int(self.tumblr_copyphoto_album_id_to_enter.get())
						#album_id=self.TumblrCopyPhotoAlbumId
						self.tumblr_copyphoto_progressbar.configure(maximum=self.TumblrPhotoCount)
						self.tumblr_copyphoto_progressbar.configure(value=0)
						threading.Thread(target=self.tumblrCopyPhotoStart, args=(self.TumblrCopyPhotoPublicId, album_id, self.TumblrPhotoCount, None, False, None, None, True)).start()
				else:
					if self.TumblrPhotoLeftCount is not None and self.TumblrCopyPhotoProcess==False:
						self.tumblr_copyphoto_progressbar.configure(maximum=self.TumblrPhotoCount)
						self.tumblr_copyphoto_progressbar.configure(value=self.TumblrPhotoCount-self.TumblrPhotoLeftCount)
						threading.Thread(target=self.tumblrCopyPhotoStart, args=(self.TumblrCopyPhotoPublicId, 'tumblr gif', self.TumblrPhotoCount, self.TumblrPhotoOffset, False, None, None, True)).start()
					if self.TumblrPhotoLeftCount==None and self.tumblr_copyphoto_album_id_to_enter!='' and self.tumblr_copyphoto_album_id_to_enter.get()=='':
						self.TumblrPhotoCounter=0
						self.TumblrPhotoOffset=0
						self.TumblrPhotoCount=int(self.tumblr_copyphoto_count_enter.get())
						self.TumblrCopyPhotoPublicId=self.tumblr_copyphoto_public_id_enter.get()
						#self.TumblrCopyPhotoAlbumId=int(self.tumblr_copyphoto_album_id_to_enter.get())
						#album_id=self.TumblrCopyPhotoAlbumId
						self.tumblr_copyphoto_progressbar.configure(maximum=self.TumblrPhotoCount)
						self.tumblr_copyphoto_progressbar.configure(value=0)
						threading.Thread(target=self.tumblrCopyPhotoStart, args=(self.TumblrCopyPhotoPublicId, 'tumblr gif', self.TumblrPhotoCount, None, False, None, None, True)).start()
			else:
				tkinter.messagebox.showwarning('Tumlbr copy photo', 'Yoy have running copying')

		def tumblrStopCopy(self):
			self.TumblrCopyRunning=False
			self.TumblrPhotoStop=True
			self.savepointRead('tumblr_photo')

		def tumblrReset(self):
			self.tumblr_copyphoto_progressbar['value']=0
			self.tumblr_copyphoto_progressbar_label.configure(text="0 of 0")
			self.tumblr_copyphoto_count_enter.delete(0, END)
			self.tumblr_copyphoto_count_enter.insert(END, self.TumblrDefaultCountPhoto)
			self.tumblr_copyphoto_public_id_enter.delete(0, END)
			self.tumblr_copyphoto_public_id_enter.insert(END, person[0])
			self.captcha_send=False
			with open('tumblrPhotoSavepoint.json', 'w'): pass
			self.savepointRead('tumblr_photo')

		def copyphoto(self, event):

				if self.copy_photo_running==False:
					self.copy_photo_running=True
					title = self.PhotoPublicName + ' ' + self.TitlePhotoAlbumToCopyTo
					if self.PhotoLeftCount==None and self.album_name_from_copyphoto_enter.get!='' and self.album_name_copyphoto_to_enter.get()=='':

						self.PhotoAlbumIdToCopyTo=vkapi.photos.createAlbum(owner_id=person[0], title=title, privacy_view=self.PhotoPrivatesAlbum)['id']
					self.albumNameToCopyTo = self.PhotoPublicName + ' ' + self.TitlePhotoAlbumToCopyTo

					if type(self.PhotoAlbumIdToCopyFrom )==str:
						if self.PhotoLeftCount==None and self.PhotoProcessStatus==False:
							self.PhotoPublicIdToCopy=self.public_id_copyphoto_enter.get()
							self.PhotoOffset=0
							self.PhotoPostCounter=0
							self.CountPhotosToCopyFrom=int(self.count_photoalbums_enter.get())

					if type(self.PhotoAlbumIdToCopyFrom )==int:

						if self.PhotoProcessStatus==False and self.PhotoLeftCount: 
								
							self.photo_progressbar.configure(maximum=self.CountPhotosToCopyFrom)
							self.photo_progressbar.configure(value=self.CountPhotosToCopyFrom-self.PhotoLeftCount)
							threading.Thread(target=self.copyPhotoToAlbum, args=(person[0], self.PhotoFromId, self.albumNameToCopyTo, self.PhotoAlbumIdToCopyTo, self.PhotoAlbumIdToCopyFrom , self.CountPhotosToCopyFrom, self.PhotoOffset, False, False, None, None, self.PhotoCaptureTextState)).start()
						else:
							self.photoCounter=0
							self.PhotoOffset=0
							self.photo_progressbar.configure(maximum=self.CountPhotosToCopyFrom)
							self.photo_progressbar.configure(value=0)
							threading.Thread(target=self.copyPhotoToAlbum, args=(person[0], self.PhotoFromId, self.albumNameToCopyTo, self.PhotoAlbumIdToCopyTo, self.PhotoAlbumIdToCopyFrom , self.CountPhotosToCopyFrom, None, False, None, None, self.PhotoCaptureTextState)).start()
					else: 
						
						if self.PhotoLeftCount and self.PhotoProcessStatus==False: 
							self.photo_progressbar.configure(maximum=self.CountPhotosToCopyFrom)
							self.photo_progressbar.configure(value=self.CountPhotosToCopyFrom-self.PhotoLeftCount)
							threading.Thread(target=self.copyPhotoToAlbum2, args=(person[0], self.PhotoFromId, self.albumNameToCopyTo, self.PhotoAlbumIdToCopyFrom , self.CountPhotosToCopyFrom, None, None, self.PhotoOffset, False, False, self.PhotoAlbumIdToCopyTo, self.PhotoCaptureTextState)).start()
						else:
							self.photo_progressbar.configure(maximum=self.CountPhotosToCopyFrom)
							self.photo_progressbar.configure(value=0)
							threading.Thread(target=self.copyPhotoToAlbum2, args=(person[0], self.PhotoFromId, self.albumNameToCopyTo, self.PhotoAlbumIdToCopyFrom ,  self.CountPhotosToCopyFrom, False, None, None, None, False, self.PhotoAlbumIdToCopyTo, self.PhotoCaptureTextState)).start()
				else:
						tkinter.messagebox.showwarning("Copy photo warning", "You should stop the previous copying")

		def PhotoAlbumsDelete(self, event):
				items = self.photo_delete_albums_list.curselection()
				#print(len(self.photo_delete_albums_list.curselection()))
				#
				self.PhotoSelectedAlbumsToDelete=[]
				for i in range(len(items)):
					for y in  self.PhotoAlbumsToDelete:
						if y['number'] == int(re.findall('\d+', self.photo_delete_albums_list.get(items[i]))[0]):
							
							self.PhotoSelectedAlbumsToDelete.append(y['id'])
				#print(self.PhotoSelectedAlbumsToDelete)
				if self.PhotoSelectedAlbumsToDelete:
					message_result=tkinter.messagebox.askquestion('Delete photo albums' , 'Do you realy want to delete these photo albums?\n%s'%( str(self.PhotoSelectedAlbumsToDelete)))
					if message_result == 'yes':
						for i in self.PhotoSelectedAlbumsToDelete:
							vkapi.photos.deleteAlbum(owner_id=person[0], album_id=i)
							time.sleep(0.6)
						self.PhotoAlbumsToDelete=self.getAlbums(person[0], 'photo')
						self.photo_delete_albums_list.delete(0, END)
						for i in self.PhotoAlbumsToDelete:
							self.photo_delete_albums_list.insert(END, '%s. %s  count: %s' % (i['number'], re.search('[\w\s]+', i['title']).group(0), i['count']))
					elif message_result == 'no':
						print('canceled delete photo albums')
				else:
					tkinter.messagebox.showwarning('Delete photo albums', 'Select any albums')

		def copy_video(self, event):
				if self.copy_video_running==False:
					self.copy_video_running=True
					if type(self.VideoAlbumIdToCopyFrom) == str:
						if self.VideoProcessStatus==False and self.VideoLeftCount:
							self.video_progressbar.configure(maximum=self.CountVideosToCopyFrom)
							self.video_progressbar.configure(value=self.CountVideosToCopyFrom-self.VideoLeftCount)
							threading.Thread(target=self.copyVideo, args=(self.VideoFromId, self.CountVideosToCopyFrom, self.VideoAlbumIdToCopyFrom, self.VideoOffset, False,  None, None )).start() 
							#print(self.VideoFromId)
							#print(self.CountVideosToCopyFrom)
							#print(self.VideoAlbumIdToCopyFrom)
							#print(self.VideoOffset)
							#print(self.VideoLeftCount)
							#self, public_id, count, source, offset=None, captcha_send=False, captcha_sid=None, captcha_key=None
						else:
							self.CountVideosToCopyFrom=int(self.count_copyvideo_enter.get())
							self.VideoCounter=0
							self.VideoOffset=0
							self.VideoPostCounter=0
							self.video_progressbar.configure(maximum=self.CountVideosToCopyFrom)
							self.video_progressbar.configure(value=0)
							threading.Thread(target=self.copyVideo, args=(self.VideoFromId, self.CountVideosToCopyFrom, self.VideoAlbumIdToCopyFrom, None, False, None, None, self.VideoPrivatesAlbum)).start()
							#print(self.VideoFromId)
							#print(self.CountVideosToCopyFrom)
							#print(self.VideoAlbumIdToCopyFrom)
							#print(self.VideoOffset)
							#print(self.VideoLeftCount)
				else:
					tkinter.messagebox.showwarning("Copy video warning", "You should stop the previous copying")

		def CurSelet(self, event, param1, maction ):

			if param1=="list1":	
				selection=self.list1.curselection()
				selection = int(re.findall("[0-9]", self.list1.get(selection[0]))[0])
				if selection==3:
					self.selector=3
				elif selection==4:
					self.selector=4
				elif selection==6:
					self.selector=6
				elif selection is 7:
					self.selector = 7
				elif selection is 8:
					 self.selector = 8

				if self.selector==3:
					for i in self.frame2.winfo_children(): i.pack_forget()
					for i in self.superFrameInner1.winfo_children(): i.pack_forget()
					self.frame3.pack(side = LEFT, fill=Y)
					self.frame4.pack(side = LEFT, fill=Y)
					self.superFrameInner1.pack(side=LEFT, fill=BOTH)
					self.superFrame.pack(side=LEFT, fill=BOTH)
					if self.PhotoLeftCount:
						self.photo_progressbar['maximum'] = self.CountPhotosToCopyFrom
						self.photo_progressbar['value'] = self.CountPhotosToCopyFrom-self.PhotoLeftCount
						self.photo_progressbar_label.configure(text='%s of %s' % (self.PhotoLeftCount, self.CountPhotosToCopyFrom))
					self.options_label.pack()
					self.public_id_copyphoto_label.pack()
					self.public_id_copyphoto_enter.pack()
					self.album_id_copyphoto_from_label.pack()
					self.album_name_from_copyphoto_enter.pack()
					self.album_id_to_copyphoto_label.pack()
					self.album_name_copyphoto_to_enter.pack()
					self.new_album_copyphoto_label.pack()
					self.new_album_name_copyphoto_enter.pack()
					self.count_copyphoto_label.pack()
					self.count_photoalbums_enter.pack()
					self.create_photoalbum_label.pack()
					self.photo_radio_button_1.pack()
					self.photo_radio_button_2.pack()
					self.photo_copy_button.pack()
					self.test_photoalbum_link.pack()
					self.photo_reset_button.pack()
					self.photo_stop_button.pack()
					self.capture_copyphoto_text_label.pack()
					self.capture_copyphoto_text_radio_y.pack()
					self.capture_copyphoto_text_radio_n.pack()
					self.capture_copyphoto_text_radio_n.select()
					self.privates_photo_list.pack()
					self.photo_progressbar_label.pack()
					self.photo_progressbar.pack()
					if self.PhotoLeftCount: self.CurSelet('dd', 'load', False)

				elif self.selector==4:
					self.superFrame.pack_forget()
					#self.UnpuckPrevWidgetsLayout()
					for i in self.frame2.winfo_children(): i.pack_forget()
					for i in self.superFrameInner1.winfo_children(): i.pack_forget()
					self.frame3.pack(side = LEFT, fill=Y)
					self.frame4.pack(side = LEFT, fill=Y)
					self.superFrameInner1.pack(side=LEFT, fill=BOTH)
					self.superFrame.pack(side=LEFT, fill=BOTH)

					self.video_radio_button_1 = Radiobutton(self.frame2, text="Yes", value=1, variable=self.video_radiovar, command=self.VideoSelRadio, bg="#F7F7F7")
					self.video_radio_button_2 = Radiobutton(self.frame2, text="No", value=2, variable=self.video_radiovar, command=self.VideoSelRadio, bg="#F7F7F7")
					self.video_copy_button = Button(self.frame2, text="Copy videos", bg="#f7f7f7")
					self.video_copy_button.bind("<Button-1>", self.copy_video)
					self.test_videoalbum_link = Button(self.frame2, text='test link', bg="#f7f7f7")
					self.video_reset_button = Button(self.frame2, text='reset', command=self.resetSavePointVideo)
					self.video_stop_button = Button(self.frame2, text='stop', command=self.stopVideoCopy)
					self.privates_video_list = ttk.Combobox(self.frame2, values=[u"all", u"friends", u"nobody"])
					self.privates_video_list.bind("<<ComboboxSelected>>", self.get_video_privates_album)
					self.privates_video_list.set(u"nobody")
					self.video_progressbar_label = Label(self.frame2, text="0 of 0", bg="#f7f7f7")
					self.video_progressbar = ttk.Progressbar(self.frame2, orient ="horizontal", length = 150, value=0, maximum=500, mode ="determinate")

					if self.VideoLeftCount:
						self.video_progressbar['maximum'] = self.CountVideosToCopyFrom
						self.video_progressbar['value'] = self.CountVideosToCopyFrom-self.VideoLeftCount
						self.video_progressbar_label.configure(text='%s of %s' % (self.VideoLeftCount, self.CountVideosToCopyFrom))

					self.test_videoalbum_link.bind('<Button-1>', self.TestVideoAlbum)
					self.video_radio_button_2.select()
					self.options_label.pack()
					self.public_id_copyvideo_label.pack()
					self.public_id_copyvideo_enter.pack()
					self.album_id_copyvideo_from_label.pack()
					self.album_name_from_copyvideo_enter.pack()
					self.album_id_to_copyvideo_label.pack()
					self.album_name_copyvideo_to_enter.pack()
					self.new_album_copyvideo_label.pack()
					self.new_album_name_copyvideo_enter.pack()
					self.count_copyvideo_label.pack()
					self.count_copyvideo_enter.pack()
					self.create_videoalbum_label.pack()
					
					self.video_radio_button_1.pack()
					self.video_radio_button_2.pack()
					self.video_copy_button.pack()
					self.test_videoalbum_link.pack()
					self.video_reset_button.pack()
					self.video_stop_button.pack()
					self.privates_video_list.pack()
					self.video_progressbar_label.pack()
					self.video_progressbar.pack()
					if self.VideoLeftCount: self.CurSelet('dd', 'load', False)

				elif self.selector==6:
					self.superFrame.pack_forget()
					#for i in self.superFrame.winfo_children(): i.pack_forget()
					for i in self.frame2.winfo_children(): i.pack_forget()
					for i in self.superFrameInner1.winfo_children(): i.pack_forget()
					self.post_public_id_enter_label.pack()
					self.post_public_id_enter.pack()
					self.post_number_after_do_label.pack()
					self.post_number_after_do.pack()
					self.post_select_ptype_label.pack()
					self.post_select_ptype_y.pack()
					self.post_select_ptype_n.pack()
					self.post_textarea.pack()
					self.post_button_send.pack()
					self.post_button_send_stop.pack()
					self.superFrameInner1.pack(side=LEFT, fill=BOTH)
					self.superFrame.pack(side=LEFT, fill=BOTH)
				elif self.selector==7:

					self.superFrame.pack_forget()

					for i in self.frame2.winfo_children(): i.pack_forget()
					for i in self.superFrameInner1.winfo_children(): i.pack_forget()
					self.photo_albums_delete_button=Button(self.frame2, text="Delete albums")
					self.photo_albums_delete_button.bind("<Button-1>", self.PhotoAlbumsDelete)
					self.photo_albums_delete_button.pack()
					self.photo_delete_albums_list_label.pack(side=TOP)
					self.photo_delete_albums_list.pack(fill=BOTH, expand=True)
    				#mlb.pack(side='top', fill='both', expand=1)
					self.photo_delete_albums_list_wrap.pack(fill=BOTH, expand=True)
					self.superFrameInner1.pack(side=LEFT, fill=BOTH, expand=True)
					self.superFrame.pack(side=LEFT, fill=BOTH, expand=True)
					self.PhotoAlbumsToDelete=self.getAlbums(person[0], 'photo')
					self.photo_delete_albums_list.delete(0, END)
					for i in self.PhotoAlbumsToDelete:
						self.photo_delete_albums_list.insert(END, '%s. %s  count: %s' % (i['number'], re.search('[\w\s]+', i['title']).group(0), i['count']))

				elif self.selector == 8:
					if self.TumblrPhotoLeftCount:
						self.tumblr_copyphoto_progressbar.configure(maximum=self.TumblrPhotoCount)
						self.tumblr_copyphoto_progressbar['value']=self.TumblrPhotoCount-self.TumblrPhotoLeftCount

					self.superFrame.pack_forget()
					for i in self.frame2.winfo_children(): i.pack_forget()
					for i in self.superFrameInner1.winfo_children(): i.pack_forget()
					self.tumblr_copyphoto_albums_list_label.pack()
					self.tumblr_copyphoto_albums_list_wrap.pack(fill=BOTH, expand=True)
					self.tumblr_copyphoto_albums_list.pack(fill=BOTH, expand=True)
					self.superFrameInner1.pack(side=LEFT, fill=BOTH, expand=True)
					self.tumblr_copyphoto_blog_url_label.pack()
					self.tumblr_copyphoto_blog_url_enter.pack()
					self.tumblr_copyphoto_public_id_label.pack()
					self.tumblr_copyphoto_public_id_enter.pack()
					self.tumblr_copyphoto_album_id_to_label.pack()
					self.tumblr_copyphoto_album_id_to_enter.pack()
					self.tumblr_copyphoto_count_label.pack()
					self.tumblr_copyphoto_count_enter.pack()
					self.tumblr_copyphoto_tags_label.pack()
					self.tumblr_copyphoto_tags_enter.pack()
					self.tumblr_copyphoto_capture_text_label.pack()
					self.tumblr_copyphoto_capture_text_y.pack()
					self.tumblr_copyphoto_capture_text_n.pack()
					self.tumblr_copyphoto_copy_button.pack()
					self.tumblr_copyphoto_stopcopy_button.pack()
					self.tumblr_copyphoto_reset_button.pack()
					self.tumblr_copyphoto_fileformat_select.pack()
					self.tumblr_copyphoto_progressbar_label.pack()
					self.tumblr_copyphoto_progressbar.pack()
					self.superFrame.pack(side=LEFT, fill=BOTH, expand=True)
					self.TumblrPhotoAlbumsToCopyTo=self.getAlbums(person[0], 'photo')
					self.tumblr_copyphoto_albums_list.delete(0, END)
					for i in self.TumblrPhotoAlbumsToCopyTo:
						self.tumblr_copyphoto_albums_list.insert(END, '%s. %s  count: %s' % (i['number'], re.search('[\w\s]+', i['title']).group(0), i['count']))

			if param1=="load":
				self.list3.delete(0, END)
				self.list4.delete(0, END)
				if self.selector==3 and not maction:
					self.list3.insert(0, "----- wall -----" )
					self.list3.insert(0, "---- profile -----" )
					if self.public_id_copyphoto_enter.get() != '':
						self.PhotoFromId=int(self.public_id_copyphoto_enter.get())
						self.PhotoPublicName = vkapi.groups.getById(group_id=str(abs(self.PhotoFromId)))[0]['name']
						try:
							self.photoAlbumsToCopyFrom = self.getAlbums(int(self.public_id_copyphoto_enter.get()), "photo")
							for i in self.photoAlbumsToCopyFrom:
								self.list3.insert(END, str(i['number'])+'. '+re.search('[\w\s]+', i['title']).group(0))
						except vkerror as e:
							print('')
						self.photoAlbumsToCopyTo=self.getAlbums(person[0], 'photo')
						for i in self.photoAlbumsToCopyTo:
							self.list4.insert(END, str(i['number'])+'. '+re.search('[\w\s]+', i['title']).group(0))

				elif self.selector==4 and not maction:
					self.list3.insert(0, "----- wall -----")
					self.list3.insert(0, "---- videobox -----")
					if self.public_id_copyvideo_enter.get()!='':
						self.VideoFromId=int(self.public_id_copyvideo_enter.get())
						self.VideoPublicIdToCopy=self.VideoFromId
						self.VideoPublicName = vkapi.groups.getById(group_id=str(abs(self.VideoFromId)))[0]['name']
						self.VideoAlbumsToCopyFrom = self.getAlbums(int(self.public_id_copyvideo_enter.get()), "video")
						for i in self.VideoAlbumsToCopyFrom:
							self.list3.insert(END, str(i['number'])+'. '+re.search('[\w\s]+', i['title']).group(0))
						self.VideoAlbumsToCopyTo=self.getAlbums(person[0], 'video')
						for i in self.VideoAlbumsToCopyTo:
							self.list4.insert(END, str(i['number'])+'. '+re.search('[\w\s]+', i['title']).group(0))

			#OPTIONS 2
			if param1=="list3":
				
				if self.selector==3 and not maction:
					selection=self.list3.curselection()
					self.PhotoPublicIdToCopy=self.public_id_copyphoto_enter.get()
					# print(public_id_enter.get())
					# print(type(public_id_to_copy))
					if "wall" in self.list3.get(selection[0]):
						self.PhotoAlbumIdToCopyFrom =str
						self.PhotoAlbumIdToCopyFrom ="wall"
						self.album_name_from_copyphoto_enter.delete(0, END)
						self.album_name_from_copyphoto_enter.insert(END, str(self.PhotoAlbumIdToCopyFrom ))
						self.TitlePhotoAlbumToCopyTo='wall'
				
					else:
						selection=self.list3.curselection()
						self.selectedPhotoAlbumToCopyFrom=int(re.search("\d+", self.list3.get(selection[0])).group(0))
						if self.selectedPhotoAlbumToCopyFrom:
							for i in self.photoAlbumsToCopyFrom:
								if self.selectedPhotoAlbumToCopyFrom==i['number']:
									self.PhotoAlbumIdToCopyFrom  = i['id']
									self.CountPhotosToCopyFrom=i['count']
									self.TitlePhotoAlbumToCopyTo=i['title']
							self.album_name_from_copyphoto_enter.delete(0, END)
							self.album_name_from_copyphoto_enter.insert(END, str(self.PhotoAlbumIdToCopyFrom ))

				elif self.selector==4 and not maction:
					selection=self.list3.curselection()
					if "wall" in self.list3.get(selection[0]):
						self.VideoAlbumIdToCopyFrom =str
						self.VideoAlbumIdToCopyFrom ="wall"
						self.album_name_from_copyvideo_enter.delete(0, END)
						self.album_name_from_copyvideo_enter.insert(END, str(self.VideoAlbumIdToCopyFrom ))
						self.TitleVideoAlbumToCopyTo='wall'
					elif "videobox" in self.list3.get(selection[0]):
						self.VideoAlbumIdToCopyFrom =str
						self.VideoAlbumIdToCopyFrom ="videobox"
						self.album_name_from_copyvideo_enter.delete(0, END)
						self.album_name_from_copyvideo_enter.insert(END, str(self.VideoAlbumIdToCopyFrom ))
						self.TitleVideoAlbumToCopyTo='videobox'
					else:
						self.selectedVideoAlbumToCopyFrom=int(re.search("\d+", self.list3.get(selection[0])).group(0))
						if self.selectedVideoAlbumToCopyFrom:
							for i in self.VideoAlbumsToCopyFrom:
								if self.selectedVideoAlbumToCopyFrom==i['number']:
									self.VideoAlbumIdToCopyFrom  = i['id']
									self.CountVideosToCopyFrom=i['count']
									self.TitleVideoAlbumToCopyTo=i['title']
							self.album_name_from_copyvideo_enter.delete(0, END)
							self.album_name_from_copyvideo_enter.insert(END, str(self.VideoAlbumIdToCopyFrom ))
				elif self.selector==8:
					selection=self.tumblr_copyphoto_albums_list.curselection()
					self.tumblrSelectedPhotoAlbumToCopyTo=int(re.search("\d+", self.tumblr_copyphoto_albums_list.get(selection[0])).group(0))
					for i in self.TumblrPhotoAlbumsToCopyTo:
						if self.tumblrSelectedPhotoAlbumToCopyTo==i['number']:
							self.TumblrCopyPhotoAlbumId=i['id']
					self.tumblr_copyphoto_album_id_to_enter.delete(0, END)
					self.tumblr_copyphoto_album_id_to_enter.insert(END, str(self.TumblrCopyPhotoAlbumId))


				#elif self.selector==7:

					#selection=self.photo_delete_albums_list.curselection()
					#print(len(selection))
					#for i in range(len(selection)):
						#self.PhotoSelectedAlbumsToDelete=[]
						#self.PhotoSelectedAlbumsToDelete.append(self.photo_delete_albums_list.get(selection[i]))
					#print(int(re.search("\d+", self.photo_delete_albums_list.get(selection[0])).group(0)))
					#print(self.PhotoSelectedAlbumsToDelete)
						
			if param1=="list4":
				selection=self.list4.curselection()
				if self.selector==3 and not maction:
					self.selectedPhotoAlbumToCopyTo=int(re.search("\d+", self.list4.get(selection[0])).group(0))
					if self.selectedPhotoAlbumToCopyTo:
						for i in self.photoAlbumsToCopyTo:
							if self.selectedPhotoAlbumToCopyTo==i['number']:
								self.PhotoAlbumIdToCopyTo = i['id']
								self.CountPhotosToCopyTo=i['count']
								self.titleAlbumToCopyFrom=i['title']
						self.album_name_copyphoto_to_enter.delete(0, END)
						self.album_name_copyphoto_to_enter.insert(END, str(self.PhotoAlbumIdToCopyTo))	

				elif self.selector==4 and not maction:
					self.selectedVideoAlbumToCopyTo=int(re.search("\d+", self.list4.get(selection[0])).group(0))
					if self.selectedVideoAlbumToCopyTo:
						for i in self.VideoAlbumsToCopyTo:
							if self.selectedVideoAlbumToCopyTo==i['number']:
								self.VideoAlbumIdToCopyTo  = i['id']
								self.CountVideoToCopyTo=i['count']
								self.TitleVideoAlbumToCopyTo=i['title']
					self.album_name_copyvideo_to_enter.delete(0, END)
					self.album_name_copyvideo_to_enter.insert(END, str(self.VideoAlbumIdToCopyTo))



window=Tk()
my_app=myapp(window)
window.mainloop()		
	
