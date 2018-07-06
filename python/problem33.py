print("""
Digit cancelling fractions
Problem 33 
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


""")
low = 1
high = 1
for i in range(10,100):
    for j in range(10,100):
        s1 = str(i)
        s2 = str(j)
        if j > i:
            try:
                
                if i / j == int(s1[1]) / int(s2[0]) and s1[0] == s2[1]:
                    high *= int(s1[1])
                    low  *= int(s2[0])
                elif i / j == int(s1[0]) / int(s2[1]) and s1[1] == s2[0]:
                    high *= int(s1[0])
                    low  *= int(s2[1])

                else:
                    pass
            except ZeroDivisionError:
                pass

for i in range(high,1,-1):
    if high % i == 0 and low % i == 0:
        high /= i
        low /= i


print(int(high*low))
