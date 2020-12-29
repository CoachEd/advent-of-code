import sys
import time

start_secs = time.time()
print()
pairs = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']

def next_password(s):
    arr = [' '] * len(s)
    for i in range(0,len(s)):
        arr[i] = s[i]
    wrap = True  
    while wrap:
        for i in range(len(s)-1,-1,-1):
            c = arr[i]
            if c == 'z':
                arr[i] = 'a'
            else:
                c = ord(c) + 1
                arr[i] = chr(c)
                wrap = False
            if not wrap:
                break
        s = ''.join(arr)
    s = ''.join(arr)
    return s
    

def valid_password(s):
    # any invalid chars?
    if s.find('i') != -1 or s.find('o') != -1 or s.find('l') != -1:
        return False

    arr = [' '] * len(s)
    for i in range(0,len(s)):
        arr[i] = s[i]
    
    # straight?
    straight = False
    for i in range(0,len(arr)-3):
        x1 = ord(arr[i+1]) - ord(arr[i])
        x2 = ord(arr[i+2]) - ord(arr[i+1])
        if x1 == 1 and x2 == 1:
            straight = True
            break
    if not straight:
        return False
    
     # doubles?
    count_pairs = 0
    for p in pairs:
        if s.find(p) != -1:
            count_pairs = count_pairs + 1
        if count_pairs > 1:
            break
    if count_pairs <= 1:
        return False
    return True

s = 'hxbxwxba'
found = False
while not found:
    s = next_password(s)
    if valid_password(s):
        print(s)
        break

print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')