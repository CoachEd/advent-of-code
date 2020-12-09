import sys

l=[]

my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    l.append(line.strip())

rst = '\x1b[0m' # reset to default colors
fg = '\x1b[30m'
bg = '\x1b[103m'
def print_instr(curr_i):

    for i in range(0,len(l)):
        if i % 19 == 0 and i != 0:
            print()    
        if i == curr_i:
            sys.stdout.write(fg+bg+l[i].ljust(8)+rst + ' ')
        else:
            sys.stdout.write(l[i].ljust(8) + ' ')
    sys.stdout.write('\033[0;0H')
    print()

accumulator=0
new_instr = True
i=0
seen=len(l) * [0]
while new_instr:
    if seen[i] > 0:
        break
    seen[i] = seen[i]+1
    s=l[i]
    #print_instr(i)
    arr = s.split(' ')
    cmd=arr[0]
    arg=int(arr[1])
    if cmd=='acc':
        accumulator = accumulator + arg
        i = i + 1
    elif cmd == 'jmp':
        i = i + arg
    elif cmd == 'nop':
        i  = i + 1
print('Part 1: ' + str(accumulator))
