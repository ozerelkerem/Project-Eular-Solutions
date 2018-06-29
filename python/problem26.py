print("""
Reciprocal cycles
Problem 26 
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

""")
primes = [2]
for i in range(3,1000,2):
    flag = True
    for j in primes:
        if i % j == 0:
            flag = False
            break
    if flag == True:
        primes.append(i)



def clen(b):
    a = 1
    t = 0
    while True:
        a = a * 10 % b
        t += 1
        if a==1:
            return t
        
primes.remove(2)
primes.remove(5)

mmax = 0
num = 0
for i in primes:

    tt = clen(i)
    if tt > mmax:
        mmax = tt
        num = i

print(num)


