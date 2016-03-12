from oauth2client.client import flow_from_clientsecrets
# import requests
import webbrowser
import multiprocessing
import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
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
import smtplib
import time
storage = Storage('a_credentials_file')
credentials =storage.get()

flow = flow_from_clientsecrets('./client_secret.json',
                               scope='https://www.googleapis.com/auth/cse',
                               redirect_uri='http://localhost/auth')
# auth_uri = flow.step1_get_authorize_url()
# webbrowser.open_new(auth_uri)
# code=input('Enter code: ')
# credentials = flow.step2_exchange(code)

http=httplib2.Http()
http=credentials.authorize(http)
service = build('customsearch', 'v1', http=http)
# storage = Storage('a_credentials_file')
# storage.put(credentials)
i=0
while i < len(range(100)):
    i+=10
    # print(i)
    res = service.cse().list(q='инфографика аргументы и факты',  gl='ru',  searchType='image',, num=10, start=i,  safe='off', cx='017774293269012910926:g4hh4a422po').execute()
    time.sleep(1)
    # print(res)
    for a in res['items']:
        print(a['link'])


# import multiprocessing, time, signal
# class myapp():
#     def __init__(self):
#         self.p = multiprocessing.Process(target=self.printer)
#         self.start()
#         # self.printer()
#     def printer(self):
#         step=glgl
#         # print(self.p.is_alive())
#         while step<10:
#             step+=1
#             print(self.p.is_alive())
#             if step==5:
                
#                 # self.p.terminate()
#                 # print(self.p.is_alive())
#                 break
#             time.sleep(1)
#     def start(self):
#         self.p.start()
# app=myapp()


# sender = 'hal3007@yandex.com'
# receivers = ['kostyabobikov@gmail.com']

# message = """From: %s  <%s>
# To: %s <%s>
# Subject: SMTP e-mail test

# This is a test e-mail message.
# """ % (sender, sender, receivers, receivers)

# try:
#    smtpObj = smtplib.SMTP('smtp.yandex.com:587')
  
#    smtpObj.ehlo()
#    smtpObj.starttls()
#    smtpObj.login("hal3007", "Lvq7xidjNP8xyv", initial_response_ok=True)
#    smtpObj.sendmail(sender, receivers, message)         
#    print ("Successfully sent email")
# except smtplib.SMTPException as e:
#    # print ("Error: unable to send email")
#    print(e)


