#!/usr/bin/env python3

from tabulate import tabulate

class solution:
  def __init__(self,fuel_tanks,wheels):
    self.f = fuel_tanks
    self.w = wheels

  def compute(self):
     l = []
     for i in range(0,self.f+1):
         for j in range(0,self.f+1):
            if 2*i+4*j==self.w:
                tup = (i,j)
                l.append(tup)
     return l

fuel_tanks= 32 # 3  # 0 
wheels = 56    # 6  # 9

s = solution(fuel_tanks,wheels)
lista = s.compute()

if lista == []:
  print("With these input numbers there are no solutions")
else:
  print(tabulate(lista, headers=["Motorcycle","Car"],tablefmt="presto"))