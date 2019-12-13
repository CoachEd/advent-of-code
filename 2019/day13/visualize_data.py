import sys
import time
import copy

start_secs = time.time()
addmem = [0 for i in range(1000000)]

#works
#arr = '104,1125899906842624,99'
#arr='1102,34915192,34915192,7,4,7,99,0'
#arr='109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'

arr='1,380,379,385,1008,2639,310356,381,1005,381,12,99,109,2640,1101,0,0,383,1101,0,0,382,20102,1,382,1,21002,383,1,2,21101,0,37,0,1105,1,578,4,382,4,383,204,1,1001,382,1,382,1007,382,40,381,1005,381,22,1001,383,1,383,1007,383,25,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1106,0,161,107,1,392,381,1006,381,161,1101,-1,0,384,1106,0,119,1007,392,38,381,1006,381,161,1102,1,1,384,21002,392,1,1,21101,23,0,2,21101,0,0,3,21102,138,1,0,1105,1,549,1,392,384,392,20102,1,392,1,21102,1,23,2,21102,1,3,3,21102,161,1,0,1106,0,549,1101,0,0,384,20001,388,390,1,21002,389,1,2,21101,180,0,0,1105,1,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,21001,389,0,2,21102,1,205,0,1106,0,393,1002,390,-1,390,1102,1,1,384,20102,1,388,1,20001,389,391,2,21102,228,1,0,1106,0,578,1206,1,261,1208,1,2,381,1006,381,253,21001,388,0,1,20001,389,391,2,21102,253,1,0,1105,1,393,1002,391,-1,391,1101,0,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21101,0,279,0,1105,1,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21101,0,304,0,1105,1,393,1002,390,-1,390,1002,391,-1,391,1101,0,1,384,1005,384,161,20102,1,388,1,20101,0,389,2,21101,0,0,3,21101,0,338,0,1106,0,549,1,388,390,388,1,389,391,389,20101,0,388,1,21001,389,0,2,21102,4,1,3,21101,0,365,0,1105,1,549,1007,389,24,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,348,18,20,1,1,20,109,3,21201,-2,0,1,21202,-1,1,2,21102,1,0,3,21101,414,0,0,1105,1,549,21202,-2,1,1,21201,-1,0,2,21101,429,0,0,1105,1,601,1201,1,0,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2106,0,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,22101,0,-3,-7,109,-8,2106,0,0,109,4,1202,-2,40,566,201,-3,566,566,101,639,566,566,1201,-1,0,0,204,-3,204,-2,204,-1,109,-4,2105,1,0,109,3,1202,-1,40,593,201,-2,593,593,101,639,593,593,21001,0,0,-2,109,-3,2105,1,0,109,3,22102,25,-2,1,22201,1,-1,1,21101,0,503,2,21101,366,0,3,21102,1,1000,4,21101,630,0,0,1105,1,456,21201,1,1639,-2,109,-3,2106,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,2,0,2,2,2,0,0,0,2,0,0,2,0,2,2,2,0,0,2,0,0,2,0,2,2,2,2,0,2,2,2,0,0,0,1,1,0,0,0,2,2,0,2,2,2,2,0,2,0,2,2,2,2,2,0,2,0,0,0,2,2,2,2,2,2,0,0,0,2,0,2,2,0,0,1,1,0,0,2,2,0,2,0,0,2,2,0,2,2,2,0,2,0,0,0,0,2,2,2,2,0,2,2,0,2,0,0,0,0,2,2,2,2,0,1,1,0,2,2,0,0,0,0,2,2,2,0,2,2,2,0,2,0,0,2,2,2,2,0,2,2,2,0,2,0,2,2,0,0,0,2,2,2,0,1,1,0,2,2,2,2,2,2,2,0,2,0,2,0,0,2,0,2,0,2,0,2,0,2,2,0,2,0,0,0,2,2,0,2,2,2,0,0,0,1,1,0,0,0,2,0,0,2,0,2,0,0,2,0,0,0,2,2,0,2,0,0,0,0,0,2,2,0,2,0,2,2,2,0,2,0,0,2,0,1,1,0,2,0,2,2,2,0,0,2,2,0,2,0,2,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,2,0,2,0,0,0,2,2,0,1,1,0,0,2,2,2,0,0,2,2,2,2,0,0,2,0,0,2,2,2,2,2,2,0,2,0,0,0,2,2,0,2,2,2,2,0,2,0,0,1,1,0,0,2,2,0,0,2,2,0,2,2,0,0,2,2,2,0,0,0,0,2,2,0,2,0,2,0,2,0,0,0,0,0,0,0,2,2,0,1,1,0,0,2,0,2,2,2,2,2,2,0,0,2,2,2,0,0,2,2,2,2,2,0,0,2,0,0,2,0,2,0,2,2,0,0,0,2,0,1,1,0,2,0,2,0,2,0,2,2,2,0,0,0,0,2,0,2,0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,0,1,1,0,2,2,2,0,2,2,2,2,2,0,0,2,2,2,0,0,0,0,0,2,0,2,0,2,2,0,2,0,0,0,0,2,2,2,2,0,0,1,1,0,2,2,2,0,2,0,2,0,0,0,0,2,0,0,2,0,0,2,2,2,2,2,0,2,0,2,0,2,2,2,0,0,2,0,0,2,0,1,1,0,0,2,2,2,2,0,2,2,2,2,0,2,0,2,2,0,2,0,2,2,0,0,2,2,2,2,2,0,2,2,2,2,2,0,2,2,0,1,1,0,2,0,2,2,2,0,0,2,0,2,2,0,2,2,0,2,0,0,2,2,0,2,2,0,2,2,0,2,2,0,2,2,2,0,2,0,0,1,1,0,2,0,0,2,2,0,0,0,0,2,0,0,2,0,2,2,2,0,2,2,0,2,2,2,0,2,0,2,0,2,0,0,2,2,0,0,0,1,1,0,2,2,2,2,2,2,0,2,2,0,2,2,2,0,2,2,2,2,2,0,2,0,2,0,0,2,2,2,2,2,2,0,0,0,2,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,24,35,13,44,44,95,83,45,69,64,58,57,22,91,79,21,65,90,94,24,82,6,96,96,64,21,91,4,36,76,6,74,41,72,32,87,50,48,47,93,86,73,24,78,50,10,95,14,50,78,6,90,98,26,68,75,40,73,80,89,1,41,68,42,47,58,32,23,48,11,83,74,68,41,55,89,46,8,27,5,3,81,42,88,49,51,55,91,22,93,13,12,10,87,42,90,35,88,12,94,79,76,89,39,71,69,32,5,72,45,12,79,57,35,60,46,28,34,79,3,97,32,52,77,66,26,55,8,89,2,76,20,49,64,72,50,15,21,22,63,19,22,44,11,44,36,4,77,24,25,29,8,31,27,68,91,90,89,18,53,67,92,68,59,7,56,2,88,83,82,83,5,73,19,53,81,85,65,93,10,21,46,69,90,32,17,37,31,69,96,93,10,98,32,86,73,91,95,13,15,83,72,10,4,52,64,35,52,42,55,4,76,13,39,54,31,51,78,62,40,14,11,81,34,93,97,47,67,26,46,86,80,69,6,8,56,12,80,88,49,20,79,40,7,54,63,15,46,64,59,74,28,11,48,27,41,20,27,29,70,73,46,18,21,48,26,42,63,7,80,54,8,43,31,3,39,10,30,7,98,87,33,62,81,61,31,64,27,94,38,42,39,55,9,61,38,76,8,48,13,94,8,85,23,72,84,6,60,18,25,30,64,37,97,59,71,16,83,83,18,92,53,39,17,73,39,37,30,9,2,87,32,23,56,11,24,1,84,82,5,8,60,55,44,57,43,14,88,72,51,83,20,3,70,33,33,1,6,86,17,4,77,69,33,65,93,97,66,42,23,34,96,4,25,76,46,2,34,52,5,17,87,69,15,22,3,87,80,36,1,70,43,56,64,11,47,39,5,64,1,41,54,34,95,42,17,8,68,73,45,54,84,16,83,59,27,56,75,34,44,78,70,19,25,90,52,65,58,1,72,2,70,3,26,11,69,73,74,29,8,22,2,93,18,98,16,10,62,92,44,70,69,86,53,2,43,62,45,18,22,46,87,48,21,56,36,71,91,94,84,95,28,74,64,16,44,27,35,33,41,66,9,74,3,94,78,3,47,91,66,92,10,2,6,45,57,24,83,4,56,25,24,51,77,39,36,28,20,6,27,14,25,54,15,84,5,29,16,98,21,32,94,93,5,75,67,65,89,32,16,79,71,31,89,9,5,39,12,14,34,61,9,80,1,65,59,48,48,46,60,98,1,29,98,57,17,18,76,49,93,13,28,37,88,37,46,4,19,48,10,58,37,47,13,85,23,10,48,77,68,92,62,74,63,7,21,31,20,53,87,74,9,32,80,91,70,9,95,90,37,61,60,26,22,56,26,79,65,58,88,51,7,42,43,89,90,11,10,27,19,10,76,96,34,55,36,2,67,11,25,15,96,35,27,50,78,12,8,77,76,26,49,77,60,41,14,24,3,52,52,49,25,35,45,21,98,1,61,2,32,55,86,55,48,28,15,69,97,42,85,90,58,1,75,8,91,60,26,9,70,86,16,50,95,52,90,17,54,1,98,12,25,13,26,94,47,24,23,54,54,65,65,94,61,14,58,35,72,23,98,32,4,84,36,58,38,98,59,1,6,56,1,43,56,33,31,39,64,88,60,30,41,98,17,89,7,15,76,20,43,44,60,65,94,32,71,12,67,87,38,35,56,84,31,12,33,5,42,66,87,47,21,4,52,16,74,18,10,32,97,76,68,76,59,77,92,65,6,15,32,32,14,2,64,67,14,34,3,44,39,56,60,88,56,88,1,76,14,20,67,53,98,74,88,90,67,40,41,56,27,81,58,93,41,78,31,28,12,25,28,94,20,18,41,40,79,10,96,1,64,57,90,30,83,87,71,75,73,63,48,18,10,39,96,60,87,24,54,73,96,6,7,32,26,18,20,4,42,33,63,76,14,21,74,72,3,85,59,16,43,3,22,11,29,96,8,51,32,5,35,94,84,48,58,17,37,58,98,64,63,63,96,31,24,67,29,85,34,29,63,42,68,53,10,47,61,87,33,74,6,76,71,38,52,56,69,32,4,11,44,34,67,13,2,92,55,69,31,15,21,24,7,54,71,93,64,53,67,24,61,25,90,4,95,85,15,44,32,86,11,10,3,32,26,43,18,98,89,82,19,34,30,74,24,96,14,79,46,87,22,53,66,60,91,40,75,92,66,13,33,13,29,55,69,77,34,87,49,83,57,76,42,11,53,27,42,82,28,46,91,310356'
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
output_arr = []
score_counter = 0
block_counter = 0
max_x = -1
max_y = -1
score_arr = []
ballx = 18
bally = 20
prevballx = -1
prevbally = -1
paddlex = 20
paddley = 23
balldirection = 1
movingup = False
board = []
changes = []

