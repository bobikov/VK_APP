# from oauth2client.client import flow_from_clientsecrets
# import requests
import webbrowser
# import httplib2
# from apiclient.discovery import build
# from oauth2client.file import Storage
from tumblpy import Tumblpy
from urllib.request import urlopen
import requests
import vk
import re
from html.parser import HTMLParser
from bs4.dammit import EntitySubstitution
import wget
htmlparser=HTMLParser()
esub=EntitySubstitution()
# storage = Storage('a_credentials_file')
# credentials =storage.get()

# flow = flow_from_clientsecrets('./client_secret.json',
#                                scope='https://www.googleapis.com/auth/cse',
#                                redirect_uri='http://localhost/auth')
# auth_uri = flow.step1_get_authorize_url()
# webbrowser.open_new(auth_uri)
# code=input('Enter code: ')
# credentials = flow.step2_exchange(code)

# http=httplib2.Http()
# http=credentials.authorize(http)
# service = build('customsearch', 'v1', http=http)
# # storage = Storage('a_credentials_file')
# # storage.put(credentials)
# res = service.cse().list(q='ancient sex', searchType='image', num=10, start=20, imgType='photo', imgSize='large', safe='off', cx='017774293269012910926:g4hh4a422po').execute()
# for i in res['items']:
#     print(i['link'])
s="Hello &amp; &laquo"


unsubbed = htmlparser.unescape(s)
print(unsubbed)



