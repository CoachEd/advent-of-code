import sys
import time

start_secs = time.time()

def build_tree(t,l,i,src):
    if len(l) == 0:
        t[src] = [-2] #leaf
        return
    t[src] = [-1,-1,-1]
    #print(l[0])
    if i >= len(l):
        t[src] = [-2]
        return
    if (l[i] - src) == 1:
        n = l[i]
        i = i + 1
        t[src][0] = n
        build_tree(t,l,i,n)
    if i < len(l) and (l[i] - src) == 2:
        n = l[i]
        i = i + 1
        t[src][1] = n
        build_tree(t,l,i,n)
    if i < len(l) and (l[i] - src) == 3:
        n = l[i]
        i = i + 1
        t[src][2] = n
        build_tree(t,l,i,n)
    return t

def count_leaves(t,i):
    if t[i][0] == -2:
        return 1
    cnt = 0
    if t[i][0] != -1:
        cnt = cnt + count_leaves(t,t[i][0])
    if t[i][1] != -1:
        cnt = cnt + count_leaves(t,t[i][1])
    if t[i][2] != -1:
        cnt = cnt + count_leaves(t,t[i][2])
    return cnt
 
l=[]
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(int(line.strip()))

l.sort()
t=dict()
print('building tree...')
build_tree(t,l,0,0)

print('counting leaves...')
print( count_leaves(t,0) )

end_secs = time.time()
print()
print(str(end_secs-start_secs))         
#ans=count_leaves(t)
#print('part 2: ' + str(ans))