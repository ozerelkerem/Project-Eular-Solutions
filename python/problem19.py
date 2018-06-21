print("""
Counting Sundays
Problem 19 
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
""")
months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

day = 2
year = 1901

count = 0
for i in range(year,2001):
    if(i % 4 == 0):
        tday = 366
    else:
        tday = 365
    for j in range(1,13):
        if day == 0:
            count += 1
        if tday == 366 and j == 2:
            day += (months[j]+1) % 7
            day = day % 7
        else:
            day += months[j] % 7
            day = day % 7


print(count)
        
        

