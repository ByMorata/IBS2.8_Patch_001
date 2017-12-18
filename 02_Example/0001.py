#!/usr/bin/python
# 题目:
# 有四个数字: 1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析: 可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列
count_00 = 0

list_00 = []

def is_list_repeat(list_01):
    if str(type(list_01)) != "<class 'list'>":
        print("[EOF]类型不匹配")
        return -1
    list_01.sort()
    if len(list_00) == 0:
        list_00.append(list_01)
        print("[EOF]初始直接添加: ", list_01)
        return 1
    for index_00 in list_00:
        if index_00 == list_01:
            print("[EOF]重复值不添加: ", index_00, " 和 ", list_01)
            return -1

    list_00.append(list_01)
    return 1


for index_00 in (1, 2, 3, 4):
    for index_01 in (1, 2, 3, 4):
        for index_02 in (1, 2, 3, 4):
            if (index_00 != index_01) and (index_00 != index_02) and (index_01 != index_02):
                print(list_00)
                if 1 == is_list_repeat([index_00, index_01, index_02]):
                    print(index_00, index_01, index_02)
                    count_00 += 1

print("总数为: ", count_00, " 谢谢! ")
print(list_00)
