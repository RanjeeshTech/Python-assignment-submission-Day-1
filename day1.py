#Day 1 Assignment Python zero to hero

#1. Check the is operator on the float and string write your findings.
'''Answer: is and is not are the identity operators in Python.
           They are used to check if two values (or variables) are located on the same part
           of the memory. True if the operands are identical.
           https://onlinegdb.com/XqGikg6xZ'''


f1=2.03 #float 1 
f2=2.03 #float 2
f3=2.10 #float 3

print(f1 is f2)
print(f2 is f3)
print(f1 is not f3)

s1='Pythonisfun' #string 1
s2='Pythonisfun' #string 2
s3='Pythonisnotfun' #string 3

print(s1 is s2)
print(s2 is s3)
print(s1 is not s3)

#2. 1>3 >4 how to solve
'''Answer: By solving this we will get False
           https://onlinegdb.com/GV0QFjW1y'''

print(min(1,3) > 4)
print(1>3 > 4)


#3. Use int (), float () and str () function
'''Answer: These functions are used to convert a value from a particular datatype to a different datatype.
           https://onlinegdb.com/tADlo4Hb7'''

x = 10

y = float(x)
print(y)
print(type(y))

z = str(x)
print(z)
print(type(z))

integer = int(z)
print(integer)
print(type(integer))
