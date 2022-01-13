"""
AoC
"""
import time
import sys

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

ranges = {}
low = sys.maxsize
arr = [-1 for i in range(len(l))]
for i in range(len(l)):
  s = l[i]
  arr2 = s.split('-')
  start = int(arr2[0])
  end = int(arr2[1])
  arr[i] = start
  ranges[start] = end

arr.sort()

pos = 0
for i in range(len(arr)-1):
  start = arr[i]
  end = ranges[start]
  next_start = arr[i+1]
  if pos >= start and pos <= end:
    pos = end + 1
    continue
  if pos < next_start:
    print(pos)
    break
  pos += 1



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
