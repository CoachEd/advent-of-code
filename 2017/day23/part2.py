import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

registers = {}
iindex = 0
mul_count = 0

def f1():
  """
  set g d
  mul g e
  sub g b
  jnz g 2
  set f 0  
  """
  global registers, mul_count
  mul_count += 1
  if ((registers['d'] * registers['e']) - registers['b']) == 0:
    registers['f'] = 0

def f2():
  global registers
  """
  sub e -1
  set g e
  sub g b
  """
  print(registers)
  registers['e'] = registers['e'] + 1
  registers['g'] = registers['e'] - registers['b']
  print(registers)
  print()

def init_registers():
  global registers
  (registers['a'], registers['b'], registers['c'], registers['d'], registers['e'], registers['f'], registers['g'], registers['h']) = (0,0,0,0,0,0,0,0)

def valueOf(z):
  global registers
  if z.isalpha():
    return registers[z]
  else:
    return int(z)

def exec_cmd_str(s):
  global iindex, registers, mul_count
  arr = s.split()
  cmd = arr[0]
  arg1 = arr[1]
  arg2 = arr[2]
  if cmd == 'set':
    registers[arg1] = valueOf(arg2)
  elif cmd == 'f1':
    f1()
  elif cmd == 'f2':
    f2()    
  elif cmd == 'sub':
    registers[arg1] = registers[arg1] - valueOf(arg2)
  elif cmd == 'mul':
    registers[arg1] = registers[arg1] * valueOf(arg2)
    mul_count += 1
  elif cmd == 'nop':
    # NOOP line
    pass # e.g., nop 0 0
  elif cmd == 'jnz':
    if valueOf(arg1) != 0:
      iindex += valueOf(arg2)
      return
  iindex += 1

# main
init_registers()

# debug mode - part 2
registers['a'] = 0

# read input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())
num_commands = len(l)
while iindex < num_commands:
  s = l[iindex]
  exec_cmd_str(s)

#print(registers)
#print(registers['h']) # part 2
print(mul_count)
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')