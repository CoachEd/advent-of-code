import numpy as np


def printmap(m):
  s = ''
  for r in range(len(m)):
    for c in range(len(m[r])):
      s = s + m[r][c]
    s = s + '\n'
  print(s)

# X,Y == col,row  0,0 is top left corner
cartchars = 'v><^'
UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'
trackchars = '/\|+- '
moves = ['left','straight','right'] # repeating
carts = []

# read in file
with open('mapsmall.txt', "r") as f:
  content = f.readlines()


maxrows = 0
maxcols = 0
for l in content:
  maxrows = maxrows + 1
  # remove trailing newline
  l = l.rstrip('\n')
  maxcols = 0
  for c in l:
    maxcols = maxcols + 1

print('maxcols: ' + str(maxcols) +  ' , maxrows: ' + str(maxrows) )
# the map only
themap = [[' ' for x in range(maxcols)] for y in range(maxrows)]
row = 0
for l in content:
  l = l.rstrip('\n')
  col = 0
  for c in l:
    themap[row][col] = c
    col = col + 1
  row = row + 1

# create carts
for r in range(len(themap)):
  for c in range(len(themap[r])):
    if themap[r][c] in cartchars:
      on = '-'
      if themap[r][c] == UP or themap[r][c] == DOWN:
        on = '|'
      cart1 = {
        'c': themap[r][c],
        'on': on,
        'x': c,
        'y': r,
        'seen': False,
        'nexti': 0
      }
      carts.append(cart1)

print('initial carts:')
for i in range(len(carts)):
  print(carts[i]['c'] + ',' + str(carts[i]['x']) + ',' + str(carts[i]['y']) + ',' + str(carts[i]['nexti']))

crash = False
t = 0
while not crash:

  # sort the carts
  for i in range(len(carts)):
    for j in range(i+1,len(carts)):
      if carts[j]['y'] < carts[i]['y']:
        # swap
        temp = carts[i]
        carts[i] = carts[j]
        carts[j] = temp
      elif carts[j]['y'] == carts[i]['y']:
        if carts[j]['x'] < carts[i]['x']:
          # swap
          temp = carts[i]
          carts[i] = carts[j]
          carts[j] = temp

  for i in range(len(carts)):      
    cart = carts[i]
    x = cart['x']
    y = cart['y']
    if not cart['seen']:
      # found it
      facing = cart['c']

      if cart['on'] == '-' or cart['on'] == '|' or cart['on'] == '+':
        if facing == RIGHT:
          nexty = y
          nextx = x+1
        elif facing == LEFT:
          nexty = y
          nextx = x-1
        elif facing == UP:
          nexty = y-1
          nextx = x
        elif facing == DOWN:
          nexty = y+1
          nextx = x
      elif cart['on'] == '/':
        if facing == RIGHT:
          nexty = y
          nextx = x+1
        elif facing == LEFT:
          nexty = y
          nextx = x-1
        elif facing == UP:
          nexty = y-1
          nextx = x
        elif facing == DOWN:
          nexty = y+1
          nextx = x
      elif cart['on'] == '\\':
        if facing == RIGHT:
          nexty = y
          nextx = x+1
        elif facing == LEFT:
          nexty = y
          nextx = x-1
        elif facing == UP:
          nexty = y-1
          nextx = x
        elif facing == DOWN:
          nexty = y+1
          nextx = x              
        
      #print(cart['c'] + ' ' + str(cart['y']) + ',' + str(cart['x']) + '    ' + str(nexty) + ',' + str(nextx) )
      if themap[nexty][nextx] in cartchars:
        print("BOOM! " + str(nextx) + ',' + str(nexty))
        crash = True
        break
      else:
        # move this cart
        # make current space a line
        # /\|+- 
        themap[y][x] = cart['on'] # put a track on the space that I am currently on
        # update track that i will be on
        cart['on'] = themap[nexty][nextx]
        
        if themap[nexty][nextx] == '-':
          # means we are facing left or right
          themap[nexty][nextx] = facing
        elif themap[nexty][nextx] == '\\':
          if facing == RIGHT:
            cart['c'] = DOWN
          elif facing == LEFT:
            cart['c'] = UP
          elif facing == UP:
            cart['c'] = LEFT
          elif facing == DOWN:
            cart['c'] = RIGHT
          themap[nexty][nextx] = cart['c']  
        elif themap[nexty][nextx] == '/':
          if facing == RIGHT:
            cart['c'] = UP
          elif facing == LEFT:
            cart['c'] = DOWN
          elif facing == UP:
            cart['c'] = RIGHT
          elif facing == DOWN:
            cart['c'] = LEFT
          themap[nexty][nextx] = cart['c'] 
        elif themap[nexty][nextx] == '+':
          move = moves[cart['nexti']] # left, straight, right, ...
          cart['nexti'] = cart['nexti'] + 1
          if cart['nexti'] >= len(moves):
            cart['nexti'] = 0
          if facing == RIGHT:
            if move == 'left':
              cart['c'] = UP
            elif move == 'right':
              cart['c'] = DOWN
          elif facing == LEFT:
            if move == 'left':
              cart['c'] = DOWN
            elif move == 'right':
              cart['c'] = UP
          elif facing == UP:
            if move == 'left':
              cart['c'] = LEFT
            elif move == 'right':
              cart['c'] = RIGHT
          elif facing == DOWN:
            if move == 'left':
              cart['c'] = RIGHT
            elif move == 'right':
              cart['c'] = LEFT
              
          themap[nexty][nextx] = cart['c'] 
        elif themap[nexty][nextx] == '|':
          # means we are facing up or down
          themap[nexty][nextx] = facing

      # lastly, update its position
      cart['x'] = nextx
      cart['y'] = nexty
      cart['seen'] = True
      
      # done processing this cart

  # done processing all carts
  
  if crash:
    break
    
  # set all carts to NOT seen
  for i in range(len(carts)):
    cart = carts[i]
    cart['seen'] = False
          
  t = t + 1

print('done.')





