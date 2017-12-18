#!/usr/bin/python

import os

dict_00 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

# 访问字典的详细数值
print("访问字典的详细数值dict_00['Alice']: ", dict_00['Alice'])
print("访问字典的详细数值dict_00['Beth']: ", dict_00['Beth'])
print("访问字典的详细数值dict_00['Cecil']: ", dict_00['Cecil'])

# 修改字典的值

tuple_00 = ("Hello","World")
dict_01 = {tuple_00:"Test_00","key_00":"Test_01"}
print(dict_01.keys())
print(dict_01.get(tuple_00))
print(dict_01.items())



file_00 = open('D:/000002/0001_index.txt',"r")
print(file_00.read())

# file_00.close()

file_01 = open('D:/000002/0001_index.txt',"r")
print(file_01.read())