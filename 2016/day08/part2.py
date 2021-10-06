"""
AoC
"""
import time

start_secs = time.time()
print('')

w,h = 50,6
screen = [['.' for x in range(w)] for y in range(h)] 

def print_screen(a):
  global w
  global h
  n = 0
  s1 = ''
  for y in range(h):
    for x in range(w):
      s1 = s1 + a[y][x]
      if a[y][x] == '#':
        n = n + 1
    s1 = s1 + '\n'
  print(s1)
  return n

def process_instruction(i):
  global screen
  global w
  global h
  arr = i.split()
  instr = arr[0]
  if instr == 'rect':
    arr2 = arr[1].split('x')
    a = int(arr2[0])
    b = int(arr2[1])
    for y in range(b):
      for x in range(a):
        screen[y][x] = '#'
  if instr == 'rotate':
    instr2 = arr[1]
    if instr2 == 'row':
      # rotate row y=0 by 4
      row = arr[2]
      row = int(row.replace('y=',''))
      by = int(arr[4])
      arrcopy = screen[row].copy()
      for x in range(w):
        screen[row][x] = '.'
      for x in range(len(arrcopy)):
        if arrcopy[x] == '.':
          continue
        newi = (x + by) % w
        screen[row][newi] = '#'
    else:
      # rotate column x=1 by 1
      col = arr[2]
      col = int(col.replace('x=',''))
      by = int(arr[4])
      arrcopy = ['.' for y in range(h)] 
      for y in range(h):
        arrcopy[y] = screen[y][col]
        screen[y][col] = '.'
      for y in range(len(arrcopy)):
        if arrcopy[y] == '.':
          continue
        newi = (y + by) % h
        screen[newi][col] = '#'

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

for i in l:
  process_instruction(i)

# PART 2: just read the letters
n = print_screen(screen)
print(n)



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
