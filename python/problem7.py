print("""
10001st prime
Problem 7 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
""")
primes = []
x=10001
primes.append(2)
i=3
while len(primes) < x:
    flag = True
    for j in primes:
        if (i % j) == 0:
            flag = False
            break
    if(flag == True):
        primes.append(i)
    i+=2
print(primes[x-1])

