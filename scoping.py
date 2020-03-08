#scoping in python 
# Global vs. Local variables
# Variables that are defined inside a function body have a local scope, 
# and those defined outside have a global scope.
# This means that local variables can be accessed only inside the function in which they are declared, 
# whereas global variables can be accessed throughout the program body by all functions.
#  When you call a function, the variables declared inside it are brought into scope.



#global 

name='Noha'
def outerFun():
    name='Shehab'

    def innerFunc():
        print(name)

    innerFunc()


outerFun()
print (name)


#global keyword

name='Ahmed'
def newOuterFun():
    global name
    name= 'Ali'

    def innerFunc():
        print(name)

    innerFunc()


newOuterFun()
print (name)


# nonlocal 
namee='Omar'
def outFun():
    namee='Noha'
    print(namee)

    def inFunc():
        nonlocal namee
        namee='Mostafa'
        print(namee) 

    inFunc()
    print(namee)


outFun()
print(namee) #see this


