
import numpy as np

generations = 20 + 1
s = '#..#.#..##......###...###'
truestr = "00011 00100 01000 01010 01011 01100 01111 10101 10111 11010 11011 11100 11101 11110"
arr1 = truestr.split()
truevals = np.zeros(shape=(len(arr1)))
for i in range(0,len(arr1)):
  truevals[i] = int(arr1[i],2)

zeroindex = 0
pots = np.zeros(shape=(len(s)))
potsn = np.zeros(shape=(len(s)))

# init pot nums
for i in range(0,len(potsn)):
  potsn[i] = i

# init pots
for i in range(len(s)):
  if s[i] == '#':
    pots[i] = 1
  else:
    pots[i] = 0
  
print('entering loop...')
sumn = 0
for g in range(0,generations):

  # print out current state
  outs = ''
  sumn = 0
  for i in range(0,len(pots)):
    c = '.'
    if pots[i] == 1:
      sumn = sumn + potsn[i]
      c = '#'
    outs = outs + c
  print(str(g).rjust(2) + ':  ' + outs + '   ' + str(sumn))

  findex = potsn[0]
  lindex = potsn[len(potsn)-1]

  # make sure starts with 00000
  if pots[0] == 1 or pots[1] == 1 or pots[2] == 1 or pots[3] == 1 or pots[4] == 1:
    # add five 0s
    pots = np.concatenate([[0,0,0,0,0],pots])
    potsn = np.concatenate([[findex-5,findex-4,findex-3,findex-2,findex-1],potsn])
  
  # make sure ends with 00000
  if pots[len(pots)-1] == 1 or pots[len(pots)-2] == 1 or pots[len(pots)-3] == 1 or pots[len(pots)-4] == 1 or pots[len(pots)-5] == 1: 
    # add five 0s
    pots = np.concatenate([pots,[0,0,0,0,0]])
    potsn = np.concatenate([potsn,[lindex+1,lindex+2,lindex+3,lindex+4,lindex+5]])

  # create next generation
  nextpots = np.zeros(shape=(len(pots)))
    
  for i in range(2,len(pots)-2):
    pattrn = pots[i-2]*(2**4) + pots[i-1]*(2**3) + pots[i]*(2**2) + pots[i+1]*(2**1) + pots[i+2]*(2**0)
    if pattrn in truevals:
      nextpots[i] = 1

  np.copyto(pots,nextpots)   


print(sumn)

