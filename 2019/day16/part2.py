import sys
import time
import math
from copy import copy, deepcopy
import cProfile, pstats
from io import StringIO

start_secs = time.time()

str1='59765216634952147735419588186168416807782379738264316903583191841332176615408501571822799985693486107923593120590306960233536388988005024546603711148197317530759761108192873368036493650979511670847453153419517502952341650871529652340965572616173116797325184487863348469473923502602634441664981644497228824291038379070674902022830063886132391030654984448597653164862228739130676400263409084489497532639289817792086185750575438406913771907404006452592544814929272796192646846314361074786728172308710864379023028807580948201199540396460310280533771566824603456581043215999473424395046570134221182852363891114374810263887875638355730605895695123598637121'
phases=100

#str1 = '12345678'
#phases=4

slen = len(str1) # 650
marr =  [0, 1, 0, -1] 

#PART2
#The first seven digits of your initial input signal also represent the message offset.
offset = int(str1[0:7])
str2 = 10000 * str1   # PART 2

def sum_row(arr,row_num,mindex):
    d1 = dict()
    big_sum = 0
    sum = 0
    cnt = 0
    if row_num > 0:
      cnt = 1
      mindex = mindex - 1
    
    for n in range(0,10000):
      key = str(mindex)+','+str(cnt)
      if key in d1:
        sum = d1[key]
      else:
        for i in range(0,slen):
          sum = sum + arr[i] * marr[ mindex ]
          cnt = cnt + 1
          if cnt >= row_num+1:
            mindex = mindex + 1
            cnt = 0
          if mindex > 3:
            mindex = 0
        d1[key] = sum
      big_sum = big_sum + sum

    return big_sum

#pr = cProfile.Profile()  # create a profile object
#pr.enable()  # start profiling
#print()

s = [None] * slen
for i in range(0,slen):
    s[i] = int(str1[i])

news=[None] * len(str2)
for phs in range(1,phases+1):
    print('phs: ' + str(phs))

    for i in range(0,len(str2)):
        x = sum_row(s,i,1)
        news[i] = abs(x) % 10
    s=news

#print(s[0:8])
#print('phases: ' + str(phases))

# part 2
ans = ''
for i in range(offset,offset+8):
    ans = ans + str(s[i])
print(ans + ' , phases: ' + str(phases))

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
