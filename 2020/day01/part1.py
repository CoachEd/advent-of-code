import sys
l=[]
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines: 
    l.append(int(line.strip()))

l.sort()

# part 1
for i in range(0,len(l)-1):
    for j in range (i+1,len(l)):
        if (l[i]+l[j]) == 2020:
            print('Part 1: '+str(l[i]*l[j]))
            sys.exit()
        elif (l[i]+l[j]) > 2020:
            break

            


        



        
