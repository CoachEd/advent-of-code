import sys
import time

start_secs = time.time()
print('For D9P1, enter 1. For D9P2, enter 2.\n')
addmem = [0 for i in range(1000000)]

#works
#arr = '104,1125899906842624,99'
#arr='1102,34915192,34915192,7,4,7,99,0'
#arr='109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'

arr='1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,1,29,1011,1102,1,27,1009,1101,23,0,1008,1101,0,25,1017,1102,1,36,1016,1101,0,31,1018,1102,35,1,1012,1101,28,0,1004,1101,779,0,1024,1102,403,1,1026,1101,0,33,1010,1102,37,1,1015,1101,32,0,1014,1101,0,752,1023,1101,0,30,1013,1102,21,1,1001,1102,1,1,1021,1102,1,34,1002,1102,400,1,1027,1101,0,22,1007,1102,1,567,1028,1101,558,0,1029,1102,26,1,1006,1102,39,1,1005,1102,1,0,1020,1101,0,38,1000,1101,0,755,1022,1102,1,770,1025,1102,1,24,1003,1102,20,1,1019,109,28,21107,40,41,-9,1005,1019,199,4,187,1106,0,203,1001,64,1,64,1002,64,2,64,109,-30,2107,38,7,63,1005,63,221,4,209,1105,1,225,1001,64,1,64,1002,64,2,64,109,-5,2102,1,8,63,1008,63,21,63,1005,63,251,4,231,1001,64,1,64,1106,0,251,1002,64,2,64,109,21,1207,-7,21,63,1005,63,267,1105,1,273,4,257,1001,64,1,64,1002,64,2,64,109,-1,1201,-7,0,63,1008,63,29,63,1005,63,293,1106,0,299,4,279,1001,64,1,64,1002,64,2,64,109,-4,1202,-3,1,63,1008,63,28,63,1005,63,319,1106,0,325,4,305,1001,64,1,64,1002,64,2,64,109,14,1206,-3,343,4,331,1001,64,1,64,1106,0,343,1002,64,2,64,109,-14,2108,21,-8,63,1005,63,361,4,349,1105,1,365,1001,64,1,64,1002,64,2,64,109,-9,1201,9,0,63,1008,63,27,63,1005,63,391,4,371,1001,64,1,64,1106,0,391,1002,64,2,64,109,27,2106,0,0,1106,0,409,4,397,1001,64,1,64,1002,64,2,64,109,-20,2101,0,0,63,1008,63,22,63,1005,63,431,4,415,1105,1,435,1001,64,1,64,1002,64,2,64,109,-7,1202,7,1,63,1008,63,22,63,1005,63,457,4,441,1105,1,461,1001,64,1,64,1002,64,2,64,109,8,1208,0,23,63,1005,63,479,4,467,1106,0,483,1001,64,1,64,1002,64,2,64,109,20,1205,-8,495,1105,1,501,4,489,1001,64,1,64,1002,64,2,64,109,-26,1208,4,28,63,1005,63,521,1001,64,1,64,1105,1,523,4,507,1002,64,2,64,109,15,21102,41,1,-2,1008,1015,41,63,1005,63,545,4,529,1106,0,549,1001,64,1,64,1002,64,2,64,109,18,2106,0,-7,4,555,1001,64,1,64,1106,0,567,1002,64,2,64,109,-30,1207,-3,35,63,1005,63,585,4,573,1105,1,589,1001,64,1,64,1002,64,2,64,109,14,1206,2,605,1001,64,1,64,1106,0,607,4,595,1002,64,2,64,109,-3,1205,5,621,4,613,1106,0,625,1001,64,1,64,1002,64,2,64,109,-5,21107,42,41,2,1005,1013,645,1001,64,1,64,1106,0,647,4,631,1002,64,2,64,109,-11,2108,42,5,63,1005,63,663,1106,0,669,4,653,1001,64,1,64,1002,64,2,64,109,4,21102,43,1,9,1008,1013,40,63,1005,63,693,1001,64,1,64,1106,0,695,4,675,1002,64,2,64,109,-1,2107,22,-2,63,1005,63,715,1001,64,1,64,1106,0,717,4,701,1002,64,2,64,109,7,21101,44,0,0,1008,1010,45,63,1005,63,741,1001,64,1,64,1106,0,743,4,723,1002,64,2,64,109,9,2105,1,4,1106,0,761,4,749,1001,64,1,64,1002,64,2,64,109,10,2105,1,-5,4,767,1001,64,1,64,1105,1,779,1002,64,2,64,109,-22,21108,45,43,10,1005,1017,799,1001,64,1,64,1105,1,801,4,785,1002,64,2,64,109,16,21101,46,0,-8,1008,1015,46,63,1005,63,827,4,807,1001,64,1,64,1105,1,827,1002,64,2,64,109,-7,2101,0,-7,63,1008,63,29,63,1005,63,851,1001,64,1,64,1106,0,853,4,833,1002,64,2,64,109,-5,2102,1,-3,63,1008,63,22,63,1005,63,877,1001,64,1,64,1106,0,879,4,859,1002,64,2,64,109,9,21108,47,47,-5,1005,1015,897,4,885,1105,1,901,1001,64,1,64,4,64,99,21102,27,1,1,21101,0,915,0,1105,1,922,21201,1,61784,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1105,1,922,22102,1,1,-1,21201,-2,-3,1,21102,1,957,0,1106,0,922,22201,1,-1,-2,1105,1,968,22101,0,-2,-2,109,-3,2105,1,0'
arr = arr.split(',')
arr.extend(addmem)

