import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

def getX(t):
  global x
  global vals
  global done
  if t in [20, 60, 100, 140, 180, 220]:
    if not t in vals:
      vals[t] = x
    if len(vals) == 6:
      done = True

i = 0
t = 0
x = 1
vals = dict()
done = False
while True:
  instr = l[i]
  if instr == 'noop':
    # cycle start
    t += 1
    getX(t)
    
    # cycle end
    
  else:
    # addx
    arr = instr.split(' ')
    n = int(arr[1])

    getX(t) # cycle start
    t += 1
    getX(t) # cycle end/start
    
    t += 1
    getX(t) # cycle end

    x += n
  i += 1
  if i >= len(l) or done:
    break

tot = 0
for x in vals:
  tot += x * vals[x]
  
print(tot)
# 13540   too high 

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')