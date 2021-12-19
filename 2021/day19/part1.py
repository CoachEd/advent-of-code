"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')

# read in input file
d=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
scanner_num = 0
points = []
for line in lines:
  # --- scanner 0 ---
  s = line.strip()
  if s.startswith('---'):
    continue
  if len(s) == 0:
    d.append(points)
    points = []
    scanner_num += 1
    continue
  arr = [ int(x) for x in s.split(',')]
  points.append(arr)
d.append(points)
  
# d is an array of scanners data; each scanner's data is an array of point x,y,z
print(d)


  



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
