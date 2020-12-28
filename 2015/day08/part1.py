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
mem_chars = 0
for s in l:
    code_chars = code_chars + len(s)
    idx = 1
    while idx < len(s)-1:
        if s[idx] == '\\':
            mem_chars = mem_chars +1
            idx=idx+1
            if s[idx] == 'x':
                idx = idx + 1
                idx = idx + 1
        else:
            mem_chars = mem_chars +1
        idx = idx+1
        if idx >= len(s)-1:
            break
            
print('part 1: ' + str(code_chars-mem_chars))  
                
# 6468 too high


end_secs = time.time()
print(str(end_secs-start_secs))