#1- shorthand if 

age = 15
print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')


# 2-Swap
#traditional way
x=4
y=5
temp=x
x=y
y=temp
print(x)
print(y)

#python way
x,y=3,4
x,y=y,x
print(x, y)


#joins
print(":".join(["1","Ali","grp"]))
print("a".join(["1","Ali","grp"]))

#splits
print("Noha Shehab".split(' '))
print("Noha:Shehab".split(':'))

#Compare
print(True == 1)
print(True is 1)
print(1 == True)

#is vs ==
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2)
print(list1 is list2) #compare ref and values

list1 =list3= [1,2,3]
print(list1 == list3)
print(list1 is list3)


##### Packing and unpacking
l = [1,13,3,7] 
a,b,c,d = l
print(a,b,c,d)
print(b)


### Enumes
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
# This enumerate object can then be used directly in for loops or be converted into a list of tuples
# using list() method.

lang=["Arabic", "English", "Frensh"]
for i, l in enumerate(lang):
    print("Element value ", l,)
    print("Element index ", i)

L = [0,5,9,7,8]


## all and any 

##Any 
# Any and All are two built ins provided in python used for successive And/Or.
# Any Returns true if any of the items is True. 
# It returns False if empty or all are false. 
# Any can be thought of as a sequence of OR operations on the provided iterables.
# It short circuit the execution i.e. stop the execution as soon as the result is known.
# Syntax : any(list of iterables)
print(any(L))


#All
# Returns true if all of the items are True (or if the iterable is empty).
# All can be thought of as a sequence of AND operations on the provided iterables. 
# It also short circuit the execution i.e. stop the execution as soon as the result is known.
# Syntax : all(list of iterables)
print(all(L))

print(type(lang))


