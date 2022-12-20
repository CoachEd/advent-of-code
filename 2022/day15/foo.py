import time
import sys
import numpy as np
from copy import copy, deepcopy
start_secs = time.time()
print('')
"""
p = [(12, 12), (2, 14), (2, 2), (-2, 2), (16, 24), (14, 18)]
p = sorted(p)
print(p)
ind = np.where(np.diff(np.array(p).flatten()) <= 0)[0]
arr = np.delete(p, [ind, ind+1]).reshape(-1, 2)
arr = list(map(tuple, arr))
print(arr)
"""

a = [(12, 12), (2, 14), (2, 2), (29,33), (-2, 2), (16, 24), (14, 18)]
b = []
for begin,end in sorted(a):
  if b and b[-1][1] >= begin - 1:
    b[-1][1] = max(b[-1][1], end)
  else:
    b.append([begin, end])
b = list(map(tuple, b))
print(b)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')