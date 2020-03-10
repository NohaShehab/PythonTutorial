# Module Regular Expressions(RE) specifies a set of strings(pattern)
#  that matches it.

import re

p = re.compile('[a-j]') 
#this creates a regular expression that contains letters from a to e
tst="welcome to iti, Python Day3, RE module"
#findAll will return with a list of the founded letters within the pattern
print(p.findall(tst)) 


#match function to check if the input match the pattern or not 
# from its starting
pattern = re.compile("o")  
print(pattern.match("dog"))

pattern = re.compile("d")  
if pattern.match("dog"):
   print('matched')


pattern = re.compile("o[gh]")
if pattern.fullmatch("dog"): 
   print('Yess')








