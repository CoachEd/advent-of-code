import sys

l=[None]*323
i=0
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines: 
    str1 = line.strip()
    lt = list(str1*73)
    l[i] = lt
    i = i + 1

def ski(mx,my):
    x=0
    y=0
    num =0
    while True:
        x = x + mx
        y = y + my
        if y > 322:
            break
        c = l[y][x]
        if c == '#':
            num = num + 1
    return num

r1 = ski(1,1)
r2 = ski(3,1)     
r3 = ski(5,1)
r4 = ski(7,1)
r5 = ski(1,2)

print('Part 2: ' + str(r1*r2*r3*r4*r5))