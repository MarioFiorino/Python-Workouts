#!/usr/bin/env python3

def find_sub_arr(arr):
  A =  []
  B =  []

  sumA = 0
  sumB = 0
  
  ct = 1 #counter

  while True:

    A.append(arr[len(arr)-ct])
    while (arr[len(arr)-ct] == arr[len(arr)-(ct+1)]):  # This is for guarantee that intersection from A and B is null
        ct+=1
        A.append(arr[len(arr)-ct])

    B = [arr[i] for i in range(0,(len(arr)- ct))] #This B = arr[:(len(arr)-ct)] this works just as well

    sumA = sum(A) 
    sumB = sum(B)

    if sumA > sumB:
      break

    else:
      ct +=1

  return A, B


l1 = [3,7,5,6,2]
l2 = [8,2,8,1,5,7,1,2,5,6,7,11]
l3 = [4,4,4,3,4,4]
l4 = [4,2,2,2,2,2,2,2,3,2,3,4,4]
l5 = [8,2,8,8,8,2,8,8,199,8,7,523]

arr = sorted(l1)
#print(arr)
A, B = find_sub_arr(arr)

print(A)  # [7, 6]   
print(B)  # [2, 3, 5]