"""
AoC
"""
import time

start_secs = time.time()

f = {}
f[4] = ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']
f[3] = ['MG','MM','RG','RM','  ','  ','  ','  ','  ','  ']
f[2] = ['  ','  ','  ','  ','PM','  ','SM','  ','  ','  ']
f[1] = ['  ','  ','  ','  ','  ','PG','  ','SG','TG','TM']
E = 1 # current floor

def printFloors(f,e):
  s = ''
  for i in range(4,0,-1):
    arr = f[i]
    stemp = ''
    for j in range(len(arr)):
      stemp += arr[j] + ' '
    if i == e:
      stemp = ' E  ' + stemp
    else:
      stemp = '    ' + stemp
    stemp = 'F' + str(i) + stemp + '\n'
    s += stemp
  print(s)

def foundPair(f,e):
  floor = f[e]
  for i in range(len(floor)):
    if floor[i] == '  ':
      continue
    l1 = floor[i][0]
    l2 = floor[i][1]
    c = 'M'
    if l2 == 'M':
      c = 'G'
    if (l1+c) in floor:
      return [floor[i], l1+c]
  return []

def findSolo(f,e):
  floor = f[e]
  solo = '  '
  for i in range(len(floor)):
    solo = '  '
    if floor[i] == '  ':
      continue
    l1 = floor[i][0]
    l2 = floor[i][1]
    c = 'M'
    if l2 == 'M':
      c = 'G'
    solo = floor[i]
    if not (l1+c) in floor:
      return solo
  return '  '

def moveUp(arr,e):
  global E
  global f
  for i in range(len(f[e])):
    if f[e][i] in arr:
      val = f[e][i]
      f[e][i] = '  '
      f[e+1][i] = val
  E += 1

print('')

printFloors(f,E)

steps = 0
while '  ' in f[4]:

  #floor = f[E]



  # if there's a match on the current floor, move them both up
  if E != 4:
    arr = foundPair(f,E)
    if len(arr) > 0:
      moveUp(arr,E)


  steps += 1

  # testing; break out
  if steps == 100:
    break


printFloors(f,E)

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
