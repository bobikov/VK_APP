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
other = [-72580409, -61330688]
person = [179349317]
app_id = 5040349
accTok = 'f98576da13f80eb5b3ab0949e1527ef48c9da72155005b7140362908471415d707eecb765bea05aa2852f'
supercitat = []
end = 0
key=str

running=True


group_ids = [-60409637, -72580409]
group_Ids_ToString = str.join(',', [str(abs(x)) for x in group_ids])
groupsNoDumps = vkapi.groups.getById(group_ids=group_Ids_ToString, indent=4, sort_keys=True, ensure_ascii=False)
groupsWithDumps = json.dumps(vkapi.groups.getById(group_ids=group_Ids_ToString),indent=4, sort_keys=True, ensure_ascii=False)
group_names = [i['name'] for i in json.loads(groupsWithDumps)]
group_screen_names=[i['screen_name'] for i in json.loads(groupsWithDumps)]
dict_names_and_ids=[];
actions_list = ['Multi-post', 'Download photos', 'Copy photos', 'Comments Bot', 'Get text from wall', 'Cross delete posts', 'Delete from board', 'Messages Bot', 'Delete photos', 'Likes', 'wheather test', 'test tkinter', 'Upload owner photo', 'Status change', 'Get Videos', 'equake', 'Copy docs', 'Download docs', 'get subscriptions', 'Friends Add', 'Get Fires', 'Get Artists', 'Set Photos captions', 'Copy Audio', 'Copy video', 'Get groups', 'Delete video album', 'Delete audio album']
for i,x,y in zip(group_names, group_ids, group_screen_names):
		dict_names_and_ids.append({'name':i, 'id':x, 'screen_name':y})

	
def delPhotos():
	photos = vkapi.photos.get(owner_id=person[0], album_id='saved')['items']
	for i in photos:
		vkapi.photos.delete(owner_id=person[0], photo_id=i['id'])
		time.sleep(0.4)

def getAlbums(public_id):
	titles = []
	ids= []
	albums = vkapi.photos.getAlbums( owner_id = public_id)['items']
	for y,i in zip(range(len(albums)), albums):
		ids.append(dict(number=y+1, id=i['id'], title=i['title'], count=i['size']))
	return ids




