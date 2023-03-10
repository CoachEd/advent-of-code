import time
import sys
import math
from copy import copy, deepcopy
start_secs = time.time()
print('')


def combine(squares, N):
  # squares is an array of 2D squares
  # N is the dimension while combining the above squares; N=2... 2x2 squares
  square_sz = len(squares[0])
  final_square_sz = square_sz * N
  image = [ [ ' ' for i in range(final_square_sz) ] for j in range(final_square_sz) ]
  for sq in squares:
    # TODO:
    # add sq to right position in 2D image array
    # square_sz and final_square_sz will help here.
    pass

  # return a 2D array of the combined squares
  pass

def print_square(square):
  s = ''
  for y in range(len(square)):
    for x in range(len(square[y])):
      s += square[y][x]
    s += '\n'
  print(s)

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
  len1 = len(a)
  if len1 == 3:
    # no rotation
    t1 = (r[0][0], r[0][1], r[0][2], r[1][0], r[1][1], r[1][2], r[2][0], r[2][1], r[2][2])
    t2 = (a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2], a[2][0], a[2][1], a[2][2])
    if t1 == t2:
      return True
    
    # rotate a one turn
    t1 = (r[0][0], r[0][1], r[0][2], r[1][0], r[1][1], r[1][2], r[2][0], r[2][1], r[2][2])
    t2 = (a[2][0], a[1][0], a[0][0], a[2][1], a[1][1], a[0][1], a[2][2], a[1][2], a[0][2])
    if t1 == t2:
      return True

    # rotate a one turn
    t1 = (r[0][0], r[0][1], r[0][2], r[1][0], r[1][1], r[1][2], r[2][0], r[2][1], r[2][2])
    t2 = (a[2][2], a[2][1], a[2][0], a[1][2], a[1][1], a[1][0], a[0][2], a[0][1], a[0][0])
    if t1 == t2:
      return True
    
    # rotate a one turn
    t1 = (r[0][0], r[0][1], r[0][2], r[1][0], r[1][1], r[1][2], r[2][0], r[2][1], r[2][2])
    t2 = (a[0][2], a[1][2], a[2][2], a[0][1], a[1][1], a[2][1], a[0][0], a[1][0], a[2][0])
    if t1 == t2:
      return True  
    
    return False
  elif len1 == 2:
    # no rotation
    t1 = (r[0][0], r[0][1], r[1][0], r[1][1])
    t2 = (a[0][0], a[0][1], a[1][0], a[1][1])
    if t1 == t2:
      return True
    
    # rotate one turn
    t1 = (r[0][0], r[0][1], r[1][0], r[1][1])
    t2 = (a[1][0], a[0][0], a[1][1], a[0][1])
    if t1 == t2:
      return True  
    
    # rotate one turn
    t1 = (r[0][0], r[0][1], r[1][0], r[1][1])
    t2 = (a[1][1], a[1][0], a[0][1], a[0][0])
    if t1 == t2:
      return True    

    # rotate one turn
    t1 = (r[0][0], r[0][1], r[1][0], r[1][1])
    t2 = (a[0][1], a[1][1], a[0][0], a[1][0])
    if t1 == t2:
      return True    
  else:
    print('error! no match for length: ' + str(len1))

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

arr = '#..#/..../..../#..#'.split('/') # TEST

image = [ [ ' ' for i in range(len(arr)) ] for j in range(len(arr)) ]
for y in range(len(arr)):
  for x in range(len(arr[y])):
    image[y][x] = arr[y][x]

# TODO LEFT OFF HERE
iterations = 1
# breaks up image into 2x2 or 3x3 images. array is in order 
# starting from top row 0, left-to-right , top-to-bottom
# for example, if 3x3 images, then dimension (x) of overall square: x = len(images) / 3
images = breakup_image(image) 
for i in range(iterations):
  new_squares = [ None for i in range(len(images)) ]
  sz = None
  for i in range(len(images)):
    square = images[i]
    pattern = get_pattern(square)
    new_squares[i] = deepcopy(pattern) # for this square, get the pattern that it becomes
  
  N = math.sqrt(len(new_squares)) # e.g., if result is N, then arrange squares in 2x2
  # TODO: take all squares in new_squares, arrange them in N x N, 2D array, assign it to images
  # images = combine(new_squares, N)  # TODO

print('')
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')