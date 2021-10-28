#!  /usr/local/bin/python3

# Find all PRIME numbers in a sequence
def isprime(n):
    if n <= 1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True

n = 948´
# print(input('Please enter an integer  between 1 and 1000000 to check if it is a prime'))

if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')