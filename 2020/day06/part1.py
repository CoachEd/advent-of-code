import sys
import time

start_secs = time.time()
l=[]
i=0
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
tmp=''
for line in Lines:
    str1 = line[:-1]
    if len(str1) == 0:
        l.append(tmp)
        tmp = ''
    else:
        tmp = tmp + str1

cnt = 0
for s in l:
    while len(s) > 0:
        c = s[0]
        cnt = cnt + 1
        s = s.replace(c,'')
print(cnt)
end_secs = time.time()
print(str(end_secs-start_secs))   
        
       
