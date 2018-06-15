print("""
Largest prime factor
Problem 3
""")
value = int(input("X="))
value2 = value
primes = list()
primes.append(2)
if value % 2 == 0:
        value2 /= 2
for i in range(3,value+1,2):
        flag = True
        for j in primes:
                if i % j == 0:
                        flag = False
                        break
        if flag == True:
                primes.append(i)
                print(i)
                print("value2",value2)
                if( value % i == 0) and (value2 / i < i):
                        print(i)
                        break
                if(value % i == 0):
                        value2 /= i
                        



x = input()

