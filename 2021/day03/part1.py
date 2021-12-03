# part 1
"""
AoC
"""
import time

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

one = [0,0,0,0,0,0,0,0,0,0,0,0]
zer = [0,0,0,0,0,0,0,0,0,0,0,0]
for s in l:
  for i in range(0, len(s)):
    if s[i] == '1':
      one[i] += 1
    else:
      zer[i] += 1

s = ''
s2 = ''
for i in range(0, len(one)):
  if one[i] > zer[i]:
    s += '1'
    s2 += '0'
  else:
    s += '0'
    s2 += '1'


gamma = int(s, 2)

epsilon = int(s2, 2)

print(gamma * epsilon )

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')