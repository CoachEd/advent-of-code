import sys
import time

start_secs = time.time()

arr = '3,225,1,225,6,6,1100,1,238,225,104,0,1001,210,88,224,101,-143,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,101,42,92,224,101,-78,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1101,73,10,225,1102,38,21,225,1102,62,32,225,1,218,61,224,1001,224,-132,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,1102,19,36,225,102,79,65,224,101,-4898,224,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1101,66,56,224,1001,224,-122,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1002,58,82,224,101,-820,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,2,206,214,224,1001,224,-648,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,76,56,224,1001,224,-4256,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,37,8,225,1101,82,55,225,1102,76,81,225,1101,10,94,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,102,2,223,223,1005,224,329,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,344,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,1107,677,677,224,1002,223,2,223,1006,224,389,101,1,223,223,108,226,677,224,102,2,223,223,1006,224,404,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,419,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,434,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,108,226,226,224,102,2,223,223,1005,224,464,101,1,223,223,8,226,226,224,1002,223,2,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,524,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,554,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,569,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,584,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,599,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,614,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,629,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,659,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226'.split(',')
#arr = '3,9,8,9,10,9,4,9,99,-1,8'.split(',')
"""
Parameter modes are stored in the same value as the instruction's opcode. 
The opcode is a two-digit number based only on the ones and tens digit of the value, that is, 
the opcode is the rightmost two digits of the first value in an instruction. 
Parameter modes are single digits, one per parameter, read right-to-left from the opcode: 
the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, 
the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.
"""
i = 0
vstring = 'arr = []; arrpos = [];\n'
while(True):
    vstring = vstring + 'arrpos.push(' + str(i) + '); arr.push(' + str(arr) + ');\n'
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
        print('input? ')
        # input
        n = input()
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
        print(x)
        i = i + 2
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

print('done')

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
vstring = vstring + ' lenv = ' + str(len(arr)) + ';\n'
print()
print(vstring)
