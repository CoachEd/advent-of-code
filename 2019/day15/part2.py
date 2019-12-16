import sys
import time
import random
# USE PART 2 to draw the map

start_secs = time.time()
addmem = [0 for i in range(1000000)]


arr='3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,101,0,1034,1039,1002,1036,1,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,1001,1034,0,1039,101,0,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1105,1,124,1001,1034,-1,1039,1008,1036,0,1041,102,1,1035,1040,1001,1038,0,1043,101,0,1037,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,101,0,1035,1040,1002,1038,1,1043,101,0,1037,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,33,1032,1006,1032,165,1008,1040,35,1032,1006,1032,165,1101,0,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1101,0,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,68,1044,1105,1,224,1101,0,0,1044,1106,0,224,1006,1044,247,101,0,1039,1034,102,1,1040,1035,1001,1041,0,1036,102,1,1043,1038,101,0,1042,1037,4,1044,1105,1,0,30,84,39,21,27,93,20,65,45,95,19,6,71,25,33,13,80,53,60,70,65,80,45,65,53,62,93,13,19,72,33,49,54,92,9,29,25,69,7,46,9,96,97,70,8,69,71,97,3,75,94,49,96,11,76,24,29,84,87,99,33,76,83,83,21,62,97,82,63,71,78,74,29,94,90,34,92,58,75,44,66,99,28,37,84,18,18,94,86,50,4,74,3,96,74,39,99,55,93,44,94,55,40,78,2,88,70,6,69,67,87,40,4,93,76,30,1,42,40,87,23,83,89,24,73,19,62,88,43,92,94,50,71,53,19,75,22,9,82,46,65,84,92,63,99,57,23,62,93,61,14,87,67,84,90,38,96,83,33,63,40,80,75,10,79,89,52,14,97,32,87,72,57,79,7,79,6,93,66,77,50,19,97,78,65,96,24,94,80,12,10,70,9,60,77,67,17,83,76,36,79,27,43,91,6,72,77,49,4,47,56,85,81,11,46,96,93,33,82,44,69,49,34,98,77,95,38,19,85,1,62,73,49,95,39,62,36,83,23,93,34,32,21,94,89,30,85,76,13,92,87,3,84,43,3,74,39,81,6,85,16,69,89,21,56,80,65,92,84,97,7,63,23,8,87,37,70,54,75,92,95,96,51,83,34,24,86,39,59,48,89,45,34,89,72,3,77,63,98,38,70,39,38,98,97,85,46,96,53,81,89,27,83,75,31,81,71,39,81,62,79,11,78,18,90,94,1,91,1,79,77,74,64,20,73,55,75,78,2,77,24,92,56,55,25,70,21,38,69,49,81,19,34,92,97,74,61,79,18,77,51,76,62,92,10,85,83,87,39,90,31,98,95,61,32,63,82,59,75,65,53,72,91,17,75,75,54,85,57,32,13,39,70,48,86,59,50,96,32,23,84,61,85,48,59,92,33,15,58,83,95,48,80,70,84,58,69,70,37,99,18,73,79,32,71,22,41,75,26,71,25,55,73,31,5,53,71,95,65,87,50,62,95,80,54,95,73,79,20,94,65,83,33,26,88,3,11,99,76,93,28,97,67,49,90,94,19,85,28,10,96,70,55,84,17,75,33,47,91,44,88,96,1,6,89,40,69,27,58,98,61,25,77,79,43,83,38,13,72,44,99,20,33,69,8,5,47,72,78,24,53,94,78,39,99,87,9,63,82,52,69,64,48,93,46,48,89,22,84,32,69,7,36,99,80,4,27,92,54,14,85,56,19,99,93,99,49,67,82,90,23,10,77,77,37,79,67,78,27,81,79,34,67,81,40,88,76,89,94,64,80,73,79,57,72,22,14,93,3,88,84,88,41,12,29,4,97,57,83,38,93,51,55,20,75,57,78,22,76,22,24,85,91,79,27,19,46,90,18,71,3,39,28,26,94,87,83,31,35,73,56,99,83,35,65,92,45,98,93,2,73,88,15,90,62,85,95,20,96,75,52,4,62,81,78,49,67,69,20,5,85,72,79,45,34,73,89,20,37,60,79,97,6,41,78,40,70,42,29,89,21,76,88,44,82,17,9,73,52,71,73,25,89,71,30,82,85,26,86,61,43,7,71,13,99,72,40,95,79,39,67,39,65,90,91,14,96,20,73,98,66,13,92,70,1,93,2,86,45,54,85,73,30,62,14,97,89,39,77,99,40,89,76,49,97,42,60,97,62,82,35,98,49,80,15,91,34,87,65,77,44,93,65,87,76,82,20,78,46,90,18,81,73,98,47,99,48,69,2,82,90,90,47,85,49,94,37,81,76,90,0,0,21,21,1,10,1,0,0,0,0,0,0'
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

