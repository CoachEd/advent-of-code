import sys
import time
from itertools import permutations

start_secs = time.time()
inputs = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
arrA = inputs.split(',')
arrB = inputs.split(',')
arrC = inputs.split(',')
arrD = inputs.split(',')
arrE = inputs.split(',')
iA = [0,0]
iB = [0,0]
iC = [0,0]
iD = [0,0]
iE = [0,0]

"""
Parameter modes are stored in the same value as the instruction's opcode. 
The opcode is a two-digit number based only on the ones and tens digit of the value, that is, 
the opcode is the rightmost two digits of the first value in an instruction. 
Parameter modes are single digits, one per parameter, read right-to-left from the opcode: 
the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, 
the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.
"""

# input , arr
def ampSoftware(input0,input1,arr,iArr):
  i = iArr[0]
  input_count = iArr[1]
  while(True):
      s = str(arr[i])

      # make sure opcode is at least length 2 (leading 0s)
      opcode = "{:02d}".format(int(s))
      opcode = opcode[-2:]
      #print('opcode: ' + opcode) # test
      #temp = input()  # test      

      if opcode == '99':
          print(str(input0) + ' halted')
          return False # halted
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
            iArr[1] = iArr[1] + 1
          else:
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
          iArr[0] = i
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
      iArr[0] = i

max_thrust = -1
max_seq = []
perms = [''.join(p) for p in permutations('56789')]

perms = ['98765'] # TEST!!!

for seq in perms:
  arrA = inputs.split(',')
  arrB = inputs.split(',')
  arrC = inputs.split(',')
  arrD = inputs.split(',')
  arrE = inputs.split(',')  
  arr_result = []
  x0 = -1
  iA = [0,0]
  iB = [0,0]
  iC = [0,0]
  iD = [0,0]
  iE = [0,0] 
  while True:
    if x0 == -1:
      x0 = 0
    x1 = ampSoftware(seq[0],x0,arrA,iA) 
    x2 = ampSoftware(seq[1],x1,arrB,iB)
    x3 = ampSoftware(seq[2],x2,arrC,iC)
    x4 = ampSoftware(seq[3],x3,arrD,iD)
    x0 = ampSoftware(seq[4],x4,arrE,iE) 
    arr_result.append(x0)
    if not x0:
      # halted
      break
  print(arr_result) # for this test, should be: 139629729
  x = arr_result[-2]
  if x > max_thrust:
    max_thrust = x
    max_seq = seq


print('max thruster signal: ' + str(max_thrust))
print('phase setting: ' + str(max_seq))

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')