# 题目：输入三个整数x,y,z，请把这三个数由小到大输出



if __name__ == "__main__":
    while True:
        list_01 = input("Input some values such as x y z : ")

        list_02 = list_01.split(" ")
        list_02.sort()

        for x in list_02:
            print("排序为: ",x)