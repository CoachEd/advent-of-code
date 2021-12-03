# part 2
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

def oxyCount(arr, pos):
  ones = 0
  zeroes = 0
  for i in range(0, len(arr)):
    s1 = arr[i]
    if s1[pos] == '1':
      ones += 1
    else:
      zeroes += 1
  if ones >= zeroes:
    return '1'
  else:
    return '0'

def c02Count(arr, pos):
  ones = 0
  zeroes = 0
  for i in range(0, len(arr)):
    s1 = arr[i]
    if s1[pos] == '1':
      ones += 1
    else:
      zeroes += 1
  if zeroes <= ones:
    return '0'
  else:
    return '1'

l1 = []
lt = l.copy()
length = len(l[0])
for i in range(0, length):
  x = oxyCount(lt, i)
  for bs in lt:
    if bs[i] == x:
      l1.append(bs)
  if len(l1) == 1:
    break 
  lt = l1.copy()
  l1 = []
oxy = int(l1[0], 2)

l1 = []
lt = l.copy()
for i in range(0, length):
  x = c02Count(lt, i)
  for bs in lt:
    if bs[i] == x:
      l1.append(bs)
  if len(l1) == 1:
    break 
  lt = l1.copy()
  l1 = []
c02 = int(l1[0], 2)

print(oxy*c02)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')