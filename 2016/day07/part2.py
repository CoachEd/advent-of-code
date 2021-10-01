"""
AoC
"""
import time

start_secs = time.time()
print('')

def findABA(s):
  arr = []
  for i in range(1,len(s)-1):
    x = s[i-1]
    y = s[i+1]
    if x == y and s[i] != y:
      arr.append(x + s[i] + y)
  return arr

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())


TOTAL = 0
for y,e1 in enumerate(l):
  e1 = e1.replace('[',' ').replace(']',' ')
  ARR = e1.split()
  arr = []
  for x,e2 in enumerate(ARR):
    if x % 2 == 0:
      arr2 = findABA(e2)
      if len(arr2) > 0:
        arr = arr + arr2

  FOUND_BAB = False
  if len(arr) > 0:
    for x1,e1 in enumerate(arr):
      c1 = e1[0]
      c2 = e1[1]
      bab = c2 + c1 + c2
      for x,e2 in enumerate(ARR):
        if x % 2 == 1:
          if e2.find(bab) != -1:
            FOUND_BAB = True
            break
      if FOUND_BAB:
        break
  
  if FOUND_BAB and len(arr) > 0:
    TOTAL = TOTAL + 1



print(str(TOTAL)) # WRONG: 193 too low, 

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
