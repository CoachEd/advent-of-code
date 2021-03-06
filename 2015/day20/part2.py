import sys
import time

start_secs = time.time()

num1=705600+2 # through process of elimination, i knew the answer was in the 700K range
arr=[0 for n in range(1, num1) ]

def factorize(num2):
    #print('f')
    global arr
    len1=len(arr)
    for i in range(1,len1):
        if num2 % i == 0 and i <= num2:
            arr[i-1]=i
        else:
            arr[i-1]=0
            
    for i in range(num2+1,len1):
        del arr[-1]
    #print('f\n')

def num_presents(housenum):
    global arr
    factorize(housenum)
    total=0
    for i in range(0,len(arr)):
        if housenum <= arr[i]*50:
            arr[i]=arr[i]*11
            total=total+arr[i]
    return(total)

n = 29000000
house_num = -1
# 735840
for i in range(num1,10,-1):
    presents = num_presents(i)
    if presents >= n:
        house_num = i
        #print('house_num: ' + str(house_num)+ '  presents: ' + str(presents))
        break

print('part 2: ' + str(house_num))

print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')