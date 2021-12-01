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

prev = int(l[0])
incr = 0
decr = 0
for i in range(1,len(l)):
  if int(l[i]) > prev:
    incr += 1
  prev = int(l[i])
print(incr)
  


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
