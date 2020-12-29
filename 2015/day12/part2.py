import sys
import time
import re
import json

start_secs = time.time()


count = 0

def recursive_iter(obj):
    global count

    if isinstance(obj, dict):
        if 'red' in obj.values():
            return
        for k,v in obj.items():
            if isinstance(v, dict):
                recursive_iter(v)
            elif isinstance(v, list):
                for e in v:
                    recursive_iter(e)
            else:
                s = str(v)
                if s.isdigit():
                    count = count + int(s)
                if len(s) > 1 and s[0] == '-' and s[1:].isdigit():
                    count = count + -1*int(s[1:])
    elif isinstance(obj, list):
        for elem in obj:
            recursive_iter(elem)
    else:
        s = str(obj)
        if s.isdigit():
            count = count + int(s)
        if len(s) > 1 and s[0] == '-' and s[1:].isdigit():
            count = count + -1*int(s[1:])
            
# read in input file
l=[]
my_file = open("inp.txt", "r")
lines = my_file.readlines()
for line in lines: 
    l.append(line.strip())

# {"field1": "blue","field2": 1,"field3": [{"s1": 9,"s2": 8}, {"s1": 9,"s2": 8,"s3": "red"}, {"s1": 9,"s2": 8,"s3": 3}],"field4": 3}
s = l[0]
obj = json.loads(s)
recursive_iter(obj)
print('part 2: ' + str(count)) # 29291 too low

print()
end_secs = time.time()
print('--- ' + str(end_secs-start_secs) + ' secs ---')