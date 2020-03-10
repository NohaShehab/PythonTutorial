#Exceptions in python 
#Exception causes
# 1- syntax error
# 2- logical error -لا يكلف الله نفساُ إلا وسعها :D -
# 3- runtime error --> exception 

# An exception is an event, which occurs during the execution of a program
# that disrupts the normal flow of the program's instructions. 
# In general, when a Python script encounters a situation that it cannot cope with, 
# it raises an exception. An exception is a Python object that represents an error.
# When a Python script raises an exception, 
# it must either handle the exception immediately otherwise it terminates and quits.

# print(name)
# Traceback (most recent call last):
#   File "g:\Python Army\day3_python\Exceptions.py", line 7, in <module>
#     print(name)
# NameError: name 'name' is not defined


# To handle exceptions
try:
    f=open("textfile.txt")
except Exception:
    print('Exception hereeeeeeeeeeeeeeeee')
    pass
else:
    #if no exception run the lines inside this block
    print('welcome')
finally: 
    # is considered as a cleanup action, 
    # this will be executed if there is exception or not
    print('I will be displayed always')




try:
    f=open("textfile.txt")
except Exception as e:
    # print('Sorry this file is not exist')
    print(e)


try:
    f=open("textfile.txt")
except FileNotFoundError as fe:
    # print('Sorry this file is not exist')
    print(fe)


#raising an exception -user defined exception-
def divNum(x,y):
    if y==0:
        raise ValueError ("Invalid division by!")
    else:
        z=x/y
        return z

print(divNum(5,4))
print(divNum(5,0))

# NameError