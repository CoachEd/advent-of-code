"""
AoC
"""
import time
import sys

start_secs = time.time()
print('')

def print_map(arr):
  s = ''
  for r in arr:
    for c in r:
      s += c
    s += '\n'
  print(s)

def count_safe_tiles(arr):
  count = 0
  for row in arr:
    for c in row:
      if c == '.':
        count += 1
  return count

def get_tile(y,x,arr):
  (l,c,r) = ('.','.','.')
  row = y-1

  lindex = x-1
  if lindex >= 0:
    l = arr[row][lindex]

  c = arr[row][x]
  rindex = x+1
  if rindex < len(arr[0]):
    r = arr[row][rindex]

  ltrap = l == '^'
  ctrap = c == '^'
  rtrap = r == '^'

  if ltrap and ctrap and not rtrap:
    return '^'
  if not ltrap and ctrap and rtrap:
    return '^'
  if ltrap and not ctrap and not rtrap:
    return '^'      
  if not ltrap and not ctrap and rtrap:
    return '^'
  return '.'        


# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

s = l[0]
cols = len(s)
rows = 400000
arr = [ [ ' ' for i in range(cols) ] for j in range(rows) ]
for i in range(len(s)):
  arr[0][i] = s[i]

for row in range(1,len(arr)):
  for col in range(len(arr[row])):
    arr[row][col] = get_tile(row,col,arr)

print( count_safe_tiles(arr) )

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
