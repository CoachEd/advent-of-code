

import sys
import time
import math
import random
import functools

start_secs = time.time()

"""
Given the starting numbers 1,3,2, the 2020th number spoken is 1.
Given the starting numbers 2,1,3, the 2020th number spoken is 10.
Given the starting numbers 1,2,3, the 2020th number spoken is 27.
Given the starting numbers 2,3,1, the 2020th number spoken is 78.
Given the starting numbers 3,2,1, the 2020th number spoken is 438.
Given the starting numbers 3,1,2, the 2020th number spoken is 1836.
"""

n = [19,0,5,1,10,13]

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
        newnum=arr[-1]-arr[-2]
        nums[prev+1]=newnum
        if not newnum in d:
            d[newnum]=[turn]
        else:
            d[newnum].append(turn)
    else:
        nums[prev+1] = 0
        if not 0 in d:
            d[0] = [turn]
        else:
            d[0].append(turn)
    if turn  == 2020:
        break
    turn = turn + 1
    prev= prev+1

print('part 1: '+str(nums[turn-1]))
    
end_secs = time.time()
print()
print(str(end_secs-start_secs) + ' seconds')


