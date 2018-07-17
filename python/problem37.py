print("""

Truncatable primes
Problem 37 
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
""")
#sieve of atkin
count = 1000001
B = [ [i for i in range(0,count)],[False] * count]


i = 1
while i*i < count:
    j = 1
    while j*j < count:
        n = (4*i*i) + (j*j)
        if (n < count) and ( (n % 12 == 5) or (n % 12 == 1)):
            B[1][n] = not B[1][n]
        n = (3*i*i) + (j*j)
        if (n < count) and ( n % 12 == 7):
            B[1][n] = not B[1][n]

        n = (3*i*i) - (j*j)
        if (i > j) and (n < count) and ( n % 12 == 11):
            B[1][n] = not B[1][n]


        j += 1
    i += 1

i = 5
while i*i < count:
    if B[1][i]:
        j = i*i
        while j < count:
            B[1][j]=False
            j += i*i

    i +=1
B[1][2] = True
B[1][3] = True
B[1][5] = True
primes = []

def isPrime(i):
    return B[1][int(i)]


def isTrunct(i):
    ss = str(i)
    for i in range(0,len(ss)):
        if not isPrime(ss[i:]):
            return False
    for i in range(1,len(ss)+1):
        if not isPrime(ss[:i]):
            return False
    return True



j = 21
num = 0
summ = 0
while num < 11:
    j += 2
    if isPrime(j) and isTrunct(j):
        num += 1
        summ += j

print(summ)    
    

