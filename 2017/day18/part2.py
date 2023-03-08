import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

"""
set X Y sets register X to the value of Y.
add X Y increases register X by the value of Y.
mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).

snd X sends the value of X to the other program. These values wait in a queue until that program is ready to receive them. Each program has its own message queue, so a program can never receive a message it sent.

rcv X receives the next value and stores it in register X. If no values are in the queue, the program waits for a value to be sent to it. Programs do not continue to the next instruction until they have received a value. Values are received in the order they are sent.

jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
"""
def run_command0():
  global l, pos0, pos1, waiting0, waiting1, queue0, queue1, registers0, registers1

  arr = l[pos0].split(' ') # specific
  registers = registers0 # specific

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
    queue1.append(X) # specific
    waiting1 = False  # specific
  elif cmd == 'rcv':
    # specific
    if len(queue0) > 0:
      waiting0 = False
      registers[X] = queue0[0]
      del queue0[0]
    else:
      waiting0 = True
      return  
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
  elif cmd == 'jgz':
    if X.isalpha():
      X = registers[X]
    else:
      X = int(X)
    if Y.isalpha():
      Y = registers[Y]
    else:
      Y = int(Y)
    if X > 0:
      pos0 += Y # specific
      return
  else:
    print('invalid instruction: ' + cmd)

  pos0 += 1 # specific
  return

def run_command1():
  global l, pos0, pos1, waiting0, waiting1, queue0, queue1, registers0, registers1, count

  arr = l[pos1].split(' ') # specific
  registers = registers1 # specific

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
    count += 1
    queue0.append(X) # specific
    waiting0 = False  # specific
  elif cmd == 'rcv':
    # specific
    if len(queue1) > 0:
      waiting1 = False
      registers[X] = queue1[0]
      del queue1[0]
    else:
      waiting1 = True
      return  
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
  elif cmd == 'jgz':
    if X.isalpha():
      X = registers[X]
    else:
      X = int(X)
    if Y.isalpha():
      Y = registers[Y]
    else:
      Y = int(Y)
    if X > 0:
      pos1 += Y # specific
      return
  else:
    print('invalid instruction: ' + cmd)

  pos1 += 1 # specific
  return

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

pos0 = 0
pos1 = 0
waiting0 = False
waiting1 = False
registers0 = dict()
registers1 = dict()
queue0 = []
queue1 = []
for c in 'abcdefghijklmnopqrstuvwxyz':
  registers0[c] = 0
  registers1[c] = 0

registers0['p'] = 0
registers1['p'] = 1

count = 0

num_commands = len(l)

while True:

  if pos0 < 0 or pos1 < 0 or pos0 >= num_commands or pos1 >= num_commands:
    print('terminated')
    print((pos0,pos1,len(pos0),len(pos1)))
    break

  while len(queue0) > len(queue1):
    run_command0()
  
  run_command0()
  run_command1()

  if waiting0 and waiting1:
    break
  if waiting0 and pos1 >= num_commands:
    break
  if waiting1 and pos0 >= num_commands:
    break  
  if pos0 >= num_commands and pos1 >= num_commands:
    break

print(count)
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')