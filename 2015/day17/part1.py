import sys
import time

start_secs = time.time()
print()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(int(line.strip()))

# fit 150 liters of egg nog



print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')