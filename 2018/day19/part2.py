"""
AoC
"""
import time
import sys
from copy import copy, deepcopy

start_secs = time.time()
print('')
registers = [ 0 for i in range(6) ]
opcodes = ['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']

def process_instr(o,a,b,c):
  # o - opcode str
  # a,b,c - params
  global registers
  if o == 'addr':
    registers[c] = registers[a] + registers[b]
  elif o == 'addi':
    # addi (add immediate) stores into register C the result of adding register A and value B.
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
    # seti (set immediate) stores value A into register C. (Input B is ignored.)
    registers[c] = a   
  elif o == 'gtir':
    if a > registers[b]:
      registers[c] = 1
    else:
      registers[c] = 0
  elif o == 'gtri':
    if registers[a] > b:
      registers[c] = 1
    else:
      registers[c] = 0
  elif o == 'gtrr':
    if registers[a] > registers[b]:
      registers[c] = 1
    else:
      registers[c] = 0
  elif o == 'eqir':
    if a == registers[b]:
      registers[c] = 1
    else:
      registers[c] = 0
  elif o == 'eqri':
    if registers[a] == b:
      registers[c] = 1
    else:
      registers[c] = 0
  elif o == 'eqrr':
    if registers[a] == registers[b]:
      registers[c] = 1
    else:
      registers[c] = 0
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
instr_register = int(l[0][4:])
del l[0]

registers[0] = 1 # PART 2
ip = 0
while True:
  a = l[ip].split()
  (instr,a,b,c) = (a[0],int(a[1]),int(a[2]),int(a[3]))
  
  registers[instr_register] = ip

  #rb = registers.copy()

  process_instr(instr,a,b,c)

  #print('ip=' + str(ip) + ' [' + ''.join(str(x)+ ' ' for x in rb) + '] ' + l[ip] + ' [' + ''.join(str(x)+ ' ' for x in registers) + ']')
  
  ip = registers[instr_register]
  
  ip += 1
  if ip >= len(l) or ip < 0:
    break

print()
print(registers[0])

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
