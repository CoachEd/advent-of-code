import sys
import time

start_secs = time.time()
print()
def print_arr(a):
    s=''
    for r in a:
        for c in r:
            s = s + str(c)
        s = s + '\n'
    print(s)

def rotate_arr(a):
    a2=[ [ None for x in range(len(a))] for y in range(len(a)) ]
    y2=0
    x2=len(a[0])-1
    for y in range(0,len(a)):
        for x in range(0,len(a[y])):
            a2[y2][x2] = a[y][x]
            y2=y2+1
        y2=0
        x2=x2-1
    return(a2)

def flip_arr(a):
    a2=[ [ None for x in range(len(a))] for y in range(len(a)) ]
    x2=len(a[0])-1
    for y in range(0,len(a)):
        for x in range(0,len(a[y])):
            a2[y][x2] = a[y][x]
            x2=x2-1
        x2=len(a[0])-1
    return(a2)

def get_edge(a,direction):
    direction=direction.upper()
    s=''
    if direction=='N':
        return(a[0])
    elif direction=='S':
        return(a[len(a)-1])
    elif direction=='E':
        x=len(a[0])-1
        temp=[ None for x in range(0,len(a[0]))]
        for y in range(0,len(a)):
            temp[y]=a[y][x]
        return temp
    elif direction=='W':
        x=0
        temp=[ None for x in range(0,len(a[0]))]
        for y in range(0,len(a)):
            temp[y]=a[y][x]
        return temp
    else:
        return []
    
def print_tile(a):
    s = ''
    for y in range(0,len(a)):
        for x in range(0,len(a[0])):
            s = s + a[y][x]
        s = s + '\n'
    print(s)

def print_tile_row(a,ids):
    s = ''
    # TODO
    print(s)
        
def get_row(id):
    row1 = [id]
    while True:
        tile1_id = row1[len(row1)-1]
        tile1 = tiles[tile1_id]
        for tile2_id in tiles:
            if tile2_id != tile1_id:
                found = False
                for j in range(0,2):
                    for i in range(0,4):
                        e1 = get_edge(tile1,'E')
                        e2 = get_edge(tiles[tile2_id],'W')
                        if e1 == e2:
                            #print('E-W: ' + str(tile1_id) + ' <-> ' + str(tile2_id))
                            found = True
                            row1.append(tile2_id)
                            break
                        tiles[tile2_id] = rotate_arr(tiles[tile2_id])
                    if found:
                        break
                    tiles[tile2_id] = flip_arr(tiles[tile2_id])   
                if found:
                    break   
        if len(row1) == 12:
            break   
    #print(row1)
    return row1    
        
def find_north(id):
    # find north
    tile1_id = id
    tile1 = tiles[tile1_id]
    for tile2_id in tiles:
        if tile2_id != tile1_id:
            found = False
            for j in range(0,2):
                for i in range(0,4):
                    e1 = get_edge(tile1,'N')
                    e2 = get_edge(tiles[tile2_id],'S')
                    if e1 == e2:
                        #print(' ' + str(tile1_id) + ' <-> ' + str(tile2_id))
                        found = True
                        return tile2_id
                        break
                    tiles[tile2_id] = rotate_arr(tiles[tile2_id])
                if found:
                    break
                tiles[tile2_id] = flip_arr(tiles[tile2_id])   
            if found:
                break 
    return None

def find_south(id):
    # find south
    tile1_id = id
    tile1 = tiles[tile1_id]
    for tile2_id in tiles:
        if tile2_id != tile1_id:
            found = False
            for j in range(0,2):
                for i in range(0,4):
                    e1 = get_edge(tile1,'S')
                    e2 = get_edge(tiles[tile2_id],'N')
                    if e1 == e2:
                        #print(' ' + str(tile1_id) + ' <-> ' + str(tile2_id))
                        found = True
                        return tile2_id
                        break
                    tiles[tile2_id] = rotate_arr(tiles[tile2_id])
                if found:
                    break
                tiles[tile2_id] = flip_arr(tiles[tile2_id])   
            if found:
                break 
    return None

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
num_tiles = 0
for line in lines: 
    if line.find('Tile') != -1:
        num_tiles = num_tiles + 1
    l.append(line.strip())

# 144 tiles
# look for 12x12
# 10 x 10 tiles
tiles = dict()

id_count = 0
temparr = []
rowarr = []
for i in range(0,len(l)):
    if l[i].find('Tile') != -1:
        arr = l[i].split()
        tileid = int(arr[1].replace(':',''))
        id_count = id_count + 1
    elif len(l[i]) == 0:
        tiles[tileid] = temparr
        temparr = []
    else:
        rowarr = []
        for c in l[i]:
            rowarr.append(c)
        temparr.append(rowarr)

#print_tile(tiles[2381]) # output individual tile
"""
N-S: 3637 <-> 2221
N-S: 2221 <-> 1399
N-S: 1399 <-> 3607
N-S: 3607 <-> 3371
N-S: 3371 <-> 1889
N-S: 1889 <-> 3533
N-S: 3533 <-> 3677
N-S: 3677 <-> 2879

N-S: 3637 <-> 1787
N-S: 1787 <-> 2293
N-S: 2293 <-> 1321
"""

final_arr = []

# find north rows
r = get_row(3637)
final_arr.insert(0,r)

n1 = find_north(3637)
r = get_row(n1)
final_arr.insert(0,r)

n1 = find_north(n1)
r = get_row(n1)
final_arr.insert(0,r)

n1 = find_north(n1)
r = get_row(n1)
final_arr.insert(0,r)

n1 = find_north(n1)
r = get_row(n1)
final_arr.insert(0,r)

n1 = find_north(n1)
r = get_row(n1)
final_arr.insert(0,r)

n1 = find_north(n1)
r = get_row(n1)
final_arr.insert(0,r)

n1 = find_north(n1)
r = get_row(n1)
final_arr.insert(0,r)

n1 = find_north(n1)
r = get_row(n1)
final_arr.insert(0,r)

# now find south rows
n1 = find_south(3637)
r = get_row(n1)
final_arr.append(r)

n1 = find_south(n1)
r = get_row(n1)
final_arr.append(r)

n1 = find_south(n1)
r = get_row(n1)
final_arr.append(r)


for r in final_arr:
    print(str(r))
    
print()
ans = final_arr[0][0] * final_arr[0][len(final_arr[0])-1] * final_arr[len(final_arr)-1][0] * final_arr[len(final_arr)-1][len(final_arr)-1]
print('part1: ' + str(ans)) # 31992776618119 (too high) 13879642730771 (too low)

end_secs = time.time()
print()
print(str(end_secs-start_secs)) 