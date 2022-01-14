"""
AoC
"""
import time
import sys

def swap(x,y,p):
  temp = p[x]
  p[x] = p[y]
  p[y] = temp

def rotate_based_on(c,p):
  # rotate based on position of letter f
  # rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
  print(p)
  steps = p.index(c)
  print(steps)
  osteps = steps
  steps += 1
  if osteps > 3:
    steps += 1

  print(steps)
  rotate_right(p,steps)  

def reverse_range(x,y,p):
  mid = ((y-x)+1)//2 + x
  i2 = y
  for i in range(x,mid):
    swap(i,i2,p)
    i2 -= 1

def rotate_right(p,steps):
  if steps >= len(p):
    steps = steps % len(p)

  p2 = p.copy()
  for x in range(len(p)):
    p[steps] = p2[x]
    steps += 1
    if steps >= len(p):
      steps = 0

def rotate_left(p,steps):
  global left_arr
  # rotate left 4 steps
  len_password = len(p)
  new_i = steps % len_password
  new_i = left_arr[new_i]
  #             abcd 0,1,2,3 i == 0         0
  # rot left 1: bcda 1,2,3,0 i == 3  1%4 == 1
  # rot left 2: cdab 2,3,0,1 i == 2  2%4 == 2
  # rot left 3: dabc 3,0,1,2 i == 1  3%4 == 3
  # rot left 4: abcd 0,1,2,3 i == 0  4%4 == 0
  # rot left 5: bcda 1,2,3,0 i == 3  5%4 == 1
  # ...
  # left_arr = [0,4,3,2,1]
  #             abcde 0,1,2,3,4 i == 0         0
  # rot left 1: bcdea 1,2,3,4,0 i == 4  1%5 == 1
  # rot left 2: cdeab 2,3,4,0,1 i == 3  2%5 == 2
  # rot left 3: deabc 3,4,0,1,2 i == 2  3%5 == 3
  # rot left 4: eabcd 4,0,1,2,3 i == 1  4%5 == 4
  # rot left 5: bcdea 0,1,2,3,4 i == 0  5%5 == 0
  # ...  
  for x in range(len(p)-1):
    swap(x,new_i,p)
    new_i += 1
    if new_i >= len_password:
      new_i = 0

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

# TEST
left_arr = [0,4,3,2,1]
password = 'abcde'

# ACTUAL INPUT
# TODO: test individual functions above
left_arr = [0,7,6,5,4,3,2,1]
password = 'abcdefgh'

len_password = len(password)
rot_arr = [ i for i in range(len(password)) ]
p = [ c for c in password ]

for s in l:
  arr = s.split(' ')
  cmd_prefix = arr[0] + ' ' + arr[1]
  if cmd_prefix == 'swap position':
    x = int(arr[2])
    y = int(arr[5])
    temp = p[x]
    p[x] = p[y]
    p[y] = temp
  elif cmd_prefix == 'swap letter':
    x = p.index(arr[2])
    y = p.index(arr[5])
    temp = p[x]
    p[x] = p[y]
    p[y] = temp
  elif cmd_prefix == 'rotate right':
    # rotate right 7 steps
    rotate_right(p,int(arr[2]))
  elif cmd_prefix == 'rotate left':
    # rotate left 4 steps
    rotate_left(p,int(arr[2])) 
  elif cmd_prefix == 'rotate based':
    # rotate based on position of letter f
    # rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
    c = arr[6]
    steps = p.index(c) + 1
    if steps > 3:
      steps += 1
    rotate_right(p,steps)
  elif cmd_prefix == 'reverse positions':
    # reverse positions 0 through 1
    # reverse positions X through Y means that the span of letters
    # at indexes X through Y (including the letters at X and Y) should be reversed in order.
    x = int(arr[2])
    y = int(arr[4])
    reverse_range(x,y,p)
  elif cmd_prefix == 'move position':
    # move position 0 to position 4
    # move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
    x = int(arr[2])
    y = int(arr[5])
    value_at_x = p[x]
    value_at_y = p[y]
    del p[x]
    p.insert(y,value_at_x)
  #print(p)


print(''.join(p))
# gdeabhfc WRONG!

    


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
