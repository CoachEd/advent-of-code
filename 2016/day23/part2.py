"""
AoC
"""
import time
import sys
import math
from copy import copy, deepcopy

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

reg = {}

#reg['a'] = 7  # INPUT part 1
#reg['a'] = 12  # INPUT part 2
reg['a'] = 0
reg['b'] = 0
reg['c'] = 0
reg['d'] = 0


def run_bunny(l,reg,a):
  reg['a'] = a
  i = 0
  while i < len(l):
    s = l[i]
    arr = s.split(' ')
    cmd = arr[0]
    arg1 = arr[1]
    arg2 = ''
    val = 0
    val2 = 0

    #print('CMD: ' + cmd + '   ' + str(reg) + ' :   ' + str(l))  # TEST

    if len(arr) == 3:
      arg2 = arr[2]
    if cmd == 'cpy':
      if arg1.isalpha():
        val = reg[arg1]
      else:
        val = int(arg1)
      reg[arg2] = val
      i += 1
    elif cmd == 'inc':
      reg[arg1] += 1
      i += 1
    elif cmd == 'dec':
      reg[arg1] -= 1
      i += 1
    elif cmd == 'jnz':
      if arg1.isalpha():
        val = reg[arg1]
      else:
        val = int(arg1)

      if arg2.isalpha():
        val2 = reg[arg2]
      else:
        val2 = int(arg2)
    
      if val != 0:
        i = i + int(val2)
      else:
        i += 1
    elif cmd == 'tgl':
      if arg1.isalpha():
        val = reg[arg1]
      else:
        val = int(arg1)

      if (val+i) >= 0 and (val+i) < len(l):
        instr = l[i+val]
        cmd1 = instr[0:3]
        cmd2 = ''
        arr2 = instr.split(' ')
        if len(arr2) == 2: 
          if cmd1 == 'inc':
            cmd2 = 'dec'
          else:
            cmd2 = 'inc'
        else:
          if cmd1 == 'jnz':
            cmd2 = 'cpy'
          else:
            cmd2 = 'jnz'
        l[i+val] = cmd2 + instr[3:]
      i += 1

    #print(cmd + ' - ' + str(reg) + ' ' + str(l) + '\n') # TEST
  return reg['a']


print( run_bunny(l,reg,7) )

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