display = [[' ' for i in range(41)] for j in range(25)]

arr[0] = 2  # play for free?

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
        #print('input?',end =" ")
        #n = input()

        if paddlex == ballx:
          n = 0
        elif paddlex < ballx:
          n = 1
        else:
          n = -1


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

        output_arr.append(x)
        if len(output_arr) == 3:
          # process
          #The software draws tiles to the screen with output instructions: 
          # every three output instructions specify the x position (distance from the left), 
          # y position (distance from the top), and tile id. The tile id is interpreted as follows:

          #0 is an empty tile. No game object appears in this tile.
          #1 is a wall tile. Walls are indestructible barriers.
          #2 is a block tile. Blocks can be broken by the ball.
          #3 is a horizontal paddle tile. The paddle is indestructible.
          #4 is a ball tile. The ball moves diagonally and bounces off objects.          
          xpos = int(output_arr[0])
          ypos = int(output_arr[1])
          if xpos == -1 and ypos == 0:
              #print()
              #print('*********************score: ' + str(output_arr[2]))
              score_arr.append(int(output_arr[2]))
              #print()
          else:
            
            tileid = int(output_arr[2])
            changes.append([xpos,ypos,tileid])
            if tileid == 0:
              # empty
              display[ypos][xpos] = '-'
              pass
            elif tileid == 1:
              # wall
              display[ypos][xpos] = '#'
              pass
            elif tileid == 2:
              # block
              display[ypos][xpos] = 'B'
              block_counter = block_counter + 1
              pass
            elif tileid == 3:
              # paddle
              display[ypos][xpos] = '~'
              paddlex = xpos
              paddley = ypos
              pass
            elif tileid == 4:
              # ball
              prevballx = ballx
              prevbally = bally              

              ballx = xpos
              bally = ypos
              display[ypos][xpos] = 'O'
              pass

          output_arr = []

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

print(score_arr[-1])
print(changes)
end_secs = time.time()
print('\nelapsed time: ' + str(end_secs - start_secs) + ' seconds')