"""
AoC
"""
import time

start_secs = time.time()
print('')

def all_zero(arr):
  tot = arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6]
  return tot == 0

def get_future_pos(t,pos,positions):
  new_pos = t + pos
  if new_pos < positions:
    return new_pos
  else:
    new_pos = ( (t+pos) % positions )
    return new_pos

def get_positions(t):
  global pos_temp
  global discs
  for i in range(len(discs)):
    pos_temp[i] = get_future_pos(t+i+1,discs[i][0],discs[i][1])
  return pos_temp

# read in input file
l=[]
my_file = open("inp2.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

discs = [ [0,0] for i in range(len(l)) ]  # [ pos, positions ]
pos_temp = [ 0 for i in range(len(l)) ]
for s in l:
  arr = s.split(' ')
  disc_num = int(arr[1].replace('#','')) - 1
  positions = int(arr[3])
  pos = int(arr[11].replace('.',''))
  discs[disc_num][0] = pos
  discs[disc_num][1] = positions

for step in range(3000000):
  res = get_positions(step)
  if all_zero(res):
    print(step)
    break
  

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
