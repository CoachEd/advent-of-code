"""
AoC
"""
import time
import sys
import random
import math
from random import randrange
from copy import copy, deepcopy
from itertools import permutations

all_weights = {}

def print_tree(d,bottom,indent):
  global the_bottom
  global all_weights
  if len(d[bottom][0]) == 0:
    #print(indent + bottom )
    return

  if bottom != the_bottom:
    sbottom = bottom.rjust(8)
    sweight = (str(all_weights[bottom])).rjust(8)
    print(indent + sbottom + ' (' +  sweight  + ')')
  else:
    sbottom = bottom.rjust(8)
    sweight = (str(all_weights[bottom])).rjust(8)    
    print(indent + sbottom + ' (' + sweight + ')')

  indent += '    '
  nodes = d[bottom][0]
  #for n in nodes:
  #  print(indent + n)
  
  for n in nodes:
    print_tree(d,n,indent)

def calc_sums(d,bottom,weights):
  global all_weights

  if len(d[bottom][0]) == 0:
    return weights[bottom]

  all_weights[bottom] = 0
  nodes = d[bottom][0]
  tot_weight = weights[bottom]
  for n in nodes:
    tot_weight += calc_sums(d,n,weights)
  all_weights[bottom] = tot_weight
  return tot_weight

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

d = {}
weights = {}
for s in l:
  arr = s.split(' -> ')
  arr2 = arr[0].split(' ')
  node = arr2[0]
  w = arr2[1][1:-1]
  weights[node] = int(w)
  if not node in d:
    d[node] = [[],[]]  # [ [above] , [below] ]  
  if len(arr) > 1:
    # process above and below
    arr3 = arr[1].split(', ')
    # above
    for s2 in arr3:
      d[node][0].append(s2)
      if not s2 in d:
        d[s2] = [[],[]]  # [ [above] , [below] ]  
      d[s2][1].append(node)


#for key,val in d.items():
#  if len(val[1]) == 0:
#    print(key)

the_bottom = 'eugwuhl'
#the_bottom = 'tknk'
calc_sums(d,the_bottom,weights)

#print(all_weights)

print_tree(d,the_bottom,'')

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
