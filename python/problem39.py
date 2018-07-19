print("""
Integer right triangles
Problem 39 
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
""")
li = dict()
def findmax(li):
    maxx = 0
    val = 0
    for i in li:
        if li.get(i) > maxx:
            maxx = li.get(i)
            val = i
    print(val,maxx)

a = 3
run = True
while run:
    b=1
    while run:
        c = (a*a + b*b) ** (0.5)
        if (a+b+c) > 1000:
            if b==1:
                run = False

            break
        if c == round(c):
            if not int(a+b+c) in li.keys():
                li[int(a+b+c)] = 1
            else:
                li[int(a+b+c)] += 1
        b+=1
    a+=1        

findmax(li)
