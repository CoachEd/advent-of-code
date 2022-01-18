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


p = ['a','b','c','d','e']
print(p)
rotate_left(p,5)
print(p)