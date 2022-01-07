"""
AoC
"""
import time
import hashlib
import sys

salt = 'ngcjuoqr'
#salt = 'abc' # test data
arr3 = ['','','']

def get_hash(s):
  return hashlib.md5(s.encode('utf-8')).hexdigest()

def get_stretched_hash(s):
  hash = s
  for i in range(2016+1):
    hash = get_hash(hash)
  return hash

def has_three(s):
  global arr3
  arr3[0] = ''
  arr3[1] = ''
  arr3[2] = ''
  for i in range(len(s)-3+1):
    if s[i] == s[i+1] and s[i] == s[i+2]:
      arr3[0] = s[i]
      arr3[1] = s[i+1]
      arr3[2] = s[i+2]
      break
  if arr3[0] != '':
    return arr3
  else:
    return []

def has_five(s,c):
  for i in range(len(s)-5+1):
    if s[i] == c and s[i+1] == c and s[i+2] == c and s[i+3] == c and s[i+4] == c:
      return True
  return False

start_secs = time.time()
print('')

"""
It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.
"""

num_hashes = 100000
print('creating ' + str(num_hashes) + ' hashes...')
saved_hashes = {}
for i in range(num_hashes):
  if i % 1000 == 0:
    print(i)
  key = salt + str(i)
  saved_hashes[ key ] = get_stretched_hash(key)

print('searching...')
hashes = {}
i = 0
count = 0
done = False
while not done:
  key = salt + str(i)
  hash = saved_hashes[key]
  if hash in hashes:
    i += 1
    continue
  three = has_three(hash)
  if len(three) > 0:
    for j in range(i+1,i+1+1000):
      key2 = salt + str(j)
      hash2 = saved_hashes[key2]
      if hash in hashes:
        continue
      if has_five(hash2,three[0]):
        count += 1
        hashes[hash] = 0
        print('index: ' + str(i) + '  hash: ' + hash)
        if count == 64:
          print()
          print('index: ' + str(i))
          done = True
  i += 1

# 12291  too low

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
