import sys
import time
import copy
import numpy as np 

start_secs = time.time()
sz = 1000
offset = sz // 2
a = np.zeros((sz,sz,sz)) # z,y,x

def getp(z,y,x):
    return a[z+offset][y+offset][x+offset]
def setp(z,y,x,v):
    a[z+offset][y+offset][x+offset] = v

minz=sys.maxsize
miny=sys.maxsize
minx=sys.maxsize
maxz=0
maxy=0
maxx=0

def setBounds(arr):
    global minx
    global miny
    global minz
    global maxx
    global maxy
    global maxz
    # set the min and max x,y,z
    for z in range(0,len(arr)):
        for y in range(0,len(arr[z])):
            for x in range(0,len(arr[z][y])):
                if getp(z,y,x) == 1:
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
    minx = minx - 2 - offset
    miny = miny - 2 - offset
    minz = minz - 2 - offset
    maxx = maxx + 2 - offset
    maxy = maxy + 2 - offset
    maxz = maxz + 2 - offset
            
# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

z=0
for y in range(0, len(l)):
    for x in range(0,len(l[y])):
        if l[y][x] == '#':
            setp(z,y,x,1)

#data2 = copy.deepcopy(data) # 2D list of points

setBounds(a) # set min/max x,y,z
s = ''
for z in range(minz,maxz+1):
    s = s + 'z=' + str(z) + '\n'
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            s = s + str(getp(z,y,z))
        s = s + '\n'
print(s)            



#plt.show()  # show 3D plot
