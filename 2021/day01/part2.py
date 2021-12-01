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

prev = int(l[0]) + int(l[1]) + int(l[2])
incr = 0
decr = 0
for i in range(1,len(l)-2):
  nxt = int(l[i]) + int(l[i+1]) + int(l[i+2])
  if nxt > prev:
    incr += 1
  prev = nxt
print(incr)
  


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