def actions():

	copy_photos=False
	copy_videos=False
	photoAlbumsToCopyFrom=[]
	photoAlbumsToCopyTo=[]
	titleAlbumToCopyTo=str
	countPhotosToCopyTo=int
	publicName=str
	titleAlbumToCopyTo=str
	albumIdToCopyFrom = int
	countPhotosToCopyFrom=int
	countPhotosToCopyTo=int
	albumIdToCopyTo=int
	titleAlbumToCopyTo=str
	fromId=int
	create_photo_album_state=int
	public_id_to_copy=str

	
	def CurSelet( event, param1, maction ):
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
		def download_captcha(url):
			readurl = urlopen(url).read()
			with open("captcha.png", 'wb') as captcha:
				captcha.write(readurl)

		def test_album(event):
			webbrowser.open_new("https://vk.com/album%s_%s"%(public_id_to_copy, albumIdToCopyFrom))

		def selradio():
			nonlocal create_photo_album_state
			create_photo_album_state=radiovar.get()

		def copyphoto(event):
			title = publicName+' '+titleAlbumToCopyTo
			vkapi.photos.createAlbum(owner_id=person[0], title=title, privacy_view='nobody')
			albumNameToCopyTo = publicName+' '+titleAlbumToCopyTo
			if type(albumIdToCopyFrom)==str:
				nonlocal countPhotosToCopyFrom
				countPhotosToCopyFrom=int(count_palbums_enter.get())
				print(countPhotosToCopyFrom)
			if type(albumIdToCopyFrom)==int:
				pb.configure(maximum=countPhotosToCopyFrom)
				pb.configure(value=0)

				def copyPhotoToAlbum(to_id, from_id, albumNameToCopyTo, albumIdToCopyFrom, countPhotos, text=False):
					album_id = []
					photo_id = []
					albumsFromIds = []
					photosToCopy = []
					updateDate=int
					text1=str
					toFile=[]
					# getAlbumsFromId = Comb.getAlbums('self', from_id)
					step=-100
					getAlbumsTo = getAlbums(to_id)
					if albumIdToCopyFrom=='wall':
						rev = 1
						source='wall'
					else:
						rev = 0
						source='album'
					for i in getAlbumsTo:
						if i['title'] == albumNameToCopyTo:
							album_id.append(i['id'])
					if countPhotos>1000:
						while step<countPhotos:
							step+=100
							try:
								photosGet=vkapi.photos.get(owner_id=from_id, album_id=albumIdToCopyFrom, count=100, offset=step, rev=rev)
								for a in photosGet['items']:
									copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'])
									movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
									time.sleep(1)
							except vkerror as e:
								captcha_sid=e['sid']
								captcha_key=e['key']
								copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'], captcha_sid=captcha_sid, captcha_key=captcha_key)
								movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
								time.sleep(1)
					else:
						photosGet=vkapi.photos.get(owner_id=from_id, album_id=albumIdToCopyFrom, extended=1, count=countPhotos, rev=rev)
						for a in photosGet['items']:
							try:
								pb['value']+=1
								# print(countPhotos)
								copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'])
								movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
								time.sleep(1)
							except vkerror as e:
								download_captcha(e.captcha_img)
								captcha_key=captcha()
								captcha_sid=e.captcha_sid
								copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['id'], captcha_sid=captcha_sid, captcha_key=captcha_key)
								movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)		
								time.sleep(1)
				threading.Thread(target=copyPhotoToAlbum, args=(person[0], fromId, albumNameToCopyTo, albumIdToCopyFrom, countPhotosToCopyFrom, False)).start()
				# copyPhotoToAlbum(person[0], fromId, albumNameToCopyTo, albumIdToCopyFrom, countPhotosToCopyFrom, False)	
			else: 
				def copyPhotoToAlbum2(to_id, from_id, albumNameToCopyTo, albumIdToCopyFrom, countPhotos, text=False):
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
					getAlbumsTo = getAlbums(to_id)
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
						UpdateData('self', from_id, date1, 'photo', 'wall')
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
											download_captcha(e.captcha_img)
											captcha_sid=e.captcha_sid
											captcha_key=captcha()
											copyPhotos = vkapi.photos.copy(owner_id=a['photo']['owner_id'], photo_id=a['photo']['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)

											print(copyPhotos)
											movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos)
											time.sleep(1)
										if text==True:
											with open("photoCaptions.json", "w") as jj:
												jj.write(json.dumps(toFile, indent=4, ensure_ascii=False))
				# threading.Thread(target=copyPhotoToAlbum2, args=(person[0], fromId, albumNameToCopyTo, albumIdToCopyFrom, countPhotosToCopyFrom, True)).start()
				copyPhotoToAlbum2(person[0], fromId, albumNameToCopyTo, albumIdToCopyFrom, countPhotosToCopyFrom, True)
		if param1=="list1":	
			selection=list1.curselection()
			# action=int(re.search("\d+", list1.get(selection[0])).group(0))
			# list2.delete(0, END)

			for i in frame2.winfo_children(): i.pack_forget()
			if re.search("3", list1.get(selection[0])).group(0) and maction:
				if len(frame2.winfo_children())<15:
					rdb1=Radiobutton(frame2, text="Yes", value=1, variable=radiovar, command=selradio, bg="#F7F7F7")
					rdb2=Radiobutton(frame2, text="No", value=2, variable=radiovar, command=selradio, bg="#F7F7F7")
					cbut_photo=Button(frame2, text="Copy", bg="#f7f7f7").bind("<Button-1>", copyphoto)
					link=Button(frame2, text='test ink', bg="#f7f7f7")
					pb = ttk.Progressbar(frame2, orient ="horizontal", length = 150, value=0, maximum=500, mode ="determinate")
					pb.pack()
					link.bind('<Button-1>', test_album)
					rdb2.select()
				for i in frame2.winfo_children(): i.pack()
				
				nonlocal copy_photos
				copy_photos=True
				# sources = [{'number':1, 'title':'Albums'}, {'number':2,'title':'Wall'}];
				# for i in sources:
				# 	list2.insert(END, str(i['number'])+'. '+i['title'])
		if param1=="load":
			list3.delete(0, END)
			list4.delete(0, END)
			list3.insert(0, "----- wall -----")
			list3.insert(0, "---- profile -----")
			if copy_photos and not maction:
				if public_id_enter.get() != '':
					nonlocal fromId
					fromId=int(public_id_enter.get())
					nonlocal publicName
					publicName = vkapi.groups.getById(group_id=str(abs(fromId)))[0]['name']
					nonlocal photoAlbumsToCopyFrom
					nonlocal photoAlbumsToCopyTo
					photoAlbumsToCopyFrom = getAlbums(int(public_id_enter.get()))
					for i in photoAlbumsToCopyFrom:
						list3.insert(END, str(i['number'])+'. '+re.search('[\w\s]+', i['title']).group(0))
					photoAlbumsToCopyTo= getAlbums(person[0])
					for i in photoAlbumsToCopyTo:
						list4.insert(END, str(i['number'])+'. '+re.search('[\w\s]+', i['title']).group(0))
		#OPTIONS 2
		if param1=="list3":
			selection=list3.curselection()
			if copy_photos and not maction:
				nonlocal public_id_to_copy
				public_id_to_copy=public_id_enter.get()
				# print(public_id_enter.get())
				# print(type(public_id_to_copy))
				nonlocal albumIdToCopyFrom
				nonlocal countPhotosToCopyFrom
				nonlocal titleAlbumToCopyTo
				if "wall" in list3.get(selection[0]):
					albumIdToCopyFrom=str
					albumIdToCopyFrom="wall"
					album_name_from.delete(0, END)
					album_name_from.insert(END, str(albumIdToCopyFrom))
					titleAlbumToCopyTo='wall'
				else:
					selectedAlbumToCopyFrom=int(re.search("\d+", list3.get(selection[0])).group(0))
					if selectedAlbumToCopyFrom:
						for i in photoAlbumsToCopyFrom:
							if selectedAlbumToCopyFrom==i['number']:
								albumIdToCopyFrom = i['id']
								countPhotosToCopyFrom=i['count']
								titleAlbumToCopyTo=i['title']
						album_name_from.delete(0, END)
						album_name_from.insert(END, str(albumIdToCopyFrom))
				

					
		if param1=="list4":
			selection=list4.curselection()
			if copy_photos and not maction:
				nonlocal albumIdToCopyTo
				selectedAlbumToCopyTo=int(re.search("\d+", list4.get(selection[0])).group(0))
				if selectedAlbumToCopyTo:

					for i in photoAlbumsToCopyTo:
						if selectedAlbumToCopyTo==i['number']:
							albumIdToCopyTo = i['id']
							countPhotosToCopyTo=i['count']
							titleAlbumToCopyFrom=i['title']
					album_name_to.delete(0, END)
					album_name_to.insert(END, str(albumIdToCopyTo))	
				
	window=Tk()
	radiovar=IntVar()
	window.geometry("1000x800+300+0")
	image = ImageTk.PhotoImage(Image.open("captcha.png"))
	def captcha():
		def restarttimer():
			window2.destroy()

		def getKey(event):
			global key
			key = e1.get()
			print(key)
			global running
			running=True
			window2.destroy()
		window2 = Toplevel(window)
		window2.geometry("200x200+600+200")
		window2.bind('<Return>', getKey)
		window2.title('Captcha')
		label=Label(window2, image=image).pack()
		e1=Entry(window2)
		e1.pack(side=TOP)
		e1.focus_set()
		button1 = Button(window2, text='Send')
		button1.bind('<Button-1>', getKey)
		button1.pack(side=TOP)
		# window2.protocol("WM_DELETE_WINDOW", restarttimer)
		# window2.call('wm', 'attributes', '.', '-topmost', True)                            
		return key
	# top.title("About this application...")
	frame1=Frame(window, height=2, bg='#F7F7F7', bd=1,  padx=5, pady=5, relief=SUNKEN)
	frame2=Frame(window, height=2, bg='#F7F7F7', bd=1,  padx=5, pady=5, relief=SUNKEN)
	frame3=Frame(window, height=2, bg='#F7F7F7', bd=1,  padx=5, pady=5, relief=SUNKEN)
	frame4=Frame(window, height=2, bg='#F7F7F7', bd=1,  padx=5, pady=5, relief=SUNKEN)
	frame1.pack(side=LEFT, fill=Y)
	frame2.pack(side=LEFT, fill=Y)
	frame3.pack(side=LEFT, fill=Y)
	frame4.pack(side=LEFT, fill=Y)
	actions_label=Label(frame1, text="Action:", bg="#f7f7f7")
	actions_label.pack()
	label=Label(frame2, text="Options:", bg="#f7f7f7")
	list1=Listbox(frame1, height=400, bd=0)
	label=Label(frame3, text="From album:", bg="#f7f7f7" )
	label.pack()
	list3=Listbox(frame3, height=400, width=50, bd=0)
	label=Label(frame4, text="To album:", bg="#f7f7f7")
	label.pack()
	list4=Listbox(frame4, height=400, width=70, bd=0)
	label=Label(frame2, text="Public Id:", bg="#f7f7f7")
	public_id_enter=Entry(frame2)
	label=Label(frame2, text="AlbumID from copy: ", bg="#f7f7f7")
	album_name_from=Entry(frame2)
	label=Label(frame2, text="AlbumID to copy:", bg="#f7f7f7")
	album_name_to=Entry(frame2)
	label=Label(frame2, text='New album title:', bg='#f7f7f7')
	new_album_name_enter=Entry(frame2)
	label=Label(frame2, text="count", bg='#f7f7f7')
	count_palbums_enter=Entry(frame2)
	label=Label(frame2, text="Create album:", bg="#f7f7f7")
	
	for i,y in zip(range(len(actions_list)), actions_list):
		if i == 0:
			list1.insert(END, str(1)+'. '+actions_list[0])
			# print(str(1)+'.', actions[0])
		else:
			# print(str(i+1)+'.', y)
			list1.insert(END, str(i+1)+'. '+y)

	list1.bind('<<ListboxSelect>>', functools.partial(CurSelet, param1="list1", maction=True))
	list3.bind('<<ListboxSelect>>', functools.partial(CurSelet, param1="list3", maction=False))
	list4.bind('<<ListboxSelect>>', functools.partial(CurSelet, param1="list4", maction=False))
	window.bind("<Return>", functools.partial(CurSelet, param1="load", maction=False))
	list1.pack()
	list3.pack()
	list4.pack()
	# window.call('wm', 'attributes', '.', '-topmost', True) 
	window.mainloop()		
if __name__ == "__main__":
		actions()
	
