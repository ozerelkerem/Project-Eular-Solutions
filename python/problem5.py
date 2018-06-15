print("""
Smallest multiple
Problem 5 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
""")

primes = []
x=20
primes.append(2)

for i in range(3,x+1,2):
    flag = True
    for j in primes:
        if (i % j) == 0:
            flag = False
            break
    if(flag == True):
        primes.append(i)



sum = []
product = 1
for i in range(2,x+1):
    sum.append(i)


for i in primes:
    flag = True
    while flag==True:
        flag = False
        j=0
        while j < len(sum):
        
            if sum[j] % i == 0:
                if flag == False:
                    product *= i
                sum[j] /= i    
                flag = True
            j += 1

print(product)
        
            
        
        
    

