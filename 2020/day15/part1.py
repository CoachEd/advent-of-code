

import sys
import time
import math
import random
import functools

start_secs = time.time()

n = [19,0,5,1,10,13]
n=[0,3,6]


size=2020+1
nums = n + [None]*size
d=dict()
turn = 1
for e in n:
    d[e]=[turn]
    turn = turn + 1
    
prev=len(n)-1
while True:
    arr = d[nums[prev]]
    if len(arr) > 1:
        lturn=arr[-1]
        newnum=turn-lturn
        nums[prev+1]=newnum
        if not newnum in d:
            d[newnum]=[turn]
        else:
            d[newnum].append(turn)
    else:
        nums[prev+1] = 0
        d[0].append(turn)
        
    if turn  == 10:
        break
    turn = turn + 1
    prev= prev+1
print(nums)
print('part 1: '+str(nums[turn-1]))
    


end_secs = time.time()
print()
print(str(end_secs-start_secs) + ' seconds')


