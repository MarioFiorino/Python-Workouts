#!/usr/bin/env python3


def ffr(ls): # find first repeated word in sentence
  
  diz = {}
  w = None
  es= "|"  # end of sentence

  for i in ls:

    if i == es:
      break

    elif i not in diz.keys():
      diz[i] = 1
    
    else :
      diz[i] += 1
      w = i # first repeated word in sentence
      break

  return  w  
  
  
s = "one two bye yes Two one."
s1 = "Hola, Hola hola. "
s2 = "He had had quite enough of this games of;; of. "
s3 = ".Ciao."

c = " | "
s =  s.lower().replace(".", c).replace("-", c).replace(",", c).replace(":", c).replace(";", c) #here to change the sentence. E.g.: s = s1.lower().replace..
ls = s.split()
print(ls)

fw = ffr(ls)
if fw == None:
  print("No repeats found")
else:
  print("First words repeated: ",fw)
  
#['one', 'two', 'bye', 'yes', 'two', 'one']
#First words repeated:  two