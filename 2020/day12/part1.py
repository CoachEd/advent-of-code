import sys
from copy import copy, deepcopy
import time

start_secs = time.time()

def getQuadrant(r,c,wr,wc):
    wposr = r + wr
    wposc = c + wc
    quadrant = 0
     
    if wposr <= r and wposc <= c:
        quadrant = 3
    elif wposr <= r and wposc >= c:
        quadrant = 2
    elif wposr >= r and wposc >= c:
        quadrant = 1
    elif wposr >= r and wposc <= c:
        quadrant = 4        
    return quadrant

l=[]

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(line.strip())

# NSEWLRF
row=0
col=0
f='E'
ha=['N','E','S','W']
hi=1
for s in l:
    c = s[0:1]
    n = int(s[1:])
    if c == 'N' or (c=='F' and f=='N'):
        row=row+n
    elif c=='S'  or (c=='F' and f=='S'):
        row=row-n
    elif c=='E'  or (c=='F' and f=='E'):
        col=col+n
    elif c =='W'  or (c=='F' and f=='W'):
        col=col-n
    elif c == 'L':
        ni=n//90
        for i2 in range(0,ni):
            hi  = hi - 1
            if hi < 0:
                hi = 3
        f=ha[hi]
    elif c == 'R':
        ni=n//90
        for i2 in range(0,ni):
            hi  = hi + 1
            if hi >3:
                hi = 0
        f=ha[hi]
        
print('Part 1: '+ str(abs(row)+abs(col)))      
                
# PART 2
row=0
col=0
wrow=row+1
wcol=col+10
ha=['N','E','S','W']
quadrant = 1
hi=1
mult=1
for s in l:
    c = s[0:1]
    n = int(s[1:])
    if c == 'N':
        wrow=wrow+n
        quadrant = getQuadrant(row,col,wrow,wcol)
    elif c=='S':
        wrow=wrow-n
        quadrant = getQuadrant(row,col,wrow,wcol)
    elif c=='E':
        wcol=wcol+n
        quadrant = getQuadrant(row,col,wrow,wcol)
    elif c =='W':
        wcol=wcol-n
        quadrant = getQuadrant(row,col,wrow,wcol)
    elif c == 'F':
        row = row + wrow*n
        col = col + wcol*n      
    elif c == 'R':
        ni=n//90
        for i2 in range(0,ni):
            quadrant = quadrant + 1
            if quadrant > 4:
                quadrant = 1
            tmp = wrow
            wrow = wcol
            wcol = tmp
            hi  = hi + 1
            if hi >3:
                hi = 0
        f=ha[hi]
        wrow = abs(wrow)
        wcol = abs(wcol)        
        if quadrant == 2:
            wrow = wrow * -1
        elif quadrant == 3:
            wrow = wrow * -1
            wcol = wcol * -1
        elif quadrant == 4:
            wcol = wcol * -1
    elif c == 'L':
        ni=n//90
        for i2 in range(0,ni):
            quadrant = quadrant - 1
            if quadrant < 1:
                quadrant = 4            
            tmp = wrow
            wrow = wcol
            wcol = tmp            
            hi  = hi - 1
            if hi < 0:
                hi = 3
        f=ha[hi]
        wrow = abs(wrow)
        wcol = abs(wcol)        
        if quadrant == 2:
            wrow = wrow * -1
        elif quadrant == 3:
            wrow = wrow * -1
            wcol = wcol * -1
        elif quadrant == 4:
            wcol = wcol * -1

print('Part 2: '+ str(abs(row)+abs(col)))                
end_secs = time.time()
print('--- ' + str(end_secs-start_secs)+ ' secs ---')                
   