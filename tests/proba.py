from tkinter import *
import tkinter.messagebox
from urllib.request import urlopen
import base64
from PIL import Image
from PIL import ImageTk
import io
import time
import threading


# This function gets called by our thread.. so it basically becomes the thread innit..                    
def wait_for_event(e):
    while True:
        print ('\tTHREAD: This is the thread speaking, we are Waiting for event to start..')
        event_is_set = e.wait()
        print ('\tTHREAD:  WHOOOOOO HOOOO WE GOT A SIGNAL  : %s', event_is_set)
        e.clear()

# Main code.. 
e = threading.Event()
t = threading.Thread(name='your_mum', 
                     target=wait_for_event,
                     args=(e,))
t.start()

while True:
    print ('MAIN LOOP: still in the main loop..')
    time.sleep(4)
    print ('MAIN LOOP: I just set the flag..')
    e.set()
    print ('MAIN LOOP: now Im gonna do some processing n shi-t')
    time.sleep(4)
    print ('MAIN LOOP:  .. some more procesing im doing   yeahhhh')
    time.sleep(4)
    print ('MAIN LOOP: ok ready, soon we will repeat the loop..')
    time.sleep(2)
# key = int

# running = True  # Global flag

# def scanning():
#     if running:  # Only do this if the Stop button has not been clicked
#         print ("hello")

#     # After 1 second, call scanning again (create a recursive loop)
#     root.after(1000, scanning)
#     # time.sleep(1)


# def start():
#     """Enable scanning by setting the global flag to True."""
#     global running
#     running = True

# def stop():
#     """Stop scanning by setting the global flag to False."""
#     global running
#     running = False

# root = Tk()
# root.title("Title")
# root.geometry("500x500")

# app = Frame(root)
# app.grid()

# start = Button(app, text="Start Scan", command=start)
# stop = Button(app, text="Stop", command=stop)

# start.grid()
# stop.grid()

# root.after(1000, scanning)  # After 1 second, call scanning
# root.mainloop()