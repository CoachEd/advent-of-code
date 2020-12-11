import sys
import time

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

"""
Preprocess/analysis - learn about the grid
row=0
col=0
maxr = -1
maxc = -1
minr = sys.maxsize
minc = sys.maxsize
s = l[0]
for c in s:
    if c == '^':
        row = row - 1
    elif c == 'v':
        row = row + 1
    elif c == '>':
        col = col + 1
    elif c == '<':
        col = col - 1
    if row > maxr:
        maxr = row
    if col > maxc:
        maxc = col
    if row < minr:
        minr = row
    if col < minc:
        minc = col

print('maxr: ' + str(maxr)) #48
print('minr: ' + str(minr)) #-43
print('maxc: ' + str(maxc)) #38
print('minc: ' + str(minc)) #-79
"""

# part 1
# 120x120 should be good and start in the middle, based on preprocessing/analysis
s = l[0]
rows = 120
cols = 120
row = rows // 2
col = cols // 2
a = [ [0]*cols for i in range(rows)]
a[row][col] = 1
for c in s:
    if c == '^':
        row = row - 1
    elif c == 'v':
        row = row + 1
    elif c == '>':
        col = col + 1
    elif c == '<':
        col = col - 1
    a[row][col] = a[row][col] + 1

count = 0
for row in range(0,len(a)):
    for col in range(0,len(a[row])):
        if a[row][col] > 0:
            count = count + 1
print('Part 1: ' + str(count))

# part 2
s = l[0]
rows = 120
cols = 120
row = rows // 2
col = cols // 2
row1 = row
col1 = col
a = [ [0]*cols for i in range(rows)]
a[row][col] = 2
santa = 1
for c in s:
    if c == '^':
        if santa > 0:
            row = row - 1
        else:
            row1 = row1 - 1 
    elif c == 'v':
        if santa > 0:
            row = row + 1
        else:
            row1 = row1 + 1             
    elif c == '>':
        if santa > 0:
            col = col + 1
        else:
            col1 = col1 + 1             
    elif c == '<':
        if santa > 0:
            col = col - 1
        else:
            col1 = col1 - 1              

    if santa > 0:
        a[row][col] = a[row][col] + 1
    else:
        a[row1][col1] = a[row1][col1] + 1
        
    santa = santa * -1

count = 0
for row in range(0,len(a)):
    for col in range(0,len(a[row])):
        if a[row][col] > 0:
            count = count + 1
print('Part 2: ' + str(count))



end_secs = time.time()
print(str(end_secs-start_secs))