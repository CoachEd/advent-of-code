import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def exec_command(s):
  global registers, iindex

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
  iindex += 1

iindex = 0
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

  #if iindex == 11:
  #  print(str(registers) + '  set g d')
  
  #print(s)
  
  exec_command(s)

  #if iindex == 19:
  #  print(str(registers) + '  jnz g -8')


print()
print(registers['h'])
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')