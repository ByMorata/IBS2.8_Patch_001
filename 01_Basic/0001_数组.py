# 1.0.0 Python提供三种数值类型:分别为整形,浮点型,虚数

# 使用type()获取对应数值的类型
print(type(1));
print(type(10.22));
print(type("Hello World!"));
# 虚数使用
print(12j + 1 + 15j);
print(type(12j + 1 + 15j));
# 在字符串中包含不同的数字
print("Hello World! %d " % 123);
# 字符串 % 用于转义
print("Test %%f");

# %格式说明符
print("%f" % (5 / 3));
print("%.2f" % (5 / 3));
print("%1.1f" % (415 * 20.2));
# str()函数可以将数值转换为字符串
print("Hello World!" + str(123));

# 习题-1
print(5 * 10);
# 习题-2
index_00 = 6;
while (index_00 != 15):
    print("%s" % index_00 + "的八进制转换位: " + oct(index_00));
    index_00 += 1;
# 习题-3
index_01 = 9;
while (index_01 != 20):
    print("%s" % index_01 + "的十六进制转换位: " + hex(index_01));
    index_01 += 1;
