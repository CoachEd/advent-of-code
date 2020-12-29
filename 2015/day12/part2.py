import sys
import time
import re
import json

start_secs = time.time()



print()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# TODO
s = l[0]

    


arr = re.split('\[|\]|\{|\}|:|,',s)
sum = 0
for s in arr:
    if s.isdigit():
        sum = sum + int(s)
    if len(s) > 1 and s[0] == '-' and s[1:].isdigit():
        sum = sum + -1*int(s[1:])
print('part 1: ' + str(sum)) 

print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')