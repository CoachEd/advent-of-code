import numpy as np
#146 and 186 , 2993 are too low
# 3093 is wrong

maxlen = 700
maxlen = 600
maxlen = 3000
s = '#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............'
truestr = "01010 10111 11110 00011 00111 10101 11101 10001 01100 01000 01101 11111 00100"

arr1 = truestr.split()
truevals = np.zeros(shape=(len(arr1)))
for i in range(0,len(arr1)):
  truevals[i] = int(arr1[i],2)

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
  
print('entering loop...')
sumn = 0
for g in range(0,5001):
  #outs = ''
  sumn = 0
  for i in range(0,len(pots)):
    #c = '.'
    if pots[i] == 1:
      sumn = sumn + potsn[i]
      #c = '#'
    #outs = outs + c
  #print(str(g).rjust(2) + ':  ' + outs + '   ' + str(sumn))
  if g % 1000 == 0:
    print(str(g).rjust(10) + str(sumn).rjust(10))

  # create next generation
  nextpots.fill(0)
  for i in range(2,len(pots)-2):
    pattrn = pots[i-2]*(2**4) + pots[i-1]*(2**3) + pots[i]*(2**2) + pots[i+1]*(2**1) + pots[i+2]*(2**0)
    if pattrn in truevals:
      nextpots[i] = 1
  np.copyto(pots,nextpots)   


print(sumn)

