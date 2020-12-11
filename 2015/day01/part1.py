import sys
import time

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

s = l[0]
print('Part 1: ' + str(s.count('(')-s.count(')')))

floor = 0
for i in range(0,len(s)):
    if s[i] == '(':
        floor = floor + 1
    else:
        floor = floor - 1
    if floor < 0:
        print('Part 2: ' + str(i+1))
        break

end_secs = time.time()
print(str(end_secs-start_secs))