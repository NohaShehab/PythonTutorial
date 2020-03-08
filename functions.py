#functions
#to make your code generic, Don't ever never repeate your code.
#function is a way of scoping 
# A function is a block of organized, reusable code that is used to perform a single, 
# related action. 
# Functions provide better modularity for your application and a high degree of code reusing

# Rules to define a function in Python.
# Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
# Any input parameters or arguments should be placed within these parentheses. 
# You can also define parameters inside these parentheses.
# The first statement of a function can be an optional statement - the documentation string of the function or docstring.
# The code block within every function starts with a colon (:) and is indented.
# The statement return [expression] exits a function, optionally passing back an expression to the caller. 
# A return statement with no arguments is the same as return None.


#simple function 
def printMsg():
    print('Welcome to iti')

printMsg()
    

#function can accept parameter, No need to define its type  
def printVal(tempVal):
    print (tempVal) 

printVal(5)
printVal("Python")


#merge function with loops and conditions
def measureTemp (temp):
    if temp> 37:
        return 'too hot'
    elif temp<37:
        return 'Too cold'
    return 'normal'

print (measureTemp(37))

#passing parameters to a function by value or reference ?
# 
# All parameters (arguments) in the Python language are passed by reference. 
# It means if you change what a parameter refers to within a function,
#  the change also reflects back in the calling function. 


def changelist( mylist ):
   mylist.append([1,2,3,4])
   print ("Values inside the function: ", mylist)
   return

# Now you can call changelist function
mylist = [10,20,30]
changelist(mylist)
print ("Values outside the function: ", mylist)

    
#note 
def changeme( mylist ):
   mylist = [1,2,3,4] # This would assig new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


#function parameters 
# 1- order doesn't matter 
# 2- no specified data types
# 3- you can add default values


# 1-  define function with explicit parameter passing
def printinfo( name, age=100 ):
   print ("Name: ", name)
   print ("Age ", age)
   return
# Now you can call printinfo function
printinfo( age=27, name="Noha")
printinfo(name="layla")


def dosum(x, y=2, z=3):
    sum=x+y+z
    print(sum)

dosum(0,5)


#return statement 
# The statement return [expression] exits a function, 
# optionally passing back an expression to the caller. 
# A return statement with no arguments is the same as return None

def mulNum(x=1,y=1):
    return x*y

print (mulNum(5,5))
x=mulNum(5,7)
print(x)

#################### define function with implict parameter passing
def doSum2(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)

doSum2(5,6,11,22)
doSum2()

# another example 
def printNum( arg1, *vartuple ):
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
printNum( 10 )
printNum( 70, 60, 50 )
# printNum() 


#keywords ** in functions
# is used to pass a keyworded, variable-length argument list.
# We use the name kwargs with the double star. 
# The reason is because the double star allows us to pass through keyword arguments (and any number of them).
# A keyword argument is where you provide a name to the variable as you pass it into the function.
# One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.

def printWords(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
printWords(first ='Information', mid ='Technology', last='Institute')
printWords(name ='Noha', age ='27', dept='OS')


# use  args and **kwargs in calling functions

def printItems(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
      
# Now we can use *args or **kwargs to 
# pass arguments to this function :  
args = ("Information", "Technology", "Institute") 
printItems(*args) 
  
kwargs = {"arg1" : "Noha", "arg2" : "Engineering", "arg3" : "Open source"} 
printItems(**kwargs)


#kwargs is just a varible identifier 
def printfun(**kwargs):
    for k in kwargs:
        print (kwargs[k])

printfun(x=5, y=7)

    
