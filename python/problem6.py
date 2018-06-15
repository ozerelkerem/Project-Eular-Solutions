print("""
Sum square difference
Problem 6 
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
""")

x=100
sum1 = 0
sum2 = 0
tmp = 0
for i in range(1,x+1):
    sum1 += i ** 2

for i in range(1,x+1):
    tmp += i

sum2 = tmp ** 2

print(sum2-sum1)
    
