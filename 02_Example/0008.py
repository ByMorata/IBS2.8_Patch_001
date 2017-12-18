# 题目：输出 9*9 乘法口诀表

list_00 = []
index_00 = 9
while index_00 != 0:
    list_00.append(index_00)
    # print(list_00)
    list_00.sort()
    index_00 -= 1

for index_01 in list_00:
    for index_02 in list_00:
        print(" ", index_01, " * ", index_02, " = ", index_01 * index_02, end=" ")
    print("")
