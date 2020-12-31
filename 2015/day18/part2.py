import sys
import time
import copy

start_secs = time.time()
print()

def is_stuck(r,c,l):
    if r == 0 and c == 0:
        return True
    if r == 0 and c == len(l[0])-1:
        return True
    if r == len(l[0])-1 and c == 0:
        return True
    if r == len(l[0])-1 and c == len(l[0])-1:
        return True
    return False

def count_lights(a):
    num = 0
    for r in range(len(a)):
        for c in range(len(a[r])):
            if a[r][c] == '#':
                num = num + 1
    return num

def print_lights(a):
    s = ''
    for r in range(len(a)):
        for c in range(len(a[r])):
            s = s + a[r][c]
        s = s + '\n'
    print(s)
    
def valid_coord(r,c,a):
    if r < 0 or c < 0 or r >= len(a) or c >= len(a[0]):
        return False
    return True
    
def get_neighbors(r,c,a):
    if not valid_coord(r,c,a):
        return 0
    n = 0
    for r1 in range(r-1,r+2):
        for c1 in range(c-1,c+2):
            if r == r1 and c == c1:
                continue
            if valid_coord(r1,c1,a) and a[r1][c1] == '#':
                n = n + 1   
    return n

# read in input file
l2=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l2.append(line.strip())

l = [ None for r in range(len(l2)) ]
temp = [ '.' for r in range(len(l2[0])) ]
j = 0
for s in l2:
    for i in range(0,len(s)):
        temp[i] = s[i]
    l[j] = temp.copy()
    j = j + 1

# stuck lights
l[0][0] = '#'
l[0][len(l[0])-1] = '#'
l[len(l[0])-1][0] = '#'
l[len(l[0])-1][len(l[0])-1] = '#'

t = 0
#print('Initial state:')
#print_lights(l)
while t < 100:
    l1 = copy.deepcopy(l)
    for r in range(0,len(l)):
        for c in range(0,len(l[r])):
            if is_stuck(r,c,l):
                continue
            n = get_neighbors(r,c,l)
            if l[r][c] == '#':
                if n != 2 and n != 3:
                    l1[r][c] = '.'
            else:
                if n == 3:
                    l1[r][c] = '#'
    l = l1
    t = t + 1
    #print('After step ' + str(t) + ':')
    #print_lights(l)


print('part 2: ' + str(count_lights(l)))
print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')