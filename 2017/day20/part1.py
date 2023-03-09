import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def distance(x,y,z):
  return abs(x) + abs(y) + abs(z)

# SOLUTION
# read in input file
# p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

particles = []
for s in l:
  for c in 'pva=<> ':
    s = s.replace(c,'')
  arr = s.split(',')
  d = dict()
  (d['px'], d['py'], d['pz']) = (int(arr[0]), int(arr[1]), int(arr[2]))
  (d['vx'], d['vy'], d['vz']) = (int(arr[3]), int(arr[4]), int(arr[5]))
  (d['ax'], d['ay'], d['az']) = (int(arr[6]), int(arr[7]), int(arr[8]))
  particles.append(d)

duration = 300
distances = [ 0 for i in range(len(particles))]
for t in range(1, duration):

  # move
  for i in range(len(particles)):
    p = particles[i]
    p['vx'] += p['ax']
    p['vy'] += p['ay']
    p['vz'] += p['az']
    p['px'] += p['vx']
    p['py'] += p['vy']
    p['pz'] += p['vz']

  # calculate distances
  for i in range(len(particles)):
    p = particles[i]
    dist = distance(p['px'],p['py'],p['pz'])
    distances[i] = dist
  
  minp = -1
  mindist = float('inf')
  for i in range(len(distances)):
    dist = distances[i]
    if dist < mindist:
      mindist = dist
      minp = i
  
  print(minp)

# after about 300 time steps, 243 keeps winning!

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')