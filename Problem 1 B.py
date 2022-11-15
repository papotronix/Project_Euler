# Find all multiples of 3 below 1000
# Find all multiples of 5 below 1000
# Add them together

# List all numbers from 0 to 999
# Calculate 1000 mod 5 and 1000 mod 3
# Check if mod == 0
# Add them together

from re import I

sum_3 = []
sum_5 = []
for i in range(1000):
    if i % 5 == 0:
        sum_5.append(i)
    if i % 3 == 0:
        sum_3.append(i)

sum_5 = set(sum_5) - set(sum_3)

total_sum = 0

for i in sum_5:
    total_sum += i

for i in sum_3:
    total_sum += i

print(total_sum)  