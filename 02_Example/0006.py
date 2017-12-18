# 题目：斐波那契数列

import types

# 在数学上，费波那契数列是以递归的方法来定义：
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)


def func_febonaqie(index_00):

    if not isinstance(index_00,int):
        return -1
    if index_00 == 0:
        return 0
    elif index_00 == 1:
        return 1
    elif index_00 > 1:
        return func_febonaqie(index_00 - 1) + func_febonaqie(index_00 - 2)



print(func_febonaqie(10))