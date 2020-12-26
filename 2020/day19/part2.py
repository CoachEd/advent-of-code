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


#print(len(msgs)) # 487 original messages, 235 matched messages, 253 unmatched messages
ctr = 0

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

#d['8'] = '42'
#d['11'] = '42 31'
#d['8'] = '42 | c '
#d['11'] = '42 31 | d '

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

#p = parse(d['0'])
for n in range(1,11):
    p='(((a(b((((a(a)(a)|b(b)(a))b|((b|a))(((b|a))((b|a)))a)b|(b(b(bb|ba)|a(ab|aa))|a(a((b|a)b|aa)|b((b|a)a|ab)))a)b|((b(b(ba|ab)|a(b)(b))|a((b)(a)a|(b)(a)b))a|((a(a)(a)|b(bb|ab))a|((ab|aa)a|(b)(a)b)b)b)a)|a(b(b(a((a)(b)a|((b|a))((b|a))b)|b(b(a)(b)|a(ba|ab)))|a((((b|a))((b|a))b|(b)(a)a)b|((b|a))(((b|a)a|ab))a))|a(b(a((ab|aa)a|(b)(a)b)|b(b(a)(a)|a(ba|ab)))|a(b(a)((b)(b))|a(((b|a)a|ab)b|(ab|aa)a)))))|b(b(b(b(b((b)(b)b|(bb|ba)a)|a(b((b|a))((b|a))|a(b(b|a)|aa)))|a((b(ab|aa)|a(ba|ab))b|(((b|a)b|aa)a|((b|a))((b|a))b)a))|a(((b(a)(b)|a(ba|ab))b|(a((b|a)b|aa)|b(b)(a))a)b|(((a)(a)a|(b)(b)b)a|((b(b|a)|aa)a|(ab|aa)b)b)a))|a((((a(a)(b)|b(b)(a))b|((ab|aa))((b|a))a)b|((b(b)(a)|a(ab|aa))a|(a(b(b|a)|aa)|b((b|a)b|aa))b)a)b|(b((a(b)(b)|b((b|a)a|ab))b|((bb|ba)b|(b)(a)a)a)|a((a(b)(b)|b((b|a))((b|a)))b|((ab|aa))((b|a))a))a)))|(a(b((((a(a)(a)|b(b)(a))b|((b|a))(((b|a))((b|a)))a)b|(b(b(bb|ba)|a(ab|aa))|a(a((b|a)b|aa)|b((b|a)a|ab)))a)b|((b(b(ba|ab)|a(b)(b))|a((b)(a)a|(b)(a)b))a|((a(a)(a)|b(bb|ab))a|((ab|aa)a|(b)(a)b)b)b)a)|a(b(b(a((a)(b)a|((b|a))((b|a))b)|b(b(a)(b)|a(ba|ab)))|a((((b|a))((b|a))b|(b)(a)a)b|((b|a))(((b|a)a|ab))a))|a(b(a((ab|aa)a|(b)(a)b)|b(b(a)(a)|a(ba|ab)))|a(b(a)((b)(b))|a(((b|a)a|ab)b|(ab|aa)a)))))|b(b(b(b(b((b)(b)b|(bb|ba)a)|a(b((b|a))((b|a))|a(b(b|a)|aa)))|a((b(ab|aa)|a(ba|ab))b|(((b|a)b|aa)a|((b|a))((b|a))b)a))|a(((b(a)(b)|a(ba|ab))b|(a((b|a)b|aa)|b(b)(a))a)b|(((a)(a)a|(b)(b)b)a|((b(b|a)|aa)a|(ab|aa)b)b)a))|a((((a(a)(b)|b(b)(a))b|((ab|aa))((b|a))a)b|((b(b)(a)|a(ab|aa))a|(a(b(b|a)|aa)|b((b|a)b|aa))b)a)b|(b((a(b)(b)|b((b|a)a|ab))b|((bb|ba)b|(b)(a)a)a)|a((a(b)(b)|b((b|a))((b|a)))b|((ab|aa))((b|a))a))a))){2,}))(((a(b((((a(a)(a)|b(b)(a))b|((b|a))(((b|a))((b|a)))a)b|(b(b(bb|ba)|a(ab|aa))|a(a((b|a)b|aa)|b((b|a)a|ab)))a)b|((b(b(ba|ab)|a(b)(b))|a((b)(a)a|(b)(a)b))a|((a(a)(a)|b(bb|ab))a|((ab|aa)a|(b)(a)b)b)b)a)|a(b(b(a((a)(b)a|((b|a))((b|a))b)|b(b(a)(b)|a(ba|ab)))|a((((b|a))((b|a))b|(b)(a)a)b|((b|a))(((b|a)a|ab))a))|a(b(a((ab|aa)a|(b)(a)b)|b(b(a)(a)|a(ba|ab)))|a(b(a)((b)(b))|a(((b|a)a|ab)b|(ab|aa)a)))))|b(b(b(b(b((b)(b)b|(bb|ba)a)|a(b((b|a))((b|a))|a(b(b|a)|aa)))|a((b(ab|aa)|a(ba|ab))b|(((b|a)b|aa)a|((b|a))((b|a))b)a))|a(((b(a)(b)|a(ba|ab))b|(a((b|a)b|aa)|b(b)(a))a)b|(((a)(a)a|(b)(b)b)a|((b(b|a)|aa)a|(ab|aa)b)b)a))|a((((a(a)(b)|b(b)(a))b|((ab|aa))((b|a))a)b|((b(b)(a)|a(ab|aa))a|(a(b(b|a)|aa)|b((b|a)b|aa))b)a)b|(b((a(b)(b)|b((b|a)a|ab))b|((bb|ba)b|(b)(a)a)a)|a((a(b)(b)|b((b|a))((b|a)))b|((ab|aa))((b|a))a))a)))(b(b((a((b((b|a)b|aa)|a(b)(a))a|((bb|ab)b|(b(b|a)|aa)a)b)|b((b(b)(a)|a(bb|ab))b|((bb|ab)b|(b(b|a)|aa)a)a))b|(b(a((b)(a))(a)|b((b)(a)a|(b)(a)b))|a((b(bb|ab)|a(b)(a))b|((ab|b(b|a))a|((b|a)a|ab)b)a))a)|a(b(((b(b(b|a)|aa)|a((b|a))((b|a)))b|(((b|a)b|aa)a|(b)(a)b)a)b|(a(((b|a)a|ab)b|((b|a))((b|a))a)|b((b)(b)b|(b)(a)a))a)|a(b((b|a))((a(ab|aa)|b(aa|bb)))|a((b(b)(a)|a(b)(b))b|(a(bb|ab)|b(a)(b))a))))|a(b(b((b((b)(b)b|(ab|aa)a)|a((bb|ab)b|(bb|ba)a))b|(b(a((b|a)b|aa)|b(bb|ba))|a(((b|a)a|ab)a|(ab|aa)b))a)|a(((b(b(b|a)|aa)|a(bb|ba))b|(((b|a)b|aa))((b|a))a)a|(a((b)(b)b|(b)(a)a)|b(b(bb|ba)|a(b)(b)))b))|a((b(((bb|ba))((b|a))a|((b|a))((bb|ab))b)|a(((a)(b)a|((b|a))((b|a))b)b|((bb|ab)a|((b|a)a|ab)b)a))a|(b(b((bb|ba))(b)|a(((b|a)b|aa))(a))|a((b((b|a))((b|a))|a(bb|ab))b|((ba|ab)a|(bb|ab)b)a))b)))|((a(b((((a(a)(a)|b(b)(a))b|((b|a))(((b|a))((b|a)))a)b|(b(b(bb|ba)|a(ab|aa))|a(a((b|a)b|aa)|b((b|a)a|ab)))a)b|((b(b(ba|ab)|a(b)(b))|a((b)(a)a|(b)(a)b))a|((a(a)(a)|b(bb|ab))a|((ab|aa)a|(b)(a)b)b)b)a)|a(b(b(a((a)(b)a|((b|a))((b|a))b)|b(b(a)(b)|a(ba|ab)))|a((((b|a))((b|a))b|(b)(a)a)b|((b|a))(((b|a)a|ab))a))|a(b(a((ab|aa)a|(b)(a)b)|b(b(a)(a)|a(ba|ab)))|a(b(a)((b)(b))|a(((b|a)a|ab)b|(ab|aa)a)))))|b(b(b(b(b((b)(b)b|(bb|ba)a)|a(b((b|a))((b|a))|a(b(b|a)|aa)))|a((b(ab|aa)|a(ba|ab))b|(((b|a)b|aa)a|((b|a))((b|a))b)a))|a(((b(a)(b)|a(ba|ab))b|(a((b|a)b|aa)|b(b)(a))a)b|(((a)(a)a|(b)(b)b)a|((b(b|a)|aa)a|(ab|aa)b)b)a))|a((((a(a)(b)|b(b)(a))b|((ab|aa))((b|a))a)b|((b(b)(a)|a(ab|aa))a|(a(b(b|a)|aa)|b((b|a)b|aa))b)a)b|(b((a(b)(b)|b((b|a)a|ab))b|((bb|ba)b|(b)(a)a)a)|a((a(b)(b)|b((b|a))((b|a)))b|((ab|aa))((b|a))a))a))){' + str(n) + '}(b(b((a((b((b|a)b|aa)|a(b)(a))a|((bb|ab)b|(b(b|a)|aa)a)b)|b((b(b)(a)|a(bb|ab))b|((bb|ab)b|(b(b|a)|aa)a)a))b|(b(a((b)(a))(a)|b((b)(a)a|(b)(a)b))|a((b(bb|ab)|a(b)(a))b|((ab|b(b|a))a|((b|a)a|ab)b)a))a)|a(b(((b(b(b|a)|aa)|a((b|a))((b|a)))b|(((b|a)b|aa)a|(b)(a)b)a)b|(a(((b|a)a|ab)b|((b|a))((b|a))a)|b((b)(b)b|(b)(a)a))a)|a(b((b|a))((a(ab|aa)|b(aa|bb)))|a((b(b)(a)|a(b)(b))b|(a(bb|ab)|b(a)(b))a))))|a(b(b((b((b)(b)b|(ab|aa)a)|a((bb|ab)b|(bb|ba)a))b|(b(a((b|a)b|aa)|b(bb|ba))|a(((b|a)a|ab)a|(ab|aa)b))a)|a(((b(b(b|a)|aa)|a(bb|ba))b|(((b|a)b|aa))((b|a))a)a|(a((b)(b)b|(b)(a)a)|b(b(bb|ba)|a(b)(b)))b))|a((b(((bb|ba))((b|a))a|((b|a))((bb|ab))b)|a(((a)(b)a|((b|a))((b|a))b)b|((bb|ab)a|((b|a)a|ab)b)a))a|(b(b((bb|ba))(b)|a(((b|a)b|aa))(a))|a((b((b|a))((b|a))|a(bb|ab))b|((ba|ab)a|(bb|ab)b)a))b))){' + str(n) + '}))$)'
    
    ### FINALLY ! I had to add the $ at the end of the pattern for rule 11, or else it didn't match patterns correctly
    count = 0
    for m in msgs:
        if isMatch(p,m):
            count = count + 1
            print(m)       
    #print('part 2: ' + str(count))   # count will be new matches

# 487 original messages, 235 matched messages, 252 unmatched messages
# 437 too high, 386 too high, 391 (?) (235 last time, so answer > 235 answer < 386)
# 437 WRONG - TOO HIGH
# 391 WRONG - TOO HIGH
# 386 WRONG - TOO HIGH
# 379
# 378 WRONG
# 357 WRONG - someone else
# 348 WRONG - WRONG!!
# 318 WRONG
# 308 WRONG
# 294 WRONG
# 249 WRONG - TOO LOW
# 235 WRONG - TOO LOW

end_secs = time.time()
#print()
#print('--- ' + str(end_secs-start_secs) + ' secs ---')