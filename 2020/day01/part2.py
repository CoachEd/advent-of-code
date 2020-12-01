# Part 2
import sys
l=[]
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines: 
    l.append(int(line.strip()))

l.sort()

for i in range(0,len(l)-2):
    for j in range (i+1,len(l)-1):
        for k in range(j+1,len(l)):
            if ( l[i] + l[j] + l[k] ) == 2020:
                print('Part 2: '+str(l[i] *l[j] * l[k]))
                sys.exit()
            elif ( l[i] + l[j] + l[k] ) > 2020:
                break