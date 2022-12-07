import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def countSizes(dirName):
  global d
  count = 0
  children = d[dirName][3]
  fileSizes = d[dirName][1]
  for n in fileSizes:
    count += n
  if len(children) == 0:
    return count
  count2 = 0
  for s in children:
    count2 += countSizes(s)
  return count + count2

# SOLUTION
# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

d = dict() # each entry is an array: [ parent_str, [ array of file sizes], [ array of file names ], [ array of children ] ]
dirs = []
currDir = ''
for s in l:
  if s[0] == '$':
    cmd = s[2:4]
    if cmd == 'cd':
      arg = s[5:].strip()
      if arg == '..':
        # go back one
        if not currDir == '/':
          currDir = d[currDir][0]
      else:
        # go to dir
        if (arg == '/'):
          d[''] = [ '', [] , [], [] ]
          currDir = ''
        else:
          newDir = currDir + ' ' + arg
          if not newDir in d:
            d[newDir] = [ currDir, [], [], [] ]
          currDir = newDir
    else:
      # ls
      pass  
  elif s[0:3] == 'dir':
    dir = s[4:]
    theDir = currDir + ' ' + dir
    if not theDir in d:
      d[theDir] = [ currDir, [] , [], [] ]
      dirs.append(theDir)
    d[currDir][3].append(theDir)
  else:
    # file
    arr = s.split()
    sz = int(arr[0])
    fn = arr[1]
    d[currDir][1].append(sz)
    d[currDir][2].append(fn)


total = 0
for s in dirs:
  count = countSizes(s)
  if count <= 100000:
    total += count
print(total)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')