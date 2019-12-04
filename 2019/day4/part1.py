import sys
import time

start_secs = time.time()

x,y = 248345,746315  # input
patterns = ['00','11','22','33','44','55','66','77','88','99']
total = 0
for n in range(x,y+1):
  s = str(n)

  # make sure that we have at least one pair of double digits
  start_len = len(s)
  orig_len = 0
  new_len = -1
  while orig_len != new_len:
    orig_len = len(s)
    for p in patterns:
      s = s.replace(p,p[0])
    new_len = len(s)
  if new_len == start_len:
    continue # no dups

  # make sure that the digits are increasing
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

print('Part 1: total = ' + str(total)) # Answer: 1019





end_secs = time.time()
print('elapsed time: ' + str(end_secs - start_secs) + ' seconds')