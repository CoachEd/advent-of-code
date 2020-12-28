import sys
import time

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

code_chars = 0
enc_chars=0
for s in l:
    code_chars = code_chars + len(s)
    enc_chars = enc_chars+2
    i = 0
    while i < len(s):
        c = s[i]
        if c == '"':
            enc_chars=enc_chars+2
        elif c=='\\':
            i = i + 1
            if i == len(s):
                break
            c= s[i]
            if c == '\\':
                enc_chars=enc_chars+4
            elif c == 'x':
                i = i + 2
                enc_chars=enc_chars+5
            elif c == '"':
                enc_chars=enc_chars+4
        else:
            enc_chars=enc_chars+1
        i = i + 1

print('part 2: ' + str(enc_chars-code_chars))  
                
# 2134 too high
# 1864 too low
# 2114 wrong
# 2124 wrong


end_secs = time.time()
print(str(end_secs-start_secs))