# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少?


def get_list(count_00):
    list_00 = [1, 1]
    count_01 = 2

    if count_00 - 1 <= 2:
        return 1
    while count_01 != count_00:
        list_00.append(list_00[count_01 - 1] + list_00[count_01 - 2])

        count_01 += 1

    print(list_00)


get_list(10)