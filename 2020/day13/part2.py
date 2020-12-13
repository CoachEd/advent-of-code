import sys
import time
import math
import random

start_secs = time.time()

def get_times(l,t):
    # arriving in table
    # t % bus ID = current minute in schedule (e.g., if 6, then bus 7 is arrving in 1 minute)
    print('At t = ' + str(t) + '...')
    for b in l:
        print('Bus ' + str(b) + ' arriving in ' + str(b-(t%b)) + ' minutes.')

s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
s='7,13,x,x,59,x,31,19' # Ans: 1068781
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
    
print(times)


#7,13,x,x,59,x,31,19
#find LCM least common multiplier among the times
#a = [7,13,59,31,19]
#lcm = a[0]
#for i in a[1:]:
#  lcm = lcm*i//math.gcd(lcm, i)
#print(lcm)
#print('lcm: ' + str(ans))
#get_times(a,931)

t = 0 # orig: 100000000000000
iterations = 0
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
                # not a good time
                done = False
                break

    if done:
        #get_times(times,t)
        print()
        print('Part 2: ' + str(t))
        break
    t = t + 1
    
        
    #if t > 1068788:
    #    print('not found')
    #    break

    #for b in times:
    #    if t % b != 0
    #if t % bus1 == 0:
    #    # bus1 arrived
    #    print(str(t) + ' bus ' + str(bus1) + ' arrived.')
    

end_secs = time.time()
print()
print(str(end_secs-start_secs))

