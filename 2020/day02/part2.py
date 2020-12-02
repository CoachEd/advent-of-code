import sys
import time

start_secs = time.time()
l=[]
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines: 
    l.append(line.strip())

# part 2
num = 0
for s in l:
    arr = s.split()
    c = arr[1]
    c = c[:-1]
    arr2 = arr[0].split('-')
    num1=int(arr2[0])-1
    num2=int(arr2[1])-1
    pswd = arr[2]
    b1 = pswd[num1] == c
    b2 = pswd[num2] == c
    if b1 ^ b2:
        num = num + 1
        
print(num)
end_secs = time.time()
print(str(end_secs-start_secs))   
    
    
    
   

            


        



        
