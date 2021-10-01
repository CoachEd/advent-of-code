"""
AoC
"""
import time
import hashlib
import sys

start_secs = time.time()
print('')

# input
INPSTR = 'reyedfim'

PASSWORD = [' ',' ',' ',' ',' ',' ',' ',' ']
COUNT = 0
for i in range(0, sys.maxsize):
  IDSTR = INPSTR + str(i)
  S1 = hashlib.md5(IDSTR.encode('utf-8')).hexdigest()
  ORD = ord(S1[5])
  if S1.startswith('00000') and ORD > 47 and ORD < 56:
    IDX = int(S1[5])
    if PASSWORD[ IDX ] != ' ':
      continue
    PASSWORD[ IDX ] = S1[6]
    COUNT = COUNT + 1
    if COUNT == 8:
      break

print("".join(PASSWORD))


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
