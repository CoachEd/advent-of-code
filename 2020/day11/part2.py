import sys
from copy import copy, deepcopy
import time

start_secs = time.time()

def v(l,r,c):
    b1 = r >= 0 and r < len(l)
    b2 = c >= 0 and c < len(l[0])
    if (b1 and b2):
        return l[r][c]
    else:
        return 'X'

def seats(l,r,c):
    
    i=1
    s1=''
    s2=''
    s3=''
    s4=''
    s5=''
    s6=''
    s7=''
    s8=''
    n=''
    while True:
        tr=r-i
        tc=c
        br=r+i
        bc=c
        rr=r
        rc=c+i
        lr=r
        lc=c-i
        trr=r-i
        trc=c+i
        brr=r+i
        brc=c+i
        tlr=r-i
        tlc=c-i
        blr=r+i
        blc=c-i

        if s1 == '' or s1 == '.':
            s1 = v(l,tr,tc)
        if s2 == '' or s2 == '.':
            s2 = v(l,br,bc)
        if s3 == '' or s3 == '.':
            s3= v(l,rr,rc)
        if s4 == '' or s4 == '.':
            s4 = v(l,lr,lc)
        if s5 == '' or s5 == '.':
            s5=v(l,trr,trc)
        if s6 == '' or s6 == '.':
            s6=v(l,brr,brc)
        if s7 == '' or s7 == '.':
            s7=v(l,tlr,tlc)
        if s8 == '' or s8 == '.':
            s8=v(l,blr,blc)
        i=i+1
        n=s1+s2+s3+s4+s5+s6+s7+s8
        if n.count('.') == 0:
            break
    #1966
    return n

l=[]

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(line.strip())

rows = len(l)
cols = len(l[0])

a = [ [None]*cols for i in range(rows)]
for r in range(0,len(a)):
    for c in range(0,len(a[r])):
        	a[r][c] = l[r][c]

phs=0
while True:        	
    #print(phs)
    z = deepcopy(a)
    changes = False
    for r in range(0,len(a)):
        for c in range(0,len(a[r])):
            s = seats(a,r,c)
            occ = s.count('#')
            emp = s.count('L')
            if a[r][c] == 'L' and occ==0:
                changes = True
                z[r][c] = '#'
            elif a[r][c] == '#' and occ >= 5:
                changes = True
                z[r][c] = 'L'
    phs = phs + 1
    a = z
    if not changes:
        break

occ = 0
for r in range(0,len(a)):
    for c in range(0,len(a[r])):
        if a[r][c] == '#':
            occ = occ +1
print('part 2: ' + str(occ))
end_secs = time.time()
print()
print(str(end_secs-start_secs))           

#If a seat is empty (L) and there are 
#no occupied seats adjacent to it, 
#the seat becomes occupied.

#If a seat is occupied (#) and five
#or more seats adjacent to it are 
#also occupied, the seat becomes empty.

#Otherwise, the seat's state does 
#not change.



