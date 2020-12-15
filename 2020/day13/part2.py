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
# LCM: 867200349647749: the product of all numbers

# LCM: 533661753629384 # TOO HIGH
#      375005556604432
#      187502778302216
# LCM: 133415438407346
# LCM: 102023570546794
#  T = 100000000000000

# LCM: 66707719203673
# LCM: 51011785273397
# LCM: 45642123665671
# LCM: 23437847287777
# LCM: 571654811897
s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
#s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509'
#s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509'
t = 0
#this approach!!
#t=398015 + ( 208338975 * 479987)   # then every 479987 GOOD
t=398015 + + ( 208338975 * 479987 )


#s='23,x,x,x,x,x,x,x,x,x,x,x,x,41' # 69, then every 943
#t=69 + (943*106044538706)
#100000000000000


#s='7,13,x,x,59,x,31,19' # ANSWER  1068781   LCM: 3162341 (product of all numbers)
#s='7,13' # t=77 , then every 91
#s='7,x,x,x,59' # 350, then every  413
#s='7,x,x,x,x,x,31' # 56, then every 217
#s='7,x,x,x,x,x,x,19' # 126, then every 133
#t= 77
#t = 350
#s='4,x,x,5'

#WORKS!!  
#s='7,13,x,x,59,x,31' # 70147, then every 166439
#t=70147
#t=0







#s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509' # 398015 #ORIG
#s='23,x,x,x,x,x,x,x,x,x,x,x,x,41' # 69
#s='23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,509' # 11684
#s='41,x,x,x,x,x,x,x,x,x,509' # 1517

# TESTS
#t = 0 # orig: 100000000000000
#s = '2,x,7'
#s='7,13,x,x,59,x,31,19' # Ans: 1068781  #TRY: 91 413 217 133 (LCM: 3162341)
arr = s.split(',')
times=[]
d = dict()
offset = 0
for e in arr:
    if e != 'x':
        times.append(int(e))
        d[int(e)] = offset
    offset = offset + 1

#for i in range(867200349647749,0,-23):
#    if get_times(times,i,d):
#        print('HERE: ' + str(i))
#        break
found = False
#
#t=867200349647749
#100000000000000
#867200349647749
#for i in range(0,3162341,1):
##    found = get_times(times,i,d)
#    if found:
#        print(i)
#        break


#end_secs = time.time()
##print()
#print(str(end_secs-start_secs) + ' seconds')


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
        reps = reps + 1
        #get_times(times,t)
        #print(t)
        #if (reps < 3):
        #   t = t + times[0]
        #   continue
        print()
        print('Part 2: ' + str(t))
        break
    #t = t + times[0]
    t = t + 479987
       
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