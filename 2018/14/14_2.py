

# get first 10 digits after this many numbers
#totalnumbers = 505961
# WOW! that took a freaking long time (10+ mins):
# CORRECT: 20231866

print('working...')
aftermaking = 100000000 # 100 000 000
totalnumbers = aftermaking + 10 + 100 # TEST
arr = [-1]*(totalnumbers + 1000000)
#print(str(len(arr)))

arr[0] = 3
arr[1] = 7
elf1 = 0
elf2 = 1
currlen = 2
numbers = 2 # count

#temp = -1
while numbers < (totalnumbers):
  #temp = temp + 1
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
    try:
      arr[currlen] = new1
      currlen = currlen + 1
      numbers = numbers + 1
    except IndexError:
      print('error1: ' + str(temp) + ' ' + str(currlen) )
  else:
    # add two recipes
    try:
      arr[currlen] = new1
      currlen = currlen + 1
      arr[currlen] = new2     # ERROR HERE
      currlen = currlen + 1
      numbers = numbers + 2
    except IndexError:
      print('error2: ' + str(temp) + ' ' + str(currlen) )

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

print('searching...')
outs = ''
out2s = ''
#for i in range(0,aftermaking+10):
for i in range(0,len(arr)):
  if arr[i] > -1:
    #if (arr[i] >= 10):
    #  print('error: i,arr[i]: ' + str(i) + ',' + str(arr[i]) )
    #if i >= aftermaking:
    #  outs = outs + str(arr[i])
    #else:
    out2s = out2s + str(arr[i])
#print(outs)

print()
print(out2s.find( '51589' ) ) #9
print(out2s.find( '01245' ) ) #5
print(out2s.find( '92510' ) ) #18
print(out2s.find( '59414' ) ) #2018

print('answer: ' + str(out2s.find( '505961' )) )





  
