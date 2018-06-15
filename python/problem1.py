print("Multiples of 3 and 5\nProblem 1")
print("Find the sum of all the multiples of 3 or 5 below X.")
high = int(input("X="))
sum = 0
for i in range(1,high):
	if ((i % 3) == 0) or ((i % 5) == 0):
		sum += i

print("Sum:",sum)
