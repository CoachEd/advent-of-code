import sys
import time
from itertools import combinations

start_secs = time.time()
print()

# read in input file

l=[]
arr=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    line = line.strip()
    arr.append(int(line))

liters=150

count=0
min_size = sys.maxsize
keep = []
for i in range(4,len(arr)+1):
    combos = combinations(arr, i)
    for l in list(combos):
        sum1=0
        sz = 0
        for x in l:
            sum1=sum1+x
            sz = sz+1
        if sum1 == liters:
            keep.append(l)
            if sz < min_size:
                min_size = sz
        
count = 0
for e in keep:
    if len(e) == min_size:
        count = count +1
print('part 2: ' + str(count)) 


print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')