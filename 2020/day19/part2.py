import sys
import re
import time

start_secs = time.time()

l=[]
msgs=[]
parsing_rules = True
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    s = line.strip()
    if len(s) == 0:
        parsing_rules = False
    if parsing_rules:
        l.append(s)        
    else:
        msgs.append(s)

d=dict()
for s in l:
    arr=s.split(':')
    rule_num=arr[0].strip()
    rule=arr[1].strip()
    if rule.find('a') != -1 or rule.find('b') != -1:
        d[rule_num]=rule.replace('"','')
    else:
        d[rule_num]=rule

# replace rules for Part 2:
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31

d['8'] = '42 42'  # 277
#d['11'] = '42 31 | 42 42 42 31 31 31'
d['11'] = '42 31 | 42 42 31 31'

"""
Only Rule 0 uses Rule 8 and Rule 11, no other rule

0: 8 11 
8: 42 | 42 8
11: 42 31 | 42 11 31

-or-

(42 | 42 8) (42 31 | 42 11 31)
Is this it? (42+)(42+31+)

42: "a" 134 | "b" 106
31: "b" 71 | "a" 120

103: "a" ("a" "b" | "a" "a") | "b" ("a" "a" | "b" "b")
57: ("b" "b" | "a" "b") "b" | ("b" "b" | "b" "a") "a"
27: "b" ("b" "b" | "b" "a") | "a" ("a" "b" | "a" "a")
127: ("b" "b" | "b" "a") "b"
130: ("b" "b" | "b" "a") ("b" | "a")
66: ("b" "a" | "a" "b") "a" | ("b" "b" | "a" "b") "b"
57: ("b" "b" | "a" "b") "b" | ("b" "b" | "b" "a") "a"
98: ("b" | "a") ("b" "b" | "a" "b")
117: ("a" "b" | "a" "a") ("b" | "a")
107: "b" ("a" "b" | "a" "a") | "a" ("b" "a" | "a" "b")
117: ("a" "b" | "a" "a") ("b" | "a")
103: "a" ("a" "b" | "a" "a") | "b" ("a" "a" | "b" "b")
122: "b" ("b" | "a") | "a" "a"
73: ("b" | "a") "b" | "a" "a"
87: ("b" | "a") "a" | "a" "b"
129: ("b" | "a") ("a" ("a" "b" | "a" "a") | "b" ("a" "a" | "b" "b"))
88: "a" "b" | "b" ("b" | "a")
13: (("b" | "a") "b" | "a" "a") ("b" | "a")
33: ("b" | "a") ("b" | "a")
94: ("b" | "a") (("b" | "a") "a" | "a" "b")
130: ("b" "b" | "b" "a") ("b" | "a")
13: (("b" | "a") "b" | "a" "a") ("b" | "a")
66: ("b" "a" | "a" "b") "a" | ("b" "b" | "a" "b") "b"
107: "b" ("a" "b" | "a" "a") | "a" ("b" "a" | "a" "b")

62: "a" "a" | "b" "b"
56: "b" "b" | "b" "a"
93: "b" "b" | "a" "b"
3: "a" "b" | "a" "a"
92: "b" | "a"
46: "b" "a" | "a" "b"




"""


# next rule number: 138

def isMatch(p,s):
    m = re.match(p,s)
    if m == None:
        return False
    else:
        (i,j) = m.span()
        if (j-i) == len(s):
            return True
        else:
            return False

def parse(rule):
    global d
    if rule == 'a' or rule == 'b' or rule == 'c' or rule == 'd':
        return rule
    s=''
    if rule.find('|') == -1:
        arr = rule.split() 
        for r in arr:
            s = s + '(' + parse(d[r]) + ')'
        return s
    else:
        s = '('
        arr2 = rule.split('|')
        for i in range(0,len(arr2)):
            arr = arr2[i].split()
            for r in arr:
                if r == 'c' or r == 'd':
                    s = s + r
                else:
                    s = s + parse(d[r])
            if i < len(arr2)-1:
                s = s + '|'
        return s + ')'


p = parse(d['0'])
#print(p)
#sys.exit()

count = 0
for m in msgs:
    if isMatch(p,m):
        count = count + 1
        
        
print('part 2: ' + str(count))   
# 437 too high, 386 too high, 391 (?) (235 last time, so answer > 235 answer < 386)
# 249 too low
# 294 WRONG
# 308 WRONG



end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')