print("""
Number spiral diagonals
Problem 28 
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
""")

size = 1001
spi = [[0 for i in range(size)] for j in range(size)]
sx = size // 2
sy= size // 2
dep = 1
val = 1
spi[sx][sy] = val
while val < size*size:

    sy += 1
    val += 1
    spi[sx][sy] = val
    
    for i in range(2*dep -1):
        val += 1
        sx += 1
        spi[sx][sy] = val
    for i in range(dep * 2):
        val += 1
        sy -= 1
        spi[sx][sy] = val
    for i in range(dep * 2):
        val += 1
        sx -= 1
        spi[sx][sy] = val
    for i in range(dep * 2):
        val += 1
        sy += 1
        spi[sx][sy] = val

   
    dep += 1

i = 0
j = 0
summ = 0
while i < size:
    summ += spi[i][j]
    i += 1
    j += 1
    
i = 0
while i < size:
    j -= 1
    summ += spi[i][j]
    i += 1



print(summ-1)

