import time
import sys
from copy import copy, deepcopy
start_secs = time.time()
print('')

def get_collisions(p):
  collided = set()
  for i in p:
    for j in p:
      if i == j:
        continue
      if p[i]['px'] == p[j]['px'] and p[i]['py'] == p[j]['py'] and p[i]['pz'] == p[j]['pz']:
        collided.add(i)
        collided.add(j)
  return collided

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

particles = dict()
i = 0
for s in l:
  for c in 'pva=<> ':
    s = s.replace(c,'')
  arr = s.split(',')
  d = dict()
  (d['px'], d['py'], d['pz']) = (int(arr[0]), int(arr[1]), int(arr[2]))
  (d['vx'], d['vy'], d['vz']) = (int(arr[3]), int(arr[4]), int(arr[5]))
  (d['ax'], d['ay'], d['az']) = (int(arr[6]), int(arr[7]), int(arr[8]))
  particles[i] = d
  i += 1

duration = 300
distances = dict()
for t in range(1, duration):

  # move
  for i in particles:
    p = particles[i]
    p['vx'] += p['ax']
    p['vy'] += p['ay']
    p['vz'] += p['az']
    p['px'] += p['vx']
    p['py'] += p['vy']
    p['pz'] += p['vz']


  collided = get_collisions(particles)
  for c in collided:
    del particles[c]

  # calculate distances
  for x in particles:
    p = particles[x]
    dist = distance(p['px'],p['py'],p['pz'])
    distances[x] = dist
  
  minp = -1
  mindist = float('inf')
  for x in distances:
    dist = distances[x]
    if dist < mindist:
      mindist = dist
      minp = x
  
  print(len(particles))

# after about 300 time steps, 243 keeps winning!

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')