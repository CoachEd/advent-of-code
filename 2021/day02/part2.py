# part2.py
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

depth = 0
horiz = 0
aim = 0
for i in range(0,len(l)):
  arr = l[i].split(' ')
  cmd = arr[0]
  x = int(arr[1])
  if cmd == 'forward':
    horiz += x
    depth += (aim * x)
  elif cmd == 'down':
    aim += x
  else:
    aim -= x

print(depth * horiz)


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')