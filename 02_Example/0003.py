# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# !/usr/bin/python
# x


import math

g_index_00 = 10000


def print_x(index_00):
    pass


def __init__():
    global g_index_00
    while (g_index_00 > 0):
        index_00 = g_index_00;

        index_01 = math.sqrt(index_00 + 100)
        index_02 = math.sqrt(index_00 + 100 + 168)
        if (index_01 == round(index_01)) and (index_02 == round(index_02)):
            print(g_index_00, " 和 ", int(index_01))
            print(g_index_00, " 和 ", int(index_02))

        g_index_00 = g_index_00 - 1

    pass


if __name__ == "__main__":
    __init__()
