

import sys
import time
import math
import random
import functools

start_secs = time.time()
print('running...')
def get_times(l,t):
    # arriving in table
    # t % bus ID = current minute in schedule (e.g., if 6, then bus 7 is arrving in 1 minute)
    print('At t = ' + str(t) + '...')
    for b in l:
        print('Bus ' + str(b) + ' arriving in ' + str(b-(t%b)) + ' minutes.')

s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
t = 100000000000000

#ALGORITHM
# run each number with first number to get offsets,
# least common multiplier is the repeating time when it will appear again
# 91, 413, 217, 133 (LCM: 3,162,341)
# Pattern:
# 1068781
# 4231122
# 7393463

# TESTS
t = 0 # orig: 100000000000000
#s = '2,x,7'
s='7,13,x,x,59,x,31,19' # Ans: 1068781  #TRY: 91, 413, 217, 133 (LCM: 3,162,341)
#s='7,13'
#s='91,x,x,x,59'
#s='5369,x,31'
#s='166439,19'
# 91 413 217 133
#LCM 3162341

# 91 413 217 133


#s='67,7,59,61' #  first occurs at timestamp 754018.
#s='67,x,7,59,61' #  first occurs at timestamp 779210.
#s='67,7,x,59,61' #  first occurs at timestamp 1261476.
#s='1789,37,47,1889' #  first occurs at timestamp 1202161486.

arr = s.split(',')
times=[]
d = dict()
offset = 0
for e in arr:
    if e != 'x':
        times.append(int(e))
        d[int(e)] = offset
    offset = offset + 1


#7,13,x,x,59,x,31,19
#find LCM least common multiplier among the times
#ans = functools.reduce(math.lcd, (7,13,59,31,19))
#print('lcd: ' + str(ans))
print(d)
iterations = 0
reps = 0
arr4=[]
while True:
    done = True
    for b, o in d.items():
        x = t % b
        if b == times[0]:
            if x != 0:
                # not a good time
                #print(str(t) + ': ')
                done = False
                break
            else:
                pass
                #print(str(t) + ': ' +  str(b))
        else:
            if b-x != o:
                # not a good time
                #print(str(t)+ ': ')
                done = False
                break
            else:
                pass
                #print(str(t) + ': ' +  str(b))
               

    if done:
        #get_times(times,t)
        print()
        print('Part 2: ' + str(t))
         
        arr4.append(t)
        reps = reps + 1
        if reps < 2:
            t = t + 1
            continue
        break
    #t = t + times[0]
    t = t + 1
   
       
    #if t > 1068788:
    #    print('not found')
    #    break

    #for b in times:
    #    if t % b != 0
    #if t % bus1 == 0:
    #    # bus1 arrived
    #    print(str(t) + ' bus ' + str(bus1) + ' arrived.')
   
print(arr4)
print(arr4[1]-arr4[0])



end_secs = time.time()
print()
print(str(end_secs-start_secs) + ' seconds')


