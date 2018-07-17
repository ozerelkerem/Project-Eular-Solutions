print("""
Double-base palindromes
Problem 36 
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
""")

def isPol(x):
    ss = str(x)
    for i in range(0,len(ss)//2):
        if ss[i] != ss[len(ss)-i-1]:
            return False

    return True


summ = 0
for i in range(0,1000000):
    if isPol(i) and isPol("{0:b}".format(i)):
        summ += i


print(summ)
