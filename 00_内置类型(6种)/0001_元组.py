#!/usr/bin/python
from io import StringIO

tuple_00 = ("Hello", " ", "World", "!")
# print(tuple_00)

flag_00 = 0;

for flag_01 in range(len(tuple_00)):
    if flag_00 == 0:
        tuple_01 = tuple_00[flag_01]
        flag_00 = 1;
    else:
        tuple_01 += tuple_00[flag_01]

print(tuple_01)
print(type(tuple_01))

# 修改元组
# 元组只允许另开辟内存空间赋值,而不能更改本身的值
tuple_01 = tuple_00 + tuple_00
print("修改之后的tupple_01的数据类型为: " + str(type(tuple_01)))
print("修改之后的tupple_01的数据打印为: " + str(tuple_01))
print("修改之后的tupple_01的数据长度为: " + str(len(tuple_01)))

# 删除元组
# 元组的元素不允许删除,可以使用del删除整个元组
tuple_02 = ("test_00", "test_01", "test_02")

print("删除元组测试: " + str(tuple_02))
del tuple_02
try:
    print(tuple_02)
except NameError as error:
    print("数据不存在: " + str(error))

    # 额外测试:
