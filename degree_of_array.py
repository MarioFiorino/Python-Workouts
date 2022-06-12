#!/usr/bin/env python3

def occ(a):
  d = {}
  for i in range(len(a)):
     if a[i] not in d:
       d[a[i]] = 1
     else:
       d[a[i]] += 1
  return d        


def m_d(d):
  max = 0
  for v in diz.values():
    if v > max :
      max = v
      
  lo = []
  for k,v in diz.items():
     if v == max:
       lo.append(k) # list of the element that occurs most frequently input in array

  print("\nThe most frequent numbers: ", lo, " -  Each occurs: ",max," time") 
  return lo, max


def scorr(arr,lo,maxd):
  arr2 = []
  for i in range(len(arr)):

    if arr[i] in lo:
      lo.remove(arr[i])
      sub_arr= []
      cont = 0
      
      for j in range(i,len(arr)): 
         if arr[j] == arr[i]:
             cont += 1

         sub_arr.append(arr[j])    
         
         if cont == maxd:
           break

      arr2.append(sub_arr)

  return arr2 # This is the list of the shortest sub-arrays that share the degree("max") 

arr = [3,1,2,3,4,78,1,1,2,2]
arr2 = [7,25,7,3,25,4,5,6,9,8,8,9]
arr3 = [1,1,1,1,1,9,1,1]

diz = occ(arr)  ##This dictionary count the occurrence of each number in array 
#print(diz) #{3: 2, 1: 3, 2: 3, 4: 1, 78: 1} # 
lo,maxd = m_d(diz)
print("The shortest sub-arrays that share array degree:")
print(scorr(arr,lo,maxd))     
#The most frequent numbers:  [1, 2]  -  Each occurs:  3  time
#The shortest sub-arrays that share array degree:
#[[1, 2, 3, 4, 78, 1, 1], [2, 3, 4, 78, 1, 1, 2, 2]]

diz = occ(arr2) 
lo,maxd = m_d(diz)
print("The shortest sub-arrays that share array degree:")
print(scorr(arr2,lo,maxd)) 
#The most frequent numbers:  [7, 25, 9, 8]  -  Each occurs:  2  time
#The shortest sub-arrays that share array degree:
#[[7, 25, 7], [25, 7, 3, 25], [9, 8, 8, 9], [8, 8]]

diz = occ(arr3) 
lo,maxd = m_d(diz)
print("The shortest sub-arrays that share array degree:")
print(scorr(arr3,lo,maxd)) 
#The most frequent numbers:  [1]  -  Each occurs:  7  time
#The shortest sub-arrays that share array degree:
#[[1, 1, 1, 1, 1, 9, 1, 1]]