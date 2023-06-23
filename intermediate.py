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
