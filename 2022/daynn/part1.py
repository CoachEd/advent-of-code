import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')


# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())
print(l)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')