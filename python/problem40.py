print("""
Champernowne's constant
Problem 40 
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
""")

val = ""
def create():
    global val
    for i in range(0,1000000):
        val += str(i)
        if len(val) > 1000000:
            break

create()



summ = 1
summ *= (int(val[1]))
summ *= (int(val[10]))
summ *= (int(val[100]))
summ *= (int(val[1000]))
summ *= (int(val[10000]))
summ *= (int(val[100000]))
summ *= (int(val[1000000]))
print(summ)

    
