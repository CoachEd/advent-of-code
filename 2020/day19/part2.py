import sys
import re
import time

start_secs = time.time()
omit = [
"ababaaaaabbbabbbbbabbbba",
"aabbaabaabbababaababbaba",
"bbbbabaaabaaabbbbbbbbaab",
"babbabbabbaababbbbbbbaab",
"baababababbaababaaabaaab",
"baabbbbaaabbabbbababbbba",
"babbabbabaabbabbaabbabaa",
"abababbaaabaabbbabbbaaaa",
"abbaaaabaabababaabaabbaa",
"baaaaaabaaaaababbababaaa",
"baaabbbaaaaaaaaaaabbbbba",
"abaabbabaabaaaaabaabaaaa",
"aabababbababaaaaabbbbbaa",
"aabababbaabbbababaabaaab",
"aabaaababaabbabaaabaaaab",
"abbbabaabbaabbabaaabbbba",
"baabaabaaababbbbbbaabbaa",
"bbaaabbbbababbabaaaababa",
"aaaaaaaabaaabaabababaaba",
"abaaaabaabbababaababbbab",
"bbaaabababbababbababbbbb",
"bbbbbbbaabababbabbabbbba",
"bbaaaaaaaabaabbbabaabbaa",
"abaababbaabaaaaaaabaaaab",
"babbabbbbbbbbbbabbaabbaa",
"bbbbabaaaabaabbbbbbbbaab",
"bbaaaaabababbabbaababbab",
"babbaabaabbbbaaaaabbbbbb",
"baaabaabbbbbaaaaabbbaaab",
"aaabbaabbabbabbbbabbbbba",
"ababaabbaabbbabababbabab",
"bbbabbbabaaabbbaaaabbbab",
"babbabbaabbabbbaababaaba",
"aaabaabaaabbababbababaab",
"abbababbbbbbabbaaabbbbbb",
"bbbbbbbaabaaaaababbaabbb",
"abbbbbabbbbbabaaabaabaab",
"abbabbbabbbbabababbbbbba",
"abababbabaaaaaabbbabaaaa",
"baabbbbabbbaaaaababaaabb",
"aabaaabbaabbaabbbababaab",
"abababbabaabbbbaaaaababa",
"aabbabbbbbaaababbbababaa",
"abbaaaababbbbbabaaaaabbb",
"bbaaaaaabbbaabababaabaab",
"bbaabbbaabababbaaaababbb",
"bbbbabbaaabaabaababaaaaa",
"babaababaaabbaabbbababaa",
"ababababababbaabbabababa",
"abbbaabbabbbbaaaaaaabaab",
"baabbabbbbaaabababaabbbb",
"babbbbabbbbbbbaaababbbba",
"abbbbababbbaaaaaaaabbbab",
"aabababbbbbbabbaabbbbbbb",
"baaabbbababbaabaabbabaaa",
"aababaababbbabbbababbaaa",
"baaabbbbbbbbabbabbbbbaab",
"bbabbaabaaabbbaaaabbbaaa",
"bbbbbbbaaabbaabaababaaba",
"aababababaaabbbaababbbaa",
"baaaaabbbaaaaabbabbaaaaa",
"ababaaaaaabbbaababbaabba",
"bbbabababbbbabbaabaaaaaa",
"baaaaaaabbbabbbaaaabbbba",
"bbbbababbaabbababbabbbab",
"baaabaabaababbbbbbabbbbb",
"bbaaaaaaabbbabbbabbbbbaa",
"bbabaabaabbabbaaababbbaa",
"aabbbaababaabbabbabaabba",
"baaabbbaaaabaababbaaaabb",
"babbbbaabbbbaabaabbbaaaa",
"bbbbaababbaaaaaabbbbbaab",
"bbaaaaaaabbbbababaabaaab",
"aaabbaabbaaabbbbbbbbbaaa",
"aabaaabbabbaaabbbabbbabb",
"bbaaaaaabaabbbbaabbbaaab",
"abbbabaabbabbaabbabbbbba",
"aaaaaaabaababbbbababbbab",
"abbababbbaaaaaabbabaaabb",
"bbabbababbabbaabbababbbb",
"abababbaaaabaabaaaababbb",
"bababbabaaabbbaaababbbbb",
"baaaababbabbbabababaabba",
"aabbababbbaababbabaababa",
"aababbaaaababbbbabbbaaaa",
"baaabbbabababbbaaabaabba",
"baabaabaababababaaabaabb",
"abbababbbbbbababbbaabaab",
"bababbbaaabaaabababababb",
"aabbabbbbaaababbbbabbaaa",
"babbbabaaabbabbbaababbba",
"aababababbaaaaaabaaaaaba",
"bbbaabbaabaaaabaabaaabaa",
"aababababbbbaabaabbbbbaa",
"bbabaabaababbabbbabbaabb",
"abaaaababbbbbbbabbabaaaa",
"bababbabbbbbabaababbbbbb",
"aabbabbbbbbbabababbabaab",
"abbababababbabaaaabbbaaa",
"abbbabbbaaaaaaabbaabbbbb",
"aaaababbaaaaaabaaabaabba",
"bbabbbaaababbabbbbbaaaab",
"aabbbaababbbbbabbababaaa",
"baaabbbbbbbaaabaabaabaab",
"baaabbaaaababaabbabaaaaa",
"aabbaaabbbaabbabaaababbb",
"bbbbabaabbbabbbaaabaaaab",
"aabbaabbbabaababbaababaa",
"babbbbabbababbbabaabbaaa",
"bbbaaaaabbaaabababbabbbb",
"aaaababbabbaababbabababb",
"aabbabababaaabbababaaaba",
"bbbaaabbabaababbbababbaa",
"abbabbbaabbaababbabaabba",
"baaababbaaaaaabaaabbbaaa",
"abbbbaababbbabbbaabaaaab",
"bbbabbaabbbbabababaaabaa",
"babbaabaabbabbaabaaaaaba",
"aababababbabbbaaabbaabba",
"bbbabaabbaaabbbabbabbaaa",
"bbbababaaabbabababababbb",
"bbbbbbbaabbbaabbbbbabbab",
"abababbabbaaaaabaabbabba",
"babbabaabbababbbbbabbaaa",
"aabaaabaababaaaaaaaabbba",
"abaaaabaaabaaabbabbabbbb",
"abaaaaabaaaaaaaabaaaaaba",
"aaabbabababbbbaaaaaabbbb",
"abaaaababaaabaabababaaba",
"bbbbabbbbbaabbbabaabbbbb",
"baaaababaaaaababbababbaa",
"bbbaaabbbaaabbbaaaababbb",
"aabaaabbabaaaaababbbaaab",
"bababbbaaaabbaabaaaabbba",
"ababbaababaabbabaaaaabba",
"aaaaaabaaaabbbaaababbaba",
"babbbbaaabbbabbbbbbabbab",
"bbbbbbbabbbbabbbabbaaaba",
"baabaabababbabbbaabbbabb",
"baaaaaaaaaaaaaaaaaaababa",
"abbaababaabbbbabaaababba",
"babaababbbaabbabbbaabbaa",
"baabbababaaaabaabababbaa",
"bbaaabbabbaaabbbbbabbabb",
"baabbbbabbaaaabaaaabbbba",
"bbababbbbaabbbbaaaaabaab",
"bbabbaabbabbaaaaaaaaabba",
"aaaababbbbbbbbaabbbabbbb",
"bbaaababbbaaabbaaabbbabb",
"abbaaabbbabbaabababaabbb",
"babbabaaabbaaabbbabaaaaa",
"aaaaaaabababababbaababbb",
"ababaabbbabbaaaaabbbbbbb",
"aabbaaabaabbbabaaaababba",
"baabbabaaabaabaaabbaaaaa",
"abaaaabaaabbbaabbabaabaa",
"bbaaabbbbaaabbbaababbbbb",
"baaababbbbbaababbbabbaaa",
"bbbbabbbababababbaabbaab",
"baaaababbabbbbabbaabbaab",
"bbaabbbaabaaabbbbababbaa",
"abbbbabbbbbbabbbbabbbbbb",
"bbbbbbbbbbbbaabbaaaabaab",
"aababaabbabbabaaaaaabaab",
"ababaaababbabbbabbaabaaa",
"bbbababbabbbbbabaaaaabaa",
"abbbaabbbabbbbabaaabbaaa",
"abbaaaabbbaaaaabaabaabba",
"aaabbabaaabaabbbaaabbabb",
"baabababbaababbabaabbaab",
"bbaaabbbaaabaabaababbaba",
"aabbbababaaaaaabababbaaa",
"baaaababbaaababbaaaaabaa",
"aabababaabaabbababababbb",
"bbbbababaabababaaabbbaaa",
"bbbbababaaabaaaabbbaaaab",
"bbbabaabbaaaababaaabaaab",
"ababababaabbaabbbababaaa",
"ababbabbaaaaaabbababbbab",
"bbbbababaabaaaaaabaaaaaa",
"bbababbbbaaaaabbaaababba",
"aabbbaabbbbababbbaaababa",
"aabaabaabaaabaababbabbbb",
"aaaaababbaaabbaabbaaaabb",
"abaababbaabbbaabbabaabbb",
"baababababbaaabbbabbaabb",
"aaaaaabaabababbabbabbbbb",
"aaabbabaaabbaabbbbabaaab",
"abbbaabbbbbbabaaaaaabaaa",
"aabbabbbabaaaabbaabbbaaa",
"bbbbababaabababaaabbabaa",
"ababaabbbbbbbbbaaaaabbbb",
"aaabababbabbaaaaababbbbb",
"baaabbbaabababbaababbbaa",
"bbabbaabbbbbbbaabbbaaaab",
"abbaababbbbabaabababbaba",
"bbaababbababababbbbbbaab",
"bbababbbabaaaaabbbbbbabb",
"babbabbaabbbabaaabbaaaaa",
"aababaaaabaabbabbabaabaa",
"aababbaaaaabbaabaaaababa",
"bbbbabaaaabbbababbbabbbb",
"bbbababaababaaabaabbabaa",
"aaabbaababbbbaaaaabbbbba",
"abaaaaabbbaaaaaabaababaa",
"bababbabbbbabbaaaaabbbab",
"aabababbaaabaaaaabbaabba",
"abaaabbabaaabaabbababbaa",
"abbbabaabbaabbbababbbbbb",
"aabbbbabbaaabaaabbaaabaa",
"abbbbabaaabababbaaabbbbb",
"abaaabbaabaaabbbbbaabbbb",
"aabaaabaaaaaaabaaaaabbba",
"abbabbbaababbabbaaaabbbb",
"abbbabbbbabbbbabbbaabaab",
"baaababbbbaaabbabbbaaaab",
"baabbabaaabbaababbbbbaab",
"bbaababbbbaaabbbababbaba",
"bbbaaabbbbbbabaabbabbaaa",
"bbbababaaababbbbbaababaa",
"baaaababaababaaaabbbbbbb",
"aabbbbabaaaababbbabaabba",
"aaaaaabaaababbaabaaaaaba",
"aaabaaaaaabbbbabbaabbaaa",
"bbbaabbaabbababaabbabaaa",
"bbbaabbababbaabaaabbbbbb",
"abbbabaaaaaaababaababbab",
"bbabaabaaabbaabbaabbabba",
"baaaabaaaababaabbbabbbab",
"aaabaabaabbbabbbaabbbbbb",
"babbaaaabaabababbaaaabbb",
"aaabbbaaaabbbabababaabaa",
"bbbaaabaababbaabababaaba",
"abababbaaababaababbaabba",
"bbaaabbabbbbababaaaabaab"
]
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

# REMOVING matched from before
#print(len(msgs)) # 487 original messages, 235 matched messages, 253 unmatched messages
ctr = 0


# remove part 1 strings?
#arr2 = []
#for m in msgs:
#    if not m in omit:
#       arr2.append(m)
#msgs = arr2


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



p = parse(d['0'])
#print(p)
#sys.exit()

#for n in range(0,30):
#    p=''
#    count = 0
#    for m in msgs:
#        if isMatch(p,m):
#            count = count + 1
#            print(m)

count = 0
for m in msgs:
    if isMatch(p,m):
        count = count + 1
        #print(m)       
print('part 2: ' + str(count))   # count will be new matches

# 487 original messages, 235 matched messages, 252 unmatched messages
# 437 too high, 386 too high, 391 (?) (235 last time, so answer > 235 answer < 386)
# 437 WRONG - TOO HIGH
# 391 WRONG - TOO HIGH
# 386 WRONG - TOO HIGH
# 378 WRONG
# 348 WRONG - WRONG!!
# 318 WRONG
# 308 WRONG
# 294 WRONG
# 249 WRONG - TOO LOW
# 235 WRONG - TOO LOW

end_secs = time.time()
#print('--- ' + str(end_secs-start_secs) + ' secs ---')