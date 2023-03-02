import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')


def genA(prev):
  return (prev * 16807) % 2147483647
  pass

def genB(prev):
  return (prev * 48271) % 2147483647
  pass

def isMatch(a,b):
  a1 = bin(a).replace('0b', '').zfill(16)[-16:]
  b1 = bin(b).replace('0b', '').zfill(16)[-16:]
  #print(a1)
  #print(b1)
  return( a1 == b1 )


#Generator A starts with 699
#Generator B starts with 124

#actual
astart = 699
bstart = 124

#test
#astart = 65
#bstart = 8921

avals = []
bvals = []

a = astart
b = bstart

i = 0
while True:
  a = genA(a)
  if a % 4 == 0 and len(avals) < 5000000:
    avals.append(a)

  b = genB(b)
  if b % 8 == 0 and len(bvals) < 5000000:
    bvals.append(b)    

  if len(avals) == 5000000 and len(bvals) == 5000000:
    break

  i += 1
  if i % 1000000 == 0:
    print(str(len(avals)) + ' , ' + str(len(bvals)))

count = 0
for i in range(5000000):
  if i % 1000000 == 0:
    print(i)
  if isMatch(avals[i],bvals[i]):
    count += 1

print()
print(count)
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')