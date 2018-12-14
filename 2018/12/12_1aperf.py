import numpy as np


maxlen =55 
s = '#..#.#..##......###...###'
truestr = "|00011|00100|01000|01010|01011|01100|01111|10101|10111|11010|11011|11100|11101|11110|"

zeroindex = int(maxlen/2) - int(len(s)/2)
pots = np.zeros(shape=(maxlen))
nextpots = np.zeros(shape=(maxlen))
potsn = np.zeros(shape=(maxlen))

# init pot nums
num = -1 * zeroindex
for i in range(0,len(potsn)):
  potsn[i] = num
  num = num + 1

# init pots
currindex = zeroindex
for i in range(len(s)):
  if s[i] == '#':
    pots[currindex] = 1
  else:
    pots[currindex] = 0
  currindex = currindex + 1
  
sumn = 0
for g in range(0,21):
  outs = ''
  sumn = 0
  for i in range(0,len(pots)):
    c = '.'
    if pots[i] == 1:
      sumn = sumn + potsn[i]
      c = '#'
    outs = outs + c
  print(str(g).rjust(2) + ':  ' + outs)    

  # create next generation
  nextpots.fill(0)
    
  for i in range(2,len(pots)-2):
    pattrn = str(int(pots[i-2]))+str(int(pots[i-1]))+str(int(pots[i]))+str(int(pots[i+1]))+str(int(pots[i+2])) 
    if pattrn in truestr:
      nextpots[i] = 1
  np.copyto(pots,nextpots)   


print(sumn)

