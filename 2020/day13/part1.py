import sys
import time

start_secs = time.time()

n=1004098
s='23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'
arr = s.split(',')
times=[]
d = dict()
for e in arr:
    if e != 'x':
        times.append(int(e))
        d[int(e)] = 0
print(times)



while True:
    cnt = 0
    for t in times:
        if d[t] < n:
            d[t] = d[t] + t
        else:
            cnt = cnt + 1
    if cnt == len(times):
        break

for key, value in d.items():
    print(str(key) + ': ' + str(value-n))

# hard-coded
print()
print('Part 1: ' + str(401*6))

end_secs = time.time()
print(str(end_secs-start_secs))