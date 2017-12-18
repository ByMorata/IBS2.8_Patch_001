# 3.0.0 变量

# 变量赋值
string_00 = "Test String_00. "
string_01 = "Test String_01. "
number_00 = 100;
number_01 = 999;
print("This is A variable as %s,%s,%s,%s" % (string_00, string_01, number_00, number_01));

# 元组3
array_00 = ("1", "2", "3", "4");
print(array_00);
print(len(array_00));
print(array_00[0]);

array_01 = (array_00, "Hello World!");
print(array_01[0][1]);

# 列表
array_03 = ["Hello", "World", "!"];
array_03.extend(["Test_00"]);
print(array_03);
print(len(array_03));

# 字典
array_04 = {}
array_04["first"] = "Hello";
array_04["second"] = "World";
array_04["third"] = "!";
print(len(array_04));
print("输出array_04的第三个数组字符: " + array_04["third"]);
print(list(array_04))
print(array_04.values())
print(array_04.keys())
#print(array_04[0:1])
print(not True)

# 创建异常以及对异常的声明
fridge_contents = {"egg": 8, "mushroom": 20, "popper": 3, "cheese": 2, "tomato": 4, "milk": 13}
try:
    if fridge_contents["orange juice"] > 3:
        print("Sure, let's have some juice.")
except KeyError as error:
    print("Woah!,There is no %s" % error)
