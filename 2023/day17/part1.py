import time
import sys
from copy import copy, deepcopy

# read in input file
fname = 'inp2.txt'
with open(fname, 'r') as file:
  data = file.read()
lines = data.split('\n')
l=[None for i in range(len(lines))]
for i in range(len(lines)):
  l[i] = lines[i].strip()
#print(l)

# SOLUTION START - start timing
start_secs = time.time()


# TODO


end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
# SOLUTION END - stop timing