#!usr/bin/bash python

def right_triangles(arr_sides):

  l = []

  if len(arr_sides) < 3:
    print("Needed at least 3 numbers!")
    return l

  for i in range (len(arr_sides)):
    for j in range(i+1,len(arr_sides)):
      for k in range(j+1,len(arr_sides)):
        if pow(arr_sides[i],2) == pow(arr_sides[j],2) + pow(arr_sides[k],2):
          l.append([arr_sides[i],arr_sides[j],arr_sides[k]])
  
  print("Possible right triangles: ", len(l)) 
  return l

#arr= [i for i in range(1,100)]
#arr = [4,2,2,2,2] 
arr = [13,3,4,5,12,13,5,12,4,4,2] 
arr = set (arr) # delete duplicates
arr = list (arr)
arr = sorted(arr,reverse = True)
print(right_triangles(arr))# out : [[13, 12, 5], [5, 4, 3]]
# check:  https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
