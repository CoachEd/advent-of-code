import sys
import time
import hashlib


start_secs = time.time()

# Part 1
for i in range(0,sys.maxsize+1):
  inp = 'yzbqklnj' + str(i)
  m = hashlib.md5(inp.encode('utf-8')).hexdigest()
  if m[0:5] == '00000':
    print('Part 1: ' + str(i))
    break

# Part 2
for i in range(0,sys.maxsize+1):
  inp = 'yzbqklnj' + str(i)
  m = hashlib.md5(inp.encode('utf-8')).hexdigest()
  if m[0:6] == '000000':
    print('Part 2: ' + str(i))
    break

end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' --- seconds')