import sys
from copy import copy, deepcopy
import time

start_secs = time.time()

rst = '\x1b[0m' # reset to defaults
fgg = '\x1b[92m'
hm = '\033[1;1H' # x,y 1,1
def print_seats(l,chg):

    #sys.stdout.write('\033[0;0H') # reset cursor pos
    s = '\n'+hm+'\n\n'
    for r in range(0,len(l)):
        for c in range(0,len(l[r])):
            if chg[r][c] == 1:
                s = s + fgg + l[r][c]+ rst
            else:
                s = s + l[r][c]
        s = s + '\n'
    sys.stdout.write(s+rst)
    time.sleep(0.10)



def v(l,r,c):
    b1 = r >= 0 and r < len(l)
    b2 = c >= 0 and c < len(l[0])
    if (b1 and b2):
        return l[r][c]
    else:
        return ''

def seats(l,r,c):
    tr=r-1
    tc=c
    br=r+1
    bc=c
    rr=r
    rc=c+1
    lr=r
    lc=c-1
    trr=r-1
    trc=c+1
    brr=r+1
    brc=c+1
    tlr=r-1
    tlc=c-1
    blr=r+1
    blc=c-1

    n  = ''
    n  = n + v(l,tr,tc)
    n  = n + v(l,br,bc)
    n  = n + v(l,rr,rc)
    n  = n + v(l,lr,lc)
    n  = n + v(l,trr,trc)
    n  = n + v(l,brr,brc)
    n  = n + v(l,tlr,tlc)
    n  = n + v(l,blr,blc)
    return n

l=[]

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(line.strip())

rows = len(l)
cols = len(l[0])
chg = [ [None]*cols for i in range(rows)]
a = [ [None]*cols for i in range(rows)]
for r in range(0,len(a)):
    for c in range(0,len(a[r])):
        a[r][c] = l[r][c]
        chg[r][c] = 0

phs=0
print_seats(a,chg)
while True:        	
    #print(phs)
    z = deepcopy(a)
    chg2=deepcopy(chg)
    changes = False
    for r in range(0,len(a)):
        for c in range(0,len(a[r])):
            s = seats(a,r,c)
            occ = s.count('#')
            emp = s.count('L')
            if a[r][c] == 'L' and occ==0:
                changes = True
                z[r][c] = '#'
                chg2[r][c] = 1
            elif a[r][c] == '#' and occ >= 4:
                changes = True
                z[r][c] = 'L'
                chg2[r][c] = 1
    phs = phs + 1
    a = z
    print_seats(a,chg2)
    if not changes:
        break

occ = 0
for r in range(0,len(a)):
    for c in range(0,len(a[r])):
        if a[r][c] == '#':
            occ = occ +1
print('part 1: ' + str(occ))
       
end_secs = time.time()
print()
print(str(end_secs-start_secs))    
#If a seat is empty (L) and there are 
#no occupied seats adjacent to it, 
#the seat becomes occupied.

#If a seat is occupied (#) and four 
#or more seats adjacent to it are 
#also occupied, the seat becomes empty.

#Otherwise, the seat's state does 
#not change.



