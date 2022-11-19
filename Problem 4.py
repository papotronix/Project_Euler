# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


import time
start = time.time()

#"input" is hardcoded, can make it an actual param
def palindrome_finder():
    for i in reversed(range(1000)):
        for j in reversed(range(1000)):
            product = str(i*j)
            if product == product[::-1]:
                print(product)
                return

palindrome_finder()

end = time.time()
print("The time of execution of above program is :", end-start)