# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:04:01 2023

@author: Wei-Yang Chou
"""

results = [35,28,45,21,14,8]


my_number = [25,28,45,22,44,8]

n = 0
for i in my_number:
    for i2 in results:
        if i == i2:
            n+=1
            print(i)
            print("有")


print(n)


