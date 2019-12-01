import math
with open('input1.txt') as f:
    content = f.readlines()
arr = [x.strip() for x in content] 

# to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
sum = 0
for num in arr:
    n = int(num)
    sum = sum +  math.trunc(n/3) - 2

print(sum)