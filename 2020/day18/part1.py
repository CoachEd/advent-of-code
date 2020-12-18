import sys
import time
import re

start_secs = time.time()
print()

# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    s = line.strip()
    l.append(s)
print(len(l))
def calc(n,m,op):
    if op == '+':
        return n + m
    if op == '*':
        return n * m
    print('error in calc: ' + str(n) + ' , ' + str(m) + ' , ' + str(op))

def isOp(c):
    if c == '+' or c == '*':
        return True
    else:
        return False


def plain_equation(s):
    # no parends here
    #1+2*3+4*5+6
    sarr = re.split(' ',s)
    ans = 0
    stack = []
    while True:
        c = sarr[0]
        sarr = sarr[1:]
        if len(stack) == 0 or isOp(c):
            stack.append(c)
        else:
            num = int(c)
            op = stack.pop()
            num1 = int(stack.pop())
            ans = calc(num1,num,op)
            stack.append(ans)
        if len(stack) == 1 and len(sarr) == 0:
            break

    return stack[0]

#1 + 2 * 3 + 4 * 5 + 6
#1 + (2 * (3+1))


sum = 0
for s in l:
    stack = []
    ans = 0
    s = s.replace('(','( ').replace(')',' )')
    sarr =  re.split(' ',s)
    if not '(' in sarr:
        s4 = ''
        for c4 in sarr:
            s4 = s4 + ' ' + c4
        s4 = s4.strip()
        ans = plain_equation(s4)
        sum = sum + ans
        continue

    #2 * 3 + (4 * 5)
    # we have at least one pair of parends
    #print('processing... ' + s)
    while True:
       #print(stack)
        if len(stack) > 0 and len(sarr) == 0 and ''.join(stack).find('(') == -1:
            s3 = ''
            for c3 in stack:
                s3 = s3 + c3 + ' '
            s3 = s3.strip()
            ans = plain_equation(s3)
            sum = sum + ans
            break

        if len(sarr) > 0:
            c = sarr[0]
            sarr = sarr[1:]
        else:
            c = ''
        if c == '':
            c = stack.pop()

        if len(stack) == 0:
            stack.append(c)
        else:
            if c == ')':
                # pop until '('
                s2 = ''
                c2 = stack.pop()
                while c2 != '(':
                    s2 = c2 + ' ' + s2
                    c2 = stack.pop()
                s2 = s2.strip()
                ans = plain_equation(s2)
                stack.append(str(ans))
            else:
                stack.append(c)

        if len(stack) <= 1 and len(sarr) == 0:
            break

print('part 1: ' + str(sum))  # too low: 202553431416

print()
end_secs = time.time()
print(str(end_secs-start_secs))