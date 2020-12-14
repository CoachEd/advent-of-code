import sys
from copy import copy, deepcopy

#68719476735

l=[]

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(line.strip())

mask=''
addr=0
val=0
mem = dict()
barr=[0]*36
for s in l:
    arr=s.split(' = ')
    if arr[0] == 'mask':
        mask=arr[1]
    else:
        addr=arr[0][4:]
        addr=int(addr.replace(']',''))
        val=int(arr[1])
        bval=str(bin(val))[2:].zfill(36)
        
        for i in range(0,len(bval)):
            if mask[i] != 'X':
                barr[i]=mask[i]
            else:
                barr[i]=bval[i]

        bs=''.join(barr)
        #print('mem: '+str(addr))
        #print(bs)
        #print(int(bs,2))
        mem[addr]=int(bs, 2)

sum = 0        
for key, value in mem.items():
    sum  = sum + value

print ('Part 1: ' + str(sum))
"""
mask = 100X100X101011111X100000100X11010011
mem[33323] = 349380
mem[52742] = 116688965
mem[4113] = 11499
mem[15819] = 313303
mem[23239] = 755579063
"""

