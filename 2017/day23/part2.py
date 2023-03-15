import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def exec_command(s):
  global registers, iindex, muls

  if s == 'nop':
    iindex += 1
    return

  a = s.split()
  cmd = a[0]
  X = a[1]
  Y = a[2]

  if cmd == 'jnz':
    if X.isalpha():
      X = int(registers[X])
    else:
      X = int(X)
    Y = int(Y)
    if X != 0:
      iindex += Y
      return
  else:
    if Y.isalpha():
      Y = registers[Y]
    else:
      Y = int(Y)
    if cmd == 'set':
      registers[X] = Y
    elif cmd == 'sub':
      registers[X] -= Y
    elif cmd == 'add':
      registers[X] += Y      
    elif cmd == 'mul':
      registers[X] *= Y
      muls += 1
  iindex += 1

iindex = 0
muls = 0
registers = dict()
for c in 'abcdefgh':
  registers[c] = 0

# debug mode
registers['a'] = 1

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

# TODO: eliminate expensive loops in the instructions; may have to do it multiple times
num_commands = len(l)
while iindex < num_commands:
  s = l[iindex]

  curr_iindex = iindex
  
  print(s)
  
  exec_command(s)

# 2002 TOO HIGH
# 1001 TOO HIGH

print()
print('muls: ' + str(muls))
print('h: ' + str(registers['h']))
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')