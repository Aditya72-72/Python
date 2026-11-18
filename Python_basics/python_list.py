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

#removing using pop() method
list1.pop(1)
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

evens = [[x*2 for x in range (1,11)]]
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

#copying list
list1 = ["apple", "banana", "cherry"]
newlistm= list1.copy()
print(newlistm)  # Output: ['apple', 'banana', 'cherry']

list1 = ["apple", "banana", "cherry"]
newlist = list(list1)
print(newlist)  # Output: ['apple', 'banana', 'cherry']

# joining list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # Output: ['a', 'b', 'c', 1, 2, 3]

#using for loop
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]

#using extend() method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]

#counting items in list
list1 = ["a", "b" , "c", "a", "b"]
x = list1.count("a")
print(x)  # Output: 2