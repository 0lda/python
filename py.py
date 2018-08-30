##1

# import  time
# print(time.localtime())

# import time as t
# print(t.localtime())
# print(t.time())

# from time import time, localtime
# print(localtime())
# print(time())

# from time import *
# print(localtime())
# print(time())

# input
# a_input=int(input('please input a number:'))#注意这里要定义一个整数型
# if a_input==1:
#     print('This is a good one')
# elif a_input==2:
#     print('See you next time')
# else:
#     print('Good luck')

# a_tuple = (12, 3, 5, 15 , 6)
# another_tuple = 12, 3, 5, 15 , 6

# list
# a = [1,2,3,4,1,1,-1]
# a.append(0)  # 在a的最后面追加一个0
# a.insert(1,0) # 在位置1处添加0
# a.remove(2) # 删除列表中第一个出现的值为2的项
# print(a.count(-1))
# print(a.index(2)) # 显示列表a中第一次出现的值为2的项的索引
# print(a)
# print(a[0])  # 显示列表a的第0位的值
# print(a[-1]) # 显示列表a的最末位的值
# print(a[0:3]) # 显示列表a的从第0位 到 第2位(第3位之前) 的所有项的值
# print(a[5:])  # 显示列表a的第5位及以后的所有项的值
# print(a[-3:]) # 显示列表a的倒数第3位及以后的所有项的值

# 多维列表
# multi_dim_a = [[1,2,3],
# 			   [2,3,4],
# 			   [3,4,5]] # 三行三列
# print(multi_dim_a[0][1])

# d1 = {'apple':1, 'pear':2, 'orange':3}
# d2 = {1:'a', 2:'b', 3:'c'}
# d3 = {1:'a', 'b':2, 'c':3}
#
# print(d1['apple'])  # 1
# print(a_list[0])    # 1
#
# del d1['pear']
# print(d1)   # {'orange': 3, 'apple': 1}
#
# d1['b'] = 20
# print(d1)   # {'orange': 3, 'b': 20, 'pear': 2, 'apple': 1}
#
# def func():
#     return 0
#
# d4 = {'apple':[1,2,3], 'pear':{1:3, 3:'a'}, 'orange':func}
# print(d4['pear'][3])    # a

# a=True
# while a:
#     b= input('type somesthing: ')
#     if b=='1':2
#         a= False
#     else:
#         pass
# print ('finish run')

# while True:
#     b= input('type somesthing:')
#     if b=='1':
#    #     break
#         continue
#     else:
#         pass
#     print('still in while')
# print ('finish run')

# try:
#     file = open('eeee.txt', 'r+')
# except Exception as e:
#     print(e)
#     response = input('do you want to create a new file:')
#     if response == 'y':
#         file = open('eeee.txt', 'w')
#     else:
#         pass
# else:
#     file.write('ssss')
#     file.close()

# a = [1,2,3]
# b = [4,5,6]
# ab=zip(a,b)
# print(list(ab))
# for i,j in zip(a,b):
#      print(i/2,j*2)

# fun= lambda x,y:x+y
# x=int(input('x='))    #这里要定义int整数，否则会默认为字符串
# y=int(input('y='))
# print(fun(x,y))

# def fun(x,y):
#     return (x+y)
# print(list(map(fun,[1],[2])))
# print(list(map(fun,[1,2],[3,4])))

# import copy
# a = [1,2,3]
# b = a
# print(id(a))
# print(id(b))
# b[0] = 12
# print(a)

## copy()
# c=copy.copy(a)  #拷贝了a的外围对象本身,
# id(c)
# print(id(a)==id(c))  #id 改变 为false
# c[1]=22222   #此时，我去改变c的第二个值时，a不会被改变。
# print(a,c)
# # [1, 2, 3] [1, 22222, 3] #a值不变,c的第二个值变了，这就是copy和‘==’的不同
# a=[1,2,[3,4]]  #第三个值为列表[3,4],即内部元素
# d=copy.copy(a) #浅拷贝a中的[3，4]内部元素的引用，非内部元素对象的本身
# id(a)==id(d)
# id(a[2])==id(d[2])
# a[2][0]=3333  #改变a中内部原属列表中的第一个值
# print(d)             #这时d中的列表元素也会被改变
# #[1, 2, [3333, 4]]
# #copy.deepcopy()
# e=copy.deepcopy(a) #e为深拷贝了a
# a[2][0]=333 #改变a中内部元素列表第一个的值
# print(a,e)
# #[1, 2, [3333, 4]] #因为时深拷贝，这时e中内部元素[]列表的值不会因为a中的值改变而改变

import pickle
# a_dict = {'da': 111, 2: [23,1,4], '23': {1:2,'d':'sad'}}
# file = open('pickle_ex.pickle','wb')
# pickle.dump(a_dict,file)
# file.close()
## reload a file to a variable
# with open('pickle_ex.pickle', 'rb') as file:
#     a_dict1 =pickle.load(file)
# print(a_dict1)

char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
sentence = 'Welcome Back to This Tutorial'
# print(set(char_list))
# print(set(sentence))
# print(set(char_list+list(sentence)))
unique_char = set(char_list)
# unique_char.add('x')
# # unique_char.add(['y', 'z']) this is wrong
# print(unique_char)
# unique_char.remove('x')
# print(unique_char)# {'b', 'd', 'c', 'a'}
# unique_char.discard('d')
# print(unique_char)# {'b', 'c', 'a'}
# unique_char.clear()
# print(unique_char)
# unique_char = set(char_list)
print(unique_char.difference({'a', 'e', 'i'}))# {'b', 'd', 'c'}
print(unique_char.intersection({'a', 'e', 'i'}))# {'a'}


