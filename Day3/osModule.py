# The OS module in python provides functions for interacting with the operating system. 
# OS, comes under Python’s standard utility modules. 
# This module provides a portable way of using operating system dependent functionality. 
# The *os* and *os.path* modules include many functions to interact with the file system.

import os

#get the operating system dependent module
print(os.name)

#get working directory
print(os.getcwd())

#os.error
try:
    file=open('xyz.txt','r')
except FileNotFoundError as e:
    print(os.error)
    # print(e)


#open file using os
# popen() is similar to open() 
# # popen() provides a pipe/gateway and accesses the file directly 
#
fileName="ABC.txt"
file1 =os.popen(fileName, 'w') 
file1.write("Helloooooo") 
file1.close() 
# Why this block throws error!
#

##

# and this no?
fd = "GFG.txt"
file = open(fd, 'w') 
file.write("Hellooooooooooooooo") 
file.close() 
file = open(fd, 'r') 
text = file.read() 
print(text) 
## 




    
