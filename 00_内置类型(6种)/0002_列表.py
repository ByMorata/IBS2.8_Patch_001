#!/usr/bin/python

list_00 = ["test_00", "test_01", "test_02"]
print("1.初始化列表: ", list_00)
list_00.append("test_03")
print("2.尾部新增元素: ",list_00)

print(list_00[:3])
print(list_00.index("test_01"))
list_00.reverse()
print("3.反向列表数据: ",list_00)
