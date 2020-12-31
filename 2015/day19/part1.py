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

r = set()
for key, value in d.items():
    for y in value:
        templ=[m.start() for m in re.finditer(key, molecule)]
        for i in templ:
            s1 = molecule[0:i] + y + molecule[i+len(key):]
            r.add(s1)

print('part 1: ' + str(len(r))) # 589 too high




print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')