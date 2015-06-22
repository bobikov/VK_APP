#!/usr/local/bin/Python3
print("Content-type: text/html")
print()
import os
path="."
dirs = os.listdir(path)

for file in dirs:
 print (file + "<br>")