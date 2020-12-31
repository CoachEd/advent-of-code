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
for i in range(4,len(arr)+1):
    combos = combinations(arr, i)
    for l in list(combos):
        sum1=0
        for x in l:
            sum1=sum1+x
        if sum1 == liters:
            count=count+1
        

print('part 1: ' + str(count)) 


print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')