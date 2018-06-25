print("""
Lexicographic permutations
Problem 24 
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


""")

li = [0,1,2,3,4,5,6,7,8,9]
num = []


target = 1000000

def fact(i):
    product = 1
    for j in range(1,i+1):
        product *= j

    return product


def myfunct(count,order):
    for i in li:
        count += fact(len(li)-1)
        if count >= target:
            li.remove(i)
            return [i ,count - fact(len(li))]

count = 0
order = 1
while(count != target-1):
    i,count = myfunct(count,order)
    order += 1
    num.append(str(i))


for i in li:
    num.append(str(i))

print("".join(num))
    


