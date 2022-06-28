#!/usr/bin/env python3

l1 = [5,3,6,7,4]
l2 = [8,5]
l3 = [10,8,7,5,2,1,1]
l = [7,2,10,2,4,8,1,12,1]

r = None
index_i = None
index_j = None

dif = []
max = -1

for i in range(len(l)):
  if i > 0:
    for j in range(0,i):
      r = l[i] - l[j]
      dif.append(r)
      
      if r > max:
        max = r
        index_i = i
        index_j = j

    print(dif)
    dif = []

print("\nMax diff : ",max)
try:
   print("\nElements  : ", l[index_i]," - ",l[index_j] )
except TypeError:
   pass
