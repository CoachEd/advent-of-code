import sys
import time
import re

start_secs = time.time()
print()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# Al => ThF
d = dict()
for i in range(0,len(l)):
    s = l[i]
    if len(s) == 0:
        molecule = l[i+1]
        break
    else:
        arr = s.replace(' ','').split('=>')
        if not arr[0] in d:
            d[arr[0]] = [arr[1]]
        else:
            d[arr[0]].append(arr[1])

for key, val in d.items():
    print(key + ' : ' + str(val))


n = 0
print('part 2: ' + str(n)) 




print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')