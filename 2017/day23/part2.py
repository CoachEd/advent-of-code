import time
import sys
from functools import reduce

from copy import copy, deepcopy


start_secs = time.time()

def factors(n):    
  return set(reduce(list.__add__, 
  ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

print('')

registers = {}
iindex = 0
mul_count = 0

def f0():
  global registers, mul_count
  start = registers['e']  # 2
  end = registers['b'] - 1 # 64
  registers['g'] = 0
  registers['e'] = registers['b']
  fs =factors(registers['b'])
  mul_count += end - start + 1
  for x in fs:
    if x >= start and x <= end:
      registers['f'] = 0
      return

def f1():
  """
  sub d -1
  set g d
  sub g b
  """
  start = registers['d']  # 2
  end = registers['b'] - 1 # 65
  registers['d'] = end

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
  if s == 'jnz f 2':
    print(registers)
    print('')
  arr = s.split()
  cmd = arr[0]
  arg1 = arr[1]
  arg2 = arr[2]
  if cmd == 'set':
    registers[arg1] = valueOf(arg2)
  elif cmd == 'f0':
    f0()  
  elif cmd == 'f1':
    f1()          
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
  if s == 'set d 2':
    print(registers)
  if s == 'sub g b':
    print('\t' + str(registers))

# main
init_registers()

# debug mode - part 2
registers['a'] = 1

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

print('h: ' + str(registers['h'])) # part 2
print(mul_count)
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')

# 115112999  TOO HIGH
# 501  TOO LOW