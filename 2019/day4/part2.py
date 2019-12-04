import sys
import time

start_secs = time.time()

x,y = 248345,746315  # input
remove_patterns = []
for i in range(0,10):
  for j in range(6,2,-1):
    remove_patterns.append(str(i) * j)

remove_patterns2 = remove_patterns[:] # copy that includes length 2 dups
for j in range(0,10):
  remove_patterns2.append(str(j) * 2)

patterns = ['00','11','22','33','44','55','66','77','88','99']
total = 0
for n in range(x,y+1):
  s = str(n)

  # remove duplicate groups greater than length 2
  for rp in remove_patterns:
    s = s.replace(rp,'')

  # make sure at least one duplicate group of length 2 exists
  start_len = len(s)
  orig_len = 0
  new_len = -1
  while orig_len != new_len:
    orig_len = len(s)
    for p in patterns:
      s = s.replace(p,p[0])
    new_len = len(s)
  if new_len == start_len:
    continue # no dups of length 2 exist

  # verify increasing digits, but start with the original string
  s = str(n)
  orig_len = 0
  new_len = -1
  # we can actually reduce all large groups to length 1 now
  while orig_len != new_len:
    orig_len = len(s)  
    for rp in remove_patterns2:
      s = s.replace(rp,rp[0])
    new_len = len(s)

  # now verify that digits increase
  stop = False
  prev = -1
  for c in s:
    d = int(c)
    if d < prev:
      stop = True
      break
    prev = d
  if stop:
    continue

  # found one
  total = total + 1

print('Part 2: total = ' + str(total)) # Answer: 660

end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')