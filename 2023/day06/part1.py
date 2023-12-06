# day 6 part 1
import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
#times = [7,15,30]
#distances = [9,40,200]

times = [54,81,70,88]
distances = [446,1292,1035,1007]


m = 1
for i in range(len(times)):
  t = times[i]
  d = distances[i]
  ways = 0
  for j in range(1,t):
    d1 = j * (t-j)
    if d1 > d:
      ways += 1
  m *= ways

print(m)
print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')

