#d12 p2 - does not scale
import time
import sys
import re
from itertools import product
from copy import copy, deepcopy
start_secs = time.time()
print('')
# SOLUTION
 
"""inp3.txt
?###???????? 3,2,1
????? 1
"""
 
def isExactMatch(p,s):
  if len(p) != len(s):
    return False
  for i in range(len(p)):
    if p[i] == '?':
      continue
    if p[i] != s[i]:
      return False
  return True
 
def countMatches(p,a):
  # p pattern    '?###????????' length 12  OR ????? 1
  # a list of gears  ['###.', '##.', '#']
  # TODO
  # in above example...
  # Loop through each c in pattern
  #   can I place ###. in the first 8 spots (length minus sum over ##. and # lengths) or 12 - (4) = 8
  #   every time I can place ###. make recursive call summing counts from that spot with the remaining gears  in []
  #   if on last gear and can place, return 1
 
  #print((p,a))
 
  # base cases
  if len(a) == 0:
    return 0
  if len(a) == 1 and len(p) == len(a[0]):
    if isExactMatch(p,a[0]):
      return 1
    else:
      return 0
   
  # loop through positions in p in order, continually looking for a starting point for the first gear,
  # then spinning off threads
 
  # TODO: THIS CASE CAN'T HAPPEN
  # ('FOR ', 8, '?###????????', ['###.', '##.', '#'], '  :  ', '????', '###.', True)
 
  n = 0
  g = a[0]  # get gear
  glen = len(g)
  for i in range(len(p)):
    #print(('FOR ',i,p,' : ',p[i:i+glen],g,isExactMatch(p[i:i+glen],g)))
 
 
    # NEED ADDITIONAL CHECK BELOW; AFTER MATCHING, MAKE SURE p (from start to end of match) has exactly the right number of gears (#).  THIS CAN'T HAPPEN: ('FOR ', 8, '?###????????', ['###.', '##.', '#'], '  :  ', '????', '###.', True)
    if isExactMatch(p[i:i+glen],g):
      # found a starting spot for the gear spin off thread
      
      # we cannot have # before i
      if p[0:i].count('#') > 0:
      	break
      
      if len(a) == 1:
        # no more gears to spin off too
        # not a match if gears remain in rest of p
        gcount3 = p[i+glen:].count('#')
        if gcount3 == 0:
          n += 1
      else:
        # spin off thread with remaining gears and shortened p
        a1 = a.copy()
        a1.pop(0)
        n += countMatches(p[i+glen:],a1)
    else:
      # gear cannot start at this position p
      pass
     
 
    # can we go back to the top?
    gcount = g.count('#')
    i2 = i
    p2 = p[0:]
    gcount2 = 0
    for i3 in range(len(g)):
      if p2[i2] == '#' or g[i3] == '#':
        gcount2 += 1
    if gcount2 > gcount:
      break
 
  return n
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

patterns = []
sizes = []
for s in l:
  arr = s.split()
  patterns.append(arr[0])

  s1 = ''
  for i in range(5):
    s1 += arr[1][0:]
    if i < 4:
      s1 += ','
  sizes.append([ int(c) for c in s1.split(',')])
  
gears = []
for sz in sizes:
  tempa = []
  for i in range(len(sz)):
    sep = '.'
    if i == len(sz)-1:
      sep = ''
    tempa.append(sz[i]*'#'+sep)
  gears.append(tempa)
	
for i in range(len(patterns)):
	s = ''
	for j in range(5):
		s += patterns[i]
		if j < 4:
			s += '?'
	patterns[i] = s

#print(patterns)  # ['?###????????']
#print(sizes)     # [[3, 2, 1]]
#print(gears)     # [['###.', '##.', '#']]

tot_count = 0
for i in range(len(patterns)):
  #print(patterns[i], gears[i])
  #print()
  count = countMatches(patterns[i],gears[i])
  tot_count += count
  print(count)
print()
print(tot_count)
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# 6102 TOO LOW
# 8263 TOO HIGH
# 9345 TOO HIGH
#
#