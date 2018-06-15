print("""
	Even Fibonacci numbers
	Problem 2
""")
max = int(input("MAX="))
old = 1
new = 2
sum = 2
while(new < max):
	old,new = new, old + new
	print(new)
	if new % 2 == 0:
		sum += new

print(sum)