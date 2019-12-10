import sys
import time
import math

print()
start_secs = time.time()

"""
for origin x,y:
Reduce: Remove up,down,left,right,tr,tl,br,bl, all but first one found, change that first one to a different character

for each x,y:
  if it is a "#" and not the origin:
  Start at curr(0,0)
  find cx and cy offset to origin(ox,oy): 
    offsetx = cx - ox
    offsety = cy - oy

  get gcd of offsetx and offsety
  reduce offsetx and offsety by gcd
  from origin, traverse to offsetx and offsety, removing all but the first one. change that first char to something else

count how many satellites remain

"""




print( math.gcd(0,4) )



end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')
