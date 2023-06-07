# name = "Beau"
# print(isinstance(name, str))

# number = "20"
# age = int(number)
# print(isinstance(age, int))

# items = ["Dog","Ceasar", "Migo", "luca"]
# print(sorted(items, key=str.lower))
# print(items)

#tuple   ****************************
# names = ("luca", "Fabba")
# names[-1]
# names.index("luca")
# len(names)
# print("luca" in names)
# print(sorted(names))
# newTuple = names + ("Sune", "ieta")

#Dictionaries   ***************************
# dog = {"name": "Migo", "age": 3, "color": "blue"}
# dog["favorite food"] = "meat"
# del dog['color']
# dogCopy = dog.copy()
# print(dog)


#Sets   ***************************
# set1 = {"luca", "Fabba", "luca"}
# set2 = {"luca"}
# print(list(set1))


#Functions   *******************************************
# def Hello(name, age):
#   print('Hello! ' + name + ", you are " + str(age) + " years old")

# Hello("Luca", 3)
# def change(value):
#   value["name"] = "fabba" 

# val = {"name": "luca"}
# change(val)

# print(val)
# def hello(name):
#   print('Hello ' + name + '!')
#   return name, "fabba", 8
# print(hello("luca"))


# def test():
#   age = 3      #local variable and outside variables 
#   print(age)

# print(age)
# test()

# def talk(phrase):
#   def say(word):
#     print(word)

#   words = phrase.split(' ')
#   for word in words:
#     say(word)
    
# talk(' will speak to luca')


# Objects  *********************************************
# everything in puthon is an object 
# it has attributes and methods

# items = [1, 2]
# items.append(3)
# items.pop()
# age = 8
# age = age + 1 


# Loops   *******************************

# count = 0 
# while count < 10:
#   print (" condition is True")
#   count += 1
  
# print("After the loop ")

# items = ["luca", "fabba", "migo", "ceasar"]
# for index, item in enumerate(items):
#   print(index, item)

# for item in range(15):
#   print(item)

#Recursion

# def factorial(n):
#   if n == 1: return 1
#   return n * factorial(n-1)

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

#Decorators

# def logtime(func):
#   def wrapper():
#     print("before")
#     val = func()
#     print("after")
#     return val
#   return wrapper

# @logtime
# def hello():
#   print("hello")

# hello()

#pip  

# list compressions

numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)