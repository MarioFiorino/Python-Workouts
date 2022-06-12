#!/usr/bin/env python3

l2 = [8,2,8,1,5,7,1,2,5,6,7,11]
l3 = [3,3,3,4,3,]
l4 = [9,1,1,1,3,9]

def Dpl(x):
    siz = len(x)
    for i in range(siz):
        k = i + 1
        for j in range(k, siz):
            if x[i] == x[j]:
                x[j] = x[j] + 1
    return x 
 
l2 = sorted(l2) # [1, 1, 2, 2, 5, 5, 6, 7, 7, 8, 8, 11]
print(Dpl(l2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

l3 = sorted(l3)
print(Dpl(l3)) # [3, 4, 5, 6, 7]

l4 = sorted(l4)
print(Dpl(l4)) # [1, 2, 3, 4, 9, 10]