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

"""
..................#.
#....##....##....###
.#..#..#..#..#..#...
"""
mpos = [[0,18],[1,0],[1,5],[1,6],[1,11],[1,12],[1,17],[1,18],[1,19],[2,1],[2,4],[2,7],[2,10],[2,13],[2,16]]
def find_monster(a):
    mposy = -1
    mposx = -1
    monster_coords = []
    for y in range(0,len(a)):
        found = True
        for x in range(0,len(a[y])):
            found = True
            for p in mpos:
                check_y = y+p[0]
                check_x = x+p[1]
                if check_y >= len(a) or check_x >= len(a[y]):
                    found = False
                    break
                #print('checking... ' + str(y) + ',' + str(x))
                if a[check_y][check_x] != '#':
                    # not a monster; get new xy
                    found = False
                    break
            if found:
                mposy = y
                mposx = x
                monster_coords.append([mposy,mposx])
                #print('monster at: y,x: ' + str(mposy)+',' + str(mposx))
                #break
        if found:
            #break
            pass
    return monster_coords
     
def remove_monsters(a,monster_coords):
    for p in monster_coords:
        for y in range(0,3):
            for x in range(0,20):
                y1 = p[0] + y
                x1 = p[1] + x
                if [y,x] in mpos:
                    a[y1][x1] = '.'
    count = 0
    for r in a:
        for c in r:
            if c == '#':
                count = count + 1
    return count                

def print_monsters(a,monster_coords):
    
    # color grey
    for y in range(0,len(a)):
        for x in range(0,len(a[y])):
            a[y][x] = '\x1b[90m' + a[y][x] + '\x1b[0m'

    for p in monster_coords:
        for y in range(0,3):
            for x in range(0,20):
                y1 = p[0] + y
                x1 = p[1] + x
                if [y,x] in mpos:
                    a[y1][x1] = '\x1b[92m#\x1b[0m'

    s = ''
    for r in a:
        for c in r:
          s = s + c
        s = s + '\n'
    print(s)  
    return

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

def remove_border(a):
    arr1 = []
    for y in range(1,len(a)-1):
        temp = []
        for x in range(1,len(a[y])-1):
            temp.append(a[y][x])
        arr1.append(temp)
    return arr1
            

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

# remove borders from all tiles
for r in final_arr:
    for id in r:
        tiles[id] = remove_border(tiles[id]) 

# combine tiles
a = [ [' ' for x in range(96)] for y in range(96) ]
offsety=0
offsetx=0
for r in final_arr:
    print(r)
    for id in r:
        tile = tiles[id]
        for y in range(0,len(tile)):
            for x in range(0,len(tile[y])):
                a[offsety+y][offsetx+x] = tile[y][x]
        offsetx = offsetx + 8
    offsety = offsety + 8
    offsetx = 0   

        
print_arr(a)
a = rotate_arr(a)
a = rotate_arr(a)
monster_coords = find_monster(a)
#print( remove_monsters(a,monster_coords))
print_monsters(a,monster_coords)

"""
a = rotate_arr(a)
print( find_monster(a) )
a = rotate_arr(a)
print( find_monster(a) )

a = flip_arr(a)
print( find_monster(a) )

a = rotate_arr(a)
print( find_monster(a) )

a = rotate_arr(a)
print( find_monster(a) )

a = rotate_arr(a)
print( find_monster(a) )

a = rotate_arr(a)
print( find_monster(a) )

a = rotate_arr(a)
print( find_monster(a) )
"""

    
ans = ''
print('part2: ' + str(ans)) # 31992776618119 (too high) 13879642730771 (too low)

end_secs = time.time()
print()
print(str(end_secs-start_secs)) 