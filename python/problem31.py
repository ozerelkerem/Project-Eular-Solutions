print("""
Coin sums
Problem 31 
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

""")

coins = [200,100,50,20,10,5,2,1]
target = 200
ccoins = []
counter = 0
count = [0 for i in coins]

for i in coins:
    ccoins.append(int(target / i))


def value():
    summ = 0
    i = 0
    while i < len(coins):
        summ += count[i] * coins[i]
        i += 1
    return summ

def myfunc(i):
    i += 1
    global counter
    global count
    global ccoins
    global target
    count[i] = 0
    while count[i] <= ccoins[i]:
        val = value()
        if val == target:
           # print(count)
            counter += 1
        if val >= target:
            count[i] = 0
            break
        if i < len(coins)-1:

            myfunc(i)
        
     
        #print(val,i,count[i],ccoins[i],count,ccoins)


        

        count[i] += 1



        
    count[i] = 0

    

myfunc(-1)


print(counter)        
    
        

