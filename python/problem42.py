print("""
Coded triangle numbers
Problem 42 
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
""")
import string

file = open("p042_words.txt","r")
data = file.read()
file.close()

words = data.split(",")

maxx = 0
for word in words:
    word = word[1:-1]
    if len(word) > maxx:
        maxx = len(word)

i=1
alphabet = {}
for s in str(string.ascii_uppercase):
    alphabet[s] = i
    i += 1
    
max_val = i * maxx
i = 0
triangles = []
while True:
    val = i * (i + 1 ) / 2
    i  += 1
    if val < max_val:
        triangles.append(int(val))
    else:
        break

def asum(s):
    summ = 0
    for i in s:
        summ += alphabet[i]
    return summ

print(asum("SKY"))
tcount = 0
for word in words:
    word = word[1:-1]
    if asum(word) in triangles:
        tcount += 1

print(tcount)

    
