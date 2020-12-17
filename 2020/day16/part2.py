import sys

print()
def poss_fields(v,i):
    #vfields = [set() for x in range(1000)]
    st = v[i]
    return(st)

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
fields = []
for i in range(0, len(rules)):
    arr = rules[i].split(':')
    field = arr[0].strip()
    fields.append(field)
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

vfields = [set() for x in range(1000)]
for i in range(0,len(ranges)):
    x=ranges[i][0]
    y=ranges[i][1]
    x1=ranges[i][2]
    y1=ranges[i][3]
    field = fields[i]
    minf = sys.maxsize
    maxf = -1
    for j in range(x,y+1):
        if j < minf:
            minf = j
        if j > maxf:
            maxf = j 
        v[j]=v[j]+1
        vfields[j].add(field)
    for j in range(x1,y1+1):
        if j < minf:
            minf = j
        if j > maxf:
            maxf = j         
        v[j]=v[j]+1
        vfields[j].add(field)

good_tickets = []

for arr in ntickets:
    good = True
    for n in arr:
        if v[n] == 0:
            good = False
            break
    if good:
        good_tickets.append(arr)
    
# good_tickets do NOT include my ticket
unique_fields = set()
for i in range(0,20):
    #print('Field ' + str(i)+ ': ')
    d = dict()
    s = ''
    for j in range(0, len(ranges)):
        good = True
        for ticket in good_tickets:
            field = ticket[i]
            if not ((field >= ranges[j][0] and field <= ranges[j][1] ) or (field >= ranges[j][2] and field <= ranges[j][3] )):
              good = False
              break
        if good:
            print('column ' + str(i) + ' could be field: ' + fields[j] )
    print()

print('analyze offline...')
#print('min field: ' + str(minf)) # 48
#print('max field: ' + str(maxf)) # 961
#print('# good tickets: ' + str(len(good_tickets))) # 190

# After analyzing output...
"""
**COLUMN 0 could be field: departure track
**COLUMN 1 could be field: seat
**COLUMN 2 could be field: arrival station
**COLUMN 3 could be field: departure date
**COLUMN 4 could be field: departure location
**COLUMN 5 could be field: class
**COLUMN 6 could be field: duration
**COLUMN 7 could be field: departure time
**COLUMN 8 could be field: row
**COLUMN 9 could be field: departure platform
**COLUMN 10 could be field: arrival location
**COLUMN 11 could be field: departure station
**COLUMN 12 could be field: arrival platform
**COLUMN 13 could be field: arrival track
**COLUMN 14 could be field: type
**COLUMN 15 could be field: train
**COLUMN 16 could be field: price
**COLUMN 17 could be field: zone
**COLUMN 18 could be field: wagon
**COLUMN 19 could be field: route
"""
my_ticket=[89,179,173,167,157,127,163,113,137,109,151,131,97,149,107,83,79,139,59,53]
val = 1
for i in range(0,len(my_ticket)):
    if i in [0,3,4,7,9,11]:
        val = val * my_ticket[i]
print('part 2: ' + str(val))        
