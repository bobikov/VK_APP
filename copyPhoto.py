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
		getAlbumsTo = Comb.getAlbums('self', to_id)
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
		date1=[i['date'] for i in requests.get("https://api.vk.com/method/wall.get?owner_id="+str(from_id)+"&count=10&v=5.37&access_token="+accTok).json()['response']['items'] if 'is_pinned' not in i][0]
		# date2=[i['date'] for i in vkapi.photos.get('owner_id')]
		if albumIdToCopyFrom=='wall':
			Comb.UpdateData('self', from_id, date1, 'photo', 'wall')
		elif albumIdToCopyFrom!='wall':
			Comb.UpdateData('self', from_id, photosGet['response']['items'][0]['date'], 'photo', 'album', from_id)

		while step<countPhotos:
			step+=1
			if stop==True:
				break
			photosGet=requests.get("https://api.vk.com/method/wall.get?owner_id="+str(from_id)+"&count=1&offset="+str(step)+"&v=5.37&access_token="+accTok).json()
			for i in photosGet['response']['items'] :
				if 'is_pinned' not in i:
					print(i['date'])
					time.sleep(1)
					if text == True:
						if 'text' in i and i['text']!=None:
							if len(i['text'])>500:
								f = re.search("[\w\W]{500}", i['text'])
								text1=f.group(0)
							else:
								text1=i['text']
					if updateDate:
						if i['date']==updateDate:
							stop=True
					if 'attachments' in i:
						for a in i['attachments']:
							if a['type']=='photo':
								# st+=1
								# print(a['photo']['photo_604'],i['text']+'_'+str(st))

								if albumIdToCopyFrom!='wall' and a['text']!=None:
									text1=i['text'].replace(',','').replace('#','')	
								copyPhotos = requests.get("https://api.vk.com/method/photos.copy?owner_id="+str(from_id)+"&photo_id="+str(a['photo']['id'])+"&v=5.35&access_token="+accTok).json()
								if 'response' in copyPhotos and text1!=None:
									toFile.append({"id":copyPhotos['response'], "text":text1})
								# time.sleep(1)
								if 'error' in copyPhotos:
									print(copyPhotos)
									if copyPhotos['error']['error_code'] == 14:
										self.captchaSid=copyPhotos['error']['captcha_sid']
										# webbrowser.open_new_tab(copyPhotos['error']['captcha_img'])
										# self.captchaKey=input('enter captcha: ')
										self.captchaKey = Comb.captcha('self', copyPhotos['error']['captcha_img'])
										copyPhotos = requests.get("https://api.vk.com/method/photos.copy?owner_id="+str(from_id)+"&photo_id="+str(a['photo']['id'])+"&v=5.35&captcha_sid="+str(self.captchaSid)+"&captcha_key="+str(self.captchaKey)+"&access_token="+accTok).json()
										if 'response' in copyPhotos:
											movePhotos = requests.get("https://api.vk.com/method/photos.move?owner_id="+str(to_id)+"&target_album_id="+str(album_id[0])+"&photo_id="+str(copyPhotos['response'])+"&v=5.35&access_token="+accTok).json()
										# vkapi.photos.edit(owner_id=person[0], photo_id=copyPhotos['response'], caption=text1)
										time.sleep(0.5)
								if 'response' in copyPhotos:
									movePhotos = requests.get("https://api.vk.com/method/photos.move?owner_id="+str(to_id)+"&target_album_id="+str(album_id[0])+"&photo_id="+str(copyPhotos['response'])+"&v=5.35&access_token="+accTok).json()
								# vkapi.photos.edit(owner_id=person[0], photo_id=copyPhotos['response'], caption=text1)
								time.sleep(0.5)
								if text1!=None:
									with open("photoCaptions.json", "w") as jj:
										jj.write(json.dumps(toFile, indent=4, ensure_ascii=False))
			Comb.delPhotos('self')	



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
		getAlbumsTo = Comb.getAlbums('self', to_id)
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
		date1=[i['date'] for i in vkapi.wall.get(owner_id=from_id, count=10, v=5.44)['items'] if 'is_pinned' not in i][0]
		# date2=[i['date'] for i in vkapi.photos.get('owner_id')]
		if albumIdToCopyFrom=='wall':
			Comb.UpdateData('self', from_id, date1, 'photo', 'wall')
		elif albumIdToCopyFrom!='wall':
			Comb.UpdateData('self', from_id, photosGet['items'][0]['date'], 'photo', 'album', from_id)

		# while step<countPhotos:
			# step+=1
			# if stop==True:
				# break
			photosGet=vkapi.wall.get(owner_id=from_id, album_id='wall', count=1000, v=5.44)
			for i in photosGet['items'] :
				if 'is_pinned' not in i:
					# time.sleep(1)
					if text == True:
						if 'text' in i and i['text']!=None:
							if len(i['text'])>500:
								f = re.search("[\w\W]{500}", i['text'])
								text1=f.group(0)
							else:
								text1=i['text']
					if updateDate:
						if i['date']==updateDate:
							stop=True
					if 'attachments' in i:
						for a in i['attachments']:
							if a['type']=='photo':
								# st+=1
								# print(a['photo']['photo_604'],i['text']+'_'+str(st))
								if albumIdToCopyFrom!='wall' and a['text']!=None:
									text1=i['text'].replace(',','').replace('#','')
								try:
									copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['photo']['id'], v=5.44)
									print(copyPhotos)
									time.sleep(1)
									if  copyPhotos and text1!=None:
										toFile.append({"id":copyPhotos, "text":text1})
									movePhotos = vkapi.photos.move(owner_id=to_id, target_album_id=album_id[0], photo_id=copyPhotos, v=5.44)
									time.sleep(1)
									if text1!=None:
										with open("photoCaptions.json", "w") as jj:
											jj.write(json.dumps(toFile, indent=4, ensure_ascii=False))
								except vkerror as e:
									if e.is_access_token_incorrect:
										continue
									else:
									    captcha_img = e.captcha_img
									    captcha_sid = e.captcha_sid
									    captcha_key = Comb.captcha('self', captcha_img)
									    copyPhotos = vkapi.photos.copy(owner_id=from_id, photo_id=a['photo']['id'], captcha_key=captcha_key, captcha_sid=captcha_sid)
			# Comb.delPhotos('self')	