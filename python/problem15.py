print("""
Lattice paths
Problem 15 
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

""")
count = 0
target = 20
lis =  [[0 for x in range(target+1)] for x in range(target+1)]



for i in range(0,target+1):
    lis[0][i] = 1

for i in range(1,target+1):
    for j in range(0,target+1):
        if(j == 0):
           lis[i][j]=lis[i-1][j]
        else:
            lis[i][j]=lis[i-1][j]+lis[i][j-1]


print(lis[target][target])
    
    
