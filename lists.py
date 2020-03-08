# ####################lists

# The most basic data structure in Python is the sequence. 
# Each element of a sequence is assigned a number - its position or index. 
# The first index is zero, the second index is one, and so forth.
# Python has six built-in types of sequences, 
# but the most common ones are lists and tuples.
# The list is a most versatile datatype available in 
# Python which can be written as a list of comma-separated values (items) between square brackets. 
# Important thing about a list is that items in a list need not be of the same type.


newlist=[]
newlist=['welcome', 455.55, True]
print(newlist[0])


myList = ["C", "JavaScript", "Python", "Java", "php"]
print (myList)

#pop
myList.pop(4)
print (myList)
myList.pop(2)
print (myList)

#append adds at the end of the list 
myList.append('hi')
print(myList)

#insert at certain index
myList.insert(3, "Scala")
print(myList)

#remove certain item
myList.remove('hi')
print(myList)

#extend the list add item to it 
yourList = ["Ruby", "Rust"]
myList.extend(yourList)
print(myList)


#List operations
#1-length 
print (len([1, 2, 3]))

#2- concatenation 
x=[1, 2, 3] + [4, 5, 6]	
print(x)

#3- Repetition
y= ['Python!'] * 4	
print(y)

#4- membership
print (3 in [1, 2, 3])  #true

#5- iteration 
for x in [1, 2, 3]:
    print (x)

#6- min 
print(min([10, 20, 30]))

#7- max
print(max([10, 20, 30]))
