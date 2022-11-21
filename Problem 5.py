# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time
start = time.time()

no_answer = True
num = 20
while no_answer:
    #print(num)
    iter = 0
    for i in range(1, 20 + 1):
        if num % 2 != 0: # if it's not even, just break out of the loop
            num += 20 # It has to be a multiple of 20 to be divisible by 20
            break

        if num % i != 0: # ifit's not divisible by one of the numbers, just break
            num += 20
            break
        else:
            iter += 1 # this counts how many numbers from 1 to 20 have mod 0 with respect to the number being tried

    if iter == 20:        
        print(num)
        no_answer = False

end = time.time()
print("The time of execution of above program is :", end-start)