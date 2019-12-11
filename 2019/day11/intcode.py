import sys
import time

start_secs = time.time()

def printArr(a):
  s = ''
  for y in range(len(a)):
    for x in range(len(a[y])):
      s = s + a[y][x]
    s = s + '\n'
  print(s)

width = 200
height = 200
board =  [['.' for x in range(width)] for y in range(height)]
robot_y = int(height/2)
robot_x = int(width/2)
robot = '^'
directions = ['^','>','V','<']
count_output = 0
color = 0
paintedpanels = []
addmem = [0 for i in range(1000000)]

#works
#arr = '104,1125899906842624,99'
#arr='1102,34915192,34915192,7,4,7,99,0'
#arr='109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'

arr='3,8,1005,8,320,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,29,2,1005,1,10,1006,0,11,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,57,1,8,15,10,1006,0,79,1,6,3,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,90,2,103,18,10,1006,0,3,2,105,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,123,2,9,2,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,150,1,2,2,10,2,1009,6,10,1,1006,12,10,1006,0,81,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,187,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,209,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,231,1,1008,11,10,1,1001,4,10,2,1104,18,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,264,1,8,14,10,1006,0,36,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,293,1006,0,80,1006,0,68,101,1,9,9,1007,9,960,10,1005,10,15,99,109,642,104,0,104,1,21102,1,846914232732,1,21102,1,337,0,1105,1,441,21102,1,387512115980,1,21101,348,0,0,1106,0,441,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,209533824219,1,1,21102,1,395,0,1106,0,441,21101,0,21477985303,1,21102,406,1,0,1106,0,441,3,10,104,0,104,0,3,10,104,0,104,0,21101,868494234468,0,1,21101,429,0,0,1106,0,441,21102,838429471080,1,1,21102,1,440,0,1106,0,441,99,109,2,21201,-1,0,1,21101,0,40,2,21102,472,1,3,21101,0,462,0,1106,0,505,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,467,468,483,4,0,1001,467,1,467,108,4,467,10,1006,10,499,1102,1,0,467,109,-2,2106,0,0,0,109,4,2101,0,-1,504,1207,-3,0,10,1006,10,522,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21102,1,1,3,21102,541,1,0,1106,0,546,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,569,2207,-4,-2,10,1006,10,569,22102,1,-4,-4,1105,1,637,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,588,1,0,1105,1,546,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,607,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,629,21201,-1,0,1,21102,629,1,0,105,1,504,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0'
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
        if board[robot_y][robot_x] == '.':
          n = 0
        else:
          n = 1
        count_output = 0

        #print('input: ' + str(n))

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
        
        #print('output: ' + str(x))
        
        if count_output == 0:
          color = x 
          count_output = count_output + 1
        elif count_output == 1:
          direction = x 
          # 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
          the_index = directions.index(robot)
          if direction == '0':
            the_index = the_index - 1
            if the_index < 0:
              the_index = len(directions)-1
          else:
            the_index = the_index + 1
            if the_index >= len(directions):
              the_index = 0
          robot = directions[the_index]

          # paint
          if color == 0:
            # black
            board[robot_y][robot_x] = '.'
          else:
            # white
            board[robot_y][robot_x] = '#'
          if [robot_y,robot_x] not in paintedpanels:
            paintedpanels.append([robot_y,robot_x])

          #print(str(robot_y) + ',' + str(robot_x))

          if robot == '^':
            robot_y = robot_y - 1
          elif robot == 'V':
            robot_y = robot_y + 1
          elif robot == '<':
            robot_x = robot_x - 1 
          elif robot == '>':  
            robot_x = robot_x + 1

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

print(len(paintedpanels))
#printArr(board)

end_secs = time.time()
print('\nelapsed time: ' + str(end_secs - start_secs) + ' seconds')