import sys

l=[]
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    s = line.strip()
    l.append(s)
    
def remove_border(a):
    arr1 = []
    for y in range(1,len(a)-1):
        temp = []
        for x in range(1,len(a[y])-1):
            temp.append(a[y][x])
        arr1.append(temp)
    return arr1

def print_arr(a):
    s=''
    for r in a:
        for c in r:
            s = s + str(c)
        s = s + '\n'
    print(s)

def rotate_arr(a):
    a2=[ [ None for x in range(len(a))] for y in range(len(a)) ]
    y2=0
    x2=len(a[0])-1
    for y in range(0,len(a)):
        for x in range(0,len(a[y])):
            a2[y2][x2] = a[y][x]
            y2=y2+1
        y2=0
        x2=x2-1
    return(a2)

def flip_arr(a):
    a2=[ [ None for x in range(len(a))] for y in range(len(a)) ]
    x2=len(a[0])-1
    for y in range(0,len(a)):
        for x in range(0,len(a[y])):
            a2[y][x2] = a[y][x]
            x2=x2-1
        x2=len(a[0])-1
    return(a2)

def get_edge(a,direction):
    direction=direction.upper()
    s=''
    if direction=='N':
        return(a[0])
    elif direction=='S':
        return(a[len(a)-1])
    elif direction=='E':
        x=len(a[0])-1
        temp=[ None for x in range(0,len(a[0]))]
        for y in range(0,len(a)):
            temp[y]=a[y][x]
        return temp
    elif direction=='W':
        x=0
        temp=[ None for x in range(0,len(a[0]))]
        for y in range(0,len(a)):
            temp[y]=a[y][x]
        return temp
    else:
        return []

arr=[
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

print_arr(arr)
arr = remove_border(arr)
print_arr(arr)

"""
print_arr(arr)
arr=rotate_arr(arr)
arr=rotate_arr(arr)
arr=rotate_arr(arr)
arr=rotate_arr(arr)
print()
print_arr(arr)

arr=flip_arr(arr)
arr=flip_arr(arr)
print_arr(arr)

print( get_edge(arr,'n') )
print( get_edge(arr,'s') )
print( get_edge(arr,'e') )
print( get_edge(arr,'w') )
"""

