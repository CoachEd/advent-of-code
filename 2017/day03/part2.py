"""
AoC
"""
from re import U
import time
import sys
import random
import math
from random import randrange
from copy import copy, deepcopy
from itertools import permutations

def valid(y,x,arr):
  if y < 0 or x < 0 or y >= len(arr) or x >= len(arr[0]):
    return False
  return True

def print_grid(arr):
  max_y = -1
  max_x = -1
  min_y = sys.maxsize
  min_x = sys.maxsize
  for y in range(len(arr)):
    for x in range(len(arr[y])):
      if arr[y][x] != '  ':
        if y > max_y:
          max_y = y
        if x > max_x:
          max_x = x
        if y < min_y:
          min_y = y
        if x < min_x:
          min_x = x
  rows = max_y - min_y + 1
  cols = max_x - min_x + 1
  arr2 = [ [ '  ' for i in range(cols) ] for j in range(rows) ]
  i = 0
  for y in range(min_y,max_y+1):
    j = 0
    for x in range(min_x,max_x+1): 
      arr2[i][j] = arr[y][x]
      j += 1
    i += 1

  s = ''
  for r in arr2:
    for c in r:
      if c == '  ':
        s += c
      else:
        s += "{:02d}".format(c) + '  '
    s += '\n'
  #print(s)
  return deepcopy(arr2)

def draw_ring(num,last_num,arr,start_y,start_x):
  if num == 1:
    last_num += 1
    arr[start_y][start_x] = last_num
    return ( 1, start_y, start_x ) # return last num, last y, last x
  
  j = (num-1) * 2
  i = j - 1

  curr_y = start_y
  curr_x = start_x

  curr_x += 1
  last_num += 1
  arr[curr_y][curr_x] = last_num

  for x in range(i):
    # U
    #print('U')
    curr_y -= 1
    last_num += 1
    arr[curr_y][curr_x] = last_num   

  for x in range(j):
    # L
    #print('L')
    curr_x -= 1
    last_num += 1
    arr[curr_y][curr_x] = last_num      

  for x in range(j):
    # D
    #print('D')
    curr_y += 1
    last_num += 1
    arr[curr_y][curr_x] = last_num      

  for x in range(j):
    # R
    #print('R')
    curr_x += 1
    last_num += 1
    arr[curr_y][curr_x] = last_num      

  return ( last_num, curr_y, curr_x )

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

rows = 750
cols = 750
find_num = 368078
arr = [ [ '  ' for i in range(cols) ] for j in range(rows) ]
start_y = rows//2
start_x = cols//2
(last_num, last_y, last_x) = draw_ring(1,0,arr,start_y,start_x)
num = 2
while last_num < find_num:
  (last_num, last_y, last_x) = draw_ring(num,last_num,arr,last_y,last_x)
  num += 1

#print( (last_num,last_y,last_x) ) 

y0 = -1
x0 = -1
y1 = -1
x1 = -1
new_arr = print_grid(arr)
for y in range(len(new_arr)):
  for x in range(len(new_arr[y])):
    if new_arr[y][x] == 1:
      y0 = y
      x0 = x

#print('starty,startx: ' + str(y0) + ',' + str(x0))
#print( abs(y1-y0) + abs(x1-x0))
#print (y0,x0,y1,x1)

neighbors = {}  # y,x -> [ (0,1), (1,0), ... ]
for y in range(len(new_arr)):
  for x in range(len(new_arr[y])):
    node = new_arr[y][x]
    new_arr[y][x] = 0
    neighbors[ node ] = [(y,x)]
    (ty,tx,by,bx,ry,rx,ly,lx) = (y-1,x,y+1,x,y,x+1,y,x-1)
    (ytl,xtl,ytr,xtr,ybl,xbl,ybr,xbr) = (y-1,x-1,y-1,x+1,y+1,x-1,y+1,x+1)
    if valid(ty,tx,new_arr):
      neighbors[node].append( (ty,tx) )
    if valid(by,bx,new_arr):
      neighbors[node].append( (by,bx) )
    if valid(ry,rx,new_arr):
      neighbors[node].append( (ry,rx) )
    if valid(ly,lx,new_arr):
      neighbors[node].append( (ly,lx) )
    if valid(ytl,xtl,new_arr):
      neighbors[node].append( (ytl,xtl) )
    if valid(ytr,xtr,new_arr):
      neighbors[node].append( (ytr,xtr) )
    if valid(ybl,xbl,new_arr):
      neighbors[node].append( (ybl,xbl) )
    if valid(ybr,xbr,new_arr):
      neighbors[node].append( (ybr,xbr) )      


# start                  
new_arr[y0][x0] = 1
#print_grid(new_arr)
#print('*****')
max_nodes = 100
for i in range(2,max_nodes):
  nbrs = neighbors[i]
  total = 0
  (y,x) = nbrs[0]
  for j in range(1,len(nbrs)):
    n = nbrs[j]
    (y1,x1) = n
    total += int(new_arr[y1][x1])

  new_arr[y][x] = total

  #print_grid(new_arr)
  #print()
  if total > find_num:
    print(str(total))
    break





# 439259 TOO HIGH
# 122 TOO LOW
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
