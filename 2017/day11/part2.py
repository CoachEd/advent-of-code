import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')


# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

s = l[0]
arr = s.split(',')

x_pos = 0
y_pos = 0
max_distance = 0
for d in arr:
  if d == 'n':
    y_pos += 1
  elif d == 's':
    y_pos -= 1
  elif d == 'ne':
    x_pos += 1
    y_pos += 1
  elif d == 'nw':
    x_pos -= 1
    y_pos += 1    
  elif d == 'se':
    x_pos += 1
    y_pos -= 1
  elif d == 'sw':
    x_pos -= 1
    y_pos -= 1  

  temp_distance = max(abs(y_pos), abs(x_pos))
  if temp_distance > max_distance:
    max_distance = temp_distance

print(max_distance)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')