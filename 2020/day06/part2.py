import sys
l=[]
i=0
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
tmp=''
groups=0
for line in Lines:
    str1 = line.strip()
    if len(str1) == 0:
        l.append(tmp+':'+str(groups))
        tmp = ''
        groups=0
    else:
        tmp = tmp + str1
        groups=groups+1

cnt = 0
for s in l:
    arr=s.split(':')
    s = arr[0]
    groups=arr[1]
    while len(s) > 0:
        c = s[0]
        if s.count(c) == int(groups):
            cnt = cnt + 1
        s = s.replace(c,'')
        
print(cnt)
    
        
       
