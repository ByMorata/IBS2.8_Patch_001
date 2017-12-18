#!/user/bin/env python 3.1

# 定义一个函数
array_00_fridge = {'apples': 10, 'oranges': 3, 'milks': 2}
wanted_food = "apples"

def func_01_in_fridge():
    '''This is a Test Function to return the count of the values's key.
    Just a Test.'''
    try:
        count = array_00_fridge[wanted_food]
        return count
    except KeyError:
        count = 0
        return count

print(func_01_in_fridge())
print(func_01_in_fridge.__doc__)
print(dir())
#print(wanted_food.__doc__)

string_00 = "hello World!";
print(string_00.upper())
print(string_00.lower().__len__())