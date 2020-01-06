import sys
import time
import itertools

"""
LOL Brute force:

"A loud, robotic voice says "Analysis complete! You may proceed." and you enter the cockpit.
Santa notices your small droid, looks puzzled for a moment, realizes what has happened, and radios your ship directly.
"Oh, hello! You should be able to get in by typing 2214608912 on the keypad at the main airlock."
"""

"""
Parameter modes are stored in the same value as the instruction's opcode. 
The opcode is a two-digit number based only on the ones and tens digit of the value, that is, 
the opcode is the rightmost two digits of the first value in an instruction. 
Parameter modes are single digits, one per parameter, read right-to-left from the opcode: 
the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, 
the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.
"""

class IntcodeComputerOptimized:

    def __init__(self, prog_str, id):
        self.id = id
        self.addmem = [0 for i in range(1000)] # TODO: BUMP THIS UP IN CASE OF "Index out of range" errors
        self.arr=prog_str
        self.arr = self.arr.split(',')
        self.arr.extend(self.addmem)
        self.i = 0
        self.relbase = 0
        self.halt = False
        self.output_queue = []
        self.input_queue = []

        # determined winning commands after one successful pass!
        self.commands = ['north','take tambourine','south','south','south','take hypercube','north','north','west','take dark matter','west','north','west','take coin','south','south']

    def halt_computer(self):
      self.halt = True
    
    def execute_forever(self):
      while not self.halt:
        self.execute_instruction()

    def execute_instruction(self):

        if self.halt:
          print('program ended.')
          return []
        self.idle = False
        s = str(self.arr[self.i])

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
            self.halt = True

        elif opcode == '03':
            # INPUT
            #print('input?',end =" ")

            if len(self.input_queue) == 0:
              # waiting for user input
              
              #n = input()
              if len(self.commands) > 0:
                # collect phase
                n = self.commands.pop(0)
              else:
                n = input()


              command = str(n)
              for c1 in command:
                self.input_queue.append(ord(c1))
              self.input_queue.append(10)

            # process user input
            n = self.input_queue.pop(0)

            if pmodes[2] == '0':
              self.arr[int(self.arr[self.i+1])] = int(n)
            else:
              self.arr[int(self.arr[self.i+1])+self.relbase] = int(n)

            self.i = self.i + 2
        elif opcode == '04':
            # OUTPUT

            if pmodes[2] == '0':
              x = self.arr[int(self.arr[self.i+1])]
            elif pmodes[2] == '1':
              x = self.arr[self.i+1]
            else:
              x = self.arr[int(self.arr[self.i+1])+self.relbase]
            
            x = int(x)
            if x == 10:
              output_str = ''
              for elem in self.output_queue:
                output_str = output_str + chr(elem)
              self.output_queue = []
              print(output_str)
            else:
              self.output_queue.append(x)
            

            self.i = self.i + 2            
        elif opcode == '01':
            # add

            # parameter 1 - determine parameter mode
            if pmodes[2] == '0':  # absolute mode
              x = self.arr[int(self.arr[self.i+1])]
            elif pmodes[2] == '1':
              x = self.arr[self.i+1]  # position mode
            else:
              x = self.arr[int(self.arr[self.i+1])+self.relbase]  # relative mode

            # parameter 2 - determine parameter mode
            if pmodes[1] == '0':
              y = self.arr[int(self.arr[self.i+2])]
            elif pmodes[1]=='1':
              y = self.arr[self.i+2]
            else:
              y = self.arr[int(self.arr[self.i+2])+self.relbase]

            # parameter 3 - store the result (can only be position mode(0) or relative mode(2))
            if pmodes[0] == '0':
              self.arr[int(self.arr[self.i+3])] = int(x) + int(y)
            elif pmodes[0] == '2':
              self.arr[int(self.arr[self.i+3]) + self.relbase] = int(x) + int(y)

            self.i = self.i + 4
        elif opcode == '02':
            # multiply

            # parameter 1
            if pmodes[2] == '0':
              x = self.arr[int(self.arr[self.i+1])]
            elif pmodes[2] == '1':
              x = self.arr[self.i+1]
            else:
              x = self.arr[int(self.arr[self.i+1])+self.relbase]
                     
            # parameter 2
            if pmodes[1] == '0':
              y = self.arr[int(self.arr[self.i+2])]
            elif pmodes[1] == '1':
              y = self.arr[self.i+2]
            else:
              y = self.arr[int(self.arr[self.i+2])+self.relbase]  
            
            # parameter 3
            if pmodes[0] == '0':
              self.arr[int(self.arr[self.i+3])] = int(x) * int(y)
            elif pmodes[0] == '2':
              self.arr[int(self.arr[self.i+3])+self.relbase] = int(x) * int(y)
        
            self.i = self.i + 4
        elif opcode == '05':
            # jump-if-true
            """
            Opcode 5 is jump-if-true: if the first parameter is non-zero, 
            it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            """
            if pmodes[2] == '0':
              x = self.arr[int(self.arr[self.i+1])]
            elif pmodes[2] == '1':
              x = self.arr[self.i+1]
            else:
              x = self.arr[int(self.arr[self.i+1])+self.relbase]
            
            if pmodes[1] == '0':
              y = self.arr[int(self.arr[self.i+2])]
            elif pmodes[1] == '1':
              y = self.arr[self.i+2]
            else:
              y = self.arr[int(self.arr[self.i+2])+self.relbase]

            if int(x) != 0:
              self.i = int(y)
            else:
              self.i = self.i + 3
        elif opcode == '06':
            # jump-if-false
            """
            Opcode 6 is jump-if-false: if the first parameter is zero, 
            it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            """
            if pmodes[2] == '0':
              x = self.arr[int(self.arr[self.i+1])]
            elif pmodes[2] == '1':
              x = self.arr[self.i+1]
            else:
              x = self.arr[int(self.arr[self.i+1])+self.relbase]

            if pmodes[1] == '0':
              y = self.arr[int(self.arr[self.i+2])]
            elif pmodes[1] == '1':
              y = self.arr[self.i+2]
            else:
              y = self.arr[int(self.arr[self.i+2])+self.relbase]
            
            if int(x) == 0:
              self.i = int(y)
            else:
              self.i = self.i + 3
        elif opcode == '07':
            # is-less-than
            """
            Opcode 7 is less than: if the first parameter is less than the second parameter, 
            it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            """
            if pmodes[2] == '0':
              x = self.arr[int(self.arr[self.i+1])]
            elif pmodes[2] == '1':
              x = self.arr[self.i+1]
            else:
              x = self.arr[int(self.arr[self.i+1])+self.relbase]
            
            if pmodes[1] == '0':
              y = self.arr[int(self.arr[self.i+2])]
            elif pmodes[1] == '1':
              y = self.arr[self.i+2]
            else:
              y = self.arr[int(self.arr[self.i+2])+self.relbase]

            z = ''
            if int(x) < int(y):
              z = '1'
            else:
              z = '0'

            if pmodes[0] == '0':
              self.arr[int(self.arr[self.i+3])] = z
            elif pmodes[0] == '2':
              self.arr[int(self.arr[self.i+3])+self.relbase] = z

            self.i = self.i + 4
        elif opcode == '08':
            # is-equals
            """
            Opcode 8 is equals: if the first parameter is equal to the second parameter, 
            it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            """
            if pmodes[2] == '0':
              x = self.arr[int(self.arr[self.i+1])]
            elif pmodes[2] == '1':
              x = self.arr[self.i+1]
            else:
              x = self.arr[int(self.arr[self.i+1])+self.relbase]
            
            if pmodes[1] == '0':
              y = self.arr[int(self.arr[self.i+2])]
            elif pmodes[1] == '1':
              y = self.arr[self.i+2]
            else:
              y = self.arr[int(self.arr[self.i+2])+self.relbase]

            z = ''
            if int(x) == int(y):
              z = '1'
            else:
              z = '0'

            if pmodes[0] == '0':
              self.arr[int(self.arr[self.i+3])] = z
            elif pmodes[0] == '2':
              self.arr[int(self.arr[self.i+3])+self.relbase] = z

            self.i = self.i + 4
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
            x = self.arr[int(self.arr[self.i+1])]
          elif pmodes[2] == '1':
            x = self.arr[self.i+1]
          else:
            x = self.arr[int(self.arr[self.i+1])+self.relbase]
          
          self.relbase = self.relbase +int(x)
          self.i = self.i + 2
        else:
            # nothing
            pass



