print("hello world")

# this is a comment
(print("Python1"))

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



  
