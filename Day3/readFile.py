# Before you can read or write a file, you have to open it using Python's built-in open() function.
# This function creates a file object, 
# which would be utilized to call other support methods associated with it.
# open() returns a file object, and is most commonly used with two arguments: open(filename, mode).

fileObj = open("test.txt", "r")
print(fileObj)

#file info
print ("Name of the file: ", fileObj.name)
print ("Closed or not : ", fileObj.closed)
print ("Opening mode : ", fileObj.mode)

#read file
x=fileObj.read()
print(x)

#readline
# if you read before the file you need to open it again 
fileObj = open("test.txt", "r")
line=fileObj.readline()
print(line)


#readlines
fileObj = open("test.txt", "r")
line=fileObj.readlines()
print(line)

#looping along the lines 
fileObj = open("test.txt", "r")
for line in fileObj:
    print(line)

fileObj.close()