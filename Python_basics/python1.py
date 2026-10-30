print("hello world")

# this is a comment
(print("Python1"))

#f-string
name = "John"
age = 36
print(f"My name is {name} and I am {age}")

#multiple lines printing
#a (""")

print(""" 
line 1= python
line 2= is
line 3= awesome
""")

#b new line function (\n)

print("line 1= python\nline 2= is\nline 3= awesome")

#variables
X= "john"
y = 15

print(X)
print(y)

#casting

a= str(3)
b= int(4)
c= float(5)

print(a)
print(b)
print(c)

#type
print(type(a))
print(type(b))
print(type(c))

# Multiple values 

x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)

x= y= z = "orange"
print(x)

##variables 

A= "Python is awesome"
print("This is " + A)

#Global variables
x = "awesome"

def myfunc():
  print("Python is " + x)   

myfunc()

#Local variables
x= "awesome"
def myfunc():  
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)


#global keyword

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)

