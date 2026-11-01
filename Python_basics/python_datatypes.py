##Data Types


#string

#printing string
print("Hello")

#slicing string
b = "Hello, World!"
print(b[2:7])

#slicing from start
b = "Hello, World!"
print(b[:8])

#slicing to end
b = "Hello, World!"
print(b[2:])

#negative indexing
b = "Hello, World!"
print(b[-5:-2])

#upper case indexing
a = "Hello, World!"
print(a.upper())

#lower case indexing
a = "Hello, World!"
print(a.lower())


#remove whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip())

#replace string
a = "Hello, World!"
print(a.replace("H", "J"))

#split string
a = "Hello, World!"
print(a.split("o"))

#concatination (adding string)
a= "Hello"
b= "World"
c= a + b
print(c)

a= "Hello"
b= "World"
c= a +" "+ b
print(c)

#escaping character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#length of string
x = "Hello World"
print(len(x))

#numeric

#integer - whole number
x = 5
print(x)

#float - deciamal number    
y = 5.5
print(y)

#complex - include imaginary numbers
z = 2 + 3j
print(z)