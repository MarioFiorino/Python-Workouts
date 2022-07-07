#!/usr/bin/env python3

class Solution:  
    def __init__(self, data , k): # window of size k
         self.data = data 
         self.k = k

    def maxSlidingWindow(self):
      if len(self.data)== 1:
         print("The max value in window : ", self.data[0])
         return self.data[0]

      elif len(self.data) < 1:
         print("No data")
         return None

      elif len(self.data) >= k:
         c = 0
         sub= []
         list_max = []

         while True: 
           for i in range(c,c + k):
             sub.append(self.data[i])

           list_max.append(max(sub))  
           c = c + 1   
           sub = []

           if c == (len(self.data)+1)-k:
               break

         print("The max value in ",len(list_max) ," windows : ", list_max)
         return list_max

      else:
         print("The max value in window : ", max(data))
         print("Note: The size 'k' of sliding windows shouldn't be bigger than len of array data")
			

###

data = [1,3,-1,-3,5,3,6,7]
k = 3 # try with k=7 # k = 1
data1 = []
data2 = [3,3]   #k = 2 o k >2

s = Solution(data,k)
ml = s.maxSlidingWindow()
#print(ml)
