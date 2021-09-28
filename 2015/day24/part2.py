import sys
import time
from itertools import permutations
from functools import reduce

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append( int(line.replace("\r", "").replace("\n", "").strip()) )

weight = 0
for w in l:
  weight = weight + w
weight = weight // 4
print(weight)


minqe = sys.maxsize
for i in permutations(l , 4):
    if sum(i) == weight:
      qe = reduce(lambda x, y: x*y, i)
      if qe < minqe:
        minqe = qe

print(minqe)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')