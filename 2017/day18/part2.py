import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

"""
snd X plays a sound with a frequency equal to the value of X.
set X Y sets register X to the value of Y.
add X Y increases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
"""
def run_command(pos, commands, registers):
  global frequency
  arr = commands[pos].split(' ')

  cmd = arr[0]
  X = arr[1]
  Y = None
  if len(arr) > 2:
    Y = arr[2]

  if cmd == 'snd':
    if X.isalpha():
      X = registers[X]
    else:
      X = int(X)
    frequency = X
  elif cmd == 'set':
    if Y.isalpha():
      Y = registers[Y]
    else:
      Y = int(Y)
    registers[X] = Y
  elif cmd == 'add':
    if Y.isalpha():
      Y = registers[Y]
    else:
      Y = int(Y)    
    registers[X] += Y
  elif cmd == 'mul':
    if Y.isalpha():
      Y = registers[Y]
    else:
      Y = int(Y)    
    registers[X] *= Y
  elif cmd == 'mod':
    if Y.isalpha():
      Y = registers[Y]
    else:
      Y = int(Y)    
    registers[X] %= Y
  elif cmd == 'rcv':
    if X.isalpha():
      X = registers[X]
    else:
      X = int(X)    
    if X != 0:
      print(frequency)
      sys.exit(0)
    else:
      # do nothing
      pass
  elif cmd == 'jgz':
    if X.isalpha():
      X = registers[X]
    else:
      X = int(X)
    if Y.isalpha():
      Y = registers[Y]
    else:
      Y = int(Y)
    if X != 0:
      pos += Y
      return pos
  else:
    print('invalid instruction: ' + cmd)
  pos += 1
  return pos

# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

frequency = 0
pos = 0

registers = dict()
for c in 'abcdefghijklmnopqrstuvwxyz':
  registers[c] = 0

while pos < len(l):
  pos = run_command(pos, l, registers)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')