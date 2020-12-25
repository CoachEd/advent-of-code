import sys
import time

start_secs = time.time()

def calc_loopsize(pkey):
    loop_size = 0
    c = 7
    while c != pkey:
        loop_size = loop_size + 1
        c = c * 7
        c = c % 20201227
    return loop_size+1

def transform(pkey,loop_size):
    c = pkey
    loop_counter = 1
    while True:
        loop_counter = loop_counter + 1
        c = c * pkey
        c = c % 20201227
        if loop_counter == loop_size:
            break
    return c
    
    
    
card_key = 10705932
door_key = 12301431
"""
Set the value to itself multiplied by the subject number.
Set the value to the remainder after dividing the value by 20201227.
"""

card_loop_size = calc_loopsize(card_key)
door_loop_size = calc_loopsize(door_key)

#print( 'loop_size:  ' + str(calc_loopsize(5764801)) )
#print( 'loop_size:  ' + str(calc_loopsize(17807724)) )

print( ' transform: ' + str(transform(door_key,card_loop_size)) ) # door public key and card loop size
print( ' transform: ' + str(transform(card_key,door_loop_size)) ) # card public key and door loop size

print()
end_secs = time.time()
print(str(end_secs-start_secs))