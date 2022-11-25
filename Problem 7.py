# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import time
start = time.time()

# Bruteforce prime list maker, from problem 3
# params: 
# max_limit - check for primes up to this number
def prime_list_maker(max_limit):
    prime_list = [1,3,5,7,11,13] # Add the first ones
    for i in range(17, max_limit + 1): # For every value up to the max limit
        isPrime = True # Innocent until proven guilty
        
        # Some quick checks
        if i % 2 == 0: 
            isPrime = False 
            continue

        if i % 3 == 0: 
            isPrime = False 
            continue
        
        if i % 5 == 0: 
            isPrime = False 
            continue

        if i % 7 == 0: 
            isPrime = False 
            continue

        if i % 11 == 0: 
            isPrime = False 
            continue

        if i % 13 == 0: 
            isPrime = False 
            continue

        for j in range(17,i): # For every number up to the number, start at 17, don't divide by itself
            if i % j == 0: # If it's divisible by another number not 1 or itself
                isPrime = False 
                break

        if isPrime:
            prime_list.append(i) 

    return(prime_list)


#print(prime_list_maker(10000))
print(prime_list_maker(250000)[10000])

end = time.time()
print("The time of execution of above program is :", end-start)