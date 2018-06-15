print("""

Largest palindrome product
Problem 4 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
    """)

def isPolydrome(x):
    x = str(x)
    for i in range(0,int(len(x)/2)):
        if x[i]!=x[-i-1]:
            return False

    return True


liste = []

for i in range(999,900,-1):
    for j in range(999,900,-1):
        if isPolydrome(i*j):
            liste.append(i*j)


liste.sort(reverse=True)
print(liste[0])
    
