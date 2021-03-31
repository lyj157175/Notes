from functools import reduce
list11 = [1, 2, 3, 4]
list1 = map(lambda x: x**2, list11)
list2 = filter(lambda x: x>0, list11)
list3 = reduce(lambda x, y: x+y, list11)   # 
print(list(list1))
print(list(list2))
print(list3)