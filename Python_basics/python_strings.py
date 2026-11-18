##Data Types


#-------------string-------------------#

#printing string
print("Hello")

#slicing string
b = "Hello, World!"
print(b[2:7])

#slicing from start
b = "Hello, World!"
print(b[::8])

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

first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16

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

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

#placeholders
name = "John"
age = 36
print("My name is %s and I am %d" % (name, age))



#-------------numeric--------------------#

#integer - whole number
x = 5
print(x)

#float - deciamal number    
y = 5.5
print(y)

#complex - include imaginary numbers
z = 2 + 3j
print(z)









