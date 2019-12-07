import sys
import time
from itertools import permutations

print()
start_secs = time.time()
inputs = '3,8,1001,8,10,8,105,1,0,0,21,34,47,72,93,110,191,272,353,434,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,2,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99'
arrA = inputs.split(',')
arrB = inputs.split(',')
arrC = inputs.split(',')
arrD = inputs.split(',')
arrE = inputs.split(',')


"""
Parameter modes are stored in the same value as the instruction's opcode. 
The opcode is a two-digit number based only on the ones and tens digit of the value, that is, 
the opcode is the rightmost two digits of the first value in an instruction. 
Parameter modes are single digits, one per parameter, read right-to-left from the opcode: 
the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, 
the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.
"""

# input , arr
def ampSoftware(input0,input1,arr):
  i = 0
  input_count = 0
  while(True):
      s = str(arr[i])

      # make sure opcode is at least length 2 (leading 0s)
      opcode = "{:02d}".format(int(s))
      opcode = opcode[-2:]
      #print('opcode: ' + opcode) # test
      #temp = input()  # test      

      if opcode == '99':
          break
      elif opcode == '01':
          # add
          pmodes = s[:-2]
          if len(pmodes) == 0:
            pmodes = '0'
          pmodes = "{:03d}".format(int(pmodes)) # ensure length 3, leading 0s
          if pmodes[2] == '0':
            x = arr[int(arr[i+1])]
          else:
            x = arr[i+1]
          if pmodes[1] == '0':
            y = arr[int(arr[i+2])]
          else:
            y = arr[i+2]
          
          # the write is always in position mode
          arr[int(arr[i+3])] = int(x) + int(y)
          i = i + 4
      elif opcode == '02':
          # multiply
          pmodes = s[:-2]
          if len(pmodes) == 0:
            pmodes = '0'
          pmodes = "{:03d}".format(int(pmodes)) # ensure length 3, leading 0s
          if pmodes[2] == '0':
            x = arr[int(arr[i+1])]
          else:
            x = arr[i+1]
          if pmodes[1] == '0':
            y = arr[int(arr[i+2])]
          else:
            y = arr[i+2]
          
          # the write is always in position mode
          arr[int(arr[i+3])] = int(x) * int(y)
          i = i + 4
      elif opcode == '03':
          # input
          if input_count == 0:
            n = input0
            input_count = input_count + 1
          elif input_count == 1:
            n = input1
          arr[int(arr[i+1])] = int(n)
          i = i + 2
      elif opcode == '04':
          # output
          pmodes = s[:-2]
          if len(pmodes) == 0:
            pmodes = '0'
          pmodes = "{:03d}".format(int(pmodes)) # ensure length 3, leading 0s
          if pmodes[2] == '0':
            x = arr[int(arr[i+1])]
          else:
            x = arr[i+1]
          i = i + 2
          return(x)
      elif opcode == '05':
      
          """
          Opcode 5 is jump-if-true: if the first parameter is non-zero, 
          it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
          """
          pmodes = s[:-2]
          if len(pmodes) == 0:
            pmodes = '0'
          pmodes = "{:03d}".format(int(pmodes)) # ensure length 3, leading 0s
          if pmodes[2] == '0':
            x = arr[int(arr[i+1])]
          else:
            x = arr[i+1]
          if pmodes[1] == '0':
            y = arr[int(arr[i+2])]
          else:
            y = arr[i+2]

          if int(x) != 0:
            i = int(y)
          else:
            i = i + 3
      elif opcode == '06':
          """
          Opcode 6 is jump-if-false: if the first parameter is zero, 
          it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
          """
          pmodes = s[:-2]
          if len(pmodes) == 0:
            pmodes = '0'
          pmodes = "{:03d}".format(int(pmodes)) # ensure length 3, leading 0s
          if pmodes[2] == '0':
            x = arr[int(arr[i+1])]
          else:
            x = arr[i+1]
          if pmodes[1] == '0':
            y = arr[int(arr[i+2])]
          else:
            y = arr[i+2]
          if int(x) == 0:
            i = int(y)
          else:
            i = i + 3
      elif opcode == '07':
          """
          Opcode 7 is less than: if the first parameter is less than the second parameter, 
          it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
          """
          pmodes = s[:-2]
          if len(pmodes) == 0:
            pmodes = '0'
          pmodes = "{:03d}".format(int(pmodes)) # ensure length 3, leading 0s
          if pmodes[2] == '0':
            x = arr[int(arr[i+1])]
          else:
            x = arr[i+1]
          if pmodes[1] == '0':
            y = arr[int(arr[i+2])]
          else:
            y = arr[i+2]

          if int(x) < int(y):
            arr[int(arr[i+3])] = '1'
          else:
            arr[int(arr[i+3])] = '0'
          i = i + 4
      elif opcode == '08':
          """
          Opcode 8 is equals: if the first parameter is equal to the second parameter, 
          it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
          """
          pmodes = s[:-2]
          if len(pmodes) == 0:
            pmodes = '0'
          pmodes = "{:03d}".format(int(pmodes)) # ensure length 3, leading 0s
          if pmodes[2] == '0':
            x = arr[int(arr[i+1])]
          else:
            x = arr[i+1]
          if pmodes[1] == '0':
            y = arr[int(arr[i+2])]
          else:
            y = arr[i+2]

          if int(x) == int(y):
            arr[int(arr[i+3])] = '1'
          else:
            arr[int(arr[i+3])] = '0'
          i = i + 4
      else:
          # nothing
          pass



max_thrust = -1
max_seq = []
perms = [''.join(p) for p in permutations('01234')]
for seq in perms:
  x = ampSoftware(seq[0],0,arrA) 
  x = ampSoftware(seq[1],x,arrB)
  x = ampSoftware(seq[2],x,arrC)
  x = ampSoftware(seq[3],x,arrD)
  x = ampSoftware(seq[4],x,arrE) 
  if x > max_thrust:
    max_thrust = x
    max_seq = seq

print('max thruster signal: ' + str(max_thrust))
print('phase setting: ' + str(max_seq))

print()
print('done')

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