"""
Parameter modes are stored in the same value as the instruction's opcode. 
The opcode is a two-digit number based only on the ones and tens digit of the value, that is, 
the opcode is the rightmost two digits of the first value in an instruction. 
Parameter modes are single digits, one per parameter, read right-to-left from the opcode: 
the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, 
the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.
"""
i = 0
relbase =0
while(True):
    s = str(arr[i])

    # get parameter modes
    pmodes = s[:-2]
    if len(pmodes) == 0:
      pmodes = '0'
    pmodes = "{:03d}".format(int(pmodes)) # ensure length 3, leading 0s

    # make sure opcode is at least length 2 (leading 0s)
    opcode = "{:02d}".format(int(s))
    opcode = opcode[-2:]     

    if opcode == '99':
        # halt
        break
    elif opcode == '01':
        # add

        # parameter 1 - determine parameter mode
        if pmodes[2] == '0':  # absolute mode
          x = arr[int(arr[i+1])]
        elif pmodes[2] == '1':
          x = arr[i+1]  # position mode
        else:
          x = arr[int(arr[i+1])+relbase]  # relative mode

        # parameter 2 - determine parameter mode
        if pmodes[1] == '0':
          y = arr[int(arr[i+2])]
        elif pmodes[1]=='1':
          y = arr[i+2]
        else:
          y = arr[int(arr[i+2])+relbase]

        # parameter 3 - store the result (can only be position mode(0) or relative mode(2))
        if pmodes[0] == '0':
          arr[int(arr[i+3])] = int(x) + int(y)
        elif pmodes[0] == '2':
          arr[int(arr[i+3]) + relbase] = int(x) + int(y)

        i = i + 4
    elif opcode == '02':
        # multiply

        # parameter 1
        if pmodes[2] == '0':
          x = arr[int(arr[i+1])]
        elif pmodes[2] == '1':
          x = arr[i+1]
        else:
          x = arr[int(arr[i+1])+relbase]
                 
        # parameter 2
        if pmodes[1] == '0':
          y = arr[int(arr[i+2])]
        elif pmodes[1] == '1':
          y = arr[i+2]
        else:
          y = arr[int(arr[i+2])+relbase]  
        
        # parameter 3
        if pmodes[0] == '0':
          arr[int(arr[i+3])] = int(x) * int(y)
        elif pmodes[0] == '2':
          arr[int(arr[i+3])+relbase] = int(x) * int(y)
    
        i = i + 4
    elif opcode == '03':
        # input
        print('input?',end =" ")

        n = input()

        if pmodes[2] == '0':
          arr[int(arr[i+1])] = int(n)
        else:
          arr[int(arr[i+1])+relbase] = int(n)

        i = i + 2
    elif opcode == '04':
        # output

        if pmodes[2] == '0':
          x = arr[int(arr[i+1])]
        elif pmodes[2] == '1':
          x = arr[i+1]
        else:
          x = arr[int(arr[i+1])+relbase]
        print(x)
        i = i + 2
    elif opcode == '05':
        # jump-if-true
        """
        Opcode 5 is jump-if-true: if the first parameter is non-zero, 
        it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
        """
        if pmodes[2] == '0':
          x = arr[int(arr[i+1])]
        elif pmodes[2] == '1':
          x = arr[i+1]
        else:
          x = arr[int(arr[i+1])+relbase]
        
        if pmodes[1] == '0':
          y = arr[int(arr[i+2])]
        elif pmodes[1] == '1':
          y = arr[i+2]
        else:
          y = arr[int(arr[i+2])+relbase]

        if int(x) != 0:
          i = int(y)
        else:
          i = i + 3
    elif opcode == '06':
        # jump-if-false
        """
        Opcode 6 is jump-if-false: if the first parameter is zero, 
        it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
        """
        if pmodes[2] == '0':
          x = arr[int(arr[i+1])]
        elif pmodes[2] == '1':
          x = arr[i+1]
        else:
          x = arr[int(arr[i+1])+relbase]

        if pmodes[1] == '0':
          y = arr[int(arr[i+2])]
        elif pmodes[1] == '1':
          y = arr[i+2]
        else:
          y = arr[int(arr[i+2])+relbase]
        
        if int(x) == 0:
          i = int(y)
        else:
          i = i + 3
    elif opcode == '07':
        # is-less-than
        """
        Opcode 7 is less than: if the first parameter is less than the second parameter, 
        it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
        """
        if pmodes[2] == '0':
          x = arr[int(arr[i+1])]
        elif pmodes[2] == '1':
          x = arr[i+1]
        else:
          x = arr[int(arr[i+1])+relbase]
        
        if pmodes[1] == '0':
          y = arr[int(arr[i+2])]
        elif pmodes[1] == '1':
          y = arr[i+2]
        else:
          y = arr[int(arr[i+2])+relbase]

        z = ''
        if int(x) < int(y):
          z = '1'
        else:
          z = '0'

        if pmodes[0] == '0':
          arr[int(arr[i+3])] = z
        elif pmodes[0] == '2':
          arr[int(arr[i+3])+relbase] = z

        i = i + 4
    elif opcode == '08':
        # is-equals
        """
        Opcode 8 is equals: if the first parameter is equal to the second parameter, 
        it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
        """
        if pmodes[2] == '0':
          x = arr[int(arr[i+1])]
        elif pmodes[2] == '1':
          x = arr[i+1]
        else:
          x = arr[int(arr[i+1])+relbase]
        
        if pmodes[1] == '0':
          y = arr[int(arr[i+2])]
        elif pmodes[1] == '1':
          y = arr[i+2]
        else:
          y = arr[int(arr[i+2])+relbase]

        z = ''
        if int(x) == int(y):
          z = '1'
        else:
          z = '0'

        if pmodes[0] == '0':
          arr[int(arr[i+3])] = z
        elif pmodes[0] == '2':
          arr[int(arr[i+3])+relbase] = z

        i = i + 4
    elif opcode == '09':
      # adjust relative base
      """
      Opcode 9 adjusts the relative base 
      by the value of its only parameter. 
      The relative base increases (or decreases, 
      	if the value is negative) by the value of 
      	the parameter.
      """
      if pmodes[2] == '0':
        x = arr[int(arr[i+1])]
      elif pmodes[2] == '1':
        x = arr[i+1]
      else:
        x = arr[int(arr[i+1])+relbase]
      
      relbase = relbase +int(x)
      i = i + 2
    else:
        # nothing
        pass

end_secs = time.time()
print('\nelapsed time: ' + str(end_secs - start_secs) + ' seconds')