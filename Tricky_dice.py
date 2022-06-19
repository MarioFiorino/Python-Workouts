#!/usr/bin/env python3

import random

class Dice():

  def __init__(self,tri,side=6):
    self.sides= side
    self.tricky = tri

  def roll_dice(self,nr): # nr = number of dice rolls for each run
    lr = []
    for _ in range(1,nr):
      n = random.randint(1,self.sides)
      
      if (self.tricky == True):
        n = random.randint(self.sides-1,self.sides)

      lr.append(n)
    
    return lr
    
    
d1 = Dice(False)  #  regular 6 sided dice
for _ in range(0,5): # 5 run of 10 roll dice 
  print(d1.roll_dice(10))

print("")

d2 = Dice(True,10)  #  tricky 10 sided dice
for _ in range(0,3):
  print(d2.roll_dice(8)) 
  
