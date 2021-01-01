import sys
import time
import re
import random

start_secs = time.time()
print()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

molecule=l[-1]
del l[-1]
del l[-1]
# Al => ThF

minsteps=sys.maxsize

d = dict()
for i in range(0,len(l)):
    s = l[i]
    arr = s.replace(' ','').split('=>')
    d[arr[1]] = arr[0]
    
steps=0
while True:
    changes=False
    for key, val in d.items():
        if molecule.find(key) != -1:
            steps=steps+1
            changes=True
        molecule=molecule.replace(key,val,1)
        if molecule == 'e':
            break
    if not changes:
        break
print()
print('part 2: ' + str(steps)) 




print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')