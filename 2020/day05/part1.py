import sys
import time

start_secs = time.time()

# read in input file
l=[]
ids=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())


for p in l:
    low = 0
    high = 127
    row = -1
    col = -1
    for c in p:
        if c == 'F' or c == 'B':
            if c == 'F':
                high = high - ( ((high - low) + 1) // 2 )
            elif c == 'B':
                low = low +  ( ((high - low) + 1) // 2 )
            if high == low:
                row = high
                high = 7
                low = 0
        else:
            if c == 'L':
                high = high - ( ((high - low) + 1) // 2 )
            elif c == 'R':
                low = low +  ( ((high - low) + 1) // 2 )
            if high == low:
                col = high
    seat_id = row * 8 + col
    ids.append(seat_id)
    
ids.sort()
print('Part 1: ' + str(ids[len(ids)-1]))
    
    
            
    
            
            




end_secs = time.time()
print(str(end_secs-start_secs))