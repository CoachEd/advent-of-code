import sys
import time

start_secs = time.time()
l=[]
my_file = open("inp.txt", "r")
Lines = my_file.readlines()
for line in Lines: 
    l.append(line.strip())

# part 1
num = 0
for s in l:
    arr = s.split()
    c = arr[1]
    c = c[:-1]
    arr2 = arr[0].split('-')
    num1=int(arr2[0])
    num2=int(arr2[1])
    pswd = arr[2]
    cnt = pswd.count(c)
    if cnt >= num1 and cnt <= num2:
        num = num + 1
        
print(num)
end_secs = time.time()
print(str(end_secs-start_secs))   
    
    
    
   

            


        



        
