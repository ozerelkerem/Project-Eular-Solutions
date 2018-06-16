print("""
Summation of primes
Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

""")
#sieve of atkin
count = 2000001
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
summ=0
for i in range(0,len(B[0])):
    if B[1][i]:
        summ+=B[0][i]

print(summ)
        
   
