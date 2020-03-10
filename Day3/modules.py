# A module allows you to logically organize your Python code. 
# Grouping related code into a module makes the code easier to understand and use. 
# A module is a Python object with arbitrarily named attributes that you can bind and reference.
# Simply, a module is a file consisting of Python code. 
# A module can define functions, classes and variables. A module can also include runnable code.


#to import a module you can use keyword import

import printModule
printModule.print_func('Called from medule')

#import specific block
from arithmenticModule import summ 
print(summ(5,10))

#import specific block and rename it 
from arithmenticModule import multiplyNums as mulFun
print(mulFun(5,10,10))

#packages 
from newPackage.arithmenticModule import multiplyNums as mull
print(mull(55,11,20))



