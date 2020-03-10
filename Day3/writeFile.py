# Writring to files using write function 

fileObj= open('testfile.txt', 'w')
fileObj.write('I am writing using write function')


#seek 
fileObj.seek(50)
fileObj.write('I am written using seek')
fileObj.close()


#append 
fileObj= open('testfile.txt', 'a')
fileObj.write('\n I am appending to the file')





