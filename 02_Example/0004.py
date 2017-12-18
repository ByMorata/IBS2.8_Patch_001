# 题目：输入某年某月某日，判断这一天是这一年的第几天？

index_00 = 0
index_01 = 1970
index_02 = 0
index_03 = 0

tuple_00 = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
tuple_01 = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
for index_01 in tuple_00:
    index_00 = index_00 + index_01


def check_input():
    if (index_01 < 1900) or (index_01 > 2200):
        print("[EOF]年份输入错误.")
        return -1
    if (index_02 < 1) or (index_02 > 12):
        print("[EOF]月份输入错误.")
        return -1
    if (index_03 < 1) or (index_03 > 31):
        print("[EOF]天数输入错误")
        return -1
    return 1


def is_good_year(year):
    if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        return 1
    else:
        return -1


def get_days(isgoodyear, month, day):
    global tuple_00
    global tuple_01

    counts = 0
    if (isgoodyear == 1):
        for index in tuple_01[:month - 1]:
            counts = counts + index
    else:
        for index in tuple_00[:month - 1]:
            counts = counts + index

    return counts + day


def print_on_console():
    global index_01
    index_01 = int(input("请输入年份: "))
    global index_02
    index_02 = int(input("请输入月份: "))
    global index_03
    index_03 = int(input("请输入天数: "))

    if -1 == check_input():
        print("[EOF]请重新输入.")
        return

    # print(type(index_01), type(index_02), type(index_03))
    print("本年已过天数位: ", get_days(is_good_year(index_01), index_02, index_03))


if __name__ == "__main__":

    while True:
        print_on_console()
