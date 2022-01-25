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
my_file = open("inp2.txt", "r", encoding='utf-8')
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

    #print('i=' + str(i) + '  ' + s)
    #print(str(reg))
    #print(str(s))
    #print('CMD: ' + cmd + '   ' + str(reg) + ' :   ' + str(l))  # TEST
    #print('CMD: ' + cmd + '   ' + str(reg))  # TEST

    if len(arr) == 3:
      arg2 = arr[2]
    if cmd == 'cpy':
      if arg1.isalpha():
        val = reg[arg1]
      else:
        val = int(arg1)

      if not arg2.isalpha():
        print("NOT1")
        sys.exit()

      reg[arg2] = val
      i += 1
    elif cmd == 'inc':

      if not arg1.isalpha():
        print("NOT2")
        sys.exit()

      reg[arg1] += 1
      i += 1
    elif cmd == 'dec':

      if not arg1.isalpha():
        print("NOT3")
        sys.exit()

      reg[arg1] -= 1
      i += 1
    elif cmd == 'nop':
      i += 1
    elif cmd == 'jn1':
      reg['a'] = (reg['d']+1)*reg['b']
      reg['d'] = 0
      i += 1
    elif cmd == 'all':
      reg[arg1] += reg[arg2]
      reg[arg2] = 0
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
        #print('i: ' + str(i) + '     val2: ' + str(val2))
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

    #print(str(reg))  
    #print()
    #print(reg)
    #print('b,d,a,c: ' + '{:05d}'.format(reg['b']) + ' ' + '{:05d}'.format(reg['d']) + ' '+ '{:05d}'.format(reg['a']) + ' '+ '{:05d}'.format(reg['c']) + '\n') # TEST
    #print('b,d,a,c: ' + '{:05d}'.format(reg['b']) + ' ' + '{:05d}'.format(reg['d']) + ' '+ '{:05d}'.format(reg['a'])  ) # TEST
  return reg['a']


#print( run_bunny(l,reg,7) )  # part 1
print( run_bunny(l,reg,12) )  # part 2

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
