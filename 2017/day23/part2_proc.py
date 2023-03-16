def proc2(registers):
  global muls
  #print('proc2 start  ' + str(registers))
  while True:
    registers['e'] = 2
    proc1(registers)
    registers['d'] -= -1
    registers['g'] = registers['d']
    registers['g'] -= registers['b']
    if registers['g'] == 0:
      break
  #print('proc2 end  ' + str(registers))
  #print()

def proc1(registers):
  global muls
  #print('proc1 start  ' + str(registers))
  while True:
    registers['g'] = registers['d']
    registers['g'] *= registers['e']
    muls += 1
    registers['g'] -= registers['b']
    if registers['g'] == 0:
      registers['f'] = 0
    registers['e'] -= -1
    registers['g'] = registers['e']
    registers['g'] -= registers['b']
    if registers['g'] == 0:
      break
  #print('proc1 end    ' + str(registers))
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