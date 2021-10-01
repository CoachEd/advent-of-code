"""
AoC
"""
import time

start_secs = time.time()
print('')

def findABBA(s):
  for i in range(1,len(s)-2):
    x = s[i-1]
    y = s[i+1]
    z = s[i+2]
    if x == z and s[i] == y and x != y:
      return True
  return False


# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())


TOTAL = 0
for y,e1 in enumerate(l):
  e1 = e1.replace('[',' ').replace(']',' ')
  ARR = e1.split()
  FOUND_OUTSIDE = False
  FOUND_INSIDE = False
  for x,e2 in enumerate(ARR):
    if not FOUND_OUTSIDE and x % 2 == 0 and findABBA(e2):
      FOUND_OUTSIDE = True
    if not FOUND_INSIDE and x % 2 == 1 and findABBA(e2):
      FOUND_INSIDE = True
    if FOUND_INSIDE:
      break

  if not FOUND_INSIDE and FOUND_OUTSIDE:
    TOTAL = TOTAL + 1



print(str(TOTAL))

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
