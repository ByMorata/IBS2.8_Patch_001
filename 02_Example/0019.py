#!/usr/bin/python
# -*-coding:UTF-8



for index_00 in range(2, 1000):

    for index_01 in range(1, index_00):

        list_00 = []
        if index_00 % index_01 == 0:
            list_00.append(index_00)

        print(list_00)