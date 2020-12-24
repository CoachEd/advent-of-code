import sys
import time
from copy import copy, deepcopy



start_secs = time.time()

def print_grid(atemp):
    s = ''
    for y in range(len(atemp)):
        for x in range(len(atemp[y])):
            if atemp[y][x] == 1:
                s = s + '*'
            else:
                s = s + '.'
        s = s + '\n'
    print(s)

def neighbors(y,x,a1):

    """
    x,y
    Center: 0,0
    E: 1,0
    W: -1,0
    NE: 1,1
    NW: 0,1
    SE: 0,-1
    SW: -1.-1
    """
    n = [ [y,x+1],[y,x-1],[y+1,x+1],[y+1,x],[y-1,x],[y-1,x-1] ]
    black = 0
    for arr in n:
        y1 = arr[0]
        x1 = arr[1]
        if y1 >= 0 and y1 < maxy and x1 >= 0 and x1 < maxx:
            if a1[y1][x1] == 1:
                black = black + 1
    return black

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    line = line.strip().replace('se','1').replace('sw','2').replace('nw','3').replace('ne','4')
    l.append(line.strip())

maxx = 500
maxy = 500
refx = maxx // 2
refy = maxy // 2
a = [ [ -1 for x in range(maxx) ] for y in range(maxy) ] # -1 means white, 1 means black

"""
x,y
Center: 0,0
E: 1,0
W: -1,0
NE: 1,1
NW: 0,1
SE: 0,-1
SW: -1.-1

Directions: e, se, sw, w, nw, ne
Changed to: e, 1 , 2,  w ,3,  4
"""
for step in l:
    y=refy
    x=refx
    for c in step:
        if c == 'e':
            # e
            x = x + 1
            pass
        elif c == 'w':
            # w
            x = x - 1
            pass
        elif c == '1':
            # se
            y = y -1
            pass
        elif c == '2':
            # sw
            x = x - 1
            y = y - 1
            pass
        elif c == '3':
            # nw
            y = y + 1
            pass
        elif c == '4':
            # ne
            x = x + 1
            y = y + 1
            pass
    a[y][x] = a[y][x] * -1

black = 0
for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x] == 1:
            black = black + 1
print('part 1: ' + str(black))
print()

days = 100
for n in range(1,days+1):
    print('Day ' + str(n) + '...')
    a2 = deepcopy(a)
    for y in range(0,len(a)):
        for x in range(0,len(a[y])):
            black_tiles = neighbors(y,x,a)
            if a[y][x] == -1:
                # white
                if black_tiles == 2:
                    a2[y][x] = a2[y][x] * -1
            else:
                # black
                if black_tiles == 0 or black_tiles > 2:
                    a2[y][x] = a2[y][x] * -1
    a = a2

black = 0
for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x] == 1:
            black = black + 1
print('part 2: ' + str(black))



print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')