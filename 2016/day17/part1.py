"""
AoC
"""
import time
import sys
import hashlib

passcode = 'hijkl' # test data

arr = [ ['.' for i in range(4)] for i in range(4) ]
data = {}
data['0,0'] = [passcode]
open_arr = ['b', 'c', 'd', 'e', 'f']


def valid_coord(y,x):
  global arr
  if y < 0 or x < 0 or y >= len(arr) or x >= len(arr[0]):
    return False
  return True

def path_to(y,x,y1,x1,direction):
  global open_arr
  passcode_curr = data[str(y)+','+str(x)]
  hash = hashlib.md5(passcode_curr.encode('utf-8')).hexdigest()
  is_open = hash[direction] in open_arr
  if valid_coord(y,x) and valid_coord(y1,x1) and is_open:
    print('open path ' + str((y,x)) + ' -> ' + str((y1,x1)) )
  else:
    return False

def print_board(arr):
  s = ''
  for row in arr:
    for c in row:
      s += c
    s += '\n'
  print(s)

for y in range(len(arr)):
  for x in range(len(arr[y])):
    path_to(y,x,y-1,x,0) # up
    path_to(y,x,y+1,x,1) # down
    path_to(y,x,y,x-1,2) # left
    path_to(y,x,y,x+1,3) # right




start_secs = time.time()
print('')





print_board(arr)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