#width = 220
#height = 220
#dx = width // 2
#dy = width // 2
width = 41
height = 40
dx = 21
dy = 21

maxx = -1
maxy = -1

origx = dx
origy = dy

last_input = -1
board = [[' ' for x in range(width)] for y in range(height)]
board[dy][dx] = '@'
found = False
ox = -1
oy = -1

count_items = 0 # 1574
override = False
# north (1), south (2), west (3), and east (4)
override_arr = [4,4,4,4,4,1,1,1,4,4,4,4,3,3,3,3,3,1,1,4,4,4,4,4,4,1,1,4,1,1,2]

"""
s = ''
for r in range(45,len(board) - 40):
  for c in range(80,160):
    if r == origy and c == origx:
      s = s + 'S'
    else:              
      s = s + board[r][c]
  s = s + '\n'
"""

while(not found and count_items < 1620):
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
        # north (1), south (2), west (3), and east (4)
        #print('input?',end =" ")
        #n = input()

        n = -1
        valid = False
        while not valid:
          """
          for n1 in range(1,5):
            tx = dx
            ty = dy
            if n1 == 1:
              ty = ty - 1
            elif n1 == 2:
              ty = ty + 1
            elif n1 == 3:
              tx = tx - 1
            elif n1 == 4:
              tx = tx + 1
            if board[ty][tx] == ' ':
              n = n1
              break
          if n < 0:
            n = random.randint(1,4)
          """
          n = random.randint(1,4)

          tx = dx
          ty = dy
          if n == 1:
            ty = ty - 1
          elif n == 2:
            ty = ty + 1
          elif n == 3:
            tx = tx - 1
          elif n == 4:
            tx = tx + 1
          if tx >= 0 and ty >= 0 and tx < width and ty < height:
            valid = True
        
        if override and len(override_arr) > 0:
            n = override_arr[0]
            del override_arr[0]
            if len(override_arr) == 0:
                override = False



        last_input = int(n)


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

        #print(x)
        # north (1), south (2), west (3), and east (4)
        newx = dx
        newy = dy
        if int(last_input) == 1:
          newy = newy - 1
        elif int(last_input) == 2:
          newy = newy + 1
        elif int(last_input) == 3:
          newx = newx - 1
        elif int(last_input) == 4:
          newx = newx + 1

        if int(x) == 0:
          # 0: The repair droid hit a wall. Its position has not changed.
          if board[newy][newx] == ' ':
            count_items = count_items + 1          
          board[newy][newx] = '#'
        elif int(x) == 2:
          # 2: The repair droid has moved one step in the requested direction; 
          #    its new position is the location of the oxygen system.
          if board[newx][newy] == ' ':
            count_items = count_items + 1          
          board[dy][dx] = '.'
          dx = newx
          dy = newy
          board[dy][dx] = '@'
          found = True
          override = True
          ox = newx
          oy = newy
          s = ''

          print('found oxygen system at y,x: ' + str(oy) + ',' + str(ox))    
          print('starty,startx: ' + str(origy) + ',' + str(origx))
          print('dy,dx: ' + str(dy) + ',' + str(dx))    
          print('maxy,maxx: ' + str(maxy) + ',' + str(maxx))

          """
          starty = -1
          startx = -1
          endy = -1
          endx = -1
          for y in range(0,len(board)):
            for x in range(0,len(board[y])):
              if board[y][x] != ' ':
                starty = y
                startx = x
                break
            if starty > 0:
              break
          for y in range(len(board)-1,-1,-1):
            for x in range(len(board[y])-1,-1,-1):
              if board[y][x] != ' ':
                endy = y
                endx = x
                break
            if endy > 0:
              break
          for y in range(starty+10,endy+10):
            for x in range(startx+10,endx+10):
              if y == origy and x == origx:
                s = s + 'S'
              else:
                s = s + board[y][x]
            s = s + '\n'
          """
          s = ''
          for r in range(0,len(board)):
            for c in range(0,len(board[r])):
              if r == origy and c == origx:
                s = s + 'S'
              else:              
                s = s + board[r][c]
            s = s + '\n'
          print(s)           
          #print('startx,starty: ' + str(startx) + ',' + str(starty)) 
          #print('endx,endy: ' + str(endx) + ',' + str(endy)) 

        elif int(x) == 1:
          # 1: The repair droid has moved one step in the requested direction.
          if board[dy][dx] == ' ':
            count_items = count_items + 1
          board[dy][dx] = '.'
          dx = newx
          dy = newy
          board[dy][dx] = '@'
          if dx > maxx:
            maxx = dx
          if dy > maxy:
            maxy = dy
          
          if override:
            s = ''
            for r in range(0,len(board)):
                for c in range(0,len(board[r])):           
                    s = s + board[r][c]
                s = s + '\n'
            print(s) 
        


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