import sys
import time

start_secs = time.time()
print()

s = '1113222113'
c = int(s[0])
count = 1
arr = []

for n in range(50):
    for i in range(1,len(s)):
        curr_c = int(s[i])
        if curr_c == c:
            count = count + 1
        elif curr_c != c:
            arr.append(str(count))
            arr.append(str(c))
            count = 1
            c = curr_c
    arr.append(str(count))
    arr.append(str(c))
    s = ''.join(arr)
    c = int(s[0])
    count = 1
    if n == 49:
        break
    arr = []

print('part 2: ' + str(len(arr)))



print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')