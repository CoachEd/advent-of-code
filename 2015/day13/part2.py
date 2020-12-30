import sys
import time
import itertools

start_secs = time.time()
print()

d = dict()
guests = ['Alice','Bob','Carol','David','Eric','Frank','George','Mallory','Ed']
happ = [ [ 0 for x in range(len(guests)) ] for y in range(len(guests)) ]
for i in range(0,len(guests)):
    d[guests[i]] = i
seating=list(itertools.permutations(guests))
    
# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    line = line.strip().replace('would','').replace('happiness units by sitting next to','').replace('.','')
    arr = line.split()
    y = d[arr[0].strip()]
    x = d[arr[3].strip()]
    eff = 1 if arr[1].strip()=='gain' else -1
    amt = int(arr[2].strip())
    happ[y][x] = eff * amt

max_happ = -1*sys.maxsize
for a in seating:
    tot_happ = 0
    for i in range(0,len(a)):
        n1 = i - 1
        n2 = i + 1
        if n1 < 0:
            n1 = len(a)-1
        if n2 > len(a)-1:
            n2 = 0
        tot_happ = tot_happ + happ[ d[a[i]] ][ d[a[n1]] ] + happ[ d[a[i]] ][ d[a[n2]] ] 
    if tot_happ > max_happ:
        max_happ = tot_happ
print('part 1: ' + str(max_happ))

print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')