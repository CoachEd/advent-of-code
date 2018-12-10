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

rows = 30
cols = 30
offset = 15
table = []

# reset table
for r in range(rows):
  r = []
  for c in range(cols):
    r.append('-')
  table.append(r)

for i in range(len(stars)):
  entry = stars[i]
  x = entry[0]-1+offset
  y = entry[1]-1+offset
  table[y][x] = '*'


s = ''
for r in range(rows):
  for c in range(cols):
    s = s + table[r][c]
  s = s + '\n'
print(s)
       
for t in range(3):

  # reset table
  for r in range(rows):
    for c in range(cols):
      table[r][c]='-'

  # advance time
  for i in range(len(stars)):
    addx = stars[i][2]
    addy = stars[i][3]
    stars[i][0] = stars[i][0] + addx
    stars[i][1] = stars[i][1] + addy
    x = stars[i][0]-1+offset
    y = stars[i][1]-1+offset
    table[y][x] = '*'

  s = ''
  for r in range(rows):
    for c in range(cols):
      s = s + table[r][c]
    s = s + '\n'
  print(s)



