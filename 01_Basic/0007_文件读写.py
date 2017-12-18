#!/usr/bin/python


path_00 = "D:/000002/0001_index.txt"

# index_00 = open(path_00,"r")
# print(index_00.read())
# index_00.close()


try:
    index_01 = open(path_00,"r")
    print(index_01.read())
except:
    print("zzzz")
finally:
    if index_01:
        index_01.close()
        print("===========")

with open(path_00,"r") as index_02:
   for line_00 in index_02.readlines():
       print(line_00.rstrip())

# for line_00 in
index_03 = open(path_00,"w")
index_03.write("Hahahahahah")
index_03.close()
