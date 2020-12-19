import sys

l=[]
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines:
    s = line.strip()
    l.append(s)

print(l)
#1 + (2 * 3) + (4 * (5 + 6))