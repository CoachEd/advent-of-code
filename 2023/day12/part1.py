import time
import sys
import re
from itertools import product
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
# SOLUTION
def getgears(sz):
  g = []
  for n in sz:
    g.append(n * '#')
  return g

def ismatch(p,s):
  if len(p) != len(s):
    return 0
  for i in range(len(p)):
    pc = p[i]
    sc = s[i]
    if pc == '.':
      if sc != '.':
        return 0
    elif pc == '#':
      if sc != '#':
        return 0
    else:
      # ?
      pass

  return 1

def countmatches(p,a):
  #print((p,a))  # ('###', ['###'])
  # p '?###????????'
  # a ['###', '##', '#']
  if len(a) == 0:
    return 0
  
  #  '?', ['#'])

  # base case - last chance to match
  if len(a) == 1 and len(p) == len(a[0]):
    return ismatch(p,a[0])

  # still need to walk
  n = 0 # count of matches
  s = a[0]
  if len(a) > 1:
    s += '.'
  slen = len(s)
  while True:
    #   ('???', '#', ['#'])
    # print((p,s,a,ismatch(p[0:slen],s)))
    if ismatch(p[0:slen],s) == 1:
      # s matches beginning of pattern, see if there are other matches if we go down the line
      
      # navigate remaining gears if any
      lena = len(a)
      if lena > 1:
        a1 = a.copy()
        a1.pop(0)
        if len(a1) > 0:
          n += countmatches(p[slen:], a1) # now try remaining gears
      elif lena == 1:
        # last gear processed
        p = p[1:]

        #print((p,a))

        if len(p) < len(a[0]):
          n += 1
          #print('break1')
          break
        else:
          #print((p,a))
          continue

      # move down the pattern to check for other landing spots for a
      p = p[1:]
    else:
      # no match - we can shift pattern to right if first char is . or ?
      # do not add to n
      if len(p) > 0 and p[0] in '.?':
        p = p[1:]  # shift
      else:
        #print('break2')
        break
  
    if slen > len(p):
      # s has gone beyond p, no more matches
      #print('break3')
      break

  return n

# read in input file
l=[]
my_file = open("inp3.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

possibles = []
patterns = []
sizes = []
for s in l:
  arr = s.split()
  patterns.append(arr[0])
  sizes.append([ int(c) for c in arr[1].split(',')])

#print( countmatches('??????',getgears([2])) ) #
print( countmatches('?###????????',getgears([3,2,1])) ) #
sys.exit()


tot_passed = 0
for i in range(len(patterns)):
  p = patterns[i]
  sz = sizes[i]
  tot_passed += countmatches(p,getgears(sz))
 
print(tot_passed)
 
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')

# 6102 TOO LOW