import sys

rst = '\x1b[0m' # reset to default colors
fgb = '\x1b[30m'
fgw = '\x1b[37m'
bgy = '\x1b[103m'
bgg = '\x1b[102m'
bgw = '\x1b[47m'
bgb = '\x1b[104m'
def print_instr(curr_i):
    print()
    for i in range(0,len(l)):
        b = ''
        f = ''
        if i % 19 == 0 and i != 0:
            print()    
        if l[i].find('jmp') != -1:
            b = bgg
            f = fgb
        elif l[i].find('acc') != -1:
            b = bgb
            f = fgw
        else:
            b = bgw
            f = fgb

        if i == curr_i:
            sys.stdout.write(f+b+l[i].ljust(8)+' '+rst)
        else:
            sys.stdout.write(l[i].ljust(8) + ' ')
    sys.stdout.write('\033[0;0H')
    print()

l=[]

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(line.strip())
    
accumulator=0
l0 = l.copy()

def run_program():
    global accumulator
    i=0
    seen=len(l) * [0]
    while i < len(l):
        if seen[i] > 0:
            return False
        seen[i] = seen[i]+1
        s=l[i]
        arr = s.split(' ')
        cmd=arr[0]
        arg=int(arr[1])
        print_instr(i)
        if cmd=='acc':
            accumulator = accumulator + arg
            i = i + 1
        elif cmd == 'jmp':
            i = i + arg
        elif cmd == 'nop':
            i  = i + 1
            
    return True

for i in range(0, len(l0)):
    l = l0.copy()
    s = l[i]
    accumulator = 0
    arr = s.split(' ')
    cmd=arr[0]
    if cmd == 'acc':
        continue
    if cmd == 'jmp':
        cmd ='nop'
    elif cmd == 'nop':
        cmd = 'jmp'
    
    l[i] = cmd + ' ' + arr[1]
    done = run_program()
    if done:
        break

print(accumulator)
