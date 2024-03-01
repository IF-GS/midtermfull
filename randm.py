
import random

# Generate random numbers
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here

# Remove numbers >50 replace with XX
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = "XX"

print("Not dying soon club list:", random_numbers)