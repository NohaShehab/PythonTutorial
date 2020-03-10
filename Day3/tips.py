# with statement in Python is used in exception handling 
# to make the code cleaner and much more readable.
# It simplifies the management of common resources like file streams.

#simple opening for a file for reading 
file = open('xfile', 'w') 
file.write('Hello world !') 
file.close() 
  
# More professionall way 
file = open('xfile2', 'w') 
try: 
    file.write('Hello world') 
except FileNotFoundError as e:
    print(e)
finally: 
    file.close() 

#with With keyword no need to add the try block and even f.close()
with open('file_path', 'w') as file: 
    file.write('Hello world !') 


# List comprehension is an elegant way to define and create list in python. 
# We can create lists just like mathematical statements and in one line 

even_square = [] 
for x in range(1, 11): 
    if x % 2 == 0: 
        even_square.append(x**2) 

print (even_square) 

# This can be implemented in one line
even_square = [x ** 2 for x in range(1, 11) if x % 2 == 0] 
print (even_square) 

noprimes = [j for i in range(2, 50) for j in range(i*2, 50, i)] 
print(noprimes)
primes = [x for x in range(2, 50) if x not in noprimes] 
print (primes) 



##Any 
# Any and All are two built ins provided in python used for successive And/Or.
# Any Returns true if any of the items is True. 
# It returns False if empty or all are false. 
# Any can be thought of as a sequence of OR operations on the provided iterables.
# It short circuit the execution i.e. stop the execution as soon as the result is known.
# Syntax : any(list of iterables)
L = [0,5,9,7,8]
print(any(L))


#All
# Returns true if all of the items are True (or if the iterable is empty).
# All can be thought of as a sequence of AND operations on the provided iterables. 
# It also short circuit the execution i.e. stop the execution as soon as the result is known.
# Syntax : all(list of iterables)
print(all(L))

