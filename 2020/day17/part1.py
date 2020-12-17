import sys
import time
import copy

start_secs = time.time()

def print_arr(a,minz,miny,minx,maxz,maxy,maxx):
    s = ''
    for z in range(minz,maxz+1):
        s = s + '\n'
        for y in range(miny,maxy+1):
            for x in range(minx,maxx+1):
                s = s + a[z][y][x]
            s = s + '\n'
        s = s + '\n'
    print(s)    

def add_neighbors(p,z,y,x):
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
    p.append([z,ty,tx])
    p.append([z,by,bx])
    p.append([z,ly,lx])
    p.append([z,ry,rx])
    p.append([z,tyr,txr])
    p.append([z,byr,bxr])
    p.append([z,tyl,txl])
    p.append([z,byl,bxl])
    p.append([z+1,y,x])
    p.append([z-1,y,x])    
    
    
def active(arr,z,y,x):
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
        num = num + (1 if arr[z][ty][tx] == '#' else 0)
        num = num + (1 if arr[z][by][bx] == '#' else 0)
        num = num + (1 if arr[z][ly][lx] == '#' else 0)
        num = num + (1 if arr[z][ry][rx] == '#' else 0)
        num = num + (1 if arr[z][tyr][txr] == '#' else 0)
        num = num + (1 if arr[z][byr][bxr] == '#' else 0)
        num = num + (1 if arr[z][tyl][txl] == '#' else 0)
        num = num + (1 if arr[z][byl][bxl] == '#' else 0)
    
    # check top and bottom center squares
    num = num + (1 if arr[z+1][y][x] == '#' else 0)
    num = num + (1 if arr[z-1][y][x] == '#' else 0)
    
    return num
    
# read in input file
max_size = 20
offset = max_size // 2
x1=offset
y1=offset
z1=offset
arr = [ [ ['.' for x in range(max_size)] for y in range(max_size) ] for z in range(max_size) ] 
l=[]
points=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

z = 0
for y in range(0,len(l)):
    for x in range(0, len(l[y])):
        arr[z1+z][y1+y][x1+x] = l[y][x]
        points.append([z1+z,y1+y,x1+x])
        if arr[z1+z][y1+y][x1+x] == '#':
            # also add its neighbors
            add_neighbors(points,z1+z,y1+y,x1+x)

"""
If a cube is active(#) and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
If a cube is inactive(.) but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
"""

cycles = 3
minz=sys.maxsize
miny=sys.maxsize
minx=sys.maxsize
maxz=0
maxy=0
maxx=0
s=''

arr2 = copy.deepcopy(arr)
for p in points:
    active_points = active(arr,p[0],p[1],p[2])
    if arr[p[0]][p[1]][p[2]] == '#':
        if active_points == 2 or active_points == 3:
            arr2[p[0]][p[1]][p[2]] = '#'
        else:
            arr2[p[0]][p[1]][p[2]] = '.'
    else:
        if active_points == 3:
            arr2[p[0]][p[1]][p[2]] = '#'
        else:
            arr2[p[0]][p[1]][p[2]] = '.'  
    
    if p[0] > maxz:
        maxz = p[0]
    if p[1] > maxy:
        maxy = p[1]
    if p[2] > maxx:
        maxx = p[2]
    if p[0] < minz:
        minz = p[0]
    if p[1] < miny:
        miny = p[1]
    if p[2] < minx:
        minx = p[2]

print('arr1:')
print_arr(arr,minz,miny,minx,maxz,maxy,maxx)

print('arr2:')
print_arr(arr2,minz,miny,minx,maxz,maxy,maxx)


end_secs = time.time()
print(str(end_secs-start_secs))