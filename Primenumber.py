import math
n = int(input("enter the number"))
list = []
# Iterate over numbers from 2 to n (100)
for i in range(2, n + 1):
    is_prime = True  # Assume the number is prime

    # Check for factors from 2 to i / 2
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            is_prime = False  # Number is not prime
            break
    
    # Print the number if it's prime
    if is_prime:
        list.append(i)
print(list)