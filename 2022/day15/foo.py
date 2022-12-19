import time
import sys
import numpy as np
from copy import copy, deepcopy
start_secs = time.time()
print('')
p = [(4, 8), (6, 10), (11, 12), (15, 20), (20, 25)] 

ind = np.where(np.diff(np.array(p).flatten()) <= 0)[0]
arr = np.delete(p, [ind, ind+1]).reshape(-1, 2)
arr = list(map(tuple, arr))
print(arr)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')