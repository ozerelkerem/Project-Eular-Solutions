from functools import reduce
number = reduce(lambda x,y:x*y,range(1,101))
summ = 0
for i in str(number):
    summ += int(i)
print(summ)
