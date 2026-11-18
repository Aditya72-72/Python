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


#---------------Sequence Types-------------------#

#list - ordered, changeable, allows duplicate members
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))
print(thislist[1])

list1 = ["abc", 34, True, 40, "male"]

#adding item to list
list1.append("orange")
print(list1)

#removing item from list
list1.remove("male")
print(list1)

#replacing item or updating item
list1[1] = 45
print(list1)

#combining two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#max and min value in list
list1 = [1, 2, 3, 4, 5]
print(max(list1))
print(min(list1))

#looping in list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#looping through index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while looping in list
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


list2 = ["apple", "banana", "cherry", "apple", "cherry"]
print(list2[::4])

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

evens = [[x for x in range (1,21) if x%2==0]]
print(evens)  # Output: [[2, 4, 6, 8, 10, 12, 14, 16, 18,20]]

newlist = [x for x in range(10) if x < 7]
print(newlist)  # Output: [0, 1, 2, 3, 4, 5, 6]

#soritng list
list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list1.sort()    
print(list1)  

list2 = [100, 50, 65, 82, 23]
print(sorted(list2))  # Output: [23, 50, 65, 82, 100]

list3 = [10,90,50, 30, 70]
print (sorted(list3, reverse=True))  # Output: [90, 70, 50, 30, 10]




