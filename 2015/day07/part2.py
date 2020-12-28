import sys
import time
import numpy as np

start_secs = time.time()

def hasInstr(s):
    if s.find('AND') != -1 or s.find('OR') != -1 or s.find('NOT') != -1 or s.find('LSHIFT') != -1 or s.find('RSHIFT') != -1:
        return True
    else:
        return False

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

d = dict()
i = 0
while len(l) > 0:
    if hasInstr(l[i]):
        arr = l[i].split('->')
        var = arr[-1].strip()
        arr2 = arr[0].strip().split()
        if l[i].find('NOT') != -1:
            operand = arr2[1].strip()
            if operand in d:
                d[var] = ~d[operand]
                del l[i]
        else:
            b1 = False
            b2 = False
            lft = arr2[0]
            op = arr2[1]
            rgt = arr2[2]
            if lft.isdigit():
                lft = int(lft)
                b1 = True
            if rgt.isdigit():
                rgt = int(rgt)
                b2 = True
            if not b1:
                b1 = lft in d
                if b1:
                    lft = d[lft]
            if not b2:
                b2 = rgt in d
                if b2:
                    rgt = d[rgt]
            if b1 and b2:
                # have operands, do cmd
                if op == 'AND':
                    d[var] = lft & rgt
                elif op == 'OR':
                    d[var] = lft | rgt
                elif op == 'LSHIFT':
                    d[var] = lft << rgt
                elif op == 'RSHIFT':
                    d[var] = lft >> rgt    
                del l[i]        
    else:
        # no instr
        arr = l[i].split('->')
        var = arr[1].strip()
        val = arr[0].strip()
        if val.isdigit():
            val = int(val)
            d[var] = val
            if var == 'b':
                d[var] = 956 # override for Part 2
            del l[i]
        else:
            if val in d:
                d[var] = d[val]
                del l[i]
        
    i = i + 1
    if i >= len(l):
        i = 0

print('part 1: ' + str(np.uint16(d['a'])))


end_secs = time.time()
print(str(end_secs-start_secs))