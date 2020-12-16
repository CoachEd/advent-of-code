import sys

rules=[]
yticket=[]
ntickets=[]
ltickets=[]
v=[0]*1000
my_file = open("inp.txt", "r")
part=1
Lines = my_file.readlines()
maxi=-1
for line in Lines:
    s = line.strip()
    if part==1:
      if len(s) == 0:
        part = part+ 1
        continue
      rules.append( line.strip())
    elif part==2:
      if len(s) == 0:
        part=part+1
        continue
      if s.find('ticket') == -1:
        yticket = s.split(',')
    elif part== 3:
      if s.find('ticket') == -1:
        ltickets.append(line)

ranges=[]
for i in range(0, len(rules)):
    arr = rules[i].split(':')
    fiels = arr[0].strip()
    ranges.append(arr[1].replace(' or ','-').split('-'))
for i in range(0, len(ranges)):
    for j in range(0,len(ranges[i])):
        ranges[i][j]=int(ranges[i][j])
        if ranges[i][j] > maxi:
            maxi=ranges[i][j]

for i in range(0, len(yticket)):    
    yticket[i] = int(yticket[i])
    if yticket[i] > maxi:
        maxi = yticket[i]

for s in ltickets:
    arr=s.split(',')
    ntickets.append(arr)
for i in range(0, len(ntickets)):
    for j in range(0,len(ntickets[i])):
        ntickets[i][j]=int(ntickets[i][j])
        if ntickets[i][j] > maxi:
            maxi=ntickets[i][j]

for i in range(0,len(ranges)):
    x=ranges[i][0]
    y=ranges[i][1]
    x1=ranges[i][2]
    y1=ranges[i][3]
    for j in range(x,y+1):
        v[j]=1
    for j in range(x1,y1+1):
        v[j]=1

invalid = 0
for arr in ntickets:
    for n in arr:
        if v[n] == 0:
            invalid=invalid+n

print('part 1: ' +str(invalid))




#print(rules)
#print(yticket)
#print(ntickets[0])
#print(ntickets[-1])