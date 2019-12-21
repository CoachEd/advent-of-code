import sys
import time

start_secs = time.time()

def printBoard(starty,startx,arr):
  s = ''
  for y in range(starty,len(arr)):
    for x in range(startx,len(arr[y])):
      s = s + arr[y][x]
    s = s + '\n' 
  print(s)

width = 50
height = 50
count_points = 0 
moves = []
board = [ ['.' for x in range(width)] for y in range(height)]
for ypos in range(0,height):
  for xpos in range(0,width):
    moves.append([xpos,ypos])

for m in moves:
  addmem = [0 for i in range(1000)]
  arr='109,424,203,1,21102,1,11,0,1106,0,282,21101,0,18,0,1105,1,259,2102,1,1,221,203,1,21102,31,1,0,1106,0,282,21101,38,0,0,1106,0,259,21002,23,1,2,21202,1,1,3,21102,1,1,1,21102,57,1,0,1106,0,303,2102,1,1,222,21001,221,0,3,21002,221,1,2,21101,0,259,1,21102,1,80,0,1106,0,225,21102,1,93,2,21102,1,91,0,1106,0,303,2101,0,1,223,21001,222,0,4,21102,1,259,3,21101,225,0,2,21101,225,0,1,21101,118,0,0,1106,0,225,20101,0,222,3,21102,1,120,2,21102,1,133,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1106,0,259,2102,1,1,223,21001,221,0,4,20102,1,222,3,21102,1,23,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,195,1,0,106,0,108,20207,1,223,2,20101,0,23,1,21101,-1,0,3,21102,1,214,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,21201,-3,0,1,21201,-2,0,2,21202,-1,1,3,21101,0,250,0,1105,1,225,21202,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21102,343,1,0,1106,0,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21101,0,384,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2106,0,0'
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
  move_index = 0
  while True:
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
          # The program uses two input instructions to request the X and Y position to which the drone should be deployed. 
          # Negative numbers are invalid and will confuse the drone; all numbers should be zero or positive.

          #print('input?',end =" ")
          #n = input()
          pos = m[move_index]
          n = pos
          move_index = move_index + 1

          if pmodes[2] == '0':
            arr[int(arr[i+1])] = int(n)
          else:
            arr[int(arr[i+1])+relbase] = int(n)

          i = i + 2
      elif opcode == '04':
          # output
          # Then, the program will output whether the drone is stationary (0) or being pulled by something (1). 
          if pmodes[2] == '0':
            x = arr[int(arr[i+1])]
          elif pmodes[2] == '1':
            x = arr[i+1]
          else:
            x = arr[int(arr[i+1])+relbase]

          #print(x)
          
          if int(x) == 1:
            board[ m[1] ] [m[0] ] = '#'
            count_points = count_points + 1

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

printBoard(0,0,board)
print('points affected: ' + str(count_points))

end_secs = time.time()
print('\nelapsed time: ' + str(end_secs - start_secs) + ' seconds')