import sys
import time

start_secs = time.time()
print('')

def rotate_matrix( m ):
  return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# TODO
valid = 0
for i in range(0, len(l), 3):

  m1 = []
  m1.append(l[i].split())
  m1.append(l[i+1].split())
  m1.append(l[i+2].split())
  m1 = rotate_matrix(m1)
  for r in range(0,3):
    x = int(m1[r][0])
    y = int(m1[r][1])
    z = int(m1[r][2])
    if (x+y) <= z or (x+z) <= y or (y+z) <= x:
      continue
    valid = valid + 1

print(valid) 

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')