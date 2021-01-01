import sys
import time

start_secs = time.time()

def factorize(num1):
    return [n for n in range(1, num1 + 1) if num1 % n == 0]

def num_presents(housenum):
    l = factorize(housenum)
    l2 =  [ i * 10 for i in l]
    return sum(l2)


n = 29000000
house_num = -1

for i in range(500000,10,-1):
    presents = num_presents(i)
    if presents >= n:
        house_num = i
        print('house_num: ' + str(house_num))



print('part 1: ' + str(house_num))
# too high: 800280
# too high: 702240 
print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')