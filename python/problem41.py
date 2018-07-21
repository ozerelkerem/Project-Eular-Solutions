print("""
Pandigital prime
Problem 41 
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
""")
def isPandigital(a):
    a = str(a)
    li = [ 0 for i in range(1,len(a)+2)]
    li[0] = 1
    for i in str(a):
        if int(i) > len(str(a)):
           return False
        li[int(i)] += 1
    for i in li:
        if i != 1:
            return False
    return True


count = 7654322
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

for i in range(count-1,0,-1):
    if isPrime(i) and isPandigital(i):
        print(i)
        break
