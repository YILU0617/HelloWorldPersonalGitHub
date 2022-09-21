import math
from multiprocessing.sharedctypes import Value
from operator import index
from re import I


list1 = [ 2.4, 0.9, 14.1, 0.1, 11.8, 18.4, 7.3, 11.2 ,4.3, 0.7 ,1.8 ,1.0, 11.8, 5.1]
list2 = sorted(list1, reverse=True) 

print (list2)


sumNums = sum(list1)
count = len(list1)
print(count)
average = sumNums / count
print(average)

mid = len(list2) // 2
res = (list2[mid] + list2[~mid]) / 2
print(res)


nummin = min(list1)
print(nummin)

nummax = max(list1)
print(nummax)

print("which number which you want to repalce: ")
index1=input()
print("which number we want to replace: ")
value=input()
txt = "2.4, 0.9, 14.1, 0.1, 11.8, 18.4, 7.3, 11.2 ,4.3, 0.7 ,1.8 ,1.0, 11.8, 5.1"
x=txt.replace(index1,value)
print("now the tet is ",x)

y=txt.replace("," ," ~")
print(y)