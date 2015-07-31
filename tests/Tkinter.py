#!/usr/local/bin/python3


import tkinter
from tkinter import *

root = Tk()
def inst():
	dis=0
	if dis==0:
		textbox.configure(state='normal')
		textbox.insert('1.0', 'ss')
		dis=1
		textbox.configure(state='disabled')
	elif dis==1:
		dis=0

		
	

root.title('VK Combain')
root.geometry('400x400+500+200')
root.resizable(False, False)
button1 = Button(root, text='Button1', command=inst).place(x=2, y=0)
button2 = Button(root, text='Button2').place(x=2, y=25)
textbox=Text(root, wrap='word', width=10, height=10)
textbox.place(x=80, y=0)
textbox.configure(state='disabled')
# textbox.insert('1.0', 'Hello\n')
# textbox.config(cursor='pointer')



# scrollbar=Scrollbar(textFrame)



root.mainloop()