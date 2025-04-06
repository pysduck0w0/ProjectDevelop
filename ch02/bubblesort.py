# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 09:12:43 2024

@author: Wei-Yang Chou
"""

temp = 0
a_list = [2,66,-1,78,-9]
   # elif change != True:
   #     break
print(a_list)

while True:    
    change = False
    for i in range(len(a_list)-1):
       print(a_list[i],a_list[i+1])
       if a_list[i] > a_list[i+1]:
           change = True
           temp = a_list[i+1]
           a_list[i+1] = a_list[i]
           a_list[i] = temp
    if change == False:
        break

       
    


print(a_list)








