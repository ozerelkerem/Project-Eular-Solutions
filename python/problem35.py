print("""
Circular primes
Problem 35 
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
""")


#sieve of atkin
count = 1000000
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
for i,val in enumerate(B[0]):
    if B[1][i]:
        primes.append(str(val))


count = 0
for i in primes:
    flag = True
    for j in range(len(i)):
        val = i[j:len(i)]+i[-len(i):j]
        if not val in primes:
            flag = False
            break
    if flag:
        count += 1

print(count)

