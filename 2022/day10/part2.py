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

def drawCRT():
  global sprite, crt, row, col
  if sprite[col] == '#':
    crt[row][col] = '#'
  else:
    crt[row][col] = '.'

def printCRT():
  global crt
  s = ''
  for r in crt:
    for c in r:
      s += c
    s += '\n'
  print(s)
      

def drawSprite(t):
  global x
  global sprite, cols, i1, i2, i3
  sprite[i1] = '.'
  sprite[i2] = '.'
  sprite[i3] = '.'
    
  i1 = (x-1) if (x-1) >= 0 else x
  i2 = x
  i3 = (x+1) if (x+1) < cols else x
  
  sprite[i1] = '#'
  sprite[i2] = '#'
  sprite[i3] = '#'
  #print('{: >3} {:}'.format(str(t), ': ' + ''.join(sprite)))
  
def getX(t):
  global x, vals, done, rows, row
  if t in vals:
    # skip this one
    return
  
  if t in [40, 80, 120, 160, 200, 240]:
    vals[t] = x
    row += 1
    if len(vals) == 6:
      done = True

i = 0
t = 0
x = 1
cols = 40
rows = 6
row = 0
col = -1
i1 = 0
i2 = 1
i3 = 2
crt = [ [' ' for x in range(cols)] for y in range(rows) ]

sprite = [ '.' for x in range(cols)]
sprite[0] = '#'
sprite[1] = '#'
sprite[2] = '#'

vals = dict()
done = False
while True:
  instr = l[i]
  if instr == 'noop':
    # cycle start
    t += 1
    col += 1
    col = 0 if col >= cols else col
    drawSprite(t)
    drawCRT()
    getX(t)
    
    # cycle end
    
  else:
    # addx
    arr = instr.split(' ')
    n = int(arr[1])

    #getX(t) # cycle start
    t += 1
    col += 1
    col = 0 if col >= cols else col
    drawSprite(t)
    drawCRT()
    getX(t) # cycle end/start
    
    t += 1
    col += 1
    col = 0 if col >= cols else col
    drawSprite(t)
    drawCRT()
    getX(t) # cycle end

    x += n
  i += 1
  if i >= len(l) or done:
    break

printCRT()

# 13540   too high 

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')