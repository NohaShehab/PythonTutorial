#dictionary 
# Each key is separated from its value by a colon (:), 
# the items are separated by commas, and the whole thing is enclosed in curly braces. 
# An empty dictionary without any items is written with just two curly braces, like this: {}.
# Keys are unique within a dictionary while values may not be. 
# The values of a dictionary can be of any type, 
# but the keys must be of an immutable data type such as strings, numbers, or tuples.


d = {"name": "Noha", "track": "Opensource"} 
print(d["name"])
print(d)

d["name"] = "Ali" 
print(d)

#dictionary functions 
print(d.keys()) #get keys
print (d.values()) #get values
print(d.items())  #get items

#looping
if "name" in d:  #check the key 
    print('yes')

if "noha" in d: #check the value  
    print ('yes')
else: 
    print('No')

d = {"name": "Noha", "track": "OS"} 
addedToD={ "track":"Python ", "branch": "Army"}  #value updated and key value updated
d.update(addedToD)
print(d)

#removes elements of dictionary 
d.clear()
print(d)  #d still exists but all values are removed 

