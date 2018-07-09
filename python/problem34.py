print("""
Digit factorials
Problem 34 
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

""")

def fact(i):
    if i <= 1:
        return 1
    else:
        product = 2
        for j in range(3,i+1):
            product *= j

        return product

def digitfactsum(i):
    summ  = 0
    for j in i:
        summ += fact(j)

    return str(summ)
        

li =  [[i] for i in range(0,10)]
pli = li.copy()
summ = 0
for i in range(1,6):
    nli = []
    for a in pli:
        for b in li:
            nli.append(a+b)
    pli = nli.copy()

    for i in pli:
        if digitfactsum(i) == ("".join([str(j) for j in i])):
            summ += int("".join([str(j) for j in i]))

print(summ)
