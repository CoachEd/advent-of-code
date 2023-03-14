import time
import sys
import math
from copy import copy, deepcopy
start_secs = time.time()
print('')

def rotate(a):
  a2 = deepcopy(a)
  x2 = len(a2) - 1
  for y in range(len(a2)):
    for x in range(len(a2[y])):
      y2 = x
      a[y2][x2] = a2[y][x]
    x2 -= 1

def flip(a):
  # flips top to bottom
  n = len(a)
  mid = n // 2
  rem = n % 2
  temp_col = [ None for i in range(n) ]
  ry = None
  ly = None
  if rem == 0:
    ry = mid
    ly = mid - 1
  else:
    ry = mid + 1
    ly = mid - 1

  while ly >= 0:
    for x in range(n):
      temp_col[x] = a[ly][x]
    for x in range(n):
      a[ly][x] = a[ry][x]
    for x in range(n):
      a[ry][x] = temp_col[x]      
    ly -= 1
    ry += 1

def combine(squares, N):
  # squares is an array of 2D squares
  # N is the dimension while combining the above squares; N=2... 2x2 squares
  N = int(N)
  square_sz = len(squares[0])
  final_square_sz = int(square_sz * N)
  image = [ [ ' ' for i in range(final_square_sz) ] for j in range(final_square_sz) ]

  row = 0
  col = 0
  for i in range(len(squares)):
    sq = squares[i]
    for y in range(len(sq)):
      for x in range(len(sq[y])):
        (iy,ix) = (y + row,col + x)
        image[iy][ix] = sq[y][x]

    col += square_sz
    if i != 0 and ((i + 1) % N == 0):
      row += square_sz
      col = 0 
  
  return image

def print_square(square):
  s = ''
  for y in range(len(square)):
    for x in range(len(square[y])):
      s += square[y][x]
    s += '\n'
  print(s)

def count_on(square):
  count = 0
  for y in range(len(square)):
    for x in range(len(square[y])):
      if (square[y][x]) == '#':
        count += 1
  return(count)

def breakup_image(image):
  len1 = len(image)
  sz = None
  if len1 % 2 == 0:
    sz = 2
  elif len1 % 3 == 0:
    sz = 3
  arr = []
  arr_temp = [ [ ' ' for i in range(sz) ] for x in range(sz) ]
  for y in range(0,len1, sz):
    for x in range(0,len1,sz):
      y0 = 0
      for y1 in range(y,y+sz):
        x0 = 0
        for x1 in range(x,x+sz):
          arr_temp[y0][x0] = image[y1][x1]
          x0 += 1
        y0 += 1
      arr.append(deepcopy(arr_temp))
  return arr

def get_pattern(a):
  global patterns, rules

  for i in range(len(rules)):
    r = rules[i]
    if len(r) != len(a):
      continue
    if is_match(a, r):
      return patterns[i]
  return []

def is_match(a, r):
  sz = len(a)
  rarr = [ [ '' for x in range(sz) ] for y in range(sz) ]
  for y in range(len(r)):
    for x in range(len(r[y])):
      rarr[y][x] = r[y][x]

  p = deepcopy(a)  # pattern
  if p == rarr:
    return True
  
  for i in range(3):
    rotate(p)
    if p == rarr:
      return True
    
  flip(p)
  if p == rarr:
    return True

  for i in range(3):
    rotate(p)
    if p == rarr:
      return True

  return False  


# read in input file
rules=[]
patterns=[]
temp_patterns=[]
l=[]
my_file = open("inp.txt", "r", encoding='utf-8')
lines = my_file.readlines()
for line in lines:
  l.append(line.strip())

for s in l:
  s = s.replace(' ','').replace('=>',',')
  a = s.split(',')
  rules.append(a[0].split('/'))
  temp_patterns.append(a[1].split('/'))

patterns = [ None for i in range(len(temp_patterns))]
for i in range(len(temp_patterns)):
  p = temp_patterns[i]
  sz = len(p)
  arr1 = [ [ '' for i in range(sz) ] for x in range(sz) ]
  for y in range(len(p)):
    for x in range(len(p[y])):
      arr1[y][x] = p[y][x]
  patterns[i] = arr1

# starting image
arr = '.#./..#/###'.split('/')

image = [ [ ' ' for i in range(len(arr)) ] for j in range(len(arr)) ]
for y in range(len(arr)):
  for x in range(len(arr[y])):
    image[y][x] = arr[y][x]

iterations = 18

# breaks up image into 2x2 or 3x3 images. array is in order 
# starting from top row 0, left-to-right , top-to-bottom
# for example, if 3x3 images, then dimension (x) of overall square: x = len(images) / 3
for t in range(iterations):
  print('t: ' + str(t) + '   count: ' + str(count_on(image)))
  images = breakup_image(image)
  new_squares = [ None for k in range(len(images)) ]
  sz = None
  for i in range(len(images)):
    square = images[i]
    pattern = get_pattern(square)
    new_squares[i] = deepcopy(pattern)

  N = int(math.sqrt(len(new_squares))) # e.g., if result is N, then arrange squares in 2x2
  image = combine(new_squares, N)

print()
print( count_on(image) )

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')