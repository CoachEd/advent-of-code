

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
    #print(d)
    #print('At t = ' + str(t) + '...')
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
# LCM: 867200349647749
s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
#t = 100000000000000
s='7,13,x,x,59,x,31,19'



#ALGORITHM
# run each number with first number to get offsets,
# least common multiplier is the repeating time when it will appear again
# 91, 413, 217, 133 (LCM: 3162341)
# Pattern:
# 1068781
# 4231122
# 7393463

# TESTS
t = 0 # orig: 100000000000000
#s = '2,x,7'
#s='7,13,x,x,59,x,31,19' # Ans: 1068781  #TRY: 91, 413, 217, 133 (LCM: 3,162,341)
#s='7,13'
#s='91,x,x,x,59'
#s='5369,x,31'
#s='166439,19'
# 91 413 217 133
#LCM 3162341
#ANS 1068781
# 91 413 217 133

#s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
#s='23,x,x,x,x,x,x,x,x,x,x,x,x,41' #943
#s='943,x,x,x,x,x,x,x,x,x,509' # 479987
#s='479987,x,x,x,x,x,x,x,x,x,x,x,x,13' # 6239831
#s='6239831,17' # 106077127
#s='106077127,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29' # 

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


for i in range(451763,451763+3162341):
    if get_times(times,i,d):
        print(i)
        break


sys.exit()

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
   




end_secs = time.time()
print()
print(str(end_secs-start_secs) + ' seconds')

