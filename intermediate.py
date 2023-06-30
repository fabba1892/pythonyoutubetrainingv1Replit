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

# function  and class decorators 

# @my_decorator
# def dosomething():
#   pass

# def start_end_decorator(func):
    
#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#     return wrapper

# @start_end_decorator
# def print_name():
#     print('Alex')
    
# # print_name()

# # print()

# # Now wrap the function by passing it as argument to the decorator function
# # and asign it to itself -> Our function has extended behaviour!
# # print_name = start_end_decorator(print_name)
# print_name()

# import functools

# class CountCalls:
#     # the init needs to have the func as argument and stores it
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#         self.num_calls = 0
    
#     # extend functionality, execute function, and return the result
#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(f"Call {self.num_calls} of {self.func.__name__!r}")
#         return self.func(*args, **kwargs)

# @CountCalls
# def say_hello(num):
#     print("Hello!")
    
# say_hello(5)
# say_hello(5)
# ////////////////////////////////////////////////////////////////////////

# generators

# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -= 1

# # this will not print 'Starting'
# cd = countdown(3)

# # this will print 'Starting' and the first value
# print(next(cd))

# # will print the next values
# print(next(cd))
# print(next(cd))

# # this will raise a StopIteration
# print(next(cd))

# without a generator, the complete sequence has to be stored here in a list

# without a generator, the complete sequence has to be stored here in a list
# def firstn(n):
#     num, nums = 0, []
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# sum_of_first_n = sum(firstn(1000000))
# print(sum_of_first_n)
# import sys
# print(sys.getsizeof(firstn(1000000)), "bytes")
# def firstn(n):
#     num, nums = 0, []
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# sum_of_first_n = sum(firstn(1000000))
# print(sum_of_first_n)
# import sys
# print(sys.getsizeof(firstn(1000000)), "bytes")

# /////////////////////////////////////

# mulyithreading and multi processing


# from multiprocessing import Process
# import os


# def square_numbers():
#     for i in range(1000):
#         result = i * i


# if __name__ == "__main__":
#     processes = []
#     num_processes = os.cpu_count()

#     # create processes and asign a function for each process
#     for i in range(num_processes):
#         process = Process(target=square_numbers)
#         processes.append(process)

#     # start all processes
#     for process in processes:
#         process.start()

#     # wait for all processes to finish
#     # block the main thread until these processes are finished
#     for process in processes:
#         process.join()

#     print('end main')


# from threading import Thread, Lock, current_thread
# from queue import Queue

# def worker(q, lock):
#     while True:
#         value = q.get()  # blocks until the item is available

#         # do stuff...
#         with lock:
#             # prevent printing at the same time with this lock
#             print(f"in {current_thread().name} got {value}")
#         # ...

#         # For each get(), a subsequent call to task_done() tells the queue
#         # that the processing on this item is complete.
#         # If all tasks are done, q.join() can unblock
#         q.task_done()


# if __name__ == '__main__':
#     q = Queue()
#     num_threads = 10
#     lock = Lock()

#     for i in range(num_threads):
#         t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
#         t.daemon = True  # dies when the main thread dies
#         t.start()
    
#     # fill the queue with items
#     for x in range(20):
#         q.put(x)

#     q.join()  # Blocks until all items in the queue have been gotten and processed.

#     print('main done')

# ////////////////////////////////////////////////////////////////////

# function arguments 

# def foo(a, b, c):
#     print(a, b, c)
    
# # positional arguments
# foo(1, 2, 3)

# # keyword arguments
# foo(a=1, b=2, c=3)
# foo(c=3, b=2, a=1) # Note that the order is not important here

# # mix of both
# foo(1, b=2, c=3)

# # This is not allowed:
# # foo(1, b=2, 3) # positional argument after keyword argument
# # foo(1, b=2, a=3) # multiple values for argument 'a'

# arguments after variable-length arguments must be keyword arguments
# def foo(*args, last):
#     for arg in args:
#         print(arg)
#     print(last)

# foo(8, 9, 10, last=50)

# def foo1():
#     x = number # global variable can only be accessed here
#     print('number in function:', x)

# number = 0
# foo1()

# # modifying the global variable
# def foo2():
#     global number # global variable can now be accessed and modified
#     number = 3

# print('number before foo2(): ', number)
# foo2() # modifies the global variable
# print('number after foo2(): ', number)

# immutable objects -> no change
# mutable objects -> change
# Rebind a mutable reference -> no change
# another example with rebinding references:
# def foo(a_list):
#     a_list += [4, 5] # this chanches the outer variable
    
# def bar(a_list):
#     a_list = a_list + [4, 5] # this rebinds the reference to a new local variable

# my_list = [1, 2, 3]
# print('my_list before foo():', my_list)
# foo(my_list)
# print('my_list after foo():', my_list)

# my_list = [1, 2, 3]
# print('my_list before bar():', my_list)
# bar(my_list)
# print('my_list after bar():', my_list)

# ////////////////////////////////////////////////////////////////

# asterisk operator

# # multiplication
# result = 7 * 5
# print(result)

# # power operation
# result = 2 ** 4
# print(result)

# list
# zeros = [0] * 10
# onetwos = [1, 2] * 5
# print(zeros)
# print(onetwos)

# # tuple
# zeros = (0,) * 10
# onetwos = (1, 2) * 5
# print(zeros)
# print(onetwos)

# # string
# A_string = "A" * 10
# AB_string = "AB" * 5
# print(A_string)
# print(AB_string)

# def my_function(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key, kwargs[key])
        
# my_function("Hey", 3, [0, 1, 2], name="Alex", age=8)

# # Parameters after '*' or '*identifier' are keyword-only parameters and may only be passed using keyword arguments.
# def my_function2(name, *, age):
#     print(name)
#     print(age)

# # my_function2("Michael", 5) --> this would raise a TypeError
# my_function2("Michael", age=5)

# def foo(a, b, c):
#     print(a, b, c)

# # length must match
# my_list = [1, 2, 3]
# foo(*my_list)

# my_string = "ABC"
# foo(*my_string)

# # length and keys must match
# my_dict = {'a': 4, 'b': 5, 'c': 6}
# foo(**my_dict)

# dump iterables into a list and merge them
# my_tuple = (1, 2, 3)
# my_set = {4, 5, 6}
# my_list = [*my_tuple, *my_set]
# print(my_list)

# # merge two dictionaries with dict unpacking
# dict_a = {'one': 1, 'two': 2}
# dict_b = {'three': 3, 'four': 4}
# dict_c = {**dict_a, **dict_b}
# print(dict_c)

# ////////////////////////////////////////////////////////////

# shallow and deep copying

class ManagedFile:
  def __init__(self, filename):
    self.filename = filename

  def __enter__(self):
    print('enter')
    self.file = open(self.filename, 'W')
    return self.file

  def __exit__(self, exc_type, exc_value, exc_traceback):
    if self.file:
      self.file.close()
    if exc_type is not None:
      print('exception has been handled')
    print('exc:', exc_type, exc_value)
    print('exit')

with ManagedFile('notes.txt') as file:
  print('do some stuff..')
  file.write('some to do...')
  file.somemethod()
print('continuing')