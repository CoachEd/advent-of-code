import sys
import time
import math
from copy import copy, deepcopy
import cProfile, pstats
from io import StringIO


pr = cProfile.Profile()  # create a profile object
pr.enable()  # start profiling
start_secs = time.time()

marr = [0, 1, 0, -1]

# added 0 in front
str1='059765216634952147735419588186168416807782379738264316903583191841332176615408501571822799985693486107923593120590306960233536388988005024546603711148197317530759761108192873368036493650979511670847453153419517502952341650871529652340965572616173116797325184487863348469473923502602634441664981644497228824291038379070674902022830063886132391030654984448597653164862228739130676400263409084489497532639289817792086185750575438406913771907404006452592544814929272796192646846314361074786728172308710864379023028807580948201199540396460310280533771566824603456581043215999473424395046570134221182852363891114374810263887875638355730605895695123598637121'

# TODO: can we calculate the big chunk in each row once? 651, then use that number when it comes up again

#PART2
#The first seven digits of your initial input signal also represent the message offset.
#offset = int(str1[0:7])
#str1 = 10000 * str1

slen = len(str1) # 651

s = []
for c in str1:
    s.append(int(c))

news=[None]*(slen)
for phs in range(0,100):
    for i in range(0,slen-1):
        sum=0
        for j in range (0,slen):
            idx =  (j // (i+1) ) % 4
            #print( str(s[j]) + '*' + str(marr[idx]) ) 
            sum = sum + marr[ idx ] * s[j]
        news[i] = abs(sum) % 10
    s=news
    del s[-1]
    s.insert(0,0)
    
print(s[1:9])

# part 2
#ans = ''
#for i in range(offset,offset+8):
#    ans = ans + str(s[i])
#print(ans + ' , phases: ' + str(phases))


print()
pr.disable()  # end profiling

# print out some stats.
s = StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())


end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')




