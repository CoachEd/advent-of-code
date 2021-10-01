"""
AoC
"""
import time
import sys

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

# a-z is ord 97-122
LEN = len(l[0])
arr = [ [ 0 for x in range( 123 ) ] for y in range(LEN) ]

for y, elem in enumerate(l):
  for x, elem2 in enumerate(elem):
    c = elem2
    o = ord(c)
    arr[x][o] = arr[x][o] + 1

STR=''
for y, e1 in enumerate(arr):
  MIN=sys.maxsize
  I=-1
  for z, e2 in enumerate(e1):
    if e2 != 0 and e2 < MIN:
      MIN = e2
      I = z
  STR = STR + chr(I)

print('')
print(STR)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
