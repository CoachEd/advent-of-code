import sys
import time
import copy

start_secs = time.time()
sz = 30
a = [[['.' for x in range(sz)] for y in range(sz)] for z in range(sz)]

minz=sys.maxsize
miny=sys.maxsize
minx=sys.maxsize
maxz=0
maxy=0
maxx=0

def count_active(a):
    global minx
    global miny
    global minz
    global maxx
    global maxy
    global maxz 
    n = 0
    for z in range(minz,maxz+1):
        for y in range(miny,maxy+1):
            for x in range(minx,maxx+1):
                if a[z][y][x] == '#':
                    n = n + 1
    return n

def cycle_arr(a):
    global minx
    global miny
    global minz
    global maxx
    global maxy
    global maxz       
    a2=copy.deepcopy(a)
    for z in range(minz,maxz+1):
        for y in range(miny,maxy+1):
            for x in range(minx,maxx+1):
                n = active_neighbors(a,z,y,x)
                c = a[z][y][x]
                if c == '#':
                    if n != 2 and n != 3:
                        a2[z][y][x] = '.'
                elif c == '.':
                    if n == 3:
                        a2[z][y][x] = '#'
                else:
                    print('SHOULD NOT GET HERE!')
    return a2

def active_neighbors(arr,z,y,x):
    global minx
    global miny
    global minz
    global maxx
    global maxy
    global maxz   
    num = 0
    
    ty=y-1
    tx=x
    by=y+1
    bx=x
    ly=y
    lx=x-1
    ry=y
    rx=x+1
    tyr=y-1
    txr=x+1
    byr=y+1
    bxr=x+1
    tyl=y-1
    txl=x-1
    byl=y+1
    bxl=x-1
    for z1 in range(z-1,z+2):
        num = num + (1 if arr[z1][ty][tx] == '#' else 0)
        num = num + (1 if arr[z1][by][bx] == '#' else 0)
        num = num + (1 if arr[z1][ly][lx] == '#' else 0)
        num = num + (1 if arr[z1][ry][rx] == '#' else 0)
        num = num + (1 if arr[z1][tyr][txr] == '#' else 0)
        num = num + (1 if arr[z1][byr][bxr] == '#' else 0)
        num = num + (1 if arr[z1][tyl][txl] == '#' else 0)
        num = num + (1 if arr[z1][byl][bxl] == '#' else 0)
    
    # check top and bottom center squares
    num = num + (1 if arr[z+1][y][x] == '#' else 0)
    num = num + (1 if arr[z-1][y][x] == '#' else 0)
    
    return num    

def print_arr(a):
    global minx
    global miny
    global minz
    global maxx
    global maxy
    global maxz
    setBounds(a) # set min/max x,y,z
    s = ''
    for z in range(minz,maxz+1):
        s = s + 'z=' + str(z) + '\n'
        for y in range(miny,maxy+1):
            for x in range(minx,maxx+1):
                if a[z][y][x] == '#':
                    s = s + a[z][y][x]
                else:
                    s = s + '.'
            s = s + '\n'
        s = s + '\n'
    print(s)

def setBounds(arr):
    global minx
    global miny
    global minz
    global maxx
    global maxy
    global maxz
    # set the min and max x,y,z
    for z in range(0,sz):
        for y in range(0,sz):
            for x in range(0,sz):
                if arr[z][y][x] == '#':
                    if x > maxx:
                        maxx = x
                    if x < minx:
                        minx = x
                    if y > maxy:
                        maxy = y
                    if y < miny:
                        miny = y
                    if z > maxz:
                        maxz = z
                    if z < minz:
                        minz = z
    minx = minx - 1
    miny = miny - 1
    minz = minz - 1
    maxx = maxx + 1
    maxy = maxy + 1
    maxz = maxz + 1
            
# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# start in the middle
start_z=sz // 2
start_x=sz // 2
start_y=sz // 2
s = ''
z1=start_z
y1=start_y
for y in range(0, len(l)):
    x1=start_x
    for x in range(0,len(l[y])):
        if l[y][x] == '#':
            a[z1][y1][x1] = '#'
            s = s + '#'
        else:
            s = s + '.'
        x1=x1+ 1
    s = s + '\n'
    y1=y1+1

#If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
#If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.

num_cycles = 6
for cycles in range(0,num_cycles+1):
    #print('After ' + str(cycles) + ' cycle(s):')
    a = cycle_arr(a)
    setBounds(a)

print('part 1: ' + str(count_active(a)))

end_secs = time.time()
print('----- ' + str(end_secs-start_secs) + 'seconds ----- ')