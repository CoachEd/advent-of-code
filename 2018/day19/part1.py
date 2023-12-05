"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')
registers = [ 0 for i in range(4) ]
opcodes = ['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']

def process_instr(o,a,b,c):
  # o - opcode str
  # a,b,c - params
  global registers
  if o == 'addr':
    registers[c] = registers[a] + registers[b]
  elif o == 'addi':
    registers[c] = registers[a] + b
  elif o == 'mulr':
    registers[c] = registers[a] * registers[b]
  elif o == 'muli':
    registers[c] = registers[a] * b
  elif o == 'banr':
    registers[c] = registers[a] & registers[b]
  elif o == 'bani':
    registers[c] = registers[a] & b
  elif o == 'borr':
    registers[c] = registers[a] | registers[b]
  elif o == 'bori':
    registers[c] = registers[a] | b
  elif o == 'setr':
    registers[c] = registers[a]    
  elif o == 'seti':
    registers[c] = a   
  elif o == 'gtir':
    registers[c] = 0
    if a > registers[b]:
      registers[c] = 1
  elif o == 'gtri':
    registers[c] = 0
    if registers[a] > b:
      registers[c] = 1
  elif o == 'gtrr':
    registers[c] = 0
    if registers[a] > registers[b]:
      registers[c] = 1
  elif o == 'eqir':
    registers[c] = 0
    if a == registers[b]:
      registers[c] = 1
  elif o == 'eqri':
    registers[c] = 0
    if registers[a] == b:
      registers[c] = 1
  elif o == 'eqrr':
    registers[c] = 0
    if registers[a] == registers[b]:
      registers[c] = 1
  else:
    print("invalid instruction!")
    sys.exit()

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

# main




print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
