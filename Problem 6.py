# The sum of the squares of the first ten natural numbers is,
# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import time
start = time.time()


sum_of_sum_of_squares = 0

for num in range(1, 100 + 1):
    sum_of_sum_of_squares += num**2 

square_of_sum = 0

for num in range(1, 100 + 1):
    square_of_sum += num
square_of_sum = square_of_sum**2

print(square_of_sum - sum_of_sum_of_squares)


end = time.time()
print("The time of execution of above program is :", end-start)