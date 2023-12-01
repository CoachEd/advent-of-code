import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

a = ['one','two','three','four','five','six','seven','eight','nine']

# SOLUTION
def findFirst(s):
  global a
  while True:
    if s[0].isdigit():
      return s[0]
    else:
      for i in range(len(a)):
        if s.startswith(a[i]):
          return str(i+1)
    s = s[1:]
    
def findLast(s):
  global a
  while True:
    if s[-1].isdigit():
      return s[-1]
    else:
      for i in range(len(a)):
        if s.endswith(a[i]):
          return str(i+1)
    s = s[:-1]

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  line = line.strip()
  l.append(line)


tot = 0
for s in l:
  fnum = findFirst(s)
  lnum = findLast(s)
  tot += int(str(fnum)+str(lnum))
print(tot)



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')