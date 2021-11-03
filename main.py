# calculate number of days between two dates

date_1 = [int(date) for date in input("date 1: (2014.6.30)\n").split(".")] # date 1
date_2 = [int(date) for date in input("date 2: (2014.6.30)\n").split(".")] # date 2

days_1 = date_1[0]*365 + date_1[1]*30 + date_1[2] # days in date 1
days_2 = date_2[0]*365 + date_2[1]*30 + date_2[2] # days in date 2

result = abs(days_2-days_1)
print("diffrence of this two date is " , result)