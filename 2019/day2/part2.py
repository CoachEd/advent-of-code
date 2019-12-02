
#prereq: replace position 1 with the value 12 and replace position 2 with the value 2.

def runProg(noun,verb):
    arr = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]
    arr[1] = noun
    arr[2] = verb
    i = 0
    while(True):
        if arr[i] == 99:
            break
        elif arr[i] == 1:
            # add
            x = arr[arr[i+1]]
            y = arr[arr[i+2]]
            arr[arr[i+3]] = x + y
            i = i + 4
        elif arr[i] == 2:
            # multiply
            x = arr[arr[i+1]]
            y = arr[arr[i+2]]
            arr[arr[i+3]] = x * y
            i = i + 4
        else:
            # nothing
            pass
    return arr[0]



done = False
for n in range(100):
    for v in range(100):
        ans = runProg(n,v)
        if ans == 19690720:
            print(str(n) + ',' + str(v))
            print(100 * n + v)
            done = True
            break
    if done:
        break


print('done')
