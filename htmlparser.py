#!/usr/local/bin/python3
from html.parser import HTMLParser

class myparser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.count = 0

	def	handle_starttag(self, tag, attrs):
		if 'error' in attrs[0]:
			print(attrs)
			self.count = self.count + 1
pars = myparser()
pars.feed("<div class='error' style='border: 1px solid black'>123</div><div class='error'>123</div><div class='error'>123</div><div class='noerror'>123</div>")
print (pars.count)



