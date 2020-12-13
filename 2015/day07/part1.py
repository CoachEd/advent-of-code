import sys
import time

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

d = dict()
for s in l:
    arr = s.split('->')
    dest = arr[1].strip()
    arr2 = arr[0].split()
    if arr2[0] == 'NOT':
        operand = arr2[1].strip()
        if operand in d:
            d[dest] = ~d[operand]
    elif len(arr2) == 1:
        # assign value to wire
        if arr2[0].isdigit():
            d[dest] = int(arr2[0])
        else:
            if arr2[0] in d:
                d[dest] = d[arr2[0]]
    else:
        b1 = False
        b2 = False
        lft = arr2[0]
        if lft.isdigit():
            lft = int(lft)
            b1 = True
        op = arr2[1]
        rgt = arr2[2]
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
                d[dest] = lft & rgt
            elif op == 'OR':
                d[dest] = lft | rgt
            elif op == 'LSHIFT':
                d[dest] = lft << rgt
            elif op == 'RSHIFT':
                d[dest] = lft >> rgt

                
print(d)
print('Part 1: ' + d['a'])
        

end_secs = time.time()
print(str(end_secs-start_secs))