import sys
import time

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append( line )

"""
hlf r sets register r to half its current value, then continues with the next instruction.
tpl r sets register r to triple its current value, then continues with the next instruction.
inc r increments register r, adding 1 to it, then continues with the next instruction.
jmp offset is a jump; it continues with the instruction offset away relative to itself.
jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
"""

commands = []
for s in lines:
  s = s.replace("\r", "").replace("\n", "").strip()
  arr = s.split()
  cmd = arr[0]
  if cmd == 'hlf' or cmd == 'tpl' or cmd == 'inc':
    if arr[1] == 'a':
      arr[1] = 0
    else:
      arr[1] = 1
  elif cmd == 'jmp':
    arr[1] = int(arr[1])
  else:
    # jie or jio
    if arr[1].startswith('a'):
      arr[1] = 0
    else:
      arr[1] = 1
    arr[2] = int(arr[2])
  
  commands.append(arr)

print(commands)
print('')
idx = 0
registers = [1, 0] # a, b  PART 2
while True:
  cmd = commands[idx]
  #print(cmd)
  instr = cmd[0]
  if instr == 'hlf':
    registers[ cmd[1] ] = registers[ cmd[1] ]  // 2
    idx = idx + 1 
  elif instr == 'tpl':
    registers[ cmd[1] ] = registers[ cmd[1] ] * 3
    idx = idx + 1 
  elif instr == 'inc':
    registers[ cmd[1] ] = registers[ cmd[1] ] + 1
    idx = idx + 1 
  elif instr == 'jmp':
    idx = idx + cmd[1]  # jump to instruction at offset
    if idx < 0 or idx > len(commands) - 1:
      break
  elif instr == 'jie':
    if (registers[ cmd[1] ] % 2) == 0:
      idx = idx + cmd[2]
    else:
      idx = idx + 1     
    if idx < 0 or idx > len(commands) - 1:
      break       
  elif instr == 'jio':
    if registers[ cmd[1] ] == 1:
      idx = idx + cmd[2]    
    else:
      idx = idx + 1     
    if idx < 0 or idx > len(commands) - 1:
      break    

print(registers)

# wrong: 0 # read the instructions wrong for 'jio'
# Right! 307



print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')