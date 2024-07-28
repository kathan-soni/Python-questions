n = int(input("Enter the number: "))

# Assume the number is prime unless proven otherwise
is_prime = True  

# Handle cases for numbers less than 2
if n < 2:
    is_prime = False
else:
    # Check for factors from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            is_prime = False  # Number is not prime
            break

# Print the result
if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
