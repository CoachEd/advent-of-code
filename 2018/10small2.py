import array
import math
from PIL import Image

stars =  [
  [ 9,  1,  0,  2],
  [ 7,  0, -1,  0],
  [ 3, -2, -1,  1],
  [ 6, 10, -2, -1],
  [ 2, -4,  2,  2],
  [-6, 10,  2, -2],
  [ 1,  8,  1, -1],
  [ 1,  7,  1,  0],
  [-3, 11,  1, -2],
  [ 7,  6, -1, -1],
  [-2,  3,  1,  0],
  [-4,  3,  2,  0],
  [10, -3, -1,  1],
  [ 5, 11,  1, -2],
  [ 4,  7,  0, -1],
  [ 8, -2,  0,  1],
  [15,  0, -2,  0],
  [ 1,  6,  1,  0],
  [ 8,  9,  0, -1],
  [ 3,  3, -1,  1],
  [ 0,  5,  0, -1],
  [-2,  2,  2,  0],
  [ 5, -2,  1,  2],
  [ 1,  4,  2,  1],
  [-2,  7,  2, -2],
  [ 3,  6, -1, -1],
  [ 5,  0,  1,  0],
  [-6,  0,  2,  0],
  [ 5,  9,  1, -2],
  [14,  7, -2,  0],
  [-3,  6,  2, -1]
];

max_x = 15
max_y = 15
rows = max_x * 2
cols = max_y * 2
offset = 15
table = []
iterations = 4

img = Image.new( 'RGB', (rows,cols), "black") # create a new black image
pixels = img.load() # create the pixel map
img.save('message','png')

# reset table
print('creating table...')
table = [array.array('b',[0])*rows for j in range(rows)]

print('adding stars...')
for i in range(len(stars)):
  entry = stars[i]
  x = entry[0]-1+offset
  y = entry[1]-1+offset
  table[y][x] = 1
  print(str(x) + ',' + str(y))
  pixels[x,y] = (255,255,255)

img.save('message','png')

print('entering loop...')
for t in range(iterations):
  print('time: ' + str(t))

  # do something with table
  s = ''
  for r in range(rows):
    for c in range(cols):
      thec = table[r][c]
      if thec == 0:
        s = s + ' '
      else:
        s = s + '*'
    s = s + '\n'
  print(s)
  #img.show()
  img.save('message','png')

  # reset table
  table = [array.array('b',[0])*rows for j in range(rows)]
  for r in range(rows):
    for c in range(cols):
      pixels[r,c] = (0,0,0)

  # update star locations
  for i in range(len(stars)):
    addx = stars[i][2]
    addy = stars[i][3]
    stars[i][0] = stars[i][0] + addx
    stars[i][1] = stars[i][1] + addy
    x = stars[i][0]-1+offset
    y = stars[i][1]-1+offset
    table[y][x] = 1
    pixels[x,y] = (255,255,255)

print('done.')

