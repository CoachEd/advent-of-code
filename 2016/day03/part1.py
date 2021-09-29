import sys
import time

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# TODO
valid = 0
for t in l:
  arr = t.split()
  x = int(arr[0])
  y = int(arr[1])
  z = int(arr[2])
  if (x+y) <= z or (x+z) <= y or (y+z) <= x:
    continue
  valid = valid + 1

print(valid) # Wrong: 865

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')