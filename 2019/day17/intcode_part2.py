import sys
import time

start_secs = time.time()

robot_y = 16
robot_x = 12
robot = '^'
instr = ''
seen_scaffolds = 0

def printBoard(arr):
  s = ''
  for row in arr:
    for c in row:
      s = s + c
    s = s + '\n' 
  print(s)

def validYX(y,x):
  #printBoard(board)
  if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]):
    return False
  return True

def countScaffoldsAhead():

  num_scaffolds = 0
  y = robot_y
  x = robot_x
  while True:
    if robot == '^':
      # facing up
      y=y-1
    elif robot == 'v':
      # facing down
      y=y+1
    elif robot == '>':
      # facing right
      x=x+1
    elif robot == '<':
      # facing left  
      x=x-1
    if validYX(y,x):
      if board[y][x] == '#':
        num_scaffolds = num_scaffolds + 1
      else:
        break
    else:
      break
  return num_scaffolds

def turnRight():
  global robot
  global instr
  instr = instr + ',R'
  if robot == '^':
    # facing up
    robot = '>'
  elif robot == 'v':
    # facing down
    robot = '<'
  elif robot == '>':
    # facing right
    robot = 'v'
  elif robot == '<':
    # facing left  
    robot = '^'

def turnLeft():
  global robot
  global instr
  instr = instr + ',L'
  if robot == '^':
    # facing up
    robot = '<'
  elif robot == 'v':
    # facing down
    robot = '>'
  elif robot == '>':
    # facing right
    robot = '^'
  elif robot == '<':
    # facing left  
    robot = 'v'

def isRightTurn():
  if not atIntersection():
    # checks if at a right turn
    y = robot_y
    x = robot_x
    if robot == '^':
      # facing up
      x=x+1
    elif robot == 'v':
      # facing down
      x=x-1
    elif robot == '>':
      # facing right
      y=y+1
    elif robot == '<':
      # facing left  
      y=y-1
    if validYX(y,x) and board[y][x] == '#':
      return True
    else:
      return False
  else:
    return False

def isLeftTurn():
  if not atIntersection():
    # checks if at a left turn
    y = robot_y
    x = robot_x
    if robot == '^':
      # facing up
      x=x-1
    elif robot == 'v':
      # facing down
      x=x+1
    elif robot == '>':
      # facing right
      y=y-1
    elif robot == '<':
      # facing left  
      y=y+1
    if validYX(y,x) and board[y][x] == '#':
      return True
    else:
      return False
  else:
    return False

def atIntersection():
  y = robot_y
  x = robot_x
  uy=y-1
  ux=x
  dy=y+1
  dx=x
  ry=y
  rx=x+1
  ly=y
  lx=x-1  
  if validYX(uy,ux) and validYX(dy,dx) and validYX(ry,rx) and validYX(ly,lx):
    check_s = board[uy][ux] + board[dy][dx] + board[ry][rx] + board[ly][lx]
    if check_s == '####':
      return True
    else:
      return False
  else:
    return False

def moveRobot(n):
  global robot_x
  global robot_y
  global instr
  global seen_scaffolds
  global board

  anyerrors = False
  for i in range(0,n):
    y = robot_y
    x = robot_x
    if robot == '^':
      # facing up
      y=y-1
    elif robot == 'v':
      # facing down
      y=y+1
    elif robot == '>':
      # facing right
      x=x+1
    elif robot == '<':
      # facing left  
      x=x-1
    if validYX(y,x):
      if board[y][x] == '#':
        # good move. TODO: execute move
        seen_scaffolds = seen_scaffolds + 1
        board[robot_y][robot_x] = '#'
        board[y][x] = robot
        robot_y = y
        robot_x = x
      else:
        print('ERROR: trying to move onto ' + board[y][x])
        anyerrors = True
    else:
      print('ERROR: invalid move to y,x: ' + str(y) + ',' + str(x))
      anyerrors = True
  if not anyerrors:
    instr = instr + ',' + str(n)
  else:
    print('ERROR(s) while moving')


addmem = [0 for i in range(1000000)]

# set first address to 2 to begin robot sequence; 1 to draw the map
arr='1,330,331,332,109,3438,1102,1182,1,16,1101,1449,0,24,101,0,0,570,1006,570,36,101,0,571,0,1001,570,-1,570,1001,24,1,24,1105,1,18,1008,571,0,571,1001,16,1,16,1008,16,1449,570,1006,570,14,21101,58,0,0,1106,0,786,1006,332,62,99,21102,333,1,1,21102,73,1,0,1106,0,579,1101,0,0,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,101,0,574,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1105,1,81,21101,0,340,1,1106,0,177,21101,0,477,1,1105,1,177,21101,0,514,1,21102,1,176,0,1105,1,579,99,21102,1,184,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,101,0,572,1182,21101,0,375,1,21102,211,1,0,1106,0,579,21101,1182,11,1,21102,222,1,0,1106,0,979,21102,1,388,1,21102,233,1,0,1105,1,579,21101,1182,22,1,21101,244,0,0,1105,1,979,21102,401,1,1,21102,255,1,0,1105,1,579,21101,1182,33,1,21102,1,266,0,1105,1,979,21102,1,414,1,21101,277,0,0,1106,0,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21101,1182,0,1,21102,1,313,0,1106,0,622,1005,575,327,1101,1,0,575,21102,327,1,0,1105,1,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,12,16,0,109,4,1202,-3,1,586,21001,0,0,-1,22101,1,-3,-3,21101,0,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1106,0,597,109,-4,2106,0,0,109,5,1201,-4,0,630,20102,1,0,-2,22101,1,-4,-4,21102,1,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20101,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21102,702,1,0,1106,0,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,1,731,0,1105,1,786,1106,0,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21102,756,1,0,1106,0,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21102,1,774,0,1106,0,622,21201,-3,1,-3,1105,1,640,109,-5,2105,1,0,109,7,1005,575,802,20101,0,576,-6,20101,0,577,-5,1106,0,814,21101,0,0,-1,21102,0,1,-5,21102,0,1,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,51,-3,22201,-6,-3,-3,22101,1449,-3,-3,1202,-3,1,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1105,1,924,1205,-2,873,21101,0,35,-4,1106,0,924,1202,-3,1,878,1008,0,1,570,1006,570,916,1001,374,1,374,1201,-3,0,895,1102,2,1,0,2102,1,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20102,1,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,51,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,39,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,1,0,575,21101,973,0,0,1106,0,786,99,109,-7,2106,0,0,109,6,21102,1,0,-4,21102,1,0,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1105,1,1041,21101,-4,0,-2,1106,0,1041,21102,-5,1,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,1202,-2,1,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,2101,0,-2,0,1106,0,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21102,439,1,1,1105,1,1150,21101,0,477,1,1106,0,1150,21102,514,1,1,21102,1,1149,0,1105,1,579,99,21102,1,1157,0,1106,0,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,1201,-5,0,1176,2102,1,-4,0,109,-6,2105,1,0,38,7,44,1,5,1,44,1,5,1,44,1,5,1,44,1,5,1,44,1,5,1,44,1,5,1,44,1,5,1,20,9,9,7,5,1,28,1,9,1,11,1,28,1,9,1,9,9,22,1,9,1,9,1,1,1,5,1,22,1,9,1,5,7,5,1,22,1,9,1,5,1,3,1,7,1,22,13,3,1,3,1,7,1,32,1,1,1,3,1,3,1,7,14,19,9,1,1,7,2,33,1,3,1,1,1,1,1,7,2,17,7,9,1,3,5,1,8,17,1,5,1,9,1,5,1,3,1,6,1,15,5,3,1,9,7,3,1,6,1,15,1,1,1,1,1,3,1,19,1,6,9,7,1,1,9,17,1,14,1,7,1,3,1,3,1,1,1,17,1,14,1,7,1,3,1,3,13,7,1,14,1,7,1,3,1,5,1,9,1,7,1,14,1,5,7,5,1,9,1,7,1,14,1,5,1,1,1,9,1,9,1,7,1,14,9,9,1,9,1,7,1,20,1,11,1,9,1,7,1,20,1,5,7,9,9,20,1,5,1,44,1,5,1,44,1,5,1,44,1,5,1,44,1,5,1,44,1,5,1,44,1,5,1,44,7,30'
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

board = []
row = []
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

        code = int(x)
        #35 means #, 46 means ., 10 starts a new line
        if code == 10 and len(row) > 1:
          board.append(row)
          row = []
        else:
          row.append(chr(code))

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

printBoard(board)

    
     


# traverse board
# sample instruction: R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2

# there are 290 pound signs (#)
# turn left and face first scaffold, then move forward one to get on the scaffold
turnLeft()

while seen_scaffolds < 295:
  n = countScaffoldsAhead()
  moveRobot(n)
  if isLeftTurn():
    turnLeft()
  elif isRightTurn():
    turnRight()
  else:
    print('ERROR: unknown stop')
    printBoard(board)
    break

printBoard(board)
instr = instr[1:]
print(instr)

# ANSWER:
# L,12,L,6,L,8,R,6,L,8,L,8,R,4,R,6,R,6,L,12,L,6,L,8,R,6,L,8,L,8,R,4,R,6,R,6,L,12,R,6,L,8,L,12,R,6,L,8,L,8,L,8,R,4,R,6,R,6,L,12,L,6,L,8,R,6,L,8,L,8,R,4,R,6,R,6,L,12,R,6,L,8
"""
L,12,L,6,L,8,R,6,   A

L,8,L,8,R,4,R,6,R,6,  B

L,12,L,6,L,8,R,6,   A

L,8,L,8,R,4,R,6,R,6,   B

L,12,R,6,L,8,   C

L,12,R,6,L,8,   C

L,8,L,8,R,4,R,6,R,6,   B

L,12,L,6,L,8,R,6,    A

L,8,L,8,R,4,R,6,R,6,    B

L,12,R,6,L,8    C
"""





    


end_secs = time.time()
print('\nelapsed time: ' + str(end_secs - start_secs) + ' seconds')