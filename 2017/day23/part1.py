import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def exec_command(s):
  global registers, iindex, num_mul
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
    elif cmd == 'mul':
      registers[X] *= Y
      num_mul += 1
  iindex += 1

iindex = 0
num_mul = 0
registers = dict()
for c in 'abcdefgh':
  registers[c] = 0

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

num_commands = len(l)
while iindex < num_commands:
  s = l[iindex]
  exec_command(s)

print(num_mul)
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')