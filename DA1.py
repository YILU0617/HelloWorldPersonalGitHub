import math
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


