#!/usr/bin/env python3

from tabulate import tabulate

class solution:
  def __init__(self,fuel_tanks,wheels):
    self.f = fuel_tanks
    self.w = wheels
    self.l = []

  def comb_wheel(self):
     self.l = []
     for i in range(0,self.w+1):
         for j in range(0,self.w+1):
            if 2*i+4*j==self.w:
                tup = (i,j)
                self.l.append(tup)
     return self.l

  def narrow_field (self):
    lf = []
    for eil in self.l:
      n = sum(eil) 
      if n==self.f:
        lf.append(eil)
    return lf


wheels =    62 #  94 # 44 # 6  # 9  # 4  # 0
fuel_tanks= 16 #  35 # 12 # 3  # 2  # 1  # 10
s = solution(fuel_tanks,wheels)
lista = s.comb_wheel()

if lista == []:
  print("With these input numbers there are no solutions")
else:
  print("  -")
  print("  Knowing that there are", wheels, "wheels in a garage, \n   the possible combinations between cars and motorcycles are: \n")
  print(tabulate(lista, headers=["Nr. Motorcycles","Nr. Cars"],tablefmt="presto"))
  print("\n")

  # Adding constraint
  print("  -")
  print("  Knowing that there are ",fuel_tanks, "fuel tanks ")
  lista = s.narrow_field() # Here i reuse the same previous memory location, nothing changes for the purposes of the exercise.
  if lista == []:
       print("   with this number of fuel tanks there are no solutions")
  else:
       print("   the possible combinations between cars and motorcycles are: \n")
       print(tabulate(lista, headers=["Nr. Motorcycles","Nr. Cars"],tablefmt="presto"))
