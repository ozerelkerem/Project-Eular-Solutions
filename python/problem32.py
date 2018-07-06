print("""
Pandigital products
Problem 32 
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

""")

    
def isPandigital(a,b,c):
    li = [ 0 for i in range(1,11)]
    li[0] = 1
    for i in str(a):
        li[int(i)] += 1
    for i in str(b):
        li[int(i)] += 1
    for i in str(c):
        li[int(i)] += 1
    for i in li:
        if i != 1:
            return False
    return True


products = set()
for i in range(1,99):
    for j in range(123,9877):
        if isPandigital(i,j,i*j):
            products.add(i*j)

summ = 0
for i in products:
    summ += i

print(summ)


    


