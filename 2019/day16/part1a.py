import sys
import time
import math
from copy import copy, deepcopy
import cProfile, pstats
from io import StringIO

def sum_row(arr,marr,row_num,mindex,firstone):
    sum = 0
    sub1 = 0
    if len(arr) == 0:
        return 0

    if firstone:
        sub1 = -1
        firstone = False
    if mindex == 0 or mindex ==2:
        del arr[:row_num+1+sub1]
    else:
        for i in range(0,row_num+1+sub1):
            print( str(arr[i]) + ' * ' + str(marr[mindex]) )
            sum = sum + arr[i] * marr[mindex]
        del arr[:row_num+1+sub1] 
    mindex = mindex + 1
    if mindex > 3:
        mindex = 0
    return sum + sum_row(arr,marr,row_num,mindex,firstone)

marr = [0, 1, 0, -1]
#print( sum_row([1,2,3,4,5,6,7,8],marr,0,1,True)) # -4
#print()
#print( sum_row([1,2,3,4,5,6,7,8],marr,1,0,True)) # -8
#print()
print( sum_row([1,2,3,4,5,6,7,8],marr,2,0,True)) # 
print()
sys.exit()





pr = cProfile.Profile()  # create a profile object
pr.enable()  # start profiling
print()


# 33 seconds is still too slow
start_secs = time.time()



"""
Input signal: 12345678

0       1      2      3      4      5      6      7         
1*1  + 2*0  + 3*-1 + 4*0  + 5*1  + 6*0  + 7*-1 + 8*0  = 4  ((pos+1) DIV 2 mod 4)
1*0  + 2*1  + 3*1  + 4*0  + 5*0  + 6*-1 + 7*-1 + 8*0  = 8  ((pos+1) DIV 2 mod 4)
1*0  + 2*0  + 3*1  + 4*1  + 5*1  + 6*0  + 7*0  + 8*0  = 2
1*0  + 2*0  + 3*0  + 4*1  + 5*1  + 6*1  + 7*1  + 8*0  = 2
1*0  + 2*0  + 3*0  + 4*0  + 5*1  + 6*1  + 7*1  + 8*1  = 6
1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*1  + 7*1  + 8*1  = 1
1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*0  + 7*1  + 8*1  = 5
1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*0  + 7*0  + 8*1  = 8

"""



str1='59765216634952147735419588186168416807782379738264316903583191841332176615408501571822799985693486107923593120590306960233536388988005024546603711148197317530759761108192873368036493650979511670847453153419517502952341650871529652340965572616173116797325184487863348469473923502602634441664981644497228824291038379070674902022830063886132391030654984448597653164862228739130676400263409084489497532639289817792086185750575438406913771907404006452592544814929272796192646846314361074786728172308710864379023028807580948201199540396460310280533771566824603456581043215999473424395046570134221182852363891114374810263887875638355730605895695123598637121'

#PART2
#The first seven digits of your initial input signal also represent the message offset.
#offset = int(str1[0:7])
str1 = 10000 * str1


slen = len(str1) # 650

s = []
for c in str1:
    s.append(int(c))

phases=100
news=[None]*slen
for phs in range(1,phases+1):
    for i in range(1,slen+1):
        sum=0
        for j in range (0,slen):
            # ((pos+1) DIV 2 mod 4)
            idx = ( (j+1) // i) % 4
            #if (s[j] == 0 or marr[idx] == 0):
            #    continue
            sum = sum + marr[ idx ] * s[j]
        news[i-1] = abs(sum) % 1               
    s=news

print(s[0:8])
print('phases: ' + str(phases))

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




