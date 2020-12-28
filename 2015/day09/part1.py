import sys
import time
import itertools


start_secs = time.time()
print()

d=dict()
d['AlphaCentauri'] = 0
d['Snowdin'] = 1
d['Tambi'] = 2
d['Faerun'] = 3
d['Norrath'] = 4
d['Straylight'] = 5
d['Tristram'] = 6
d['Arbre'] = 7

cities = ['AlphaCentauri','Snowdin','Tambi','Faerun','Norrath','Straylight','Tristram','Arbre']
routes=list(itertools.permutations(cities))

l=[]
darr=[ [ 0 for c in range(8)] for r in range(8) ]

my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())
for s in l:
    arr = s.split('=')
    arr2 = arr[0].strip().split()
    dist=int(arr[1].strip())
    r=d[arr2[0]]
    c=d[arr2[2]]
    darr[r][c] = dist
    darr[c][r] = dist

mind = sys.maxsize    
for r in routes:
    newd=0
    good = True
    for i in range(0,len(r)-1):
        c1=r[i]
        c2=r[i+1]
        row=d[c1]
        col=d[c2]
        if darr[row][col] == 0:
            good = False
            #print('no route from ' + c1 + ' to ' + c2)
            break
        newd = newd + darr[row][col]
    if good and newd < mind:
        mind = newd
print('part 1: '+str(mind))
#316 too high



print()
end_secs = time.time()
print(str(end_secs-start_secs))