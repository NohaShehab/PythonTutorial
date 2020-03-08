
########tuples
# A tuple is a sequence of immutable Python objects. 
# Tuples are sequences, just like lists. 
# The differences between tuples and lists are, 
# the tuples cannot be changed unlike lists 
# tuples use parentheses, whereas lists use square brackets.
t = (1, "hi", True) 
print(t[1]) 

tup3 = "a", "b", "c", "d"
print(tup3)

# doesnot suppot item assigments
# t[1] = 4

#updating tubles 
# immutable which means you cannot update or change the values of tuple elements.
# You are able to take portions of existing tuples to create new tuples

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)


#delete from tuples 

tup = ('Python', 'django', 'flusk', 3 , 2020)
print (tup)
del tup
print ("After deleting tup : ")
# print (tup) #not defined 


#tuples operations
#List operations
#1-length 
print (len((1, 2, 3)))

#2- concatenation 
x=(1, 2, 3) + (4, 5, 6)
print(x)

#3- Repetition
y= ('Python!') * 4	
print(y)

#4- membership
print (3 in (1, 2, 3))  #true

#5- iteration 
for x in (1, 2, 3):
    print (x)

#6- min 
print(min((10, 20, 30)))

#7- max
print(max((10, 20, 30)))




