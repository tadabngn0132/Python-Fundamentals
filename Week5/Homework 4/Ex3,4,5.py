# 3. Write a function to check if a number is a prime or not. Name the function is_prime, parameter: n, return: True if n is a prime, False otherwise.

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int((n**0.5)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        
    return True

print()
k = is_prime(25)
print(k, end=' ')
print()
print()

# 4. Write a function print_primes(n) that prints all the primes up to n. This function should use the function is_prime in the exercise 3. 

def print_primes(n):
    for i in range(2, n+1):
        if is_prime(i):
            print(i, end=' ')
    print()

print_primes(25)
print()

# 5. Add 1 more parameter to the function print_primes(n, m) that prints all the primes up to n so that m primes are in one line.
# For example if you call print_primes(20, 3) it will print:
# 2 3 5
# 7 11 13
# 17 19
# Hint: Using a counter to count number of primes. If counter value is divisible by m, print a new line.

def print_primes(n,  m):
    count = 0
    for i in range(2, n+1):
        if is_prime(i):
            count += 1
            print(i, end=' ')
            if count == m:
                print()
                count = 0  
    print()

print_primes(25,4)
print()