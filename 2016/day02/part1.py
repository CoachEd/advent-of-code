import sys
import time

start_secs = time.time()
print('')

# read in input file
l=[]
m= [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# TODO
y = 1
x = 1
combo = ''
for i in l:
  for c in i:
    oy = y
    ox = x
    if c == 'U':
      y = y - 1
      if y < 0:
        y = 0
    elif c == 'D':
      y = y + 1
      if y > 2:
        y = 2
    elif c == 'R':
      x = x + 1
      if x > 2:
        x = 2
    else:
      x = x - 1
      if x < 0:
        x = 0
  combo = combo + str(m[y][x])

print(combo)
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')