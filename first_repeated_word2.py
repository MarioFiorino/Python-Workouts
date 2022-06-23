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
  
  
s = "one two bye yes Two one. "
s1 = "Hola, Hola hola. "
s2 = "He had had quite enough of this games of;; the sword swords the. "
s3 = ".Ciao."
s4 = "Perhaps a disinterested spectator would consider this the most desirable consummation, in view of man's long record of folly and cruelty. But we who are actors in the drama, who are entangled in the net of private affections and public hopes, can hardly take this attitude with any sincerity. True, I have heard men say that they would prefer the end of man to submission to the Soviet government, and doubtless in Russia there are those who would say the same about submission to Western capitalism. But this is rhetoric with a bogus air of heroism. Although it must be regarded as unimaginative humbug, it is dangerous, because it makes men less energetic in seeking ways of avoiding the catastrophe that they pretend not not to dread." # cit. The Future of Man - Bertrand Russel

c = " | "
s =  s2.lower().replace(".", c).replace("-", c).replace(",", c).replace(":", c).replace(";", c) #here to change the sentence. E.g.: s = s1.lower().replace..
ls = s.split()
print(ls)
lw = []

for i in ls:
  lw.append(i)
  if i == "|":
    fw = ffr(lw)
    if fw == None:
       print("No repeats found")
    else:
       print("First words repeated: ",fw)
    lw = []
	 
#out:
#['he', 'had', 'had', 'quite', 'enough', 'of', 'this', 'games', 'of', '|', '|', 'the', 'sword', 'swords', 'the', '|']
#First words repeated:  had
#No repeats found
#First words repeated:  the

