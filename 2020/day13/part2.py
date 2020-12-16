
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
        #print('Bus ' + str(b) + ' arriving in ' + str(b-(t%b)) + ' minutes.')
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
s='23,x,x,x,x,x,x,x,x,x,x,x,x,41'
t=0
every=1
# 69,943

s='41,x,x,x,x,x,x,x,x,x,509'
t= 69+13
every=943


s='509,x,x,x,x,x,x,x,x,x,x,x,x,13'
t=398028 + 10
every=479987

s='13,17'
t=4717921+ 13
every=6239831


s='17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'
t= 35917089 + 1
every= 106077127


s='29,x,401'
t= 2687845265+15
every= 3076236683


s='401,x,x,x,x,x,37'
t= 107279892502+2
every= 1233570909883


s='37,x,x,x,x,x,x,x,x,x,x,x,x,19'
t= 43282261738409+6
every= 45642123665671

#ans: 
#     225850756401099 ?????
#evr: 867200349647749



s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
#t=225850756401099
#every=1




#s='23,x,x,x,x,x,x,x,x,x,x,x,x,41' # 69, every 943
#s='41,x,x,x,x,x,x,x,x,x,509'  # 398028, every 479987
#s='509,x,x,x,x,x,x,x,x,x,x,x,x,13' # 4717921, every 6239831
#s='13,17' # 35917089 , every 106077127
#s='17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'  # 2687845265, every 3076236683
#s='29,x,401' # 107279892502 , every 1233570909883
#s='401,x,x,x,x,x,37' # 43282261738409 , every 45642123665671
#s='37,x,x,x,x,x,x,x,x,x,x,x,x,19' # ******* ANSWER: 225850756401099 (- 73 = 225850756401026) (225850756401099 - 12)
                                                  # 100000000000000
                                                  # WRONG: 225850756401026, 225850756401099
#t=43282261738409+ 6  # prev answer +  spots away
#every= 45642123665671 # every from prev answer


# SAMPLE TRY 1
#s='7,13,x,x,59,x,31,19'
#s='7,13' # ans,evr 77,91
#s='13,x,x,59'
#s='59,x,31'
#s='31,19'
#t= 70151+2 # prev+spots
#every= 166439
#real answer 1068788
#ans:        1068787


#SAMPLE TRY 2
#s='7,x,x,x,59,x,x,19' #REAL ANSWER: 1589
#t=0
#every=1
#s='7,x,x,x,59' # ans: 350, evr: 413
#t=0
#every=1
#s='59,x,x,19' # ans: 1593  (subtract the +4 = 1589) ??????
#t=350+4
#every=413


#s='4,x,x,5,6' # 32 , then every 60
#s='4,x,x,5' # 12 , then every 20
#s='5,6' # 35 - 3 (spots back) = 32
#t=12+3    # 12+3
#every = 20

# sample tests
#s='67,7,59,61' # first occurs at timestamp 754018.
#s='67,x,7,59,61' # first occurs at timestamp 779210.
#s='67,7,x,59,61' # first occurs at timestamp 1261476.
#s='1789,37,47,1889' # first occurs at timestamp 1202161486.

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

"""
s='67,7,59,61' # first occurs at timestamp 754018.
s='67,x,7,59,61' # first occurs at timestamp 779210.
s='67,7,x,59,61' # first occurs at timestamp 1261476.
s='1789,37,47,1889' # first occurs at timestamp 1202161486.
"""
#print(get_times(times,754018,d))
#print(get_times(times,779210,d))
#print(get_times(times,1261476,d))
#print(get_times(times,1202161486,d))
#sys.exit()

# ATTEMPT
#print(get_times(times,225850756401099-6,d))
#sys.exit()


t=225850756401099
  
for i in range(100000000000000,t+100000000000000):
    b = get_times(times,i,d)
    if b:
        print(i)
        break
sys.exit()




print()
print('Running...')
#t=225850756400993
#for i in range(t,999999999999999,1):
#    b = get_times(times,i,d)
#    if b:
#        print('FOUND: ' + str(i))
#        break
       
#sys.exit()
#every = 23
#n=1000000
#for i in range(225850756400740-n,225850756400740+n,1):
#    if ( get_times(times,t,d) ):
#        print('FOUND!!!!!! ' + i)
#        break

#print('done')
#sys.exit()


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
            arr4.append(t)
            if (reps < 3):
                t = t + every
                continue
            print('ans: '+str(arr4[0]))
            print('evr: '+str(arr4[2]-arr4[1]))

        print()
        print('Part 2: ' + str(t))
        break
    t = t + every

end_secs = time.time()
print()
print(str(end_secs-start_secs) + ' seconds')


