

# get first 10 digits after this many numbers
#totalnumbers = 505961

aftermaking = 9
totalnumbers = aftermaking + 10 + 100 # TEST
arr = [-1]*(totalnumbers)


arr[0] = 3
arr[1] = 7
elf1 = 0
elf2 = 1
currlen = 2
numbers = 2 # count

while numbers < (totalnumbers):
  combined = arr[elf1] + arr[elf2]
  nexti = currlen

  # calculate recipes
  new1 = -1
  new2 = -1
  if combined == 10:
    new1 = 1
    new2 = 0
  elif combined < 10:
    # only one new recipe
    new1 = combined
  else:
    # two new recipes
    new1 = int(combined / 10)
    new2 = combined - 10

  if new2 == -1:
    # add one recipe
    arr[currlen] = new1
    currlen = currlen + 1
    numbers = numbers + 1
  else:
    # add two recipes
    arr[currlen] = new1
    currlen = currlen + 1
    arr[currlen] = new2
    currlen = currlen + 1
    numbers = numbers + 2

  # move elves
  elf1_next = 1 + arr[elf1]
  elf2_next = 1 + arr[elf2]

  # inefficient for now
  for i in range(0,elf1_next):
    elf1 = elf1 + 1
    if arr[elf1] == -1 or elf1 >= len(arr):
      elf1 = 0
  for i in range(0,elf2_next):
    elf2 = elf2 + 1
    if arr[elf2] == -1 or elf2 >= len(arr):
      elf2 = 0

outs = ''
for i in range(0,aftermaking+10):
  if arr[i] > -1 and i >= aftermaking:
    outs = outs + str(arr[i])
print(outs)
  










    



  
