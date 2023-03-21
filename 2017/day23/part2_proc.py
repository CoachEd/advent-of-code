
import sys

def proc2_a(registers):
  registers['e'] = 2
  proc1_a(registers) # e, f, g
  registers['g'] = 0
  registers['d'] = registers['b']

def proc2(registers):
  global muls
  print('proc2 start  ' + str(registers))
  while True:
    registers['e'] = 2
    proc1_a(registers) # e, f, g
    registers['d'] -= -1
    registers['g'] = registers['d']
    registers['g'] -= registers['b']
    if registers['g'] == 0:
      break
  print('proc2 end    ' + str(registers))

def proc1_a(r):
  r['e'] = r['b']
  r['g'] = 0
  if r['b'] % 2 == 0:
    r['f'] = 0
  else:
    r['f'] = 1


def proc1(registers):
  global muls
  #print('proc1 start  ' + str(registers))
  print()
  print('proc1 start   ' + str(registers))
  while True:
    #print('proc1 top  ' + str(registers))
    registers['g'] = registers['d']
    registers['g'] *= registers['e']
    muls += 1
    registers['g'] -= registers['b']
    if registers['g'] == 0:
      registers['f'] = 0
    registers['e'] -= -1
    registers['g'] = registers['e']
    registers['g'] -= registers['b']
    #print('proc1 bot  ' + str(registers))
    if registers['g'] == 0:
      break

  print('proc1 end     ' + str(registers))
  print()
  #print()
  #print()

muls = 0
registers = dict()
for c in 'abcdefgh':
  registers[c] = 0

registers['a'] = 1  # debug mode
#registers['a'] = 0  # normal mode


# main
registers['b'] = 65
registers['c'] = registers['b']
if registers['a'] != 0:
  registers['b'] *= 100
  muls += 1
  registers['b'] -= -100000
  registers['c'] = registers['b']
  registers['c'] -= -17000

while True:

  registers['f'] = 1
  registers['d'] = 2
  proc2(registers)
  print()

  if registers['f'] == 0:
    registers['h'] -= -1
  
  registers['g'] = registers['b']
  registers['g'] -= registers['c']

  if registers['g'] == 0:
    # done
    break

  registers['b'] -= -17

print()
print('muls: ' + str(muls))
print()
print('h: ' + str(registers['h']))
print()