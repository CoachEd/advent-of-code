import sys
import time
import re 

start_secs = time.time()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

"""
It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
"""
badregex = re.compile(r'ab|cd|pq|xy') 
dupregex = re.compile (r'a{2}|b{2}|c{2}|d{2}|e{2}|f{2}|g{2}|h{2}|i{2}|j{2}|k{2}|l{2}|m{2}|n{2}|o{2}|p{2}|q{2}|r{2}|s{2}|t{2}|u{2}|v{2}|w{2}|x{2}|y{2}|z{2}') 
vowregex = re.compile(r'a|e|i|o|u')

# part 1
cnt = 0
for w in l:
    #filter out bad words
    mo = badregex.search(w)
    if mo != None:
        continue
    # must have at least one repeated letter
    mo = dupregex.search(w)
    if mo == None:
        continue
    # must have at least three vowels
    arr = re.findall(vowregex,w)
    if len(arr) < 3:
        continue
    cnt = cnt + 1
print('Part 1: ' + str(cnt))

# part 2
"""
It contains a pair of any two letters that appears at least twice in the string without overlapping, 
like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

It contains at least one letter which repeats with exactly one letter between them, 
like xyx, abcdefeghi (efe), or even aaa.
"""
cnt = 0
idx=0
for w in l:
    idx = idx +1
    # rule 1
    b = False
    for i in range(0,len(w)-3):
        s = w[i:i+2]
        #print(s + ' , ' + w[i+2:])
        if w[i+2:].find(s) != -1:
            b = True
            break
    if not b:
        continue

    # rule 2
    b = False
    for i in range(0,len(w)-2):
        s = w[i:i+3]
        if (s[0] == s[2]):
            #print(s + '   ' + w)
            b = True
            break
    if not b:
        continue
    #print(idx)
    cnt = cnt + 1

print('Part 2: ' + str(cnt)) # 409 too high , 65, 67, 59

end_secs = time.time()
print(str(end_secs-start_secs))