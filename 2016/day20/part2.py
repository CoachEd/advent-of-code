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

# combine overlapping ranges
i = 0
while True:
  num_ranges = len(ranges)
  for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
      start1 = arr[i]
      start2 = arr[j]
      if start1 in ranges and start2 in ranges:
        end1 = ranges[start1]
        end2 = ranges[start2]
        if start2 >= start1 and start2 <= end1:
          del ranges[start2]
          if end2 > end1:
            ranges[start1] = end2
  if num_ranges == len(ranges):
    # no changes
    break


i = 0
count = 0
last_end = 0
for start in arr:
  if start in ranges:
    count += start - i
    i = ranges[start] + 1
    print('start-end: ' + str(start) + '-' + str(ranges[start]))
    last_end = ranges[start]

count += (4294967295 - last_end)
print(count)
  

sys.exit()


pos = 0
count = 0
for i in range(len(arr)-1):
  start = arr[i]
  end = ranges[start]
  next_start = arr[i+1]
  next_end = ranges[next_start]
  if pos >= start and pos <= end:
    pos = end + 1
    continue
  if pos < start:
    count += (start - pos)
    pos = end + 1
    continue

  pos += 1


print(count)
# 929 (too high)
# 47 (INCORRECT)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
