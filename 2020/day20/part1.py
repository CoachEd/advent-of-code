import sys
import time

start_secs = time.time()

def print_tile(a):
    s = ''
    for y in range(0,10):
        for x in range(0,10):
            s = s + a[y][x]
        s = s + '\n'
    print(s)

def print_tile_row(a,ids):
    s = ''
    # TODO
    print(s)
        


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

print_tile(tiles[2381]) # output individual tile

end_secs = time.time()
print(str(end_secs-start_secs))