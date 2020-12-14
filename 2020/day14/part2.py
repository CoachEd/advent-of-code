import sys
from copy import copy, deepcopy
import itertools
from itertools import combinations


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
barr=[' ']*36
for s in l:
    arr=s.split(' = ')
    if arr[0] == 'mask':
        mask=arr[1]
    else:
        addr=arr[0][4:]
        addr=int(addr.replace(']',''))
        val=int(arr[1])
        bval=str(bin(addr))[2:].zfill(36)
        #print(bval)
        
        for i in range(0,len(bval)):
            if mask[i] == '1':
                barr[i]='1'
            elif mask[i]=='X':
                barr[i]='X'
            else:
                barr[i]=bval[i]

        #print(''.join(barr))
        n  = barr.count('X')
        sz = pow(2,n)
        arr2 = [ barr.copy() for i in range(sz)]
        
        lst = list(map(list, itertools.product([0, 1], repeat=n)))
        for j in range(0,len(arr2)):
            idx=0
            for k in range(0, len(arr2[j])):
                if arr2[j][k] == 'X':
                    arr2[j][k] = str(lst[j][idx])
                    idx =idx+1
        
                    
        for j in range(0,len(arr2)): 
            #print(arr2[j])
            bs=''.join(arr2[j])
            #print(bs)
            addr=int(bs,2)
            mem[addr]=val
            

        #print('mem: '+str(addr))
        #print(bs)
        #print(int(bs,2))
        #mem[addr]=int(bs, 2)

sum = 0        
for key, value in mem.items():
    sum  = sum + value




print ('Part 2: ' + str(sum))
"""
mask = 100X100X101011111X100000100X11010011
mem[33323] = 349380
mem[52742] = 116688965
mem[4113] = 11499
mem[15819] = 313303
mem[23239] = 755579063
"""
