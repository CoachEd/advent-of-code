import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def spin(x):
  global dancers, positions
  p1 = positions[-x:]
  p2 = positions[0:len(positions)-x]
  positions = p1 + p2
  for i in range(len(positions)):
    dancers[positions[i]] = i

def exchange(i, j):
  global dancers, positions
  a = positions[i]
  b = positions[j]
  dancers[a] = j
  dancers[b] = i
  positions[i] = b
  positions[j] = a

def partner(a, b):
  global dancers, positions
  i = dancers[a]
  j = dancers[b]
  dancers[a] = j
  dancers[b] = i
  positions[i] = b
  positions[j] = a

# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())
l = l[0].split(',')

s = 'abcde' # sample
s = 'abcdefghijklmnop'

positions = [ c for c in s]
dancers = dict()
for i in range(len(positions)):
  dancers[positions[i]] = i

for m in l:
  if m[0] == 's':
    # spin
    x = int(m[1:])
    spin(x)
  elif m[0] == 'x':
    # exchange
    arr2 = m[1:].split('/')
    i = int(arr2[0])
    j = int(arr2[1])
    exchange(i,j)
  else:
    # partner
    a = m[1]
    b = m[3]
    partner(a, b)

print(''.join(positions))

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')