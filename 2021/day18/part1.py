"""
AoC
"""
import time
import math
import sys
from copy import copy, deepcopy

start_secs = time.time()

def get_left_num(s,i0):
  start_pos = -1
  end_pos = -1
  for i in range(i0-1,-1,-1):
    if s[i].isdigit():
      end_pos = i
      start_pos = i
      while s[i].isdigit():
        start_pos = i
        i -= 1
      return (s[start_pos:end_pos+1],start_pos,end_pos)
  return ('',-1,-1)

def get_right_num(s,i0):
  start_pos = -1
  end_pos = -1  
  for i in range(i0, len(s)):
    if s[i].isdigit():
      end_pos = i
      start_pos = i
      while s[i].isdigit():
        end_pos = i
        i += 1
      return (s[start_pos:end_pos+1],start_pos,end_pos)
  return ('',-1,-1)

def explode_sn(s,ei,ej):
  exploding_pair = s[ei:ej] # e.g. [7,3]  
  s = s[0:ei] + 'REPLACE' + s[ej:]

  # get left num, left num index, right num, right num index
  arr = get_list(exploding_pair)
  (left, li, lj) = get_left_num(s,ei-1)  
  if len(left) > 0:
    left = int(left)   
    s = s[0:li] + str(int(left+arr[0])) + s[lj+1:]
  
  (right, ri, rj) = get_right_num(s,ei+5)  
  if len(right) > 0:
    right = int(right)    
    s = s[0:ri] + str(int(right+arr[1])) + s[rj+1:]
  
  s = s.replace('REPLACE','0')
  
  return s

def one_split(s):
  # stop after doing one split!
  curr = 0
  while curr < len(s):
    starti = -1
    endi = -1
    for i in range(curr,len(s)):
      if s[i].isdigit():
        starti = i
        while s[i].isdigit():
          endi = i
          i += 1
        endi += 1
        break
    if s[starti:endi] == '':
      break
    num = int(s[starti:endi])
    if num >= 10:
      s1 = '[' + str(math.floor(num/2)) + ',' + str(math.ceil(num/2)) + ']'
      s = s[0:starti] + s1 + s[endi:]
      break
    curr = i
  return s

def reduce_sn(s):
  while True:
    len1 = len(s)    
    # explode any?
    exploded = False
    left_parend_count = 0
    for i in range(len(s)):
      if s[i] == '[':
        left_parend_count += 1
        if left_parend_count == 5 and s[i+1] != '[':
          # assume that this is a plain [x,y] pair. okay?
          ei = i
          ej = i
          while s[ej] != ']':
            ej += 1
          ej += 1                 
          s = explode_sn(s,ei,ej)
          exploded = True
          break
      elif s[i] == ']':
        left_parend_count -= 1
        
    # split any if nothing exploded
    if not exploded:
      # try finding a split, but exit after one split, to let explode have priority
      s = one_split(s)

    len2 = len(s)
    if len1 == len2:
      break
  return s
  
def all_nums_in_order(arr):
  if isinstance(arr, list):
    all_nums_in_order(arr[0])
    all_nums_in_order(arr[1])
  else:
    print(arr)

def level_four_elems(arr, i):
  if i == 4:
    print(arr)
    return
  if isinstance(arr, list):
    level_four_elems(arr[0], i+1)
    level_four_elems(arr[1], i+1)

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

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

stree = []
for s in l:
  if len(stree) == 0:
    stree = get_list(s)
  else:
    stree = [ stree.copy() , get_list(s) ]
    stree_s = str(stree).replace(' ','')
    stree_s = reduce_sn(stree_s)
    stree = get_list(stree_s)

print(stree_s)




#print( get_left_num('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]',10) ) # from [7,3]
#print( get_right_num('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]',14) ) # from [7,3]

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
