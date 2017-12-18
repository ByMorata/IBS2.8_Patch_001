# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
# 如果能被整除，则表明此数不是素数，反之是素数
import math
import types

def is_good_number(index_00):
    index_01 = round(math.sqrt(index_00))
    # print(index_01)

    for index_02 in range(2, index_01 + 1):

        if index_00 % index_02 == 0:
            return 1
    return -1

if __name__ == "__main__":

    for index_00 in range(101, 201):
        if is_good_number(index_00) == 1:
            print("素数: ", index_00)
