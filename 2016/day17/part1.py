"""
AoC
"""
import time
import sys
import hashlib

passcode = 'pgflpeqp' # test data
opasscode = passcode[0:]

arr = [ ['.' for i in range(4)] for i in range(4) ]
open_arr = ['b', 'c', 'd', 'e', 'f']
dirs = ['U','D','L','R']
good_paths = {}

def is_open(passcode,direction):
  hash = hashlib.md5(passcode.encode('utf-8')).hexdigest()
  return hash[direction] in open_arr

def valid_coord(y,x):
  global arr
  if y < 0 or x < 0 or y >= len(arr) or x >= len(arr[0]):
    return False
  return True

def print_board(arr):
  s = ''
  for row in arr:
    for c in row:
      s += c
    s += '\n'
  print(s)

def find_paths(passcode,y,x,seen):
  global arr
  key = str(y)+','+str(x)

  if key in seen and seen[key] > 10:
    return

  if not valid_coord(y,x):
    return
  if y == 3 and x == 3:
    the_path = passcode.replace(opasscode,'')
    if not the_path in good_paths:
      good_paths[the_path] = 0
    return
    
  seen2 = seen.copy()
  if not key in seen2:
    seen2[key] = 0
  seen2[key] += 1
  if is_open(passcode,0): # U
    find_paths(passcode+dirs[0],y-1,x,seen2)
  if is_open(passcode,1): # D
      find_paths(passcode+dirs[1],y+1,x,seen2)
  if is_open(passcode,2): # L 
      find_paths(passcode+dirs[2],y,x-1,seen2)
  if is_open(passcode,3): # R
      find_paths(passcode+dirs[3],y,x+1,seen2)

start_secs = time.time()
print('')

find_paths(passcode,0,0,{})

min_len = sys.maxsize
min_path = ''
for p in good_paths:
  if len(p) < min_len:
    min_path = p
    min_len = len(p)

print(min_path)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
