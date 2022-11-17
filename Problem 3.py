# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import time
start = time.time()

# Bruteforce prime list maker
# params: 
# max_limit - check for primes up to this number
def prime_list_maker(max_limit):
    prime_list = [1] # Add the first one
    for i in range(2, max_limit + 1): # For every value up to the max limit
        isPrime = True # Innocent until proven guilty
        for j in range(2,i): # For every number up to the number, start at 2, don't divide by itself
            if i % j == 0: # If it's divisible by another number not 1 or itself
                isPrime = False 
                break
        if isPrime:
            prime_list.append(i) 
    return(prime_list)


#Use the prime list generated and check for prime factors?
prime_list = prime_list_maker(100000)
print("Prime list: ", end = "")
print(prime_list, end = "\n\n")

prime_factors = []
for i in prime_list:
    if 600851475143 % i == 0:
        prime_factors.append(i)

print("prime factors: ", end = "")
print(prime_factors,end = "\n\n")

print("max prime factor: ", end = "")
print(max(prime_factors))

end = time.time()
print("The time of execution of above program is :", end-start)