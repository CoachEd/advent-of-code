import sys
import time

start_secs = time.time()
print()

# read in input file
sues=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    d = dict()
    line = line.strip()
    first_colon = line.find(':')
    name = line[0:first_colon]
    rest = line[first_colon+1:]
    arr = rest.split(',')
    for e in arr:
        e = e.replace(' ','')
        arr2 = e.split(':')
        d[arr2[0]] = int(arr2[1])
    sues.append(d)

dsue = dict()
dsue['children']=3
dsue['cats']=7
dsue['samoyeds']=2
dsue['pomeranians']=3
dsue['akitas']=0
dsue['vizslas']=0
dsue['goldfish']=5
dsue['trees']=3
dsue['cars']=2
dsue['perfumes']=1

max_matches = 0
suei = 0
for i in range(0,len(sues)):
    sue = sues[i]
    matches = 0
    for key,value in sue.items():
        
        if key == 'cats' or key == 'trees':
            if value > dsue[key]:
                matches = matches + 1
        elif key == 'pomeranians' or key == 'goldfish':
            if value < dsue[key]:
                matches = matches + 1
        else:
            if dsue[key] == value:
                matches = matches + 1
    if matches >= max_matches:
        max_matches = matches
        suei = i
            
print('part 2: Sue ' + str(suei+1))


print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')