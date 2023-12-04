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
samples = 0
for i in range(0,len(l),4):
  if len(lines[i].strip()) == 0:
    break

  bef = lines[i].split(':')[1].strip().replace(' ','').replace('[','').replace(']','')
  arr2 = bef.split(',')
  for j in range(len(arr2)):
    registers[j] = int(arr2[j])
  breg = registers.copy()
  aft = lines[i+2].split(':')[1].strip().replace(' ','').replace('[','').replace(']','') # 3,2,2,1
  instr = lines[i+1].strip()

  arr3 = instr.split()
  (o,a,b,c) = (int(arr3[0]),int(arr3[1]),int(arr3[2]),int(arr3[3]))

  count_opcodes = 0
  for k in range(len(opcodes)):

    (registers[0],registers[1],registers[2],registers[3]) = (breg[0],breg[1],breg[2],breg[3])
    process_instr(opcodes[k],a,b,c)
    aft2 = ','.join(str(x) for x in registers)
    if aft == aft2:
      # match
      count_opcodes += 1
  if count_opcodes >= 3:
    samples += 1

  # blank = lines[i+3]

print(samples)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
