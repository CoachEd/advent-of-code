
zeroindex = 0
s = "#..#.#..##......###...###"

# true strings
hm = "|...##|..#..|.#...|.#.#.|.#.##|.##..|.####|#.#.#|#.###|##.#.|##.##|###..|###.#|####.|"

# initialize the pot numbers
potsn = [0]*len(s)
for i in range(0,len(s)):
  potsn[i] = i

sumn = 0
for g in range(21):
  outs = ''

  outs = outs + str(g).rjust(2) + ':  '

  # if first 2 isn't .., add two empty pots to the front
  firsti = potsn[0]
  lasti = potsn[len(potsn)-1]

  if s[0:3] != '...':
    s = '..'+s
    potsn.insert(0,0)
    potsn.insert(0,0)
    potsn[0] = firsti-2
    potsn[1] = firsti-1

  if s[len(s)-3:] != '...':
    s = s + '..'
    potsn.append(0)
    potsn.append(0)
    potsn[len(potsn)-1] = lasti+2
    potsn[len(potsn)-2] = lasti+1
  
  # print out the current generation
  pots = ['.']*len(s)
  sumn = 0
  for i in range(0,len(s)):
    pots[i] = s[i]
    outs = outs + pots[i]
    if pots[i] == '#':
      sumn = sumn + potsn[i]
  print(outs)

  # create next generation of pots 
  npots = ['.']*len(pots)
  for i in range(2,len(pots)-2):
    pattern = s[i-2:i+3]  
    if "|"+pattern+"|" in hm:
      npots[i] = '#'

  s = ''
  for c in npots:
    s = s + c

print(sumn)
