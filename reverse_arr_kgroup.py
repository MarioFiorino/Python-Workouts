#!/usr/bin/env python3


def inser_value(len_l):
  while True:
     k = input("Insert an integer smaller than " + str(len_l) + "\n")
     k = int(k)
     if (k <= len_l):
        break
     else:  
        print("Invalid value, insert a new integer\n")
  return k
  
  
def arr_sub_rev(l,k):

  sub_l = []
  new_l = [] 
  indx = len(l)
  
  d = len(l)/k
  d = int(d)

  if (k == 1)  :
    new_l =  sorted(l, reverse = True)

  else: 
    for j in range(0,d):
      sub_l = [l[i] for i in range((j*k),((j+1))*k)]
      #print(sub_l)
      sub_l =  sorted(sub_l, reverse = True)
      for i in sub_l:
        new_l.append(i)
      sub_l = []
      indx = (((j+1))*k)

  #fill the rest of the array, if necessary
  if indx != len(l):
     for i in range(indx,len(l)):
        new_l.append(l[i])

  return new_l  
  
l  = [1,2,3,4,5,6,7,8,9,10,11]
l1 = [1,5,8]
l2 = [4]
l3 = [1,2,3,4,5,6,7,8,9,10,11,12]

k = inser_value(len(l))

nrl = arr_sub_rev(l,k) # l list, k group

print(l)
print(nrl)
