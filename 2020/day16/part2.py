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
        v[j]=1
        vfields[j].add(field)
    for j in range(x1,y1+1):
        if j < minf:
            minf = j
        if j > maxf:
            maxf = j         
        v[j]=1
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
    for ticket in good_tickets:
        field = ticket[i]
        unique_fields.add(field)
        st = poss_fields(vfields,field)
        for nm in st:
            if not nm in d:
                d[nm]=1
            else:
                d[nm] = d[nm] + 1

        #num_poss_fields = len(poss_fields(vfields,field)) # all fields map to 19 or 20 possible fields


print('min field: ' + str(minf)) # 48
print('max field: ' + str(maxf)) # 961
print('# good tickets: ' + str(len(good_tickets))) # 190
print('unique_fields: ' + str(unique_fields))