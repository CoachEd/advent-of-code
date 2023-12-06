
#day 6 part 2
import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')
 
#times = [71530]
#distances = [940200]

#times = [7,15,30]
#distances = [9,40,200]
times = [54817088]
distances = [446129210351007]


m = 1
for i in range(len(times)):
  t = times[i]
  d = distances[i]
  ways = 0
  for j in range(1,t):
    d1 = j * (t-j)
    if d1 > d:
      ways += 1
  print(ways)

print('')

#sample answer 71503

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')