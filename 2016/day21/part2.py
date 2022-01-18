"""
AoC
"""
import time
import sys

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
  len_password = len(p)
  new_head = steps % len_password
  # shift left by new_head
  n = new_head
  new_arr = [ ' ' for i in range(len(p)) ]
  idx = new_head
  for i in range(len(p)):
    new_arr[i] = p[idx]
    idx += 1
    if idx >= len_password:
      idx = 0
  for i in range(len(p)):
    p[i] = new_arr[i]

def swap(x,y,p):
  temp = p[x]
  p[x] = p[y]
  p[y] = temp

start_secs = time.time()
print('')

# read in input file
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()

for i in range(len(lines)-1,-1,-1):
  line = lines[i]
  l.append(line.strip())

# TEST
#password = 'abcde'

# ACTUAL INPUT
# TODO: test individual functions above
password = 'fbgdceah'
password = 'dgfaehcb' # part1 answer

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
    rotate_left(p,int(arr[2]))
  elif cmd_prefix == 'rotate left':
    # rotate left 4 steps
    rotate_right(p,int(arr[2])) 
  elif cmd_prefix == 'rotate based':
    
    # TODO: CHECK THIS!!
    # ex: 
    #   rotate based on position of letter h
    #
    # rotate based on position of letter f
    # rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.

    c = arr[6]
    the_index = p.index(c)
    rotate_left(p,the_index)
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
    value_at_y = p[y] # remove
    del p[y]
    p.insert(x,value_at_y)
  #print(p)


print(''.join(p))
# defbahcg WRONG
# dcehgbfa WRONG
print('\nTESTING... should be: \nabcdefgh')


print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')
