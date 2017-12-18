#!/usr/bin/python

#导入自建的模板库
import sys
print("The Command line arguments are.")
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is',sys.path)

#用来判断是否被别的模块调用
if __name__ == '__main__':
    print("this is program is being run by itself")
else:
    print("i am being imported from another module.")

def sayHi():
    print("Hi, My name is Lin Hong Jie.")
