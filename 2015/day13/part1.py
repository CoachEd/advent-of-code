import sys
import time
import itertools

start_secs = time.time()
print()

d = dict()
guests = ['Alice','Bob','Carol','David','Eric','Frank','George','Mallory']
for i in range(0,len(guests)):
    d[guests[i]] = i
seating=list(itertools.permutations(guests))
    
# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())



print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')