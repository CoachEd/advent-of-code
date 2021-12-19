"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()

stree = []

# [1,2]
# [4,[3,[9,[9,0]]]]
# [[6,1],[6,4]]
# [ 
# 
#arr = [[[7,3],[7,9]],[8,[6,2]]] , [[8,[4,5]],[[6,4],[6,7]]] 
def get_list(sn):
  if sn.isdigit():
    return int(sn)
  
  sn = sn[1:-1]
  comma_index = 0
  skips = 0
  for i in range(len(sn)):
    if sn[i] == '[':
      skips += 1
      continue
    
    if sn[i] == ',' and skips == 0:
      comma_index = i
      break
    
    if sn[i] == ',' and skips != 0:
      skips -= 1
      
  left = sn[0:comma_index]
  right = sn[comma_index+1:]
  return [ get_list(left) , get_list(right) ]

# test
arr = get_list('[[[[4,0],[1,9]],[7,[3,6]]],[[2,[8,6]],[[2,8],[8,2]]]]')
print(arr)

sys.exit()
# test


print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

print(l)






print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
