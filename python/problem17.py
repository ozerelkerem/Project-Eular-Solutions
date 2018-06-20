print("""Number letter counts
Problem 17 
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
""")
dic = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"
,10:"ten",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",
       20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",
       11:"eleven",1000:"one thousand"
    }
count = 0
for i in range(1,1001):
    tcount = 0
    wr = ""
    if i == 1000:
        wr += dic[i]
    else:
        if(i // 100 != 0):
            wr += dic[i//100] + " hundred"
        other = i-(i // 100)*100
        if(i // 100 > 0 and other > 0):
            wr += " and "
        if other < 20 and other > 0:
           wr += dic[other]
        elif other >=20:
            wr += dic[other//10*10]
            if (other - other//10*10 > 0):
                wr+=dic[other - other//10*10]
    for j in wr:
        if j != " ":
            tcount += 1
    print(i,":",wr,tcount)
    
    count += tcount
print(count)
    
        
