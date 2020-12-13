import sys
import time

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip().replace('turn',''))

cols = 1000
rows = 1000
a = [ [-1]*cols for i in range(rows)]

# Part 1
#toggle|off|on 370,39 through 425,839 (y,x)
for s in l:
    arr = s.split()
    cmd = arr[0]
    arr2 = arr[1].split(',')
    y1 = int(arr2[0])
    x1 = int(arr2[1])
    arr3 = arr[3].split(',')
    y2 = int(arr3[0])
    x2 = int(arr3[1])
    for r in range(y1,y2+1):
        for c in range(x1,x2+1):
            if cmd == 'on':
                a[r][c] = 1
            elif cmd == 'off':
                a[r][c] = -1
            elif cmd == 'toggle':
                a[r][c] = a[r][c] * -1

cnt = 0
for r in range(0,rows):
    for c in range(0,cols):
       if a[r][c] == 1:
           cnt = cnt + 1 
print('Part 1: ' + str(cnt))

# Part 2
a = [ [0]*cols for i in range(rows)]
for s in l:
    arr = s.split()
    cmd = arr[0]
    arr2 = arr[1].split(',')
    y1 = int(arr2[0])
    x1 = int(arr2[1])
    arr3 = arr[3].split(',')
    y2 = int(arr3[0])
    x2 = int(arr3[1])
    for r in range(y1,y2+1):
        for c in range(x1,x2+1):
            if cmd == 'on':
                a[r][c] = a[r][c] + 1
            elif cmd == 'off':
                a[r][c] = a[r][c] - 1
                if a[r][c] < 0:
                    a[r][c] = 0
            elif cmd == 'toggle':
                a[r][c] = a[r][c] + 2

brightness = 0
for r in range(0,rows):
    for c in range(0,cols):
        brightness = brightness + a[r][c]
print('Part 2: ' + str(brightness))





end_secs = time.time()
print(str(end_secs-start_secs))