import sys
import time

start_secs = time.time()

# read in input file
l=[]
ids=[]
seats=[]
counts=[0] * 104
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
    #print('row ' + str(row) + ', column ' + str(col))
    seat_id = row * 8 + col
    if row != 8 and row != 103:
        counts[row] = counts[row] + 1
    # FOUND IT
    if row == 84:
        seats.append(str(row)+','+str(col))
    ids.append(seat_id)
    
ids.sort()
seats.sort()
#for i in range(0,len(counts)):
#    print(str(i) + ': ' + str(counts[i])) # it's row 84
    

#print(seats) # '84,0', '84,1', '84,2', '84,3', '84,4', '84,5', '84,7']
print('Part 2: ' + str(84*8+6))

    
            
            




end_secs = time.time()
print(str(end_secs-start_secs))