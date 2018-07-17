print("""
Pandigital multiples
Problem 38 
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

""")

def isPandigital(a):
    if len(str(a)) != 9:
        return False
    li = [ 0 for i in range(1,11)]
    li[0] = 1
    for i in str(a):
        li[int(i)] += 1
    for i in li:
        if i != 1:
            return False
    return True

def process(a,b):
    st = ""
    for i in range(1,b+1):
        st += str(a*i)
    return st

maxx = 0
for i in range(999999,0,-1):
    j=2
    while True:
        result = process(i,j)
        j+=1
        if len(str(result)) > 9:
            break
        if isPandigital(result):
            if int(result) > maxx:
                maxx = int(result)

print(maxx)
            
