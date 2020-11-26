import sys
import time
import math
from copy import copy, deepcopy
import cProfile, pstats
from io import StringIO

marr =  [0, 1, 0, -1]


#TODO: instead of deleting from the array, keep the array but skip forward    
def sum_row(arr,row_num):
    sum = 0
    sub1 = 0
    mindex = 0
    if row_num == 0:
        mindex = 1
    if row_num > 0:
        sub1 = -1

    while True:
        if mindex == 0 or mindex ==2:
            del arr[:row_num+1+sub1]
        else:
            for i in range(0,row_num+1+sub1):
                if i >= len(arr):
                    break
                #print( str(arr[i]) + ' * ' + str(marr[mindex]) )
                sum = sum + arr[i] * marr[mindex]
            del arr[:row_num+1+sub1]
        sub1 = 0
        mindex = mindex + 1
        if mindex > 3:
            mindex = 0
        if len(arr) == 0:
            break

    return sum


marr = [0, 1, 0, -1]
#print( sum_row([1,2,3,4,5,6,7,8],0)) # -4
#print()
#print( sum_row([1,2,3,4,5,6,7,8],1)) # -8
#print()
#print( sum_row([1,2,3,4,5,6,7,8],2)) # 
#print()
#print( sum_row([1,2,3,4,5,6,7,8],3)) # 
#print()
#sys.exit()

#pr = cProfile.Profile()  # create a profile object
#pr.enable()  # start profiling
#print()

# 33 seconds is still too slow
start_secs = time.time()

str1='59765216634952147735419588186168416807782379738264316903583191841332176615408501571822799985693486107923593120590306960233536388988005024546603711148197317530759761108192873368036493650979511670847453153419517502952341650871529652340965572616173116797325184487863348469473923502602634441664981644497228824291038379070674902022830063886132391030654984448597653164862228739130676400263409084489497532639289817792086185750575438406913771907404006452592544814929272796192646846314361074786728172308710864379023028807580948201199540396460310280533771566824603456581043215999473424395046570134221182852363891114374810263887875638355730605895695123598637121'

#PART2
#The first seven digits of your initial input signal also represent the message offset.
#offset = int(str1[0:7])
#str1 = 10000 * str1   # PART 2

slen = len(str1) # 650

s = [None] * slen
for i in range(0,len(str1)):
    s[i] = int(str1[i])

phases=100
news=[None]*slen
for phs in range(1,phases+1):
    #print('phs: ' + str(phs))
    for i in range(0,slen):
        news[i] = abs(sum_row(s.copy(),i)) % 10
    s=news

print(s[0:8])
print('phases: ' + str(phases))

# part 2
#ans = ''
#for i in range(offset,offset+8):
#    ans = ans + str(s[i])
#print(ans + ' , phases: ' + str(phases))


#print()
#pr.disable()  # end profiling

# print out some stats.
#s = StringIO()
#sortby = 'cumulative'
#ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#ps.print_stats()
#print(s.getvalue())


end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')




