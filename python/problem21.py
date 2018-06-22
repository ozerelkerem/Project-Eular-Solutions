print("""
Amicable numbers
Problem 21 
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
""")



def fb(num):
    msum = 1
    if num % 2 == 0:
        msum += 2
        for i in range(3,num):
            if num % i == 0:
                msum += i
    else:
        for i in range(3,num,2):
            if num % i == 0:
                msum += i

    return msum
nums = set()
for i in range(1,10000):
    tmp = fb(i)
    tmp2 = fb(tmp)
    if i == tmp2 and i != tmp:
        nums.add(i)


summ = 0
for i in nums:
    summ += i
print(summ)
    

    
        
