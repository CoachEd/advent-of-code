import sys
import time
import math
from copy import copy, deepcopy
import cProfile, pstats
from io import StringIO

"""
pr = cProfile.Profile()  # create a profile object
pr.enable()  # start profiling
print()
"""

# 33 seconds is still too slow
start_secs = time.time()

str1='59765216634952147735419588186168416807782379738264316903583191841332176615408501571822799985693486107923593120590306960233536388988005024546603711148197317530759761108192873368036493650979511670847453153419517502952341650871529652340965572616173116797325184487863348469473923502602634441664981644497228824291038379070674902022830063886132391030654984448597653164862228739130676400263409084489497532639289817792086185750575438406913771907404006452592544814929272796192646846314361074786728172308710864379023028807580948201199540396460310280533771566824603456581043215999473424395046570134221182852363891114374810263887875638355730605895695123598637121'
slen = len(str1)

s = []
for c in str1:
    s.append(int(c))

phases=100
for phs in range(1,phases+1):
    
    news=[]
    for i in range(1,slen+1):
        ppos=1
       
        idx1=i
        idx2=i*2
        idx3=i*3
        idx4=i*4
        
        sum=0
        for j in range (0,slen):
            if ppos < idx1:
                pass
            elif ppos < idx2:
                p=1
                sum = sum + s[j]
            elif ppos < idx3:
                pass
            elif ppos < idx4:
                sum = sum - s[j]
            else:
                ppos=0
                
            ppos=ppos+1            

        sum=str(sum)                          
        keep=sum[-1:]
        news.append(int(keep))
        
    s=news

print(s[0:8])
print('phases: ' + str(phases))



"""
print()
pr.disable()  # end profiling

# print out some stats.
s = StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
"""

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')