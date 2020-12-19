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
# 31: 116 71 | 53 120
# 42: 53 134 | 116 106
d['8'] = '42 | 42 8'
d['11'] = '42 31 | 42 11 31'

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
    if rule == 'a' or rule == 'b':
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
                s = s + parse(d[r])
            if i < len(arr2)-1:
                s = s + '|'
        return s + ')'


p = parse(d['0'])
print(p)

count = 0
for m in msgs:
    if isMatch(p,m):
        count = count + 1
print('part 2: ' + str(count))

    
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')