print("""
Quadratic primes
Problem 27 
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
""")

primes = [2]
for i in range(3,10000,2):
    flag = True
    for j in primes:
        if i % j == 0:
            flag = False
            break
    if flag == True:
        primes.append(i)

def formula(n,a,b):
    return n*n + a*n + b


mmax = 0
mmaxa = 0
mmaxb = 0
for a in range(-999,1000):
    for b in [elem for elem in primes if elem < 1000]:
        n = 1
        count = 1
        while True:
            if not formula(n,a,b) in primes:
                break
            n += 1
            count += 1
        if count > mmax:
            mmax = count
            mmaxa = a
            mmaxb = b

    
print(mmaxa*mmaxb)
