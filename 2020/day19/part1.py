import sys

l=[]
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    s = line.strip()
    l.append(s)

d=dict()
for s in l:
    arr=s.split(':')
    rule_num=arr[0].strip()
    rule=arr[1].strip()
    if rule.find('a') != -1 or rule.find('b') != -1:
        d[rule_num]=rule.replace('"','')
    else:
        d[rule_num]=rule

def parse(rule):
    global d
    if rule == 'a' or rule == 'b':
        return rule
    s=''
    if rule.find('|') == -1:
        arr = rule.split() 
        for r in arr:
            s = s + parse(d[r])
        return s
    else:
        arr2 = rule.split('|')
        for i in range(0,len(arr2)):
            arr = arr2[i].split()
            for r in arr:
                s = s + parse(d[r])
            if i < len(arr2)-1:
                s = s + '|'
        return s

print(d)
print(parse('1'))
print(parse('2'))