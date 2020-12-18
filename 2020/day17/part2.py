import sys
import time
import copy

start_secs = time.time()
sz = 100
a = [ [[['.' for x in range(sz)] for y in range(sz)] for z in range(sz)] for w in range(sz) ]

minz=sys.maxsize
miny=sys.maxsize
minx=sys.maxsize
minw=sys.maxsize
maxz=0
maxy=0
maxx=0
maxw=0

def count_active(a):
    global minx
    global miny
    global minz
    global minw
    global maxx
    global maxy
    global maxz 
    global maxw
    n = 0
    for w in range(minw,maxw+1):
        for z in range(minz,maxz+1):
            for y in range(miny,maxy+1):
                for x in range(minx,maxx+1):
                    if a[w][z][y][x] == '#':
                        n = n + 1
    return n

def cycle_arr(a):
    global minx
    global miny
    global minz
    global minw
    global maxx
    global maxy
    global maxz 
    global maxw      
    a2=copy.deepcopy(a)
    """
    print_arr(a)
    print('minw: ' + str(minw))
    print('maxw: ' + str(maxw))
    print('minz: ' + str(minz))
    print('maxz: ' + str(maxz))
    print('miny: ' + str(miny))
    print('maxy: ' + str(maxy))
    print('minx: ' + str(minx))
    print('maxx: ' + str(maxx))
    sys.exit()
    """
    for w in range(minw,maxw+1):
        for z in range(minz,maxz+1):
            for y in range(miny,maxy+1):
                for x in range(minx,maxx+1):
                    n = active_neighbors(a,z,y,x,w)
                    c = a[w][z][y][x]
                    if c == '#':
                        if n != 2 and n != 3:
                            a2[w][z][y][x] = '.'
                    elif c == '.':
                        if n == 3:
                            a2[w][z][y][x] = '#'
                    else:
                        print('SHOULD NOT GET HERE!')
    return a2

def active_neighbors(arr,z,y,x,w):
    global minx
    global miny
    global minz
    global minw
    global maxx
    global maxy
    global maxz 
    global maxw 
    num = 0
    
    for w1 in range(minw,maxw+1):
        for z1 in range(minz,maxz+1):
            for y1 in range(miny,maxy+1):
                for x1 in range(minx,maxx+1):
                    if w1==w and z1==z and y1==y and x1==x:
                        continue
                    if abs(w-w1) <= 1 and abs(z-z1) <= 1 and abs(y-y1) <= 1 and abs(x-x1) <= 1:
                        if arr[w1][z1][y1][x1] == '#':
                            num = num + 1
    return num    

def print_arr(a):
    global minx
    global miny
    global minz
    global minw
    global maxx
    global maxy
    global maxz 
    global maxw
    setBounds(a) # set min/max x,y,z,w

    s = ''
    for w in range(minw,maxw+1):
        for z in range(minz,maxz+1):
            s = s + 'z=' + str(z) + ' w=' + str(w) + '\n'
            for y in range(miny,maxy+1):
                for x in range(minx,maxx+1):
                    if a[w][z][y][x] == '#':
                        s = s + a[w][z][y][x]
                    else:
                        s = s + '.'
                s = s + '\n'
            s = s + '\n'
        s = s + '\n'
    print(s)

def setBounds(arr):
    global minx
    global miny
    global minz
    global minw
    global maxx
    global maxy
    global maxz 
    global maxw
    # set the min and max x,y,z
    for w in range(0,sz):
        for z in range(0,sz):
            for y in range(0,sz):
                for x in range(0,sz):
                    if arr[w][z][y][x] == '#':
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
                        if w > maxw:
                            maxw = w
                        if w < minw:
                            minw = w                            
    minx = minx - 1
    miny = miny - 1
    minz = minz - 1
    minw = minw - 1
    maxx = maxx + 1
    maxy = maxy + 1
    maxz = maxz + 1
    maxw = maxw + 1
            
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
start_w=sz // 2
s = ''
w1=start_w
z1=start_z
y1=start_y
for y in range(0, len(l)):
    x1=start_x
    for x in range(0,len(l[y])):
        if l[y][x] == '#':
            a[w1][z1][y1][x1] = '#'
            s = s + '#'
        else:
            s = s + '.'
        x1=x1+ 1
    s = s + '\n'
    y1=y1+1

#If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
#If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
setBounds(a)
num_cycles = 6
for cycles in range(0,num_cycles):
    print('After ' + str(cycles+1) + ' cycle(s)...')
    a = cycle_arr(a)
    setBounds(a)
    #print_arr(a)
    #print_arr(a)
    print('----')
print('part 2: ' + str(count_active(a)))


end_secs = time.time()
print('----- ' + str(end_secs-start_secs) + ' seconds ----- ') # 6224 too high (47 mins)