import sys
import time
import math
import random
import functools

start_secs = time.time()
print('running...')
def get_times(l,t,d):
    # arriving in table
    # t % bus ID = current minute in schedule (e.g., if 6, then bus 7 is arrving in 1 minute)
    for i in range(0,len(l)):
        b = l[i]
        if i == 0:
            if b-(t%b) != b:
                return False
        else:
            if b-(t%b) != d[b]:
                return False
        #print('Bus ' + str(b) + ' arriving in ' + str(b-(t%b)) + ' minutes.')
    return True

# INPUT DATA
s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
t = 0

s='7,13,x,x,59,x,31,19' # ANSWER  1068781   LCM: 3162341 (product of all numbers)
s='7,13,x,x,59,x,31' # ANSWER 70147, then every 166439. BTW, 70147 * 998634 = 1068781
t = 0

arr = s.split(',')
times=[]
d = dict()
offset = 0
for e in arr:
    if e != 'x':
        times.append(int(e))
        d[int(e)] = offset
    offset = offset + 1

found = False

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
                done = False
                break
        else:
            if b-x != o:
                done = False
                break

    if done:

        # TESTING
        if True:
            reps = reps + 1
            print(t)
            if (reps < 3):
                t = t + times[0]
                continue
            print()

        print('Part 2: ' + str(t))
        break
    t = t + times[0]

end_secs = time.time()
print()
print(str(end_secs-start_secs) + ' seconds')