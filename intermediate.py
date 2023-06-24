# # collections

# # from collections import defaultdict
# # d= defaultdict(float)
# # d['a'], = 1
# # d['b'] =2
# # print(d['c'])
# # error

# # from collections import deque
# d = deque()

# d.append(1)
# d.append(2)

# d.appendleft(3)
# print(d)

# d.extend([4, 5, 6])
# print(d)
# d.rotate(2)
# print(d)

# ///////////////////////////////////////////////////////////////////////////////

# itertools iterator
# from itertools import product
# a= [1, 2]
# b = [3]
# prod = product (a, b, repeat=2)
# print(list(prod))

# from itertools import groupby

# persons = [{'name': 'Tim', 'age': '3'}]

# group_obj = groupby(a, key=lambda x: x<3)
# for key, value in group_obj:
#   print(key, list(value))

# from itertools import count, cycle, repeat

# a = [1, 2, 3]
# for i in repeat(1, 5):
#   print(i)

# //////////////////////////////////////////////////////////

# lambda

# //////////////////////////////////////////////////////////

# exceptions

# f = open('sometextfile.txt')
# x = -5
# assert (x==0), 'x is not positive'
# try:
#   a = 5/0
#   b =a+ '10'
# except ZeroDivisionError as e:
#   print(e)
# ////////////////////////////////////////////////////////

# logging

# import logging
# # logging.basicConfig(level=logging.DEBUG, format='%(asctime%' - &name& - &&)

# # logging.debug('this is a debug message')
# # logging.info('this is a info message')
# # logging.warning('this is a warning message')
# # logging.error('this is a error message')
# # logging.critical('this is a critical message')

# logger = logging.getLogger((__name__))

# ////////////////////////////////////////////////////////////////////////////


# Json
# serialization and deserializarion
# import json

# person = {"name": "Fabba", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# # convert into JSON:
# person_json = json.dumps(person)
# # use different formatting style
# person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# # the result is a JSON string:
# print(person_json) 
# print(person_json2) 

# /////////////////////////////////////////////////////////////////////

# random number

# import random

# random float in [0,1)
# a = random.normalvariate(0, 1)
# print(a)

# shuffle list 
# a = list("ABCDEFGHI")
# random.shuffle(a)

# random.seed(1)

# print(random.random())
# print(random.uniform(1,10))
# print(random.choice(list("ABCDEFGHI")))

# print('\nRe-seeding with 42...\n')
# random.seed(42)  # Re-seed

# print(random.random())
# print(random.uniform(1,10))
# print(random.choice(list("ABCDEFGHI")))


# secrets for passwords etc 

# import secrets 

# # random integer in range [0, n).
# a = secrets.randbelow(10)
# print(a)

# # return an integer with k random bits.
# a = secrets.randbits(5)
# print(a)

# # choose a random element from a sequence
# a = secrets.choice(list("ABCDEFGHI"))
# print(a)

# import numpy as np

# a = np.random.randint(0, 10, (3, 4))
# print(a)

# randomly shuffle a nd array.
# only shuffles the array along the first axis of a multi-dimensional array
# arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(arr)
# np.random.shuffle(arr)
# print(arr)

# ////////////////////////////////////////////////////////////////////////////////