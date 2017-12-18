# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
#!/usr/bin/python
# -*- coding: UTF-8 -*-

for n in range(100, 1000):
    i = int(n / 100)
    j = int(n / 10 % 10)
    k = int(n % 10)

    # print(i,j,k)


    if n == i ** 3 + j ** 3 + k ** 3:
        print("请输出",n)