'''
User enter year
check if year is a leap year
if year % 4 == 0 and year % 100 != 0 or (year % 400 != 0) then
    print year is a leap year

'''

year = int(input("Please enter the year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("{} is a leap year.".format(year))
else:
    print("{} is a not leap year.".format(year))
